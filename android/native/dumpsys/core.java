for (int i=0; i<N; i++) {
    final String name = pkg.requestedPermissions.get(i);
    final BasePermission bp = mSettings.mPermissions.get(name);

    if (DEBUG_INSTALL) {
        Log.i(TAG, "Package " + pkg.packageName + " checking " + name + ": " + bp);
    }

    if (bp == null || bp.packageSetting == null) {
        if (packageOfInterest == null || packageOfInterest.equals(pkg.packageName)) {
            Slog.w(TAG, "Unknown permission " + name
                    + " in package " + pkg.packageName);
        }
        continue;
    }

    final String perm = bp.name;
    boolean allowedSig = false;
    int grant = GRANT_DENIED;

    // Keep track of app op permissions.
    if ((bp.protectionLevel & PermissionInfo.PROTECTION_FLAG_APPOP) != 0) {
        ArraySet<String> pkgs = mAppOpPermissionPackages.get(bp.name);
        if (pkgs == null) {
            pkgs = new ArraySet<>();
            mAppOpPermissionPackages.put(bp.name, pkgs);
        }
        pkgs.add(pkg.packageName);
    }

    final int level = bp.protectionLevel & PermissionInfo.PROTECTION_MASK_BASE;
    switch (level) {
        case PermissionInfo.PROTECTION_NORMAL: {
            // For all apps normal permissions are install time ones.
            grant = GRANT_INSTALL;
        } break;

        case PermissionInfo.PROTECTION_DANGEROUS: {
            if (pkg.applicationInfo.targetSdkVersion <= Build.VERSION_CODES.LOLLIPOP_MR1){
                // For legacy apps dangerous permissions are install time ones.
                grant = GRANT_INSTALL_LEGACY;
            } else if (origPermissions.hasInstallPermission(bp.name)) {
                // For legacy apps that became modern, install becomes runtime.
                grant = GRANT_UPGRADE;
            } else if (mPromoteSystemApps
                    && isSystemApp(ps)
                    && mExistingSystemPackages.contains(ps.name)) {
                // For legacy system apps, install becomes runtime.
                // We cannot check hasInstallPermission() for system apps since those
                // permissions were granted implicitly and not persisted pre-M.
                grant = GRANT_UPGRADE;
            } else {
                // For modern apps keep runtime permissions unchanged.
                grant = GRANT_RUNTIME;
            }
        } break;

        case PermissionInfo.PROTECTION_SIGNATURE: {
            // For all apps signature permissions are install time ones.
            allowedSig = grantSignaturePermission(perm, pkg, bp, origPermissions);
            if (allowedSig) {
                grant = GRANT_INSTALL;
            }
        } break;
    }

    if (DEBUG_INSTALL) {
        Log.i(TAG, "Package " + pkg.packageName + " granting " + perm);
    }

    if (grant != GRANT_DENIED) {
        if (!isSystemApp(ps) && ps.installPermissionsFixed) {
            // If this is an existing, non-system package, then
            // we can't add any new permissions to it.
            if (!allowedSig && !origPermissions.hasInstallPermission(perm)) {
                // Except...  if this is a permission that was added
                // to the platform (note: need to only do this when
                // updating the platform).
                if (!isNewPlatformPermissionForPackage(perm, pkg)) {
                    grant = GRANT_DENIED;
                }
            }
        }

        switch (grant) {
            case GRANT_INSTALL: {
                // Revoke this as runtime permission to handle the case of
                // a runtime permission being downgraded to an install one.
                for (int userId : UserManagerService.getInstance().getUserIds()) {
                    if (origPermissions.getRuntimePermissionState(
                            bp.name, userId) != null) {
                        // Revoke the runtime permission and clear the flags.
                        origPermissions.revokeRuntimePermission(bp, userId);
                        origPermissions.updatePermissionFlags(bp, userId,
                                PackageManager.MASK_PERMISSION_FLAGS, 0);
                        // If we revoked a permission permission, we have to write.
                        changedRuntimePermissionUserIds = ArrayUtils.appendInt(
                                changedRuntimePermissionUserIds, userId);
                    }
                }
                // Grant an install permission.
                if (permissionsState.grantInstallPermission(bp) !=
                        PermissionsState.PERMISSION_OPERATION_FAILURE) {
                    changedInstallPermission = true;
                }
            } break;

            case GRANT_INSTALL_LEGACY: {
                // Grant an install permission.
                if (permissionsState.grantInstallPermission(bp) !=
                        PermissionsState.PERMISSION_OPERATION_FAILURE) {
                    changedInstallPermission = true;
                }
            } break;

            case GRANT_RUNTIME: {
                // Grant previously granted runtime permissions.
                for (int userId : UserManagerService.getInstance().getUserIds()) {
                    PermissionState permissionState = origPermissions
                            .getRuntimePermissionState(bp.name, userId);
                    final int flags = permissionState != null
                            ? permissionState.getFlags() : 0;
                    if (origPermissions.hasRuntimePermission(bp.name, userId)) {
                        if (permissionsState.grantRuntimePermission(bp, userId) ==
                                PermissionsState.PERMISSION_OPERATION_FAILURE) {
                            // If we cannot put the permission as it was, we have to write.
                            changedRuntimePermissionUserIds = ArrayUtils.appendInt(
                                    changedRuntimePermissionUserIds, userId);
                        }
                    }
                    // Propagate the permission flags.
                    permissionsState.updatePermissionFlags(bp, userId, flags, flags);
                }
            } break;

            case GRANT_UPGRADE: {
                // Grant runtime permissions for a previously held install permission.
                PermissionState permissionState = origPermissions
                        .getInstallPermissionState(bp.name);
                final int flags = permissionState != null ? permissionState.getFlags() : 0;

                if (origPermissions.revokeInstallPermission(bp)
                        != PermissionsState.PERMISSION_OPERATION_FAILURE) {
                    // We will be transferring the permission flags, so clear them.
                    origPermissions.updatePermissionFlags(bp, UserHandle.USER_ALL,
                            PackageManager.MASK_PERMISSION_FLAGS, 0);
                    changedInstallPermission = true;
                }

                // If the permission is not to be promoted to runtime we ignore it and
                // also its other flags as they are not applicable to install permissions.
                if ((flags & PackageManager.FLAG_PERMISSION_REVOKE_ON_UPGRADE) == 0) {
                    for (int userId : currentUserIds) {
                        if (permissionsState.grantRuntimePermission(bp, userId) !=
                                PermissionsState.PERMISSION_OPERATION_FAILURE) {
                            // Transfer the permission flags.
                            permissionsState.updatePermissionFlags(bp, userId,
                                    flags, flags);
                            // If we granted the permission, we have to write.
                            changedRuntimePermissionUserIds = ArrayUtils.appendInt(
                                    changedRuntimePermissionUserIds, userId);
                        }
                    }
                }
            } break;

            default: {
                if (packageOfInterest == null
                        || packageOfInterest.equals(pkg.packageName)) {
                    Slog.w(TAG, "Not granting permission " + perm
                            + " to package " + pkg.packageName
                            + " because it was previously installed without");
                }
            } break;
        }
    } else {
        if (permissionsState.revokeInstallPermission(bp) !=
                PermissionsState.PERMISSION_OPERATION_FAILURE) {
            // Also drop the permission flags.
            permissionsState.updatePermissionFlags(bp, UserHandle.USER_ALL,
                    PackageManager.MASK_PERMISSION_FLAGS, 0);
            changedInstallPermission = true;
            Slog.i(TAG, "Un-granting permission " + perm
                    + " from package " + pkg.packageName
                    + " (protectionLevel=" + bp.protectionLevel
                    + " flags=0x" + Integer.toHexString(pkg.applicationInfo.flags)
                    + ")");
        } else if ((bp.protectionLevel&PermissionInfo.PROTECTION_FLAG_APPOP) == 0) {
            // Don't print warning for app op permissions, since it is fine for them
            // not to be granted, there is a UI for the user to decide.
            if (packageOfInterest == null || packageOfInterest.equals(pkg.packageName)) {
                Slog.w(TAG, "Not granting permission " + perm
                        + " to package " + pkg.packageName
                        + " (protectionLevel=" + bp.protectionLevel
                        + " flags=0x" + Integer.toHexString(pkg.applicationInfo.flags)
                        + ")");
            }
        }
    }
}