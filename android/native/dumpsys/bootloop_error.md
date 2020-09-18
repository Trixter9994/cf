05-02 00:56:42.054 587-587/? D/SPL: Call QSEECom_register_listener()
    Registered listener sucessfully!
    pipe read-fd [24] write-fd [25]
    Create thread
    Thread created sucessfully.
05-02 00:56:42.055 587-598/? D/SPL: spl_dispatch() started
    ==== Wait For Request ======
05-02 00:56:42.187 603-603/? I/vold: Vold 3.0 (the awakening) firing up
05-02 00:56:42.187 603-603/? D/vold: Detected support for: exfat ext4 f2fs ntfs vfat
05-02 00:56:42.190 603-603/? W/vold: Failed to LOOP_GET_STATUS64 /dev/block/loop15: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop6: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop12: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop8: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop0: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop3: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop14: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop5: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop10: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop9: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop1: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop7: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop13: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop4: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop11: No such device or address
    Failed to LOOP_GET_STATUS64 /dev/block/loop2: No such device or address
05-02 00:56:42.191 603-603/? I/vold: [libfs_mgr]dt_fstab: Using a specified mount point /system_root for system
05-02 00:56:42.192 603-603/? D/vold: VoldNativeService::start() completed OK
05-02 00:57:27.945 603-603/? I/Checkpoint: cp_prepareCheckpoint called
05-02 00:57:27.968 603-603/? I/vold: fscrypt_initialize_systemwide_keys
05-02 00:57:27.968 603-603/? D/vold: Key exists, using: /data/unencrypted/key
05-02 00:57:27.990 603-603/? I/vold: List of Keymaster HALs found:
    Keymaster HAL #1: SoftwareWrappedKeymaster1Device from Google SecurityLevel: TRUSTED_ENVIRONMENT HAL: android.hardware.keymaster@3.0::IKeymasterDevice/default
    Using SoftwareWrappedKeymaster1Device from Google for encryption.  Security level: TRUSTED_ENVIRONMENT, HAL: android.hardware.keymaster@3.0::IKeymasterDevice/default
05-02 00:57:28.019 603-603/? D/vold: Added key 739201105 (ext4:48c4394631c70c7a) to keyring 465366917 in process 603
    Added key 746232260 (f2fs:48c4394631c70c7a) to keyring 465366917 in process 603
    Added key 110309937 (fscrypt:48c4394631c70c7a) to keyring 465366917 in process 603
05-02 00:57:28.023 603-603/? I/vold: Wrote system DE key reference to:/data/unencrypted/ref
05-02 00:57:28.023 603-603/? D/vold: Added key 313180708 (ext4:219265056f84c380) to keyring 465366917 in process 603
    Added key 464397789 (f2fs:219265056f84c380) to keyring 465366917 in process 603
    Added key 633176482 (fscrypt:219265056f84c380) to keyring 465366917 in process 603
05-02 00:57:28.025 603-603/? I/vold: Wrote per boot key reference to:/data/unencrypted/per_boot_ref
05-02 00:57:28.242 603-603/? D/vold: fscrypt_init_user0
    Preparing: /data/misc/vold/user_keys
05-02 00:57:28.243 603-603/? D/vold: Preparing: /data/misc/vold/user_keys/ce
05-02 00:57:28.244 603-603/? D/vold: Preparing: /data/misc/vold/user_keys/de
05-02 00:57:28.250 603-603/? I/vold: List of Keymaster HALs found:
    Keymaster HAL #1: SoftwareWrappedKeymaster1Device from Google SecurityLevel: TRUSTED_ENVIRONMENT HAL: android.hardware.keymaster@3.0::IKeymasterDevice/default
05-02 00:57:28.251 603-603/? I/vold: Using SoftwareWrappedKeymaster1Device from Google for encryption.  Security level: TRUSTED_ENVIRONMENT, HAL: android.hardware.keymaster@3.0::IKeymasterDevice/default
05-02 00:57:28.265 603-603/? D/vold: Added key 1021060334 (ext4:9847c2ff56775825) to keyring 465366917 in process 603
    Added key 748728261 (f2fs:9847c2ff56775825) to keyring 465366917 in process 603
    Added key 99421279 (fscrypt:9847c2ff56775825) to keyring 465366917 in process 603
    Installed de key for user 0
    Skipping non-de-key ..
    Skipping non-de-key .
05-02 00:57:28.272 603-603/? I/vold: List of Keymaster HALs found:
05-02 00:57:28.273 603-603/? I/vold: Keymaster HAL #1: SoftwareWrappedKeymaster1Device from Google SecurityLevel: TRUSTED_ENVIRONMENT HAL: android.hardware.keymaster@3.0::IKeymasterDevice/default
    Using SoftwareWrappedKeymaster1Device from Google for encryption.  Security level: TRUSTED_ENVIRONMENT, HAL: android.hardware.keymaster@3.0::IKeymasterDevice/default
05-02 00:57:28.286 603-603/? D/vold: Added key 41747831 (ext4:5e0fdc3c4b74c147) to keyring 465366917 in process 603
    Added key 404595416 (f2fs:5e0fdc3c4b74c147) to keyring 465366917 in process 603
    Added key 475936675 (fscrypt:5e0fdc3c4b74c147) to keyring 465366917 in process 603
    Installed de key for user 999
    fscrypt_prepare_user_storage for volume null, user 0, serial 0, flags 1
    Preparing: /data/system/users/0
05-02 00:57:28.287 603-603/? D/vold: Preparing: /data/misc/profiles/cur/0
    Preparing: /data/system_de/0
05-02 00:57:28.288 603-603/? D/vold: Preparing: /data/misc_de/0
    Preparing: /data/vendor_de/0
    Preparing: /data/user_de/0
05-02 00:57:28.289 603-603/? I/vold: Found policy 9847c2ff56775825 at /data/system_de/0 which matches expected value
    Found policy 9847c2ff56775825 at /data/misc_de/0 which matches expected value
05-02 00:57:28.290 603-603/? I/vold: Found policy 9847c2ff56775825 at /data/vendor_de/0 which matches expected value
    Found policy 9847c2ff56775825 at /data/user_de/0 which matches expected value
05-02 00:57:28.290 603-603/? D/vold: /system/bin/vold_prepare_subdirs
05-02 00:57:28.291 603-603/? D/vold:     prepare
        
        0
        1
    
    --------- beginning of main
05-02 00:57:28.852 672-673/? I/Magisk: bind_mount: /system/lib64/android.hardware.graphics.mapper@2.0.so
    bind_mount: /system/lib64/android.hardware.graphics.mapper@2.1.so
    bind_mount: /system/lib64/android.hardware.graphics.mapper@3.0.so
    bind_mount: /system/lib64/android.hardware.health.storage@1.0.so
    bind_mount: /system/lib64/android.hardware.health@1.0.so
    bind_mount: /system/lib64/android.hardware.health@2.0.so
    bind_mount: /system/lib64/android.hardware.input.classifier@1.0.so
    bind_mount: /system/lib64/android.hardware.input.common@1.0.so
    bind_mount: /system/lib64/android.hardware.ir@1.0.so
    bind_mount: /system/lib64/android.hardware.keymaster@3.0.so
    bind_mount: /system/lib64/android.hardware.keymaster@4.0.so
    bind_mount: /system/lib64/android.hardware.light@2.0.so
    bind_mount: /system/lib64/android.hardware.media.bufferpool@2.0.so
    bind_mount: /system/lib64/android.hardware.media.c2@1.0.so
    bind_mount: /system/lib64/android.hardware.media.omx@1.0.so
    bind_mount: /system/lib64/android.hardware.media@1.0.so
    bind_mount: /system/lib64/android.hardware.memtrack@1.0.so
05-02 00:57:28.853 672-673/? I/Magisk: bind_mount: /system/lib64/android.hardware.neuralnetworks@1.0.so
    bind_mount: /system/lib64/android.hardware.neuralnetworks@1.1.so
    bind_mount: /system/lib64/android.hardware.neuralnetworks@1.2.so
    bind_mount: /system/lib64/android.hardware.nfc@1.0.so
    bind_mount: /system/lib64/android.hardware.nfc@1.1.so
    bind_mount: /system/lib64/android.hardware.nfc@1.2.so
    bind_mount: /system/lib64/android.hardware.power.stats@1.0.so
    bind_mount: /system/lib64/android.hardware.power@1.0.so
    bind_mount: /system/lib64/android.hardware.power@1.1.so
    bind_mount: /system/lib64/android.hardware.power@1.2.so
    bind_mount: /system/lib64/android.hardware.power@1.3.so
    bind_mount: /system/lib64/android.hardware.renderscript@1.0.so
    bind_mount: /system/lib64/android.hardware.sensors@1.0.so
    bind_mount: /system/lib64/android.hardware.sensors@2.0.so
    bind_mount: /system/lib64/android.hardware.soundtrigger@2.0.so
05-02 00:57:28.854 672-673/? I/Magisk: bind_mount: /system/lib64/android.hardware.soundtrigger@2.1.so
    bind_mount: /system/lib64/android.hardware.soundtrigger@2.2.so
    bind_mount: /system/lib64/android.hardware.tetheroffload.config@1.0.so
    bind_mount: /system/lib64/android.hardware.thermal@1.0.so
    bind_mount: /system/lib64/android.hardware.tv.cec@1.0.so
    bind_mount: /system/lib64/android.hardware.tv.input@1.0.so
    bind_mount: /system/lib64/bootstrap
    bind_mount: /system/lib64/drm
    bind_mount: /system/lib64/android.hardware.usb.gadget@1.0.so
    bind_mount: /system/lib64/android.hardware.vibrator@1.0.so
    bind_mount: /system/lib64/android.hardware.vibrator@1.1.so
    bind_mount: /system/lib64/android.hardware.vibrator@1.2.so
    bind_mount: /system/lib64/android.hardware.vibrator@1.3.so
    bind_mount: /system/lib64/android.hardware.vr@1.0.so
    bind_mount: /system/lib64/android.hardware.wifi.offload@1.0.so
    bind_mount: /system/lib64/android.hidl.allocator@1.0.so
    bind_mount: /system/lib64/android.hidl.memory.token@1.0.so
05-02 00:57:28.855 672-673/? I/Magisk: bind_mount: /system/lib64/android.hidl.memory@1.0.so
    bind_mount: /system/lib64/android.hidl.safe_union@1.0.so
    bind_mount: /system/lib64/android.hidl.token@1.0-utils.so
    bind_mount: /system/lib64/android.hidl.token@1.0.so
    bind_mount: /system/lib64/android.system.net.netd@1.0.so
    bind_mount: /system/lib64/android.system.net.netd@1.1.so
    bind_mount: /system/lib64/android.system.suspend@1.0.so
    bind_mount: /system/lib64/android.system.wifi.keystore@1.0.so
    bind_mount: /system/lib64/apex_aidl_interface-cpp.so
    bind_mount: /system/lib64/ashmemd_aidl_interface-cpp.so
    bind_mount: /system/lib64/com.qualcomm.qti.ant@1.0.so
    bind_mount: /system/lib64/com.qualcomm.qti.dpm.api@1.0.so
    bind_mount: /system/lib64/dnsresolver_aidl_interface-V2-cpp.so
    bind_mount: /system/lib64/gsi_aidl_interface-cpp.so
    bind_mount: /system/lib64/heapprofd_client.so
    bind_mount: /system/lib64/hw
    bind_mount: /system/lib64/ld-android.so
05-02 00:57:28.856 672-673/? I/Magisk: bind_mount: /system/lib64/lib-imscamera.so
    bind_mount: /system/lib64/lib-imsvideocodec.so
    bind_mount: /system/lib64/lib-imsvt.so
    bind_mount: /system/lib64/lib-imsvtextutils.so
    bind_mount: /system/lib64/lib-imsvtutils.so
    bind_mount: /system/lib64/lib7z.so
    bind_mount: /system/lib64/libEGL.so
    bind_mount: /system/lib64/libETC1.so
    bind_mount: /system/lib64/libFFTEm.so
    bind_mount: /system/lib64/libGLESv1_CM.so
    bind_mount: /system/lib64/libGLESv2.so
    bind_mount: /system/lib64/libGLESv3.so
    bind_mount: /system/lib64/libLLVM_android.so
    bind_mount: /system/lib64/libOpenMAXAL.so
    bind_mount: /system/lib64/libOpenSLES.so
    bind_mount: /system/lib64/libRS.so
05-02 00:57:28.857 672-673/? I/Magisk: bind_mount: /system/lib64/libRSCacheDir.so
    bind_mount: /system/lib64/libRSCpuRef.so
    bind_mount: /system/lib64/libRSDriver.so
    bind_mount: /system/lib64/libRS_internal.so
    bind_mount: /system/lib64/libRScpp.so
    bind_mount: /system/lib64/libSurfaceFlingerProp.so
    bind_mount: /system/lib64/libaaudio.so
    bind_mount: /system/lib64/libaaudioservice.so
    bind_mount: /system/lib64/libadbd.so
    bind_mount: /system/lib64/libadbd_services.so
    bind_mount: /system/lib64/libamidi.so
    bind_mount: /system/lib64/libandroid.so
    bind_mount: /system/lib64/libandroid_net.so
    bind_mount: /system/lib64/libandroid_runtime.so
    bind_mount: /system/lib64/libandroid_runtime_lazy.so
    bind_mount: /system/lib64/libandroid_servers.so
    bind_mount: /system/lib64/libandroidfw.so
05-02 00:57:28.858 672-673/? I/Magisk: bind_mount: /system/lib64/libantradio.so
    bind_mount: /system/lib64/libappfuse.so
    bind_mount: /system/lib64/libartpalette-system.so
    bind_mount: /system/lib64/libashmemd_client.so
    bind_mount: /system/lib64/libasyncio.so
    bind_mount: /system/lib64/libaudio-resampler.so
    bind_mount: /system/lib64/libaudioclient.so
    bind_mount: /system/lib64/libaudioeffect_jni.so
    bind_mount: /system/lib64/libaudioflinger.so
    bind_mount: /system/lib64/libaudiohal.so
    bind_mount: /system/lib64/libaudiohal@2.0.so
    bind_mount: /system/lib64/libaudiohal@4.0.so
    bind_mount: /system/lib64/libaudiohal@5.0.so
    bind_mount: /system/lib64/libaudiohal_deathhandler.so
    bind_mount: /system/lib64/libaudiomanager.so
    bind_mount: /system/lib64/libaudiopolicy.so
    bind_mount: /system/lib64/libaudiopolicyenginedefault.so
05-02 00:57:28.859 672-673/? I/Magisk: bind_mount: /system/lib64/libaudiopolicymanager.so
    bind_mount: /system/lib64/libaudiopolicymanagerdefault.so
    bind_mount: /system/lib64/libaudiopolicyservice.so
    bind_mount: /system/lib64/libaudioprocessing.so
    bind_mount: /system/lib64/libaudiospdif.so
    bind_mount: /system/lib64/libaudioutils.so
    bind_mount: /system/lib64/libavservices_minijail.so
    bind_mount: /system/lib64/libbacktrace.so
    bind_mount: /system/lib64/libbase.so
    bind_mount: /system/lib64/libbcc.so
    bind_mount: /system/lib64/libbcinfo.so
    bind_mount: /system/lib64/libbfqio.so
    bind_mount: /system/lib64/libbinder.so
    bind_mount: /system/lib64/libbinder_ndk.so
    bind_mount: /system/lib64/libbinderthreadstate.so
    bind_mount: /system/lib64/libblas.so
    bind_mount: /system/lib64/libbluetooth-binder.so
    bind_mount: /system/lib64/libbluetooth.so
05-02 00:57:28.860 672-673/? I/Magisk: bind_mount: /system/lib64/libbluetooth_jni.so
    bind_mount: /system/lib64/libbootanimation.so
    bind_mount: /system/lib64/libbootloader_message.so
    bind_mount: /system/lib64/libbpf.so
    bind_mount: /system/lib64/libbpf_android.so
    bind_mount: /system/lib64/libbufferhub.so
    bind_mount: /system/lib64/libbufferhubqueue.so
    bind_mount: /system/lib64/libbz.so
    bind_mount: /system/lib64/libc++.so
    copy_link : /system/lib64/libc.so
    bind_mount: /system/lib64/libc_malloc_debug.so
    bind_mount: /system/lib64/libc_malloc_hooks.so
    bind_mount: /system/lib64/libc_scudo.so
    bind_mount: /system/lib64/libcamera2ndk.so
    bind_mount: /system/lib64/libcamera_client.so
    bind_mount: /system/lib64/libcamera_metadata.so
05-02 00:57:28.861 672-673/? I/Magisk: bind_mount: /system/lib64/libcap.so
    bind_mount: /system/lib64/libcgrouprc.so
    bind_mount: /system/lib64/libchrome.so
    bind_mount: /system/lib64/libclang_rt.asan-aarch64-android.so
    bind_mount: /system/lib64/libclcore.bc
    bind_mount: /system/lib64/libclcore_debug.bc
    bind_mount: /system/lib64/libclcore_debug_g.bc
    bind_mount: /system/lib64/libclcore_g.bc
    bind_mount: /system/lib64/libcodec2.so
    bind_mount: /system/lib64/libcodec2_client.so
    bind_mount: /system/lib64/libcodec2_hidl_client@1.0.so
    bind_mount: /system/lib64/libcodec2_vndk.so
    bind_mount: /system/lib64/libcompiler_rt.so
    bind_mount: /system/lib64/libcrypto.so
    bind_mount: /system/lib64/libcrypto_utils.so
    bind_mount: /system/lib64/libcups.so
    bind_mount: /system/lib64/libcutils.so
    bind_mount: /system/lib64/libdebuggerd_client.so
05-02 00:57:28.862 672-673/? I/Magisk: bind_mount: /system/lib64/libdexfile_support.so
    bind_mount: /system/lib64/libdiag_system.so
    bind_mount: /system/lib64/libdiskconfig.so
    bind_mount: /system/lib64/libdisplayconfig.so
    bind_mount: /system/lib64/libdisplayservicehidl.so
    copy_link : /system/lib64/libdl.so
    bind_mount: /system/lib64/libdl_android.so
    bind_mount: /system/lib64/libdng_sdk.so
    bind_mount: /system/lib64/libdpmctmgr.so
    bind_mount: /system/lib64/libdpmfdmgr.so
    bind_mount: /system/lib64/libdpmframework.so
    bind_mount: /system/lib64/libdpmtcm.so
    bind_mount: /system/lib64/libdrmframework.so
    bind_mount: /system/lib64/libdrmframework_jni.so
    bind_mount: /system/lib64/libdumpstateaidl.so
    bind_mount: /system/lib64/libdumpstateutil.so
    bind_mount: /system/lib64/libdumputils.so
05-02 00:57:28.863 672-673/? I/Magisk: bind_mount: /system/lib64/libeffectsconfig.so
    bind_mount: /system/lib64/libevent.so
    bind_mount: /system/lib64/libexif.so
    bind_mount: /system/lib64/libexpat.so
    bind_mount: /system/lib64/libext2_blkid.so
    bind_mount: /system/lib64/libext2_com_err.so
    bind_mount: /system/lib64/libext2_e2p.so
    bind_mount: /system/lib64/libext2_misc.so
    bind_mount: /system/lib64/libext2_quota.so
    bind_mount: /system/lib64/libext2_uuid.so
    bind_mount: /system/lib64/libext2fs.so
    bind_mount: /system/lib64/libext4_utils.so
    bind_mount: /system/lib64/libf2fs_sparseblock.so
    bind_mount: /system/lib64/libfec.so
    bind_mount: /system/lib64/libfilterfw.so
    bind_mount: /system/lib64/libfilterpack_imageproc.so
    bind_mount: /system/lib64/libfmq.so
    bind_mount: /system/lib64/libframesequence.so
    bind_mount: /system/lib64/libfruit.so
05-02 00:57:28.864 672-673/? I/Magisk: bind_mount: /system/lib64/libfs_mgr.so
    bind_mount: /system/lib64/libfscrypt.so
    bind_mount: /system/lib64/libft2.so
    bind_mount: /system/lib64/libfuse-lite.so
    bind_mount: /system/lib64/libgatekeeper.so
    bind_mount: /system/lib64/libgraphicsenv.so
    bind_mount: /system/lib64/libgsi.so
    bind_mount: /system/lib64/libgtest_prod.so
    bind_mount: /system/lib64/libgui.so
    bind_mount: /system/lib64/libhardware.so
    bind_mount: /system/lib64/libhardware_legacy.so
    bind_mount: /system/lib64/libharfbuzz_ng.so
    bind_mount: /system/lib64/libheif.so
    bind_mount: /system/lib64/libhidcommand_jni.so
    bind_mount: /system/lib64/libhidl-gen-hash.so
    bind_mount: /system/lib64/libhidl-gen-utils.so
    bind_mount: /system/lib64/libhidlallocatorutils.so
    bind_mount: /system/lib64/libhidlbase.so
05-02 00:57:28.865 672-673/? I/Magisk: bind_mount: /system/lib64/libhidlmemory.so
    bind_mount: /system/lib64/libhidltransport.so
    bind_mount: /system/lib64/libhwbinder.so
    bind_mount: /system/lib64/libhwui.so
    bind_mount: /system/lib64/libidmap2.so
    bind_mount: /system/lib64/libimg_utils.so
    bind_mount: /system/lib64/libimscamera_jni.so
    bind_mount: /system/lib64/libimsmedia_jni.so
    bind_mount: /system/lib64/libincident.so
    bind_mount: /system/lib64/libinput.so
    bind_mount: /system/lib64/libinputflinger.so
    bind_mount: /system/lib64/libinputflinger_base.so
    bind_mount: /system/lib64/libinputreader.so
    bind_mount: /system/lib64/libinputreporter.so
    bind_mount: /system/lib64/libinputservice.so
    bind_mount: /system/lib64/libion.so
    bind_mount: /system/lib64/libiprouteutil.so
    bind_mount: /system/lib64/libjni_pacprocessor.so
05-02 00:57:28.866 672-673/? I/Magisk: bind_mount: /system/lib64/libjni_terminal.so
    bind_mount: /system/lib64/libjnigraphics.so
    bind_mount: /system/lib64/libjpeg.so
    bind_mount: /system/lib64/libjsoncpp.so
    bind_mount: /system/lib64/libkeymaster4support.so
    bind_mount: /system/lib64/libkeymaster_messages.so
    bind_mount: /system/lib64/libkeymaster_portable.so
    bind_mount: /system/lib64/libkeystore-engine.so
    bind_mount: /system/lib64/libkeystore_aidl.so
    bind_mount: /system/lib64/libkeystore_binder.so
    bind_mount: /system/lib64/libkeystore_parcelables.so
    bind_mount: /system/lib64/libkeyutils.so
    bind_mount: /system/lib64/liblayers_proto.so
    bind_mount: /system/lib64/libldacBT_abr.so
    bind_mount: /system/lib64/libldacBT_enc.so
    bind_mount: /system/lib64/liblineage-sdk_platform_jni.so
    bind_mount: /system/lib64/liblog.so
05-02 00:57:28.867 672-673/? I/Magisk: bind_mount: /system/lib64/liblogwrap.so
    bind_mount: /system/lib64/liblp.so
    bind_mount: /system/lib64/liblpdump.so
    bind_mount: /system/lib64/liblpdump_interface-cpp.so
    bind_mount: /system/lib64/liblshal.so
    bind_mount: /system/lib64/liblzma.so
    copy_link : /system/lib64/libm.so
    bind_mount: /system/lib64/libmdnssd.so
    bind_mount: /system/lib64/libmedia.so
    bind_mount: /system/lib64/libmedia2_jni_core.so
    bind_mount: /system/lib64/libmedia_helper.so
    bind_mount: /system/lib64/libmedia_jni.so
    bind_mount: /system/lib64/libmedia_jni_utils.so
    bind_mount: /system/lib64/libmedia_omx.so
    bind_mount: /system/lib64/libmedia_omx_client.so
    bind_mount: /system/lib64/libmediadrm.so
    bind_mount: /system/lib64/libmediadrmmetrics_lite.so
05-02 00:57:28.868 672-673/? I/Magisk: bind_mount: /system/lib64/libmediaextractorservice.so
    bind_mount: /system/lib64/libmedialogservice.so
    bind_mount: /system/lib64/libmediametrics.so
    bind_mount: /system/lib64/libmediandk.so
    bind_mount: /system/lib64/libmediandk_utils.so
    bind_mount: /system/lib64/libmediautils.so
    bind_mount: /system/lib64/libmeminfo.so
    bind_mount: /system/lib64/libmemunreachable.so
    bind_mount: /system/lib64/libmetricslogger.so
    bind_mount: /system/lib64/libminijail.so
    bind_mount: /system/lib64/libminikin.so
    bind_mount: /system/lib64/libmmosal.so
    bind_mount: /system/lib64/libmtp.so
    bind_mount: /system/lib64/libnativebridge_lazy.so
    bind_mount: /system/lib64/libnativeloader_lazy.so
    bind_mount: /system/lib64/libnativewindow.so
    bind_mount: /system/lib64/libnbaio.so
05-02 00:57:28.869 672-673/? I/Magisk: bind_mount: /system/lib64/libnblog.so
    bind_mount: /system/lib64/libncurses.so
    bind_mount: /system/lib64/libnetd_client.so
    bind_mount: /system/lib64/libnetdbpf.so
    bind_mount: /system/lib64/libnetdutils.so
    bind_mount: /system/lib64/libnetlink.so
    bind_mount: /system/lib64/libnetutils.so
    bind_mount: /system/lib64/libneuralnetworks.so
    bind_mount: /system/lib64/libnfc-nci.so
    bind_mount: /system/lib64/libnfc_nci_jni.so
    bind_mount: /system/lib64/libnl.so
    bind_mount: /system/lib64/libntfs-3g.so
    bind_mount: /system/lib64/libpackagelistparser.so
    bind_mount: /system/lib64/libpcap.so
    bind_mount: /system/lib64/libpcre2.so
    bind_mount: /system/lib64/libpcrecpp.so
    bind_mount: /system/lib64/libpdfium.so
05-02 00:57:28.870 672-673/? I/Magisk: bind_mount: /system/lib64/libpdx_default_transport.so
    bind_mount: /system/lib64/libperfetto.so
    bind_mount: /system/lib64/libperfetto_android_internal.so
    bind_mount: /system/lib64/libpiex.so
    bind_mount: /system/lib64/libpixelflinger.so
    bind_mount: /system/lib64/libpng.so
    bind_mount: /system/lib64/libpower.so
    bind_mount: /system/lib64/libpowermanager.so
    bind_mount: /system/lib64/libprintspooler_jni.so
    bind_mount: /system/lib64/libprocessgroup.so
    bind_mount: /system/lib64/libprocessgroup_setup.so
    bind_mount: /system/lib64/libprocinfo.so
    bind_mount: /system/lib64/libprotobuf-cpp-full.so
    bind_mount: /system/lib64/libprotobuf-cpp-lite.so
    bind_mount: /system/lib64/libprotoutil.so
    bind_mount: /system/lib64/libpsi.so
    bind_mount: /system/lib64/libqdMetaData.system.so
    bind_mount: /system/lib64/libqtaguid.so
05-02 00:57:28.871 672-673/? I/Magisk: bind_mount: /system/lib64/libradio_metadata.so
    bind_mount: /system/lib64/librcc.so
    bind_mount: /system/lib64/librs_jni.so
    bind_mount: /system/lib64/librtp_jni.so
    bind_mount: /system/lib64/libsanitizer-status.so
    bind_mount: /system/lib64/libschedulerservicehidl.so
    bind_mount: /system/lib64/libscudo_wrapper.so
    bind_mount: /system/lib64/libselinux.so
    bind_mount: /system/lib64/libsensor.so
    bind_mount: /system/lib64/libsensorprivacy.so
    bind_mount: /system/lib64/libsensorservice.so
    bind_mount: /system/lib64/libsensorservicehidl.so
    bind_mount: /system/lib64/libsepol.so
    bind_mount: /system/lib64/libservices.so
    bind_mount: /system/lib64/libsfplugin_ccodec.so
    bind_mount: /system/lib64/libsfplugin_ccodec_utils.so
    bind_mount: /system/lib64/libsoftkeymasterdevice.so
05-02 00:57:28.872 672-673/? I/Magisk: bind_mount: /system/lib64/libsonic.so
    bind_mount: /system/lib64/libsonivox.so
    bind_mount: /system/lib64/libsoundpool.so
    bind_mount: /system/lib64/libsoundtrigger.so
    bind_mount: /system/lib64/libsoundtriggerservice.so
    bind_mount: /system/lib64/libsparse.so
    bind_mount: /system/lib64/libspeexresampler.so
    bind_mount: /system/lib64/libsqlite.so
    bind_mount: /system/lib64/libsquashfs_utils.so
    bind_mount: /system/lib64/libssh.so
    bind_mount: /system/lib64/libssl.so
    bind_mount: /system/lib64/libstagefright.so
    bind_mount: /system/lib64/libstagefright_amrnb_common.so
    bind_mount: /system/lib64/libstagefright_bufferpool@2.0.1.so
    bind_mount: /system/lib64/libstagefright_bufferqueue_helper.so
    bind_mount: /system/lib64/libstagefright_codecbase.so
    bind_mount: /system/lib64/libstagefright_enc_common.so
05-02 00:57:28.873 672-673/? I/Magisk: bind_mount: /system/lib64/libstagefright_foundation.so
    bind_mount: /system/lib64/libstagefright_http_support.so
    bind_mount: /system/lib64/libstagefright_omx.so
    bind_mount: /system/lib64/libstagefright_omx_utils.so
    bind_mount: /system/lib64/libstagefright_xmlparser.so
    bind_mount: /system/lib64/libstatslog.so
    bind_mount: /system/lib64/libstatssocket.so
    bind_mount: /system/lib64/libstdc++.so
    bind_mount: /system/lib64/libsurfaceflinger.so
    bind_mount: /system/lib64/libsuspend.so
    bind_mount: /system/lib64/libsync.so
    bind_mount: /system/lib64/libsysutils.so
    bind_mount: /system/lib64/libtextclassifier.so
    bind_mount: /system/lib64/libtextclassifier_hash.so
    bind_mount: /system/lib64/libtflite.so
    bind_mount: /system/lib64/libtimestats_proto.so
    bind_mount: /system/lib64/libtinyalsa.so
    bind_mount: /system/lib64/libtinyxml2.so
05-02 00:57:28.874 672-673/? I/Magisk: bind_mount: /system/lib64/libtombstoned_client.so
    bind_mount: /system/lib64/libui.so
    bind_mount: /system/lib64/libunwindstack.so
    bind_mount: /system/lib64/libusbhost.so
    bind_mount: /system/lib64/libutils.so
    bind_mount: /system/lib64/libutilscallstack.so
    bind_mount: /system/lib64/libvibrator.so
    bind_mount: /system/lib64/libvintf.so
    bind_mount: /system/lib64/libvndksupport.so
    bind_mount: /system/lib64/libvorbisidec.so
    bind_mount: /system/lib64/libvulkan.so
    bind_mount: /system/lib64/libwebviewchromium_loader.so
    bind_mount: /system/lib64/libwebviewchromium_plat_support.so
    bind_mount: /system/lib64/libwfdclient.so
    bind_mount: /system/lib64/libwfdnative.so
    bind_mount: /system/lib64/libwfds.so
    bind_mount: /system/lib64/libwifi-service.so
    bind_mount: /system/lib64/libwifi-system-iface.so
    bind_mount: /system/lib64/libwifikeystorehal.so
    bind_mount: /system/lib64/libwilhelm.so
    bind_mount: /system/lib64/libxml2.so
    bind_mount: /system/lib64/libz.so
05-02 00:57:28.875 672-673/? I/Magisk: bind_mount: /system/lib64/libziparchive.so
    bind_mount: /system/lib64/netd_aidl_interface-V2-cpp.so
    bind_mount: /system/lib64/netd_event_listener_interface-V1-cpp.so
    bind_mount: /system/lib64/netd_event_listener_interface-cpp.so
    bind_mount: /system/lib64/oemnetd_aidl_interface-cpp.so
    bind_mount: /system/lib64/pppol2tp-android.so
    bind_mount: /system/lib64/pppopptp-android.so
    bind_mount: /system/lib64/server_configurable_flags.so
    bind_mount: /system/lib64/slicer.so
    bind_mount: /system/lib64/suspend_control_aidl_interface-cpp.so
    bind_mount: /system/lib64/vendor.lineage.power@1.0.so
    bind_mount: /system/lib64/vendor.qti.imsrtpservice@1.0.so
    bind_mount: /system/lib64/vndk-29
    bind_mount: /system/lib64/vndk-sp-29
    bind_mount: /system/bin/app_process64
    bind_mount: /system/bin/app_process32
05-02 00:57:28.949 757-757/? I/art_apex: === ART pre-boot integrity checks ===
05-02 00:57:28.978 759-759/? A/art_apex: Device is not fsverity-enabled.
05-02 00:57:29.029 761-761/? E//system/bin/recovery-persist: Failed to unlink /cache/recovery/last_install: No such file or directory
05-02 00:57:29.047 763-763/? I//system/bin/flags_health_check: ServerConfigurableFlagsReset reset_mode value: 0
    ServerConfigurableFlagsReset attempted boot count is under threshold, skipping reset.
05-02 00:57:29.093 767-767/? I/bootstat: Service started: /system/bin/bootstat --set_system_boot_reason 
05-02 00:57:29.139 764-764/? I/netdClient: Skipping libnetd_client init since *we* are netd
05-02 00:57:29.141 764-764/? I/netd: netd 1.0 starting
05-02 00:57:29.151 771-771/? I/ServiceManagement: Registered android.hidl.allocator@1.0::IAllocator/ashmem (start delay of 34ms)
    Removing namespace from process name android.hidl.allocator@1.0-service to allocator@1.0-service.
05-02 00:57:29.159 773-773/? I/android.hardware.bluetooth@1.0-service: registering BT & FM services
05-02 00:57:29.162 773-773/? D/vndksupport: Loading /vendor/lib64/hw/android.hardware.bluetooth@1.0-impl-qti.so from current namespace instead of sphal namespace.
05-02 00:57:29.172 780-780/? D/vndksupport: Loading /vendor/lib64/hw/android.hardware.gatekeeper@1.0-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.172 777-777/? D/vndksupport: Loading /vendor/lib64/hw/android.hardware.drm@1.0-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.178 764-764/? I/Netd: Loaded resolver library from /apex/com.android.resolv/lib64/libnetd_resolv.so
05-02 00:57:29.180 780-780/? D/vndksupport: Loading /vendor/lib64/hw/gatekeeper.msm8998.so from current namespace instead of sphal namespace.
05-02 00:57:29.183 780-780/? D/gatekeeper_device: HwGkOpen called
05-02 00:57:29.183 780-780/? D/QSEECOMAPI: QSEECom_get_handle sb_length = 0xa000
05-02 00:57:29.184 780-780/? D/QSEECOMAPI: App is already loaded QSEE and app id = 65537
05-02 00:57:29.185 780-780/? E/gatekeeper_device: Gatekeeper initialized
05-02 00:57:29.200 780-780/? I/ServiceManagement: Registered android.hardware.gatekeeper@1.0::IGatekeeper/default (start delay of 64ms)
05-02 00:57:29.201 780-780/? I/ServiceManagement: Removing namespace from process name android.hardware.gatekeeper@1.0-service to gatekeeper@1.0-service.
05-02 00:57:29.201 780-780/? I/android.hardware.gatekeeper@1.0-service: Registration complete for android.hardware.gatekeeper@1.0::IGatekeeper/default.
05-02 00:57:29.201 781-781/? D/vndksupport: Loading /vendor/lib64/hw/android.hardware.gnss@1.0-impl-qti.so from current namespace instead of sphal namespace.
05-02 00:57:29.202 776-776/? W//vendor/bin/hw/android.hardware.configstore@1.1-service: libminijail[776]: allowing syscall: connect
    libminijail[776]: allowing syscall: fcntl
    libminijail[776]: allowing syscall: sendto
    libminijail[776]: allowing syscall: socket
    libminijail[776]: allowing syscall: writev
05-02 00:57:29.203 788-788/? D/vndksupport: Loading /vendor/lib64/hw/android.hardware.memtrack@1.0-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.205 792-792/? D/vndksupport: Loading /vendor/lib64/hw/android.hardware.sensors@1.0-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.206 777-777/? I/ServiceManagement: Registered android.hardware.drm@1.0::IDrmFactory/default (start delay of 80ms)
    Removing namespace from process name android.hardware.drm@1.0-service to drm@1.0-service.
05-02 00:57:29.207 788-788/? D/vndksupport: Loading /vendor/lib64/hw/memtrack.msm8998.so from current namespace instead of sphal namespace.
05-02 00:57:29.207 777-777/? D/vndksupport: Loading /vendor/lib64/hw/android.hardware.drm@1.0-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.207 773-773/? I/ServiceManagement: Registered android.hardware.bluetooth@1.0::IBluetoothHci/default (start delay of 91ms)
05-02 00:57:29.208 773-773/? I/ServiceManagement: Removing namespace from process name android.hardware.bluetooth@1.0-service-qti to bluetooth@1.0-service-qti.
05-02 00:57:29.208 776-776/? W//vendor/bin/hw/android.hardware.configstore@1.1-service: libminijail[776]: logging seccomp filter failures
05-02 00:57:29.208 783-783/? D/vndksupport: Loading /vendor/lib64/hw/android.hardware.graphics.allocator@2.0-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.204 787-787/? I/ServiceManagement: Registered android.hardware.light@2.0::ILight/default (start delay of 57ms)
05-02 00:57:29.209 787-787/? I/ServiceManagement: Removing namespace from process name android.hardware.light@2.0-service.xiaomi_msm8998 to light@2.0-service.xiaomi_msm8998.
05-02 00:57:29.209 787-787/? I/android.hardware.light@2.0-service.xiaomi_msm8998: Light HAL service ready.
05-02 00:57:29.209 793-793/? I/ServiceManagement: Registered android.hardware.usb@1.0::IUsb/default (start delay of 53ms)
    Removing namespace from process name android.hardware.usb@1.0-service to usb@1.0-service.
05-02 00:57:29.210 793-793/? I/android.hardware.usb@1.0-service: USB HAL Ready.
05-02 00:57:29.210 773-773/? D/vndksupport: Loading /vendor/lib64/hw/com.qualcomm.qti.ant@1.0-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.211 776-776/? I/ServiceManagement: Registered android.hardware.configstore@1.1::ISurfaceFlingerConfigs/default (start delay of 84ms)
    Removing namespace from process name android.hardware.configstore@1.1-service to configstore@1.1-service.
05-02 00:57:29.212 777-777/? I/ServiceManagement: Registered android.hardware.drm@1.0::ICryptoFactory/default (start delay of 86ms)
    Removing namespace from process name android.hardware.drm@1.0-service to drm@1.0-service.
05-02 00:57:29.213 784-784/? D/vndksupport: Loading /vendor/lib64/hw/android.hardware.graphics.composer@2.1-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.215 791-791/? I/android.hardware.power@1.2-service-qti: Power HAL Service 1.2 is starting.
05-02 00:57:29.215 791-791/? I/QTI PowerHAL: Initing
05-02 00:57:29.216 788-788/? I/ServiceManagement: Registered android.hardware.memtrack@1.0::IMemtrack/default (start delay of 70ms)
05-02 00:57:29.217 788-788/? I/ServiceManagement: Removing namespace from process name android.hardware.memtrack@1.0-service to memtrack@1.0-service.
05-02 00:57:29.217 791-791/? I/ServiceManagement: Registered android.hardware.power@1.2::IPower/default (start delay of 60ms)
05-02 00:57:29.217 788-788/? I/android.hardware.memtrack@1.0-service: Registration complete for android.hardware.memtrack@1.0::IMemtrack/default.
05-02 00:57:29.217 791-791/? I/ServiceManagement: Removing namespace from process name android.hardware.power@1.2-service-qti to power@1.2-service-qti.
05-02 00:57:29.217 791-791/? I/android.hardware.power@1.2-service-qti: Successfully registered IPower
05-02 00:57:29.217 781-781/? I/ServiceManagement: Registered android.hardware.gnss@1.0::IGnss/default (start delay of 80ms)
    Removing namespace from process name android.hardware.gnss@1.0-service-qti to gnss@1.0-service-qti.
05-02 00:57:29.217 781-781/? I/android.hardware.gnss@1.0-service-qti: Registration complete for android.hardware.gnss@1.0::IGnss/default.
05-02 00:57:29.218 794-794/? D/vndksupport: Loading /vendor/lib64/hw/android.hardware.vibrator@1.0-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.221 783-783/? D/vndksupport: Loading /vendor/lib64/hw/gralloc.msm8998.so from current namespace instead of sphal namespace.
05-02 00:57:29.222 794-794/? D/vndksupport: Loading /vendor/lib64/hw/vibrator.default.so from current namespace instead of sphal namespace.
05-02 00:57:29.223 791-791/? I/ServiceManagement: Registered vendor.lineage.power@1.0::ILineagePower/default (start delay of 67ms)
05-02 00:57:29.223 791-791/? I/android.hardware.power@1.2-service-qti: Successfully registered ILineagePower
    Power Service is ready
05-02 00:57:29.223 773-773/? I/ServiceManagement: Registered com.qualcomm.qti.ant@1.0::IAntHci/default (start delay of 107ms)
05-02 00:57:29.225 786-786/? I/health@2.0/: health@2.0/default: Hal starting main loop...
    health@2.0/default Hal is starting up...
05-02 00:57:29.229 784-784/? D/vndksupport: Loading /vendor/lib64/hw/hwcomposer.msm8998.so from current namespace instead of sphal namespace.
05-02 00:57:29.228 775-775/? I/ServiceManagement: Registered android.hardware.cas@1.1::IMediaCasService/default (start delay of 111ms)
05-02 00:57:29.230 775-775/? I/ServiceManagement: Removing namespace from process name android.hardware.cas@1.1-service to cas@1.1-service.
05-02 00:57:29.232 778-778/? D/android.hardware.drm@1.0-service.widevine: android.hardware.drm@1.1-service.widevine starting...
05-02 00:57:29.233 794-794/? I/ServiceManagement: Registered android.hardware.vibrator@1.0::IVibrator/default (start delay of 66ms)
    Removing namespace from process name android.hardware.vibrator@1.0-service to vibrator@1.0-service.
05-02 00:57:29.233 783-783/? I/ServiceManagement: Registered android.hardware.graphics.allocator@2.0::IAllocator/default (start delay of 86ms)
05-02 00:57:29.233 794-794/? I/android.hardware.vibrator@1.0-service: Registration complete for android.hardware.vibrator@1.0::IVibrator/default.
05-02 00:57:29.233 783-783/? I/ServiceManagement: Removing namespace from process name android.hardware.graphics.allocator@2.0-service to allocator@2.0-service.
05-02 00:57:29.233 783-783/? I/android.hardware.graphics.allocator@2.0-service: Registration complete for android.hardware.graphics.allocator@2.0::IAllocator/default.
05-02 00:57:29.238 809-809/? I/irsc_util: Starting irsc tool
05-02 00:57:29.239 778-778/? I/ServiceManagement: Registered android.hardware.drm@1.1::IDrmFactory/widevine (start delay of 112ms)
    Removing namespace from process name android.hardware.drm@1.1-service.widevine to drm@1.1-service.widevine.
05-02 00:57:29.238 779-779/? I/ServiceManagement: Registered android.hardware.drm@1.2::IDrmFactory/clearkey (start delay of 101ms)
05-02 00:57:29.239 778-778/? I/ServiceManagement: Registered android.hardware.drm@1.1::ICryptoFactory/widevine (start delay of 113ms)
    Removing namespace from process name android.hardware.drm@1.1-service.widevine to drm@1.1-service.widevine.
05-02 00:57:29.239 779-779/? I/ServiceManagement: Removing namespace from process name android.hardware.drm@1.2-service.clearkey to drm@1.2-service.clearkey.
05-02 00:57:29.241 779-779/? I/ServiceManagement: Registered android.hardware.drm@1.2::ICryptoFactory/clearkey (start delay of 104ms)
    Removing namespace from process name android.hardware.drm@1.2-service.clearkey to drm@1.2-service.clearkey.
05-02 00:57:29.241 798-798/? D/vndksupport: Loading /vendor/lib64/hw/vendor.qti.hardware.alarm@1.0-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.245 786-786/? I/ServiceManagement: Registered android.hardware.health@2.0::IHealth/default (start delay of 98ms)
    Removing namespace from process name android.hardware.health@2.0-service to health@2.0-service.
05-02 00:57:29.245 786-786/? I/health@2.0/: health@2.0/default: Hal init done
05-02 00:57:29.246 797-797/? I/vendor.lineage.trust@1.0-service: Trust HAL service is starting.
05-02 00:57:29.248 796-796/? I/android.hardware.wifi@1.0-service: Wifi Hal is booting up...
05-02 00:57:29.249 798-798/? I/ServiceManagement: Registered vendor.qti.hardware.alarm@1.0::IAlarm/default (start delay of 63ms)
    Removing namespace from process name vendor.qti.hardware.alarm@1.0-service to alarm@1.0-service.
05-02 00:57:29.250 797-797/? I/ServiceManagement: Registered vendor.lineage.trust@1.0::IUsbRestrict/default (start delay of 63ms)
    Removing namespace from process name vendor.lineage.trust@1.0-service to trust@1.0-service.
05-02 00:57:29.250 797-797/? I/vendor.lineage.trust@1.0-service: Trust HAL service is ready.
05-02 00:57:29.251 809-809/? I/irsc_util: Num of entries:295
    Ending irsc tool
05-02 00:57:29.255 796-796/? I/ServiceManagement: Registered android.hardware.wifi@1.3::IWifi/default (start delay of 88ms)
    Removing namespace from process name android.hardware.wifi@1.0-service to wifi@1.0-service.
05-02 00:57:29.255 810-810/? I/vendor.rmt_storage: Modem subsystem found on target!
05-02 00:57:29.255 789-789/? D/nxpnfc@1.0-service: NFC HAL Service 1.1 is starting.
05-02 00:57:29.256 810-810/? I/vendor.rmt_storage: Shared memory initialised successfully.
    Registering modemst1: 0x4a /boot/modem_fs1
    Registering modemst2: 0x4b /boot/modem_fs2
    Registering fsc: 0xff /boot/modem_fsc
    Registering fsg: 0x58 /boot/modem_fsg
    4 GPT partitions found
    Capset success!
05-02 00:57:29.258 789-789/? I/ServiceManagement: Registered android.hardware.nfc@1.1::INfc/default (start delay of 112ms)
05-02 00:57:29.259 789-789/? I/ServiceManagement: Removing namespace from process name android.hardware.nfc@1.1-service to nfc@1.1-service.
05-02 00:57:29.260 789-789/? D/nxpnfc@1.0-service: Could not register service for NXP NFC Extn Iface (-2147483648).
    NFC service is ready
05-02 00:57:29.267 792-792/? E/libsensor1: check_sensors_enabled: Sensors enabled = true
05-02 00:57:29.270 774-774/? I/android.hardware.camera.provider@2.4-service: CameraProvider@2.4 legacy service is starting.
05-02 00:57:29.271 807-807/? D/QSEECOMAPI: QSEECom_get_handle sb_length = 0x2000
    App is not loaded in QSEE
05-02 00:57:29.272 807-807/? D/QSEECOMAPI: app_arch = 1, total_files = 9
05-02 00:57:29.276 774-774/? D/vndksupport: Loading /vendor/lib/hw/android.hardware.camera.provider@2.4-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.278 812-812/? I/tftp_server: Initializing tftp_server RING buffer
05-02 00:57:29.279 812-812/? I/tftp_server: Starting...
05-02 00:57:29.279 817-817/? E/MSM-irqbalance: WARNING: Cannot find matching virq for hwirq(22).
05-02 00:57:29.280 804-804/? I/ServiceManagement: Registered vendor.qti.hardware.tui_comm@1.0::ITuiComm/default (start delay of 73ms)
    Removing namespace from process name vendor.qti.hardware.tui_comm@1.0-service-qti to tui_comm@1.0-service-qti.
05-02 00:57:29.283 802-802/? D/vndksupport: Loading /vendor/lib64/hw/vendor.qti.hardware.soter@1.0-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.289 817-817/? E/MSM-irqbalance: WARNING: Cannot find matching virq for hwirq(446).
05-02 00:57:29.292 817-817/? E/MSM-irqbalance: WARNING: Cannot find matching virq for hwirq(455).
05-02 00:57:29.293 802-802/? D/QSEECOMAPI: QSEECom_get_handle sb_length = 0xa000
    App is not loaded in QSEE
05-02 00:57:29.295 817-817/? E/MSM-irqbalance: WARNING: Cannot find matching virq for hwirq(456).
05-02 00:57:29.295 817-817/? I/MSM-irqbalance: msm-irq_balance (1.3) initialized
    Configuration
    Rate: 0.2 Hz
    Decay Factor: 75.0
    Balancing Factor: 0.1
    Debug Log: OFF
    Cfg file: /vendor/etc/msm_irqbalance.conf
    CPU PRIO: CPU0: 1 CPU1: 1 CPU2: 1 CPU3: 1 CPU4: 0 CPU5: 0 CPU6: 0 CPU7: 0 
    Ignored IRQs: 3 5 319 53 93 164 
05-02 00:57:29.296 772-772/? D/vndksupport: Loading /vendor/lib/hw/android.hardware.audio@5.0-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.305 831-831/? I/lowmemorykiller: Using in-kernel low memory killer interface
05-02 00:57:29.305 802-802/? D/QSEECOMAPI: app_arch = 2, total_files = 9
05-02 00:57:29.308 800-800/? I/ServiceManagement: Registered vendor.qti.hardware.perf@1.0::IPerf/default (start delay of 111ms)
    Removing namespace from process name vendor.qti.hardware.perf@1.0-service to perf@1.0-service.
05-02 00:57:29.314 820-820/? I/PerMgrSrv: Adding entry for modem : offTimeout : 500 ackTimeout : 200
05-02 00:57:29.315 820-820/? I/PerMgrSrv: Adding entry for spss : offTimeout : 5000 ackTimeout : 200
05-02 00:57:29.315 800-800/? E/vendor.qti.hardware.perf@1.0-service: Registered IPerf HAL service success!
05-02 00:57:29.315 820-820/? I/PerMgrSrv: Adding entry for slpi : offTimeout : 5000 ackTimeout : 200
05-02 00:57:29.318 767-767/? I/bootstat: Canonical boot reason: reboot,
    Canonical boot reason: reboot,
05-02 00:57:29.321 820-820/? I/PerMgrSrv: Peripheral Mananager service start
    power-off timeout 500,ms; event-ack timeout 200,ms; debug-mode false
    Statistics for : modem
    modem: Current State : is off-line
    modem: Voter/Listener count : 0/0
    modem: Power on count : 0
    modem: Power off count: 0
    modem: Client list:
    Statistics for : spss
    spss: Current State : is off-line
    spss: Voter/Listener count : 0/0
    spss: Power on count : 0
    spss: Power off count: 0
    spss: Client list:
    Statistics for : slpi
    slpi: Current State : is off-line
    slpi: Voter/Listener count : 0/0
    slpi: Power on count : 0
    slpi: Power off count: 0
    slpi: Client list:
05-02 00:57:29.322 772-772/? I/ServiceManagement: Registered android.hardware.audio@5.0::IDevicesFactory/default (start delay of 205ms)
    Removing namespace from process name android.hardware.audio@2.0-service to audio@2.0-service.
05-02 00:57:29.322 772-772/? I/audiohalservice: Registration complete for android.hardware.audio@5.0::IDevicesFactory/default.
05-02 00:57:29.323 772-772/? D/vndksupport: Loading /vendor/lib/hw/android.hardware.audio.effect@5.0-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.325 820-848/? I/PerMgrSrv: QMI service start
05-02 00:57:29.329 784-784/? I/ServiceManagement: Registered vendor.display.config@1.9::IDisplayConfig/default (start delay of 183ms)
05-02 00:57:29.330 807-807/? D/QSEECOMAPI: Loaded image: APP id = 131074
05-02 00:57:29.330 821-821/? I/pd-mapper-svc: Starting pd-mapper service
05-02 00:57:29.331 784-784/? I/SDM: HWCSession::StartServices: IDisplayConfig service registration completed.
05-02 00:57:29.331 821-821/? I/pd-mapper-svc: Parsing file :/vendor/firmware_mnt/image/adspr.jsn:
05-02 00:57:29.331 784-784/? D/vndksupport: Loading /vendor/lib64/hw/gralloc.msm8998.so from current namespace instead of sphal namespace.
05-02 00:57:29.331 821-821/? I/pd-mapper-svc: Parsing file :/vendor/firmware_mnt/image/adspua.jsn:
05-02 00:57:29.332 807-807/? D/MlipayService: Load app mlipay from /vendor/firmware_mnt/image OK
    run_cmd: cmd->cmd_id = 0x0000f001
05-02 00:57:29.337 821-821/? I/pd-mapper-svc: Parsing file :/vendor/firmware_mnt/image/modemr.jsn:
05-02 00:57:29.338 772-772/? I/ServiceManagement: Registered android.hardware.audio.effect@5.0::IEffectsFactory/default (start delay of 221ms)
05-02 00:57:29.338 772-772/? I/audiohalservice: Registration complete for android.hardware.audio.effect@5.0::IEffectsFactory/default.
05-02 00:57:29.338 772-772/? D/vndksupport: Loading /vendor/lib/hw/android.hardware.soundtrigger@2.2-impl.so from current namespace instead of sphal namespace.
05-02 00:57:29.339 784-784/? I/SDM: ExtensionInterface::CreateExtensionInterface: 
    SDM-EXTENSION Version: Date: 09/28/19, Commit: 3fc34c4, Change: Iec044d2856
05-02 00:57:29.339 821-821/? I/pd-mapper-svc: Parsing file :/vendor/firmware_mnt/image/slpir.jsn:
05-02 00:57:29.340 784-784/? I/SDM: HWInfo::GetHWResourceInfo: SDE Version = 5, SDE Revision = 30000001, RGB = 0, VIG = 4, DMA = 4, Cursor = 2
    HWInfo::GetHWResourceInfo: Upscale Ratio = 20, Downscale Ratio = 4, Blending Stages = 7
    HWInfo::GetHWResourceInfo: SourceSplit = 1 QSEED3 = 1
    HWInfo::GetHWResourceInfo: BWC = 0, UBWC = 1, Decimation = 1, Tile Format = 0 Concurrent Writeback = 1
    HWInfo::GetHWResourceInfo: MaxLowBw = 9400000 , MaxHighBw = 9400000
    HWInfo::GetHWResourceInfo: MaxPipeBw = 4700000 KBps, MaxSDEClock = 412500000 Hz, ClockFudgeFactor = 1.050000
    HWInfo::GetHWResourceInfo: Prefill factors: Tiled_NV12 = 8, Tiled = 4, Linear = 1, Scale = 1, Fudge_factor = 2
05-02 00:57:29.340 784-784/? W/SDM: HWInfo::GetMDSSRotatorInfo: File '/sys/devices/virtual/rotator/mdss_rotator/caps' not found
05-02 00:57:29.341 784-784/? I/SDM: HWInfo::GetV4L2RotatorInfo: V4L2 Rotator: Count = 1, Downscale = 1, Min_downscale = 1.500000, Downscale_compression = 1
    SessionManager::SessionManager: Allocate buffers synchronously = 0
05-02 00:57:29.342 821-821/? I/pd-mapper-svc: Parsing file :/vendor/firmware_mnt/image/slpius.jsn:
05-02 00:57:29.346 821-821/? I/pd-mapper-svc: Parsing file :/vendor/firmware_mnt/image/modemuw.jsn:
05-02 00:57:29.346 784-853/? W/SDM: HWCSession::UEventThread: UEvent dropped. No uevent listener.
05-02 00:57:29.349 772-772/? D/vndksupport: Loading /vendor/lib/hw/sound_trigger.primary.msm8998.so from current namespace instead of sphal namespace.
05-02 00:57:29.350 807-807/? D/QSEECOMAPI: QSEECom_dealloc_memory 
    QSEECom_shutdown_app, app_id = 131074
05-02 00:57:29.351 784-853/? W/SDM: HWCSession::UEventThread: UEvent dropped. No uevent listener.
    HWCSession::UEventThread: UEvent dropped. No uevent listener.
05-02 00:57:29.353 774-774/? D/vndksupport: Loading /vendor/lib/hw/camera.msm8998.so from current namespace instead of sphal namespace.
05-02 00:57:29.358 784-784/? I/SDM: CoreInterface::CreateCore: Open interface handle = 0x7c3563c000
    HWCSession::Register: Set uevent listener = 0x7c35626280
    HWInfo::GetFirstDisplayInterfaceType: First display is internal display
05-02 00:57:29.359 784-784/? I/SDM: CPUHint::Init: CPU Hint Pre-enable Window 50
05-02 00:57:29.360 784-784/? I/SDM: CPUHint::Init: Successfully Loaded Vendor Extension Library symbols
05-02 00:57:29.361 784-784/? I/SDM: HWDevice::GetHWPanelMaxBrightnessFromNode: Max brightness level = 4095
    HWDevice::Init: access(/dev/graphics/fb0) successful
    HWDevice::GetHWPanelMaxBrightnessFromNode: Max brightness level = 4095
    HWDevice::PopulateHWPanelInfo: Device type = 0, Display Port = 1, Display Mode = 1, Device Node = 0, Is Primary = 1
    HWDevice::PopulateHWPanelInfo: Partial Update = 0, supported roi_count =0, Dynamic FPS = 1
    HWDevice::PopulateHWPanelInfo: Align: left = 0, width = 0, top = 0, height = 0
    HWDevice::PopulateHWPanelInfo: ROI: min_width = 0, min_height = 0, need_merge = 0
    HWDevice::PopulateHWPanelInfo: FPS: min = 55, max =60
    HWDevice::PopulateHWPanelInfo: Ping Pong Split = 0
    HWDevice::PopulateHWPanelInfo: Left Split = 0, Right Split = 0
05-02 00:57:29.367 772-772/? D/sound_trigger_hw: stdev_open: Enter
05-02 00:57:29.370 784-784/? I/SDM: HWDevice::GetHWPanelMaxBrightnessFromNode: Max brightness level = 4095
    HWDevice::GetHWPanelMaxBrightnessFromNode: Max brightness level = 4095
05-02 00:57:29.370 784-784/? W/SDM: HWDevice::GetHWPanelInfoByNode: Failed to open msm_fb_panel_info node device node 2
    HWDevice::GetHWPanelInfoByNode: Failed to open msm_fb_panel_info node device node 3
05-02 00:57:29.370 784-784/? I/SDM: HWDevice::GetHWPanelMaxBrightnessFromNode: Max brightness level = 4095
    HWDevice::GetHWPanelMaxBrightnessFromNode: Max brightness level = 4095
05-02 00:57:29.370 784-784/? W/SDM: HWDevice::GetHWPanelInfoByNode: Failed to open msm_fb_panel_info node device node 2
    HWDevice::GetHWPanelInfoByNode: Failed to open msm_fb_panel_info node device node 3
05-02 00:57:29.371 784-784/? I/SDM: StrategyImpl::SetIdleTimeoutMs: Idle timeout: active = 70, inactive = 520
    StrategyImpl::Init: HDR LUT Generation disabled
05-02 00:57:29.371 784-784/? W/SDM: ColorManager::CreateColorManagerProxy: PAV2 version is versions = 11, version = 11 
05-02 00:57:29.374 821-858/? I/pd-mapper-svc: Starting servloc server
05-02 00:57:29.381 802-802/? D/QSEECOMAPI: Loaded image: APP id = 196611
05-02 00:57:29.402 772-772/? D/sound_trigger_hw: load_audio_hal: ahal is using proprietary API version 0x0101
05-02 00:57:29.402 772-772/? I/sound_trigger_platform: platform_stdev_init: Enter
05-02 00:57:29.406 772-772/? W/sound_trigger_platform: load_smlib: generate_sound_trigger_phrase_recognition_event_v3 not found. undefined symbol: generate_sound_trigger_phrase_recognition_event_v3
05-02 00:57:29.413 869-869/? E/PerMgrProxy: Starting pm-proxy service
05-02 00:57:29.414 820-852/? D/PerMgrSrv: modem state: is off-line, add client PM-PROXY-THREAD
    PM-PROXY-THREAD registered
05-02 00:57:29.415 869-869/? D/PerMgrLib: PM-PROXY-THREAD successfully registered for modem
05-02 00:57:29.415 869-869/? I/PerMgrProxy: Casting proxy vote for modem
05-02 00:57:29.415 869-869/? D/PerMgrLib: PM-PROXY-THREAD voting for modem
05-02 00:57:29.415 820-852/? D/PerMgrSrv: PM-PROXY-THREAD voting for modem
    modem new state: going on-line
    modem num voters is 1
05-02 00:57:29.415 869-869/? I/PerMgrProxy: pm-proxy-thread vote successful for modem
05-02 00:57:29.421 832-832/? I/SurfaceFlinger: Using HWComposer service: 'default'
    SurfaceFlinger is starting
05-02 00:57:29.426 832-832/? I/SurfaceFlinger: Enabling backpressure propagation for Client Composition
    Enabling HWC virtual displays
    Treble testing override: 'false'
    SurfaceFlinger's main thread ready to run. Initializing graphics H/W...
    Phase offset NS: 2000000
05-02 00:57:29.426 832-832/? D/RenderEngine: RenderEngine GLES Backend
05-02 00:57:29.432 807-807/? E/MlipayService: key version 4
05-02 00:57:29.435 784-784/? I/SDM: DisplayBase::InitializeColorModes: Number of Color Modes = 39
05-02 00:57:29.439 832-832/? D/libEGL: loaded /vendor/lib64/egl/libEGL_adreno.so
05-02 00:57:29.441 870-884/? I/adbd: opening control endpoint /dev/usb-ffs/adb/ep0
05-02 00:57:29.480 774-774/? E/linker: normalize_path - invalid input: "C", the input path should be absolute
05-02 00:57:29.481 774-774/? W/linker: Warning: unable to normalize "C" (ignoring)
05-02 00:57:29.481 774-774/? E/linker: normalize_path - invalid input: "\Android\sdk\ndk-bundle\toolchains\llvm\prebuilt\windows-x86_64\lib64\clang\5.0.300080\lib\linux\arm", the input path should be absolute
05-02 00:57:29.481 774-774/? W/linker: Warning: unable to normalize "\Android\sdk\ndk-bundle\toolchains\llvm\prebuilt\windows-x86_64\lib64\clang\5.0.300080\lib\linux\arm" (ignoring)
05-02 00:57:29.483 832-832/? D/libEGL: loaded /vendor/lib64/egl/libGLESv1_CM_adreno.so
05-02 00:57:29.484 765-765/? I/Riru: Riru v21.3 (36) in zygote64
    config dir is /data/misc/riru
    system version 10 (api 29, preview_sdk 0)
05-02 00:57:29.485 832-832/? D/libEGL: loaded /vendor/lib64/egl/libGLESv2_adreno.so
05-02 00:57:29.487 765-765/? I/Riru: hook installed
05-02 00:57:29.487 880-880/? I/ServiceManagement: Registered com.qualcomm.qti.dpm.api@1.0::IdpmQmi/dpmQmiService (start delay of 70ms)
05-02 00:57:29.497 832-832/? I/Adreno: QUALCOMM build                   : 2c6a1c7, I1490fecf6e
    Build Date                       : 02/04/19
    OpenGL ES Shader Compiler Version: EV031.25.03.02
    Local Branch                     : 
    Remote Branch                    : 
    Remote Branch                    : 
    Reconstruct Branch               : 
    Build Config                     : S L 6.0.7 AArch64
05-02 00:57:29.533 774-774/? E/linker: normalize_path - invalid input: "C", the input path should be absolute
05-02 00:57:29.533 774-774/? W/linker: Warning: unable to normalize "C" (ignoring)
05-02 00:57:29.533 774-774/? E/linker: normalize_path - invalid input: "\Android\sdk\ndk-bundle\toolchains\llvm\prebuilt\windows-x86_64\lib64\clang\5.0.300080\lib\linux\arm", the input path should be absolute
05-02 00:57:29.533 774-774/? W/linker: Warning: unable to normalize "\Android\sdk\ndk-bundle\toolchains\llvm\prebuilt\windows-x86_64\lib64\clang\5.0.300080\lib\linux\arm" (ignoring)
05-02 00:57:29.554 784-784/? I/SDM: HWCDisplay::Init: Display created with id: 0
05-02 00:57:29.554 784-784/? E/SDM: DisplayBase::GetColorModeAttr: Failed: Mode default4-default without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode warm without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode cool without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode 03-sRGB without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode 37sRGB-N without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode default3-oled without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm01 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm02 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm03 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm04 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm05 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm06 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm07 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm08 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm09 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm10 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm11 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm12 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm13 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm14 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm15 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm16 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm17 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm18 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm19 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm20 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm21 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm22 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm23 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm24 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm25 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm26 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm27 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm28 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm29 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm30 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm31 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode pm32 without attribute
    DisplayBase::GetColorModeAttr: Failed: Mode  without attribute
05-02 00:57:29.555 784-784/? I/SDM: DisplayBase::SetFrameBufferConfig: New framebuffer resolution (1080x2160)
05-02 00:57:29.568 879-879/? E/QCNEA: Cne Version 4.9
05-02 00:57:29.580 766-766/? I/Riru: Riru v21.3 (36) in zygote
    config dir is /data/misc/riru
    system version 10 (api 29, preview_sdk 0)
05-02 00:57:29.584 766-766/? I/Riru: hook installed
05-02 00:57:29.623 823-823/? I/FastMixerState: sMaxFastTracks = 8
05-02 00:57:29.625 823-823/? V/MediaUtils: physMem: 5966712832
    requested limit: 536870912
05-02 00:57:29.625 823-823/? I/libc: malloc_limit: Allocation limit enabled, max size 536870912 bytes
05-02 00:57:29.626 823-823/? I/audioserver: ServiceManager: 0x77c281edc0
05-02 00:57:29.626 823-823/? W/BatteryNotifier: batterystats service unavailable!
05-02 00:57:29.628 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.audio@5.0::IDevicesFactory/msd in either framework or device manifest.
05-02 00:57:29.630 823-823/? I/AudioFlinger: Using default 3000 mSec as standby time.
05-02 00:57:29.631 823-823/? E/APM::Serializer: deserialize: Could not parse /odm/etc/audio_policy_configuration.xml document.
    deserialize: Could not parse /vendor/etc/audio/audio_policy_configuration.xml document.
05-02 00:57:29.649 823-823/? E/APM::AudioPolicyEngine/Config: parse: Could not parse document /vendor/etc/audio_policy_engine_configuration.xml
05-02 00:57:29.649 823-823/? W/APM::AudioPolicyEngine/Base: loadAudioPolicyEngineConfig: No configuration found, using default matching phone experience.
05-02 00:57:29.649 823-823/? E/APM::AudioPolicyEngine/Config: parseLegacyVolumeFile: Could not parse document /odm/etc/audio_policy_configuration.xml
05-02 00:57:29.653 772-847/? D/vndksupport: Loading /vendor/lib/hw/audio.primary.msm8998.so from current namespace instead of sphal namespace.
05-02 00:57:29.653 772-847/? D/audio_hw_primary: adev_open: enter
05-02 00:57:29.654 772-847/? W/audio_hw_utils: vndk_fwk_init: failed to dlopen VNDK_FWK_LIB No such file or directory
    audio_extn_utils_get_vendor_enhanced_info: default to vendor_enhanced_info 0x0
05-02 00:57:29.654 772-847/? D/audio_hw_extn: snd_mon_feature_init: Called with feature NOT Enabled
05-02 00:57:29.654 772-847/? W/audio_hw_extn: :: snd_mon_feature_init: ---- Feature SND_MONITOR is disabled ----
    :: compr_cap_feature_init: ---- Feature COMPRESS_CAPTURE is disabled ----
05-02 00:57:29.654 772-847/? D/audio_hw_extn: dsm_feedback_feature_init: Called with feature NOT Enabled
05-02 00:57:29.654 772-847/? W/audio_hw_extn: :: dsm_feedback_feature_init: ---- Feature DSM_FEEDBACK is disabled ----
    :: ssrec_feature_init: ---- Feature SSREC is disabled ----
05-02 00:57:29.654 772-847/? D/audio_hw_extn: src_trkn_feature_init:: ---- Feature SOURCE_TRACKING is Enabled ----
    hdmi_edid_feature_init: HDMI_EDID feature NOT Enabled
05-02 00:57:29.654 772-847/? W/audio_hw_extn: :: hdmi_edid_feature_init: ---- Feature HDMI_EDID is disabled ----
05-02 00:57:29.654 772-847/? D/audio_hw_extn: :: keep_alive_feature_init: ---- Feature KEEP_ALIVE is  NOT ENABLED ----
    :: hifi_audio_feature_init: ---- Feature HIFI_AUDIO is  NOT ENABLED ----
    :: ras_feature_init: ---- Feature RAS_FEATURE is ENABLED ----
    :: kpi_optimize_feature_init: ---- Feature KPI_OPTIMIZE is ENABLED ----
    usb_offload_feature_init: Called with feature Enabled
    usb_offload_burst_mode_feature_init: Called with feature NOT Enabled
    usb_offload_sidetone_volume_feature_init: Called with feature NOT Enabled
    a2dp_offload_feature_init: Called with feature NOT Enabled
05-02 00:57:29.654 772-847/? W/audio_hw_extn: :: a2dp_offload_feature_init: ---- Feature A2DP_OFFLOAD is disabled ----
05-02 00:57:29.654 772-847/? D/audio_hw_extn: :: vbat_feature_init: ---- Feature VBAT is ENABLED ----
    :: display_port_feature_init: ---- Feature DISPLAY_PORT is ENABLED ----
    :: fluence_feature_init: ---- Feature FLUENCE is ENABLED ----
    :: custom_stereo_feature_init: ---- Feature CUSTOM_STEREO is ENABLED ----
    :: anc_headset_feature_init: ---- Feature ANC_HEADSET is ENABLED----
    spkr_prot_feature_init: Called with feature NOT Enabled, vendor_enhanced_info 0x0
05-02 00:57:29.654 772-847/? W/audio_hw_extn: :: spkr_prot_feature_init: ---- Feature SPKR_PROT is disabled ----
05-02 00:57:29.654 772-847/? D/audio_hw_extn: fm_feature_init: ---- Feature FM_POWER_OPT is ENABLED----
    external_qdsp_feature_init: Called with feature NOT Enabled
05-02 00:57:29.654 772-847/? W/audio_hw_extn: :: external_qdsp_feature_init: ---- Feature EXTERNAL_QDSP is disabled ----
05-02 00:57:29.654 772-847/? D/audio_hw_extn: external_speaker_feature_init: Called with feature NOT Enabled
05-02 00:57:29.654 772-847/? W/audio_hw_extn: :: external_speaker_feature_init: ---- Feature EXTERNAL_SPKR is disabled ----
05-02 00:57:29.654 772-847/? D/audio_hw_extn: external_speaker_tfa_feature_init: Called with feature NOT Enabled
05-02 00:57:29.654 772-847/? W/audio_hw_extn: :: external_speaker_tfa_feature_init: ---- Feature EXTERNAL_SPKR_TFA is disabled ----
05-02 00:57:29.654 772-847/? D/audio_hw_extn: hwdep_cal_feature_init: Called with feature NOT Enabled
05-02 00:57:29.654 772-847/? W/audio_hw_extn: :: hwdep_cal_feature_init: ---- Feature HWDEP_CAL is disabled ----
05-02 00:57:29.654 772-847/? D/audio_hw_extn: hfp_feature_init: Called with feature Enabled
05-02 00:57:29.656 772-847/? D/audio_hw_extn: hfp_feature_init:: ---- Feature HFP is Enabled ----
    ext_hw_plugin_feature_init: Called with feature NOT Enabled
05-02 00:57:29.656 772-847/? W/audio_hw_extn: :: ext_hw_plugin_feature_init: ---- Feature EXT_HW_PLUGIN is disabled ----
05-02 00:57:29.656 772-847/? D/audio_hw_extn: record_play_concurency_feature_init: ---- Feature RECORD_PLAY_CONCURRENCY is NOT ENABLED----
    hdmi_passthrough_feature_init: Called with feature NOT Enabled
05-02 00:57:29.656 772-847/? W/audio_hw_extn: :: hdmi_passthrough_feature_init: ---- Feature HDMI_PASSTHROUGH is disabled ----
05-02 00:57:29.656 772-847/? D/audio_hw_extn: concurrent_capture_feature_init: ---- Feature CONCURRENT_CAPTURE is NOT ENABLED----
    compress_in_feature_init: ---- Feature COMPRESS_IN is NOT ENABLED----
05-02 00:57:29.656 772-847/? W/audio_hw_extn: :: battery_listener_feature_init: ---- Feature BATTERY_LISTENER is disabled ----
05-02 00:57:29.656 772-847/? D/audio_hw_extn: maxx_audio_feature_init: Called with feature NOT Enabled
05-02 00:57:29.656 772-847/? W/audio_hw_extn: :: maxx_audio_feature_init: ---- Feature MAXX_AUDIO is disabled ----
05-02 00:57:29.656 772-847/? D/audio_hw_extn: audiozoom_feature_init: Called with feature NOT Enabled
05-02 00:57:29.656 772-847/? W/audio_hw_extn: :: audiozoom_feature_init: ---- Feature AUDIOZOOM is disabled ----
05-02 00:57:29.656 772-847/? D/voice_extn: :: dynamic_ecns_feature_init: ---- Feature DYNAMIC_ECNS is NOT ENABLED ----
05-02 00:57:29.672 802-802/? D/vendor.qti.hardware.soter@1.0-service: soter: svc service starting.
05-02 00:57:29.672 802-802/? I/ServiceManagement: Registered vendor.qti.hardware.soter@1.0::ISoter/default (start delay of 476ms)
05-02 00:57:29.673 802-802/? I/ServiceManagement: Removing namespace from process name vendor.qti.hardware.soter@1.0-service to soter@1.0-service.
05-02 00:57:29.674 802-802/? E/vendor.qti.hardware.soter@1.0-service: Registered SOTER HAL service success
05-02 00:57:29.678 765-765/? I/Riru: module loaded: edxp (api 4)
05-02 00:57:29.678 765-765/? V/Riru: edxp: onModuleLoaded
05-02 00:57:29.678 765-765/? I/EdXposed: onModuleLoaded: welcome to EdXposed!
    Start to install inline hooks
    Using api level 29
    Start to install Riru hook
05-02 00:57:29.679 870-884/? I/adbd: UsbFfsConnection constructed
05-02 00:57:29.681 879-879/? I/ServiceManagement: Registered vendor.qti.hardware.data.latency@1.0::ILinkLatency/default (start delay of 264ms)
05-02 00:57:29.683 879-879/? E/QMI_FW: QMUXD: WARNING qmi_qmux_if_pwr_up_init failed! rc=-6
05-02 00:57:29.683 879-879/? I/ServiceManagement: Registered vendor.qti.data.factory@1.1::IFactory/default (start delay of 266ms)
05-02 00:57:29.683 807-807/? I/ServiceManagement: Registered vendor.xiaomi.hardware.mlipay@1.1::IMlipayService/default (start delay of 476ms)
05-02 00:57:29.685 766-766/? I/Riru: module loaded: edxp (api 4)
05-02 00:57:29.685 766-766/? V/Riru: edxp: onModuleLoaded
05-02 00:57:29.685 766-766/? I/EdXposed: onModuleLoaded: welcome to EdXposed!
    Start to install inline hooks
    Using api level 29
    Start to install Riru hook
05-02 00:57:29.692 765-765/? I/EdXposed: Riru hooks installed
05-02 00:57:29.696 915-915/? I/NetUtilsWrapper: Unexpected command: /system/bin/iptables -w -W 10000 -t mangle -A PREROUTING -m mark --mark 0x20 -j ACCEPT
05-02 00:57:29.699 926-926/? E//vendor/bin/adsprpcd: vendor/qcom/proprietary/commonsys-intf/adsprpc/src/adsprpcd.c:29:adsp daemon starting
05-02 00:57:29.702 766-766/? I/EdXposed: Riru hooks installed
05-02 00:57:29.703 765-765/? D/AndroidRuntime: >>>>>> START com.android.internal.os.ZygoteInit uid 0 <<<<<<
05-02 00:57:29.717 766-766/? D/AndroidRuntime: >>>>>> START com.android.internal.os.ZygoteInit uid 0 <<<<<<
05-02 00:57:29.721 926-926/? V//vendor/bin/adsprpcd: vendor/qcom/proprietary/commonsys-intf/adsprpc/src/fastrpc_apps_user.c:1009: remote_handle_open: Successfully opened handle 0x5c for '":;./\attachguestos on domain 0
05-02 00:57:29.724 917-917/? I/QTI_SDM_INFO: [qti_main.c:391] main():Successfully got the watch descriptor for the hex dumps
    [qti_main.c:408] main():Start QTI
05-02 00:57:29.725 917-917/? I/QTI_SDM_INFO: [qti_main.c:497] main():DPL mode only 0
    [qti_rmnet_peripheral.c:801] qti_rmnet_ph_init():Open peripheral file to receive QMI messages
    [qti_rmnet_peripheral.c:747] qti_file_open():Successfully opened device file. FD is 7
    [qti_rmnet_peripheral.c:819] qti_rmnet_ph_init():Opened USB file's fd is 7
05-02 00:57:29.725 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:739] qti_file_open():Could not open device file. Errno 2 error msg=No such file or directory
05-02 00:57:29.726 924-924/? D/QC-time-services: Daemon:genoff_pre_init::Base = 0
    Daemon:ats_rtc_init: Time read from RTC -- year = 70, month = 4,day = 1
05-02 00:57:29.728 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
05-02 00:57:29.730 930-930/? I/NetUtilsWrapper: Unexpected command: /system/bin/iptables -w -W 10000 -t mangle -D PREROUTING -m mark --mark 0x20 -j ACCEPT
05-02 00:57:29.730 924-924/? D/QC-time-services: Daemon ats_rtc_init: seconds = 10429049
    Daemon:Value read from RTC seconds = 10429049000
    Daemon:genoff_init_config: ATS_RTC initialized with rc: 0
    Daemon:genoff_pre_init::Base = 1
    Daemon: Storage Name: ats_1 
    Daemon:Opening File: /mnt/vendor/persist/time/ats_1 /data/vendor/time/ats_1
    Daemon:time_persistent_memory_opr:Genoff Read operation 
05-02 00:57:29.731 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
    [IMS_QMID] |imsqmiserver.c | 541 | QMID#$$#0#QMI DAEMON STARTED
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
05-02 00:57:29.731 926-926/? V//vendor/bin/adsprpcd: vendor/qcom/proprietary/commonsys-intf/adsprpc/src/fastrpc_apps_user.c:1009: remote_handle_open: Successfully opened handle 0xf0490960 for adsp_default_listener on domain 0
05-02 00:57:29.732 926-926/? V//vendor/bin/adsprpcd: vendor/qcom/proprietary/commonsys-intf/adsprpc/src/fastrpc_apps_user.c:1009: remote_handle_open: Successfully opened handle 0x7 for '":;./\geteventfd on domain 0
05-02 00:57:29.732 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
05-02 00:57:29.736 926-944/? E//vendor/bin/adsprpcd: vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for oemconfig.so. (No such file or directory)
05-02 00:57:29.736 883-883/? I/IPAHALService: makeIPAHAL(1, provided)
05-02 00:57:29.739 924-924/? D/QC-time-services: Daemon:Open File: /mnt/vendor/persist/time/ats_1
05-02 00:57:29.740 926-944/? E//vendor/bin/adsprpcd: vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for oemconfig.so. (No such file or directory)
05-02 00:57:29.743 924-924/? D/QC-time-services: Daemon:genoff_pre_init::Base = 2
05-02 00:57:29.743 883-883/? I/ServiceManagement: Registered android.hardware.tetheroffload.control@1.0::IOffloadControl/default (start delay of 306ms)
05-02 00:57:29.743 883-883/? I/IPAHALService: Successfully registered IOffloadControl
05-02 00:57:29.743 924-924/? D/QC-time-services: Daemon: Storage Name: ats_2 
    Daemon:Opening File: /mnt/vendor/persist/time/ats_2 /data/vendor/time/ats_2
    Daemon:time_persistent_memory_opr:Genoff Read operation 
    Daemon:Open File: /mnt/vendor/persist/time/ats_2
05-02 00:57:29.744 765-765/? I/EdXposed: ART hooks installed
05-02 00:57:29.744 765-765/? I/AndroidRuntime: Using default boot image
    Leaving lock profiling enabled
05-02 00:57:29.744 765-765/? I/EdXposed: system_property_get: dalvik.vm.dex2oat-filter -> quicken
    system_property_get: dalvik.vm.dex2oat-flags -> --inline-max-code-units=0
05-02 00:57:29.745 883-883/? I/ServiceManagement: Registered android.hardware.tetheroffload.config@1.0::IOffloadConfig/default (start delay of 308ms)
05-02 00:57:29.745 883-883/? I/IPAHALService: Successfully registered IOffloadConfig
05-02 00:57:29.746 765-765/? I/zygote64: option[0]=-Xzygote
    option[1]=exit
    option[2]=vfprintf
    option[3]=sensitiveThread
    option[4]=-verbose:gc
    option[5]=-Xms8m
    option[6]=-Xmx512m
    option[7]=-XX:HeapGrowthLimit=192m
    option[8]=-XX:HeapMinFree=8m
    option[9]=-XX:HeapMaxFree=16m
    option[10]=-XX:HeapTargetUtilization=0.6
    option[11]=-Xusejit:true
05-02 00:57:29.747 765-765/? I/zygote64: option[12]=-Xjitsaveprofilinginfo
    option[13]=-XjdwpOptions:suspend=n,server=y
    option[14]=-XjdwpProvider:default
    option[15]=-Xlockprofthreshold:500
    option[16]=-Ximage-compiler-option
    option[17]=--runtime-arg
    option[18]=-Ximage-compiler-option
    option[19]=-Xms64m
    option[20]=-Ximage-compiler-option
    option[21]=--runtime-arg
    option[22]=-Ximage-compiler-option
    option[23]=-Xmx64m
05-02 00:57:29.754 931-931/? I/imsrcsd: Uce Service HAL  is starting up...
05-02 00:57:29.760 931-931/? I/imsrcsd: Uce Service HAL  loading imsrcsbaseimpl
09-19 00:10:53.850 956-956/? I/installd: installd firing up
09-19 00:10:53.867 931-931/? I/imsrcsd: Starting Service for First Time imsbaseimpl
09-19 00:10:53.867 931-931/? I/ServiceManagement: Registered com.qualcomm.qti.uceservice@2.0::IUceService/com.qualcomm.qti.uceservice (start delay of 115ms)
09-19 00:10:53.879 931-931/? I/imsrcsd: ImsRcsBaseImpl CM_IMSCONNECTIONMANAGER_CREATE_CONNECTION Before Registering Service
09-19 00:10:53.879 931-931/? I/ServiceManagement: Registered com.qualcomm.qti.imscmservice@2.1::IImsCmService/qti.ims.connectionmanagerservice (start delay of 127ms)
09-19 00:10:53.881 931-931/? I/imsrcsd: ImsRcsBaseImpl CM_IMSCONNECTIONMANAGER_CREATE_CONNECTION After Registering Service
09-19 00:10:53.882 931-931/? I/ServiceManagement: Registered vendor.qti.ims.callinfo@1.0::IService/default (start delay of 130ms)
09-19 00:10:53.883 931-931/? I/imsrcsd: ImsRcsBaseImpl ImsCallInfo After Registering Service
09-19 00:10:53.925 925-925/? I/ThermalEngine: Found field 'set_point'
    Found field 'set_point_clr'
    Found field 'time_constant'
    Found field 'device_perf_floor'
    Created section 'CPU6_HOTPLUG_MONITOR'
    Algo Type 'monitor'
    Parsing section CPU6_HOTPLUG_MONITOR
    Found field 'sampling'
    Found field 'sensor'
    Found field 'thresholds'
    Found field 'thresholds_clr'
    Found field 'actions'
    Found field 'action_info'
    Created section 'CPU7_HOTPLUG_MONITOR'
    Algo Type 'monitor'
    Parsing section CPU7_HOTPLUG_MONITOR
    Found field 'sampling'
    Found field 'sensor'
    Found field 'thresholds'
    Found field 'thresholds_clr'
    Found field 'actions'
    Found field 'action_info'
    Created section 'SKIN-BATTERY-MONITOR'
    Algo Type 'monitor'
    Parsing section SKIN-BATTERY-MONITOR
    Found field 'sampling'
    Found field 'sensor'
    Found field 'thresholds'
    Found field 'thresholds_clr'
    Found field 'actions'
    Found field 'action_info'
09-19 00:10:53.926 925-925/? I/ThermalEngine: Created section 'GPU_management'
    Algo Type 'monitor'
    Parsing section GPU_management
    Found field 'sampling'
    Found field 'sensor'
    Found field 'thresholds'
    Found field 'thresholds_clr'
    Found field 'actions'
    Found field 'action_info'
    Created section 'TEMP_STATE'
    Algo Type 'monitor'
    Parsing section TEMP_STATE
    Found field 'sampling'
    Found field 'sensor'
    Found field 'thresholds'
    Found field 'thresholds_clr'
    Found field 'actions'
    Found field 'action_info'
    Created section 'HISTORY-XO'
    Algo Type 'history'
    Parsing section HISTORY-XO
    Found field 'sampling'
    Found field 'sensor'
    Found field 'thresholds'
    Found field 'thresholds_clr'
    Found field 'actions'
    Found field 'action_info'
    Created section 'HISTORY-CPU0'
    Algo Type 'history'
    Parsing section HISTORY-CPU0
    Found field 'sampling'
    Found field 'sensor'
    Found field 'thresholds'
    Found field 'thresholds_clr'
    Found field 'actions'
    Found field 'action_info'
    Created section 'HISTORY-CPU4'
    Algo Type 'history'
    Parsing section HISTORY-CPU4
    Found field 'sampling'
    Found field 'sensor'
    Found field 'thresholds'
    Found field 'thresholds_clr'
    Found field 'actions'
    Found field 'action_info'
    Created section 'HISTORY-MODEM-PA0'
    Algo Type 'history'
    Parsing section HISTORY-MODEM-PA0
    Found field 'sampling'
    Found field 'sensor'
    Found field 'thresholds'
    Found field 'thresholds_clr'
    Found field 'actions'
    Found field 'action_info'
    Created section 'HISTORY-MODEM-PA1'
09-19 00:10:53.927 925-925/? I/ThermalEngine: Algo Type 'history'
    Parsing section HISTORY-MODEM-PA1
    Found field 'sampling'
    Found field 'sensor'
    Found field 'thresholds'
    Found field 'thresholds_clr'
    Found field 'actions'
    Found field 'action_info'
09-19 00:10:53.927 925-925/? E/ThermalEngine: devices_manager_reg_clnt: Invalid dev cpu.
    pid_algo_init: Device clnt create fail cpu
    devices_manager_reg_clnt: Invalid dev cpu3.
    pid_algo_init: Device clnt create fail cpu3
    devices_manager_reg_clnt: Invalid dev cpu2.
    pid_algo_init: Device clnt create fail cpu2
    devices_manager_reg_clnt: Invalid dev cpu1.
    pid_algo_init: Device clnt create fail cpu1
    devices_manager_reg_clnt: Invalid dev cpu0.
    pid_algo_init: Device clnt create fail cpu0
09-19 00:10:53.927 925-925/? I/ThermalEngine: pid_algo_init: No PID's to be configured.
    [TEMP_STATE]
    algo_type monitor
    sampling 1000
    sensor SKIN-VIRTUAL-SENSOR
    thresholds 58000
    thresholds_clr 48000
    actions temp_state
    action_info 1
    [GPU_management]
    algo_type monitor
    sampling 2000
    sensor SKIN-VIRTUAL-SENSOR
    thresholds 43000 45000
    thresholds_clr 41000 43000
    actions gpu gpu
    action_info 515000000 414000000
    [SKIN-BATTERY-MONITOR]
    algo_type monitor
    sampling 2000
    sensor SKIN-VIRTUAL-SENSOR
    thresholds 37000 39000 41000 43000 44000 60000
    thresholds_clr 35000 37000 39000 41000 43000 44000
    actions battery battery battery battery battery battery
    action_info 0 1 2 3 4 7
    [CPU7_HOTPLUG_MONITOR]
    algo_type monitor
    sampling 2000
    sensor SKIN-VIRTUAL-SENSOR
    thresholds 41000
    thresholds_clr 39000
    actions hotplug_7
    action_info 1
    [CPU6_HOTPLUG_MONITOR]
    algo_type monitor
    sampling 2000
    sensor SKIN-VIRTUAL-SENSOR
    thresholds 43000
    thresholds_clr 41000
    actions hotplug_6
    action_info 1
    [PMIC-ALARM-MONITOR]
    #algo_type monitor
    sampling 1000
    sensor pm8998_tz
    thresholds 107000 127000
    thresholds_clr 103000 123000
    actions hotplug_7+hotplug_6+hotplug_5+hotplug_4+hotplug_3+hotplug_2+hotplug_1+cluster1+cluster0 hotplug_7+hotplug_6+hotplug_5+hotplug_4+hotplug_3+hotplug_2+hotplug_1
    action_info 0+0+0+0+0+0+0+302400+302400 1+1+1+1+1+1+1
    [VDD_RSTR_MONITOR-TSENS21]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor21
    thresholds 5000
09-19 00:10:53.928 925-925/? I/ThermalEngine: thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS20]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor20
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS19]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor19
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS18]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor18
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS17]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor17
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS16]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor16
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS15]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor15
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS14]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor14
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS13]
09-19 00:10:53.928 974-974/? I/wificond: wificond is starting up...
09-19 00:10:53.928 925-925/? I/ThermalEngine: #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor13
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS12]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor12
    thresholds 5000
    thresholds_clr 10000
09-19 00:10:53.929 925-925/? I/ThermalEngine: actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS11]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor11
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS10]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor10
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS9]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor9
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS8]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor8
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS7]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor7
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS4]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor4
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS3]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor3
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS2]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor2
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS1]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor1
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [VDD_RSTR_MONITOR-TSENS0]
    #algo_type monitor
    sampling 1000
    sensor tsens_tz_sensor0
    thresholds 5000
    thresholds_clr 10000
    actions vdd_restriction
    action_info 1
    descending
    [SS-CLUSTER1-SP4]
    algo_type ss
    sampling 2000
    sensor SKIN-VIRTUAL-SENSOR
    device cluster1
    set_point 51000
    set_point_clr 48000
    time_constant 0
    device_perf_floor 1056000
    [SS-CLUSTER1-SP3]
    algo_type ss
    sampling 2000
    sensor SKIN-VIRTUAL-SENSOR
    device cluster1
    set_point 48000
    set_point_clr 45000
    time_constant 0
    device_perf_floor 1344000
    [SS-CLUSTER1-SP2]
    algo_type ss
09-19 00:10:53.930 925-925/? I/ThermalEngine: sampling 2000
    sensor SKIN-VIRTUAL-SENSOR
    device cluster1
    set_point 45000
    set_point_clr 43000
    time_constant 0
    device_perf_floor 1574400
    [SS-CLUSTER1-SP1]
    algo_type ss
    sampling 2000
    sensor SKIN-VIRTUAL-SENSOR
    device cluster1
    set_point 43000
    set_point_clr 41000
    time_constant 0
    device_perf_floor 1728000
    [SS-CLUSTER1-SP0]
    algo_type ss
    sampling 2000
    sensor SKIN-VIRTUAL-SENSOR
    device cluster1
    set_point 39000
    set_point_clr 37000
    time_constant 0
    device_perf_floor 2112000
    [VIRTUAL-GPU-SS]
    #algo_type ss
    sampling 1000
    sensor VIRTUAL-GPU
    device gpu
    set_point 52000
    set_point_clr 48000
    time_constant 0
    device_perf_floor 414000
    [SS-GPU-2]
    #algo_type ss
    sampling 10
    sensor tsens_tz_sensor13
    device gpu
    set_point 95000
    set_point_clr 65000
    time_constant 0
    [SS-GPU-1]
    #algo_type ss
    sampling 10
    sensor tsens_tz_sensor12
    device gpu
    set_point 95000
    set_point_clr 65000
    time_constant 0
    [SS-POPMEM]
    #algo_type ss
    sampling 10
    sensor pop_mem
    device cluster1
    set_point 95000
    set_point_clr 65000
    time_constant 16
    [SPEAKER-CAL]
    sampling 30000 30000 10 1800000
    sensor pm8998_tz
    sensors tsens_tz_sensor14 tsens_tz_sensor15 tsens_tz_sensor16 tsens_tz_sensor17 tsens_tz_sensor18 tsens_tz_sensor19 tsens_tz_sensor20 tsens_tz_sensor21
    temp_range 6000 10000 2000
    max_temp 45000
    offset -4000
    [HISTORY-MODEM-PA1]
    algo_type history
    sampling 1000
    sensor pa_therm1
    thresholds 31000 36000 41000 46000 51000 56000 61000
    thresholds_clr 30000 35000 40000 45000 50000 55000 60000
    actions history_log history_log history_log history_log history_log history_log history_log
    action_info 0 1 2 3 4 5 6
    [HISTORY-MODEM-PA0]
    algo_type history
    sampling 1000
    sensor pa_therm0
    thresholds 31000 36000 41000 46000 51000 56000 61000
    thresholds_clr 30000 35000 40000 45000 50000 55000 60000
    actions history_log history_log history_log history_log history_log history_log history_log
    action_info 0 1 2 3 4 5 6
    [HISTORY-CPU4]
    algo_type history
    sampling 1000
    sensor tsens_tz_sensor7
    thresholds 61000 76000 91000
    thresholds_clr 60000 75000 90000
    actions history_log history_log history_log
    action_info 0 1 2
    [HISTORY-CPU0]
    algo_type history
    sampling 1000
    sensor tsens_tz_sensor1
    thresholds 61000 76000 91000
    thresholds_clr 60000 75000 90000
    actions history_log history_log history_log
    action_info 0 1 2
    [HISTORY-XO]
    algo_type history
    sampling 1000
    sensor xo_therm
    thresholds 31000 41000 46000 51000 56000 61000
    thresholds_clr 30000 40000 45000 50000 55000 60000
    actions history_log history_log history_log history_log history_log history_log
    action_info 0 1 2 3 4 5
09-19 00:10:53.934 784-784/? D/SDM: HWCSession::RegisterCallback: Registering callback: Hotplug
09-19 00:10:53.935 832-832/? I/HWComposer: Switching to legacy multi-display mode
09-19 00:10:53.936 969-969/? I/ServiceManagement: Registered android.frameworks.stats@1.0::IStats/default (start delay of 134ms)
09-19 00:10:53.937 969-969/? W/statsd: statscompanion service unavailable!
09-19 00:10:53.937 832-1086/? W/SurfaceFlinger: Ignoring VSYNC request while display is disconnected
    Ignoring VSYNC request while display is disconnected
09-19 00:10:53.937 832-1087/? W/SurfaceFlinger: Ignoring VSYNC request while display is disconnected
09-19 00:10:53.937 961-961/? I/mediaserver: ServiceManager: 0x710c21a580
09-19 00:10:53.938 784-784/? I/SDM: HWCDisplay::GetHdrCapabilities: HDR is not supported
    HWCDisplay::GetHdrCapabilities: HDR is not supported
09-19 00:10:53.938 784-784/? D/SDM: HWCSession::RegisterCallback: Registering callback: Refresh
    HWCSession::RegisterCallback: Registering callback: Vsync
09-19 00:10:53.940 764-764/? I/netd: Setting up FirewallController hooks: 31.1ms
09-19 00:10:53.941 925-1083/? I/ThermalEngine: no other thermal config be find
09-19 00:10:53.942 925-1082/? E/LimitsPwr: UIO mapping failed
09-19 00:10:53.942 925-1005/? I/ThermalEngine: ADSP thermal mitigation available.
09-19 00:10:53.943 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.keymaster@4.0::IKeymasterDevice/default in either framework or device manifest.
09-19 00:10:53.943 925-1005/? I/ThermalEngine: Mitigation:vdd_restriction[ADSP]:0 pending QMI request succeded
09-19 00:10:53.944 925-1080/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 42000 mC, weight[0] 2
09-19 00:10:53.945 764-764/? I/netd: Setting up TetherController hooks: 4.8ms
09-19 00:10:53.946 925-1080/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
    handle_thresh_sig: SS Id SS-CLUSTER1-SP4, Read SKIN-VIRTUAL-SENSOR 40000mC
09-19 00:10:53.947 925-1080/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 42000 mC, weight[0] 2
09-19 00:10:53.950 764-764/? I/netd: Setting up BandwidthController hooks: 5.3ms
    Setting up IdletimerController hooks: 0.1ms
09-19 00:10:53.952 960-960/? I/keystore: found android.hardware.keymaster@3.0::IKeymasterDevice with interface name default and seclevel TRUSTED_ENVIRONMENT
09-19 00:10:53.952 969-969/? I/statsd: Statsd starts to listen to socket.
09-19 00:10:53.956 925-1080/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
    handle_thresh_sig: SS Id SS-CLUSTER1-SP3, Read SKIN-VIRTUAL-SENSOR 40000mC
09-19 00:10:53.956 764-764/? I/netd: Setting up StrictController hooks: 6.2ms
09-19 00:10:53.956 764-764/? I/ClatdController: Pre-4.9 kernel or pre-P api shipping level - disabling clat ebpf.
09-19 00:10:53.956 764-764/? I/netd: Initializing ClatdController: 0.0ms
    Initializing traffic control: 0.0ms
09-19 00:10:53.957 925-1080/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 42000 mC, weight[0] 2
09-19 00:10:53.958 925-1080/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
    handle_thresh_sig: SS Id SS-CLUSTER1-SP2, Read SKIN-VIRTUAL-SENSOR 40000mC
09-19 00:10:53.964 764-764/? I/netd: Enabling bandwidth control: 7.5ms
09-19 00:10:53.967 764-764/? I/netd: Initializing RouteController: 2.8ms
09-19 00:10:53.967 764-764/? D/XfrmController: XfrmController::ipSecAddXfrmInterface, line=1379
    XfrmController::ipSecRemoveTunnelInterface, line=1592
    deviceName=ipsec_test
    Sending Netlink XFRM Message: XFRM_MSG_FLUSHSA
    Sending Netlink XFRM Message: XFRM_MSG_FLUSHPOLICY
09-19 00:10:53.967 764-764/? I/netd: Initializing XfrmController: 0.8ms
09-19 00:10:53.968 764-764/? E/Netd: Unable to create netlink socket for family 5: Protocol not supported
09-19 00:10:53.968 764-764/? W/Netd: Unable to open qlog quota socket, check if xt_quota2 can send via UeventHandler
09-19 00:10:53.969 764-764/? I/libnetd_resolv: resolv_init: Initializing resolver
09-19 00:10:53.969 1000-1000/? E/wifidisplayhal-service: Start with vendor binder
    Registering wifidisplayhdcphal service...
09-19 00:10:53.969 1000-1000/? I/ServiceManagement: Registered com.qualcomm.qti.wifidisplayhal@1.0::IHDCPSession/wifidisplayhdcphal (start delay of 138ms)
09-19 00:10:53.973 925-1080/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 42000 mC, weight[0] 2
09-19 00:10:53.974 925-1080/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
    handle_thresh_sig: SS Id SS-CLUSTER1-SP1, Read SKIN-VIRTUAL-SENSOR 40000mC
09-19 00:10:53.974 922-922/? E/Sensors: sns_debug_main.c(294):Debug Config File missing in EFS!
09-19 00:10:53.975 925-1080/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 42000 mC, weight[0] 2
    vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:10:53.976 925-1080/? I/ThermalEngine: handle_thresh_sig: SS Id SS-CLUSTER1-SP0, Read SKIN-VIRTUAL-SENSOR 40000mC
    vs_get_temperature: read[0] tsens_tz_sensor13 45000 mC, weight[0] 50
09-19 00:10:53.976 1000-1000/? E/wifidisplayhal-service: Registering wifidisplaydshal service...
09-19 00:10:53.976 1000-1000/? I/ServiceManagement: Registered com.qualcomm.qti.wifidisplayhal@1.0::IDSManager/wifidisplaydshal (start delay of 144ms)
09-19 00:10:53.976 960-960/? I/ServiceManagement: Registered android.system.wifi.keystore@1.0::IKeystore/default (start delay of 195ms)
09-19 00:10:53.977 925-1080/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 50
    handle_thresh_sig: SS Id VIRTUAL-GPU-SS, Read VIRTUAL-GPU 40500mC
    handle_thresh_sig: SS Id SS-GPU-2, Read tsens_tz_sensor13 45000mC
    handle_thresh_sig: SS Id SS-GPU-1, Read tsens_tz_sensor12 44000mC
    handle_thresh_sig: SS Id SS-POPMEM, Read pop_mem 44000mC
09-19 00:10:53.978 925-1079/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 42000 mC, weight[0] 2
09-19 00:10:53.979 925-1079/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
    handle_thresh_sig: TM Id TEMP_STATE Sensor SKIN-VIRTUAL-SENSOR Temp 40000
09-19 00:10:53.981 963-963/? V/MediaUtils: physMem: 5966712832
09-19 00:10:53.982 963-963/? V/MediaUtils: requested limit: 1193342560
09-19 00:10:53.982 963-963/? I/libc: malloc_limit: Allocation limit enabled, max size 1193342560 bytes
09-19 00:10:53.986 925-1079/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 42000 mC, weight[0] 2
09-19 00:10:53.987 925-1079/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
    handle_thresh_sig: TM Id GPU_management Sensor SKIN-VIRTUAL-SENSOR Temp 40000
09-19 00:10:53.987 764-764/? D/MDnsDS: MDnsSdListener::Hander starting up
09-19 00:10:53.988 925-1079/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 42000 mC, weight[0] 2
09-19 00:10:53.989 925-1079/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
    handle_thresh_sig: TM Id SKIN-BATTERY-MONITOR Sensor SKIN-VIRTUAL-SENSOR Temp 40000
    TM Id 'SKIN-BATTERY-MONITOR' Sensor 'SKIN-VIRTUAL-SENSOR' - alarm  raised 2 at 40.0 degC
    TM Id 'SKIN-BATTERY-MONITOR' Sensor 'SKIN-VIRTUAL-SENSOR' - alarm  raised 1 at 40.0 degC
    j=0 i=1 TM Id SKIN-BATTERY-MONITOR Sensor SKIN-VIRTUAL-SENSOR: Action battery value 1
    ACTION: BATTERY - Setting battery charging mitigation to 1
    Mitigation:Battery:1
09-19 00:10:53.990 764-764/? I/netd: Registering NetdNativeService: 2.3ms
09-19 00:10:53.990 925-1079/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 42000 mC, weight[0] 2
09-19 00:10:53.991 925-1079/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
    handle_thresh_sig: TM Id CPU7_HOTPLUG_MONITOR Sensor SKIN-VIRTUAL-SENSOR Temp 40000
09-19 00:10:53.992 963-963/? W//system/bin/mediaextractor: libminijail[963]: failed to get path of fd 5: No such file or directory
    libminijail[963]: allowing syscall: connect
    libminijail[963]: allowing syscall: fcntl
    libminijail[963]: allowing syscall: sendto
    libminijail[963]: allowing syscall: socket
    libminijail[963]: allowing syscall: writev
09-19 00:10:54.002 672-1116/? I/Magisk: ** late_start service mode running
09-19 00:10:54.002 925-1079/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 42000 mC, weight[0] 2
09-19 00:10:54.002 672-1116/? I/Magisk: * Running service.d scripts
09-19 00:10:54.003 925-1079/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
    handle_thresh_sig: TM Id CPU6_HOTPLUG_MONITOR Sensor SKIN-VIRTUAL-SENSOR Temp 40000
09-19 00:10:54.003 963-963/? W//system/bin/mediaextractor: libminijail[963]: logging seccomp filter failures
09-19 00:10:54.003 925-1079/? I/ThermalEngine: handle_thresh_sig: TM Id PMIC-ALARM-MONITOR Sensor pm8998_tz Temp 44756
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS21 Sensor tsens_tz_sensor21 Temp 44000
09-19 00:10:54.004 925-1079/? I/ThermalEngine: handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS20 Sensor tsens_tz_sensor20 Temp 46000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS19 Sensor tsens_tz_sensor19 Temp 48000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS18 Sensor tsens_tz_sensor18 Temp 46000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS17 Sensor tsens_tz_sensor17 Temp 50000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS16 Sensor tsens_tz_sensor16 Temp 53000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS15 Sensor tsens_tz_sensor15 Temp 48000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS14 Sensor tsens_tz_sensor14 Temp 53000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS13 Sensor tsens_tz_sensor13 Temp 45000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS12 Sensor tsens_tz_sensor12 Temp 44000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS11 Sensor tsens_tz_sensor11 Temp 64000
09-19 00:10:54.005 925-1079/? I/ThermalEngine: handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS10 Sensor tsens_tz_sensor10 Temp 72000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS9 Sensor tsens_tz_sensor9 Temp 69000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS8 Sensor tsens_tz_sensor8 Temp 66000
09-19 00:10:54.005 672-1116/? I/Magisk: * Running module service scripts
09-19 00:10:54.005 925-1079/? I/ThermalEngine: handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS7 Sensor tsens_tz_sensor7 Temp 66000
09-19 00:10:54.007 925-1079/? I/ThermalEngine: handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS4 Sensor tsens_tz_sensor4 Temp 63000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS3 Sensor tsens_tz_sensor3 Temp 60000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS2 Sensor tsens_tz_sensor2 Temp 61000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS1 Sensor tsens_tz_sensor1 Temp 63000
    handle_thresh_sig: TM Id VDD_RSTR_MONITOR-TSENS0 Sensor tsens_tz_sensor0 Temp 54000
09-19 00:10:54.014 993-993/? I/media.codec: mediacodecservice starting
09-19 00:10:54.015 993-993/? W/media.codec: libminijail[993]: failed to get path of fd 5: No such file or directory
09-19 00:10:54.016 993-993/? W/media.codec: libminijail[993]: allowing syscall: clock_gettime
    libminijail[993]: allowing syscall: connect
    libminijail[993]: allowing syscall: fcntl64
    libminijail[993]: allowing syscall: socket
    libminijail[993]: allowing syscall: writev
09-19 00:10:54.018 993-993/? W/media.codec: libminijail[993]: logging seccomp filter failures
09-19 00:10:54.019 993-993/? D/vndksupport: Loading libstagefrighthw.so from current namespace instead of sphal namespace.
09-19 00:10:54.021 766-766/? I/EdXposed: using installer org.meowcat.edxposed.manager
    data path prefix: /data/user_de/0/
      application list mode: false
        using whitelist: false
      dynamic modules mode: false
      resources hook: true
      deopt boot image: false
      no module log: false
09-19 00:10:54.022 765-765/? I/EdXposed: using installer org.meowcat.edxposed.manager
    data path prefix: /data/user_de/0/
      application list mode: false
        using whitelist: false
      dynamic modules mode: false
      resources hook: true
      deopt boot image: false
      no module log: false
09-19 00:10:54.022 764-1111/? D/MDnsDS: MDnsSdListener starting to monitor
    Going to poll with pollCount 1
09-19 00:10:54.023 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.usb.gadget@1.0::IUsbGadget/default in either framework or device manifest.
09-19 00:10:54.023 1117-1117/? I/usbd: Usb HAL not found
09-19 00:10:54.024 764-764/? I/ServiceManagement: Registered android.system.net.netd@1.1::INetd/default (start delay of 912ms)
09-19 00:10:54.024 764-764/? I/netd: Registering NetdHwService: 34.3ms
    Netd started in 828ms
09-19 00:10:54.033 870-916/? I/adbd: USB event: FUNCTIONFS_BIND
09-19 00:10:54.034 1081-1081/? I/Atfwd_Daemon: *** Starting ATFWD-daemon *** 
09-19 00:10:54.035 1081-1081/? I/Atfwd_Daemon: init all signals
    Explicitly disbling qmux 
    Disabling QMUX complete...
    getting at svc obj for access terminal QMI svc
     TrtyInit: retryCnt: 1
    Using QCCI. Skipping qmi_init
    result : 1 	 ,Init step :0 	 ,qmiErrorCode: 0
     Back to main.
     tryinit complete with connectresult: 1
     TrtyInit: retryCnt: 1
     qmi_client_init_instance....
09-19 00:10:54.035 993-993/? D/vndksupport: Loading libstagefright_softomx_plugin.so from current namespace instead of sphal namespace.
09-19 00:10:54.042 1097-1120/? D/QCALOG: [location-mq] SRV Socket-Opend
09-19 00:10:54.043 993-993/? I/SoftOMXPlugin: createOMXPlugin
09-19 00:10:54.044 993-993/? D/MediaCodecsXmlParser: parsing /vendor/etc/media_codecs.xml...
09-19 00:10:54.046 993-993/? D/MediaCodecsXmlParser: parsing /vendor/etc/media_codecs_google_audio.xml...
09-19 00:10:54.046 1091-1091/? I/CLD80211: /vendor/bin/cnss-daemon: initialized exit socket pair
    /vendor/bin/cnss-daemon: nlctrl family id: 16 group: svc_msgs mcast_id: 9
09-19 00:10:54.046 993-993/? I/MediaCodecsXmlParser: limit: max-channel-count = 2
    limit: sample-rate-ranges = 8000,11025,12000,16000,22050,24000,32000,44100,48000
    limit: bitrate-range = 8000-320000
    limit: max-channel-count = 1
    limit: sample-rate-ranges = 8000
    limit: bitrate-range = 4750-12200
    limit: max-channel-count = 1
    limit: sample-rate-ranges = 16000
    limit: bitrate-range = 6600-23850
    limit: max-channel-count = 8
    limit: sample-rate-ranges = 7350,8000,11025,12000,16000,22050,24000,32000,44100,48000
    limit: bitrate-range = 8000-960000
    limit: max-channel-count = 1
    limit: sample-rate-ranges = 8000-48000
    limit: bitrate-range = 64000
    limit: max-channel-count = 1
    limit: sample-rate-ranges = 8000-48000
    limit: bitrate-range = 64000
09-19 00:10:54.047 993-993/? I/MediaCodecsXmlParser: limit: max-channel-count = 8
    limit: sample-rate-ranges = 8000-96000
    limit: bitrate-range = 32000-500000
    limit: max-channel-count = 8
    limit: sample-rate-ranges = 48000
    limit: bitrate-range = 6000-510000
    limit: max-channel-count = 8
    limit: sample-rate-ranges = 8000-192000
    limit: bitrate-range = 1-10000000
    limit: max-channel-count = 8
    limit: sample-rate-ranges = 1-655350
    limit: bitrate-range = 1-21000000
    limit: max-channel-count = 6
    limit: sample-rate-ranges = 8000,11025,12000,16000,22050,24000,32000,44100,48000
    limit: bitrate-range = 8000-960000
    limit: max-channel-count = 1
    limit: sample-rate-ranges = 8000
    limit: bitrate-range = 4750-12200
    limit: feature-bitrate-modes = CBR
    limit: max-channel-count = 1
    limit: sample-rate-ranges = 16000
    limit: bitrate-range = 6600-23850
    limit: feature-bitrate-modes = CBR
    limit: max-channel-count = 2
    limit: sample-rate-ranges = 1-655350
    limit: bitrate-range = 1-21000000
    limit: complexity-default = 5
    limit: complexity-range = 0-8
    limit: feature-bitrate-modes = CQ
09-19 00:10:54.047 993-993/? D/MediaCodecsXmlParser: parsing /vendor/etc/media_codecs_google_telephony.xml...
09-19 00:10:54.048 993-993/? I/MediaCodecsXmlParser: limit: max-channel-count = 1
    limit: sample-rate-ranges = 8000
    limit: bitrate-range = 13000
    limit: size-range = 96x96-4096x2160
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-979200
    limit: bitrate-range = 1-100000000
    limit: frame-rate-range = 1-240
    limit: max-concurrent-instances = 16
    limit: feature-can-swap-width-height = 0
    limit: performance-point-3840x2160-range = 24-24
    limit: size-range = 96x64-1920x1088
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-489600
    limit: bitrate-range = 1-60000000
    limit: frame-rate-range = 1-240
    limit: max-concurrent-instances = 16
    limit: performance-point-1920x1088-range = 30-30
    limit: size-range = 96x64-864x480
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-48600
    limit: bitrate-range = 1-2000000
    limit: frame-rate-range = 1-240
    limit: max-concurrent-instances = 16
    limit: performance-point-720x480-range = 30-30
    limit: size-range = 96x64-3840x2160
    limit: alignment = 2x2
09-19 00:10:54.049 993-993/? I/MediaCodecsXmlParser: limit: block-size = 16x16
    limit: blocks-per-second-range = 1-979200
    limit: bitrate-range = 1-100000000
    limit: frame-rate-range = 1-240
    limit: max-concurrent-instances = 16
    limit: performance-point-3840x2160-range = 30-30
    limit: size-range = 162x64-4096x2160
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-979200
09-19 00:10:54.049 585-998/? W/libc: Unable to set property "ctl.interface_start" to "android.hardware.graphics.composer@2.1::IComposer/default": error code: 0x20
09-19 00:10:54.049 993-993/? I/MediaCodecsXmlParser: limit: bitrate-range = 1-100000000
    limit: frame-rate-range = 1-240
    limit: max-concurrent-instances = 16
    limit: performance-point-3840x2160-range = 24-24
09-19 00:10:54.049 585-998/? E/hwservicemanager: Failed to set property for starting android.hardware.graphics.composer@2.1::IComposer/default
09-19 00:10:54.049 993-993/? I/MediaCodecsXmlParser: limit: size-range = 64x64-4096x2160
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-1958400
    limit: bitrate-range = 1-100000000
    limit: frame-rate-range = 1-240
    limit: feature-adaptive-playback = 0
    limit: max-concurrent-instances = 16
    limit: feature-can-swap-width-height = 0
    limit: performance-point-3840x2160-range = 60-60
09-19 00:10:54.049 585-996/? W/libc: Unable to set property "ctl.interface_start" to "android.hardware.graphics.composer@2.1::IComposer/default": error code: 0x20
09-19 00:10:54.049 993-993/? I/MediaCodecsXmlParser: limit: size-range = 64x64-3840x2160
09-19 00:10:54.049 585-996/? E/hwservicemanager: Failed to set property for starting android.hardware.graphics.composer@2.1::IComposer/default
09-19 00:10:54.049 993-993/? I/MediaCodecsXmlParser: limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-1958400
    limit: bitrate-range = 1-35000000
    limit: frame-rate-range = 1-30
    limit: feature-adaptive-playback = 0
    limit: feature-secure-playback = 1
    limit: max-concurrent-instances = 6
    limit: performance-point-3840x2160-range = 60-60
    limit: size-range = 64x64-1920x1088
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-489600
    limit: bitrate-range = 1-60000000
09-19 00:10:54.050 993-993/? I/MediaCodecsXmlParser: limit: frame-rate-range = 1-240
    limit: feature-adaptive-playback = 0
    limit: max-concurrent-instances = 16
    limit: performance-point-1920x1088-range = 60-60
    limit: size-range = 96x64-1920x1088
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-244800
    limit: bitrate-range = 1-40000000
    limit: frame-rate-range = 1-240
    limit: feature-adaptive-playback = 0
    limit: max-concurrent-instances = 16
    limit: performance-point-1920x1088-range = 30-30
    limit: size-range = 96x64-1920x1088
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-244800
    limit: bitrate-range = 1-20000000
    limit: frame-rate-range = 1-30
    limit: feature-adaptive-playback = 0
    limit: feature-secure-playback = 1
    limit: max-concurrent-instances = 6
    limit: performance-point-1920x1088-range = 30-30
    limit: size-range = 64x64-864x480
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-489600
    limit: bitrate-range = 1-2000000
    limit: frame-rate-range = 1-240
    limit: feature-adaptive-playback = 0
    limit: max-concurrent-instances = 16
    limit: performance-point-720x480-range = 30-30
    limit: size-range = 64x64-3840x2160
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-979200
    limit: bitrate-range = 1-100000000
    limit: frame-rate-range = 1-240
    limit: feature-adaptive-playback = 0
    limit: max-concurrent-instances = 16
09-19 00:10:54.051 993-993/? I/MediaCodecsXmlParser: limit: performance-point-3840x2160-range = 60-60
    limit: size-range = 64x64-3840x2160
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-979200
    limit: bitrate-range = 1-100000000
    limit: frame-rate-range = 1-240
    limit: feature-adaptive-playback = 0
    limit: max-concurrent-instances = 16
    limit: performance-point-3840x2160-range = 60-60
    limit: size-range = 64x64-3840x2160
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-979200
    limit: bitrate-range = 1-35000000
    limit: frame-rate-range = 1-30
    limit: feature-adaptive-playback = 0
    limit: feature-secure-playback = 1
    limit: max-concurrent-instances = 6
    limit: performance-point-3840x2160-range = 60-60
    limit: size-range = 64x64-4096x2160
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-1958400
    limit: bitrate-range = 1-100000000
    limit: frame-rate-range = 1-240
    limit: feature-adaptive-playback = 0
    limit: max-concurrent-instances = 16
    limit: performance-point-3840x2160-range = 60-60
    limit: size-range = 64x64-3840x2160
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: blocks-per-second-range = 1-1958400
    limit: bitrate-range = 1-35000000
    limit: frame-rate-range = 1-30
    limit: feature-adaptive-playback = 0
    limit: feature-secure-playback = 1
    limit: max-concurrent-instances = 6
09-19 00:10:54.052 993-993/? I/MediaCodecsXmlParser: limit: performance-point-3840x2160-range = 60-60
09-19 00:10:54.052 993-993/? D/MediaCodecsXmlParser: parsing /vendor/etc/media_codecs_google_video.xml...
09-19 00:10:54.052 755-755/? I/Riru: found Riru in zygote64 (pid=765)
09-19 00:10:54.052 755-755/? V/Riru: check again after 1s, remaining 2 times
09-19 00:10:54.059 1091-1137/? E/QMI_FW: QMUXD: WARNING qmi_qmux_if_pwr_up_init failed! rc=-6
09-19 00:10:54.061 993-993/? I/MediaCodecsXmlParser: limit: size-range = 2x2-352x288
    limit: alignment = 2x2
    limit: block-size = 16x16
09-19 00:10:54.062 993-993/? I/MediaCodecsXmlParser: limit: blocks-per-second-range = 12-11880
    limit: bitrate-range = 1-384000
    limit: feature-adaptive-playback = 0
    limit: size-range = 2x2-352x288
    limit: alignment = 2x2
    limit: bitrate-range = 1-384000
    limit: feature-adaptive-playback = 0
    limit: size-range = 2x2-4080x4080
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: block-count-range = 1-32768
    limit: blocks-per-second-range = 1-1966080
    limit: bitrate-range = 1-48000000
    limit: feature-adaptive-playback = 0
    limit: size-range = 2x2-4096x4096
    limit: alignment = 2x2
    limit: block-size = 8x8
    limit: block-count-range = 1-196608
    limit: blocks-per-second-range = 1-2000000
    limit: bitrate-range = 1-10000000
    limit: feature-adaptive-playback = 0
    limit: size-range = 2x2-2048x2048
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: block-count-range = 1-16384
    limit: blocks-per-second-range = 1-1000000
    limit: bitrate-range = 1-40000000
    limit: feature-adaptive-playback = 0
    limit: size-range = 2x2-2048x2048
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: block-count-range = 1-16384
    limit: blocks-per-second-range = 1-500000
    limit: bitrate-range = 1-40000000
    limit: feature-adaptive-playback = 0
    limit: size-range = 176x144-176x144
    limit: alignment = 16x16
    limit: bitrate-range = 1-128000
    limit: size-range = 16x16-2048x2048
    limit: alignment = 2x2
    limit: block-size = 16x16
09-19 00:10:54.063 993-993/? I/MediaCodecsXmlParser: limit: block-count-range = 1-8192
    limit: blocks-per-second-range = 1-245760
    limit: bitrate-range = 1-12000000
    limit: feature-intra-refresh = 0
    limit: size-range = 16x16-176x144
    limit: alignment = 16x16
    limit: block-size = 16x16
    limit: blocks-per-second-range = 12-1485
    limit: bitrate-range = 1-64000
    limit: size-range = 2x2-2048x2048
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: block-count-range = 1-16384
    limit: bitrate-range = 1-40000000
    limit: feature-bitrate-modes = VBR,CBR
    limit: size-range = 2x2-2048x2048
    limit: alignment = 2x2
    limit: block-size = 16x16
    limit: block-count-range = 1-3600
    limit: bitrate-range = 1-40000000
    limit: feature-bitrate-modes = VBR,CBR
09-19 00:10:54.063 993-993/? D/MediaCodecsXmlParser: parsing /vendor/etc/media_codecs_performance.xml...
09-19 00:10:54.064 993-993/? I/MediaCodecsXmlParser: limit: measured-frame-rate-320x240-range = 238-238
    limit: measured-frame-rate-720x480-range = 123-123
    limit: measured-frame-rate-1280x720-range = 50-50
    limit: measured-frame-rate-1920x1080-range = 16-40
    limit: measured-frame-rate-320x240-range = 80-200
    limit: measured-frame-rate-720x480-range = 100-150
    limit: measured-frame-rate-1280x720-range = 45-55
    limit: measured-frame-rate-1920x1080-range = 16-45
    limit: measured-frame-rate-3840x2160-range = 6-24
    limit: measured-frame-rate-176x144-range = 120-130
    limit: measured-frame-rate-352x288-range = 80-80
    limit: measured-frame-rate-176x144-range = 120-135
    limit: measured-frame-rate-352x288-range = 100-110
    limit: measured-frame-rate-640x480-range = 80-100
    limit: measured-frame-rate-320x180-range = 100-110
    limit: measured-frame-rate-640x360-range = 100-100
    limit: measured-frame-rate-1280x720-range = 49-49
    limit: measured-frame-rate-1920x1080-range = 16-40
    limit: measured-frame-rate-320x240-range = 215-215
    limit: measured-frame-rate-720x480-range = 100-100
    limit: measured-frame-rate-1280x720-range = 56-56
    limit: measured-frame-rate-1920x1080-range = 30-30
09-19 00:10:54.064 993-993/? D/MediaCodecsXmlParser: MediaCodec: cannot update non-existing codec at line 58 of /vendor/etc/media_codecs_performance.xml
09-19 00:10:54.064 993-993/? I/MediaCodecsXmlParser: limit: measured-frame-rate-176x144-range = 200-200
09-19 00:10:54.064 993-993/? D/MediaCodecsXmlParser: MediaCodec: cannot update non-existing codec at line 67 of /vendor/etc/media_codecs_performance.xml
09-19 00:10:54.064 993-993/? I/MediaCodecsXmlParser: limit: measured-frame-rate-176x144-range = 370-390
09-19 00:10:54.064 993-993/? D/MediaCodecsXmlParser: MediaCodec: cannot update non-existing codec at line 73 of /vendor/etc/media_codecs_performance.xml
09-19 00:10:54.064 993-993/? I/MediaCodecsXmlParser: limit: measured-frame-rate-320x180-range = 68-70
    limit: measured-frame-rate-640x360-range = 32-32
    limit: measured-frame-rate-1280x720-range = 17-24
09-19 00:10:54.065 993-993/? I/MediaCodecsXmlParser: limit: measured-frame-rate-1920x1080-range = 8-12
09-19 00:10:54.065 993-993/? D/MediaCodecsXmlParser: MediaCodec: cannot update non-existing codec at line 82 of /vendor/etc/media_codecs_performance.xml
09-19 00:10:54.065 993-993/? I/MediaCodecsXmlParser: limit: measured-frame-rate-320x180-range = 205-205
    limit: measured-frame-rate-640x360-range = 68-68
    limit: measured-frame-rate-1280x720-range = 17-17
09-19 00:10:54.065 993-993/? D/MediaCodecsXmlParser: MediaCodec: cannot update non-existing codec at line 93 of /vendor/etc/media_codecs_performance.xml
09-19 00:10:54.065 993-993/? I/MediaCodecsXmlParser: limit: measured-frame-rate-320x240-range = 455-455
    limit: measured-frame-rate-720x480-range = 360-360
    limit: measured-frame-rate-1280x720-range = 300-300
    limit: measured-frame-rate-1920x1088-range = 240-240
    limit: measured-frame-rate-352x288-range = 87-285
    limit: measured-frame-rate-640x360-range = 85-227
    limit: measured-frame-rate-720x480-range = 80-230
    limit: measured-frame-rate-1280x720-range = 269-269
    limit: measured-frame-rate-1920x1080-range = 254-254
    limit: measured-frame-rate-3840x2160-range = 70-70
    limit: measured-frame-rate-176x144-range = 435-435
    limit: measured-frame-rate-352x288-range = 425-425
    limit: measured-frame-rate-176x144-range = 487-487
    limit: measured-frame-rate-480x360-range = 360-360
    limit: measured-frame-rate-320x180-range = 400-400
    limit: measured-frame-rate-640x360-range = 350-350
    limit: measured-frame-rate-1280x720-range = 308-308
    limit: measured-frame-rate-1920x1080-range = 146-146
    limit: measured-frame-rate-320x180-range = 280-280
    limit: measured-frame-rate-640x360-range = 270-270
    limit: measured-frame-rate-1280x720-range = 260-260
    limit: measured-frame-rate-1920x1080-range = 155-155
    limit: measured-frame-rate-3840x2160-range = 36-36
    limit: measured-frame-rate-320x240-range = 410-410
    limit: measured-frame-rate-720x480-range = 129-129
    limit: measured-frame-rate-1280x720-range = 111-112
    limit: measured-frame-rate-1920x1080-range = 24-24
09-19 00:10:54.065 993-993/? D/MediaCodecsXmlParser: MediaCodec: cannot update non-existing codec at line 139 of /vendor/etc/media_codecs_performance.xml
09-19 00:10:54.066 993-993/? I/MediaCodecsXmlParser: limit: measured-frame-rate-176x144-range = 160-160
    limit: measured-frame-rate-352x288-range = 172-172
09-19 00:10:54.066 993-993/? D/MediaCodecsXmlParser: MediaCodec: cannot update non-existing codec at line 149 of /vendor/etc/media_codecs_performance.xml
09-19 00:10:54.066 993-993/? I/MediaCodecsXmlParser: limit: measured-frame-rate-352x288-range = 340-340
    limit: measured-frame-rate-640x360-range = 200-200
    limit: measured-frame-rate-720x480-range = 180-180
    limit: measured-frame-rate-1280x720-range = 80-80
    limit: measured-frame-rate-1920x1080-range = 40-40
09-19 00:10:54.066 993-993/? D/MediaCodecsXmlParser: MediaCodec: cannot update non-existing codec at line 160 of /vendor/etc/media_codecs_performance.xml
09-19 00:10:54.066 993-993/? I/MediaCodecsXmlParser: limit: measured-frame-rate-176x144-range = 165-165
09-19 00:10:54.066 993-993/? D/MediaCodecsXmlParser: MediaCodec: cannot update non-existing codec at line 172 of /vendor/etc/media_codecs_performance.xml
09-19 00:10:54.066 993-993/? I/MediaCodecsXmlParser: limit: measured-frame-rate-320x180-range = 170-500
    limit: measured-frame-rate-320x240-range = 1318-1318
    limit: measured-frame-rate-640x360-range = 100-110
    limit: measured-frame-rate-1280x720-range = 100-100
    limit: measured-frame-rate-1920x1080-range = 40-40
09-19 00:10:54.066 993-993/? D/MediaCodecsXmlParser: MediaCodec: cannot update non-existing codec at line 184 of /vendor/etc/media_codecs_performance.xml
09-19 00:10:54.066 993-993/? I/MediaCodecsXmlParser: limit: measured-frame-rate-320x240-range = 472-472
    limit: measured-frame-rate-640x360-range = 177-177
    limit: measured-frame-rate-1280x720-range = 90-90
    limit: measured-frame-rate-1920x1080-range = 54-54
09-19 00:10:54.066 993-993/? D/MediaCodecsXmlParser: MediaCodec: cannot update non-existing codec at line 197 of /vendor/etc/media_codecs_performance.xml
    Cannot find /data/misc/media/media_codecs_profiling_results.xml
09-19 00:10:54.070 1115-1115/? I//system/bin/tombstoned: tombstoned successfully initialized
09-19 00:10:54.076 993-993/? I/ServiceManagement: Registered android.hardware.media.omx@1.0::IOmx/default (start delay of 254ms)
    Removing namespace from process name android.hardware.media.omx@1.0-service to omx@1.0-service.
09-19 00:10:54.077 993-993/? I/media.codec: IOmx HAL service created.
09-19 00:10:54.078 993-993/? D/MediaCodecsXmlParser: parsing /vendor/etc/media_codecs.xml...
    parsing /vendor/etc/media_codecs_google_audio.xml...
09-19 00:10:54.078 993-993/? I/MediaCodecsXmlParser: limit: max-channel-count = 2
    limit: sample-rate-ranges = 8000,11025,12000,16000,22050,24000,32000,44100,48000
    limit: bitrate-range = 8000-320000
    limit: max-channel-count = 1
    limit: sample-rate-ranges = 8000
    limit: bitrate-range = 4750-12200
    limit: max-channel-count = 1
    limit: sample-rate-ranges = 16000
    limit: bitrate-range = 6600-23850
    limit: max-channel-count = 8
    limit: sample-rate-ranges = 7350,8000,11025,12000,16000,22050,24000,32000,44100,48000
    limit: bitrate-range = 8000-960000
09-19 00:10:54.094 1114-1114/? I/gatekeeperd: Starting gatekeeperd...
09-19 00:10:54.101 1119-1119/? I/vendor.lineage.livedisplay@2.0-service-sdm: LiveDisplay HAL service is starting.
09-19 00:10:54.113 1119-1119/? I/ServiceManagement: Registered vendor.lineage.livedisplay@2.0::IPictureAdjustment/default (start delay of 111ms)
    Removing namespace from process name vendor.lineage.livedisplay@2.0-service-sdm to livedisplay@2.0-service-sdm.
09-19 00:10:54.113 766-766/? D/ICU: Time zone APEX file found: /apex/com.android.tzdata/etc/icu/icu_tzdata.dat
09-19 00:10:54.116 1118-1118/? D/vndksupport: Loading /vendor/lib64/hw/fingerprint.fpc.msm8998.so from current namespace instead of sphal namespace.
09-19 00:10:54.116 765-765/? D/ICU: Time zone APEX file found: /apex/com.android.tzdata/etc/icu/icu_tzdata.dat
09-19 00:10:54.117 1119-1119/? I/ServiceManagement: Registered vendor.lineage.livedisplay@2.0::IDisplayModes/default (start delay of 115ms)
    Removing namespace from process name vendor.lineage.livedisplay@2.0-service-sdm to livedisplay@2.0-service-sdm.
09-19 00:10:54.117 1119-1119/? I/vendor.lineage.livedisplay@2.0-service-sdm: LiveDisplay HAL service is ready.
09-19 00:10:54.119 1134-1134/? I/LOWI-8.6.0.33: [MessageQ_Client] connecting to server [/dev/socket/location/mq/location-mq-s]
    [MessageQ_Client] connected
    [LOWIController] loadConfigItems: Log level = 3, Cache Records = 100, max queue size = 255, fresh scan threshold = 500
09-19 00:10:54.119 1134-1134/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:54.119 1134-1134/? E/LOWI-8.6.0.33: [LOWIDiagLog] Diag logging could not be enabled
09-19 00:10:54.120 1134-1152/? I/LOWI-8.6.0.33: [LOWIController] Client controller entering event loop
09-19 00:10:54.123 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:54.138 1135-1135/? D/LocSvc_LBSProxy: checkIfLocationExtendedClientExists] File does not Exist
09-19 00:10:54.141 1135-1157/? E/QMI_FW: QMUXD: WARNING qmi_qmux_if_pwr_up_init failed! rc=-6
09-19 00:10:54.147 1118-1118/? D/fpc_fingerprint_hal: fpc_hal_open
09-19 00:10:54.147 1118-1118/? I/fpc_tac: fpc_hw_resource_init  entry
09-19 00:10:54.154 1135-1135/? E/LocSvc_LocIpc: sendData:193] cannot send to socket. reason:No such file or directory
09-19 00:10:54.157 765-765/? V/Riru: jniRegisterNativeMethods com/android/internal/os/RuntimeInit
    jniRegisterNativeMethods com/android/internal/os/ZygoteInit
    jniRegisterNativeMethods android/os/SystemClock
09-19 00:10:54.158 766-766/? V/Riru: jniRegisterNativeMethods com/android/internal/os/RuntimeInit
    jniRegisterNativeMethods com/android/internal/os/ZygoteInit
    jniRegisterNativeMethods android/os/SystemClock
09-19 00:10:54.159 926-944/? E//vendor/bin/adsprpcd: vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for custom_sm_ecns_1.so.1. (No such file or directory)
    vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for custom_sm_ecns_2.so.1. (No such file or directory)
09-19 00:10:54.160 926-944/? E//vendor/bin/adsprpcd: vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for custom_dm_ecns_1.so.1. (No such file or directory)
    vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for custom_dm_ecns_2.so.1. (No such file or directory)
    vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for custom_qm_ecns_1.so.1. (No such file or directory)
    vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for custom_qm_ecns_2.so.1. (No such file or directory)
09-19 00:10:54.161 926-944/? E//vendor/bin/adsprpcd: vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for capi_v2_dummy_ecns.so.1. (No such file or directory)
    vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for capi_v2_voice_imc_tx.so.1. (No such file or directory)
    vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for capi_v2_dummy_ecns.so.1. (No such file or directory)
    vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for capi_v2_voice_imc_rx.so.1. (No such file or directory)
09-19 00:10:54.161 766-766/? V/Riru: jniRegisterNativeMethods android/util/EventLog
09-19 00:10:54.162 766-766/? V/Riru: jniRegisterNativeMethods android/util/Log
    jniRegisterNativeMethods android/util/MemoryIntArray
    jniRegisterNativeMethods android/util/PathParser
    jniRegisterNativeMethods android/util/StatsLog
    jniRegisterNativeMethods android/util/StatsLogInternal
09-19 00:10:54.163 766-766/? V/Riru: jniRegisterNativeMethods android/app/admin/SecurityLog
09-19 00:10:54.163 926-944/? E//vendor/bin/adsprpcd: vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for capi_v2_dummy_ecns.so.1. (No such file or directory)
09-19 00:10:54.163 765-765/? V/Riru: jniRegisterNativeMethods android/util/EventLog
    jniRegisterNativeMethods android/util/Log
    jniRegisterNativeMethods android/util/MemoryIntArray
    jniRegisterNativeMethods android/util/PathParser
    jniRegisterNativeMethods android/util/StatsLog
    jniRegisterNativeMethods android/util/StatsLogInternal
09-19 00:10:54.164 766-766/? V/Riru: jniRegisterNativeMethods android/content/res/AssetManager
    jniRegisterNativeMethods android/content/res/StringBlock
    jniRegisterNativeMethods android/content/res/XmlBlock
    jniRegisterNativeMethods android/content/res/ApkAssets
    jniRegisterNativeMethods android/text/AndroidCharacter
    jniRegisterNativeMethods android/text/Hyphenator
    jniRegisterNativeMethods android/view/KeyCharacterMap
    jniRegisterNativeMethods android/os/Process
    jniRegisterNativeMethods android/os/SystemProperties
09-19 00:10:54.164 766-766/? I/Riru: replaced android.os.SystemProperties#native_set
09-19 00:10:54.164 766-766/? V/Riru: jniRegisterNativeMethods android/os/Binder
09-19 00:10:54.164 765-765/? V/Riru: jniRegisterNativeMethods android/app/admin/SecurityLog
    jniRegisterNativeMethods android/content/res/AssetManager
09-19 00:10:54.165 765-765/? V/Riru: jniRegisterNativeMethods android/content/res/StringBlock
    jniRegisterNativeMethods android/content/res/XmlBlock
    jniRegisterNativeMethods android/content/res/ApkAssets
    jniRegisterNativeMethods android/text/AndroidCharacter
    jniRegisterNativeMethods android/text/Hyphenator
    jniRegisterNativeMethods android/view/KeyCharacterMap
    jniRegisterNativeMethods android/os/Process
    jniRegisterNativeMethods android/os/SystemProperties
09-19 00:10:54.165 765-765/? I/Riru: replaced android.os.SystemProperties#native_set
09-19 00:10:54.165 765-765/? V/Riru: jniRegisterNativeMethods android/os/Binder
09-19 00:10:54.178 1118-1118/? D/fpc_tac: 'modalias'='of:Nfingerprint_fpcT<NULL>Cfpc,' found on  path '/sys/bus/platform/devices/soc:fingerprint_fpc/'
09-19 00:10:54.179 765-765/? V/Riru: jniRegisterNativeMethods com/android/internal/os/BinderInternal
    jniRegisterNativeMethods android/os/BinderProxy
09-19 00:10:54.181 766-766/? V/Riru: jniRegisterNativeMethods com/android/internal/os/BinderInternal
    jniRegisterNativeMethods android/os/BinderProxy
09-19 00:10:54.188 964-964/? I/mediametrics: ServiceManager: 0x7dc87ac280
09-19 00:10:54.188 964-964/? D/MediaAnalyticsService: MediaAnalyticsService created
09-19 00:10:54.193 923-923/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:54.195 1118-1118/? I/fpc_tac: fpc_hw_resource_init  OK
09-19 00:10:54.197 765-765/? V/Riru: jniRegisterNativeMethods android/os/Parcel
    jniRegisterNativeMethods android/os/HidlSupport
    jniRegisterNativeMethods android/os/HwBinder
    jniRegisterNativeMethods android/os/HwBlob
    jniRegisterNativeMethods android/os/HwParcel
09-19 00:10:54.198 765-765/? V/Riru: jniRegisterNativeMethods android/os/HwRemoteBinder
    jniRegisterNativeMethods android/os/VintfObject
    jniRegisterNativeMethods android/os/VintfRuntimeInfo
    jniRegisterNativeMethods android/graphics/Canvas
    jniRegisterNativeMethods android/graphics/BaseCanvas
    jniRegisterNativeMethods android/graphics/BaseRecordingCanvas
    jniRegisterNativeMethods android/graphics/ColorSpace$Rgb
09-19 00:10:54.201 965-965/? I/mediaserver: ServiceManager: 0xf43232a0
09-19 00:10:54.201 965-965/? W/BatteryNotifier: batterystats service unavailable!
    batterystats service unavailable!
09-19 00:10:54.203 766-766/? V/Riru: jniRegisterNativeMethods android/os/Parcel
    jniRegisterNativeMethods android/os/HidlSupport
    jniRegisterNativeMethods android/os/HwBinder
    jniRegisterNativeMethods android/os/HwBlob
09-19 00:10:54.204 766-766/? V/Riru: jniRegisterNativeMethods android/os/HwParcel
    jniRegisterNativeMethods android/os/HwRemoteBinder
    jniRegisterNativeMethods android/os/VintfObject
    jniRegisterNativeMethods android/os/VintfRuntimeInfo
    jniRegisterNativeMethods android/graphics/Canvas
    jniRegisterNativeMethods android/graphics/BaseCanvas
    jniRegisterNativeMethods android/graphics/BaseRecordingCanvas
    jniRegisterNativeMethods android/graphics/ColorSpace$Rgb
09-19 00:10:54.206 1050-1050/? I//apex/com.android.media.swcodec/bin/mediaswcodec: media swcodec service starting
09-19 00:10:54.208 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
    [IMS_DataD] imsdatad.c | 5855 | | 1132 |DATAD#$$#0#DATAD STARTED
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:54.209 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:54.209 765-765/? V/Riru: jniRegisterNativeMethods android/view/DisplayEventReceiver
09-19 00:10:54.209 766-766/? V/Riru: jniRegisterNativeMethods android/view/DisplayEventReceiver
09-19 00:10:54.209 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/RenderNode
09-19 00:10:54.209 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/RenderNode
09-19 00:10:54.209 765-765/? V/Riru: jniRegisterNativeMethods android/view/RenderNodeAnimator
09-19 00:10:54.209 766-766/? V/Riru: jniRegisterNativeMethods android/view/RenderNodeAnimator
09-19 00:10:54.209 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/RecordingCanvas
09-19 00:10:54.209 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/RecordingCanvas
09-19 00:10:54.209 765-765/? V/Riru: jniRegisterNativeMethods android/view/InputApplicationHandle
09-19 00:10:54.209 766-766/? V/Riru: jniRegisterNativeMethods android/view/InputApplicationHandle
09-19 00:10:54.209 765-765/? V/Riru: jniRegisterNativeMethods android/view/InputWindowHandle
09-19 00:10:54.209 766-766/? V/Riru: jniRegisterNativeMethods android/view/InputWindowHandle
09-19 00:10:54.209 765-765/? V/Riru: jniRegisterNativeMethods android/view/TextureLayer
09-19 00:10:54.209 766-766/? V/Riru: jniRegisterNativeMethods android/view/TextureLayer
09-19 00:10:54.209 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/HardwareRenderer
09-19 00:10:54.209 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/HardwareRenderer
09-19 00:10:54.209 765-765/? V/Riru: jniRegisterNativeMethods android/view/Surface
09-19 00:10:54.209 766-766/? V/Riru: jniRegisterNativeMethods android/view/Surface
09-19 00:10:54.209 765-765/? V/Riru: jniRegisterNativeMethods android/view/SurfaceControl
09-19 00:10:54.209 766-766/? V/Riru: jniRegisterNativeMethods android/view/SurfaceControl
09-19 00:10:54.210 765-765/? V/Riru: jniRegisterNativeMethods android/view/SurfaceSession
09-19 00:10:54.210 766-766/? V/Riru: jniRegisterNativeMethods android/view/SurfaceSession
09-19 00:10:54.210 765-765/? V/Riru: jniRegisterNativeMethods android/view/CompositionSamplingListener
09-19 00:10:54.210 766-766/? V/Riru: jniRegisterNativeMethods android/view/CompositionSamplingListener
09-19 00:10:54.210 765-765/? V/Riru: jniRegisterNativeMethods android/view/TextureView
09-19 00:10:54.210 766-766/? V/Riru: jniRegisterNativeMethods android/view/TextureView
09-19 00:10:54.210 765-765/? V/Riru: jniRegisterNativeMethods com/android/internal/view/animation/NativeInterpolatorFactoryHelper
09-19 00:10:54.210 766-766/? V/Riru: jniRegisterNativeMethods com/android/internal/view/animation/NativeInterpolatorFactoryHelper
09-19 00:10:54.210 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:10:54.210 766-766/? V/Riru: jniRegisterNativeMethods com/google/android/gles_jni/EGLImpl
09-19 00:10:54.210 765-765/? V/Riru: jniRegisterNativeMethods com/google/android/gles_jni/EGLImpl
09-19 00:10:54.210 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:54.210 765-765/? V/Riru: jniRegisterNativeMethods com/google/android/gles_jni/GLImpl
09-19 00:10:54.210 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:10:54.210 766-766/? V/Riru: jniRegisterNativeMethods com/google/android/gles_jni/GLImpl
09-19 00:10:54.210 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:54.211 765-765/? V/Riru: jniRegisterNativeMethods android/opengl/EGL14
    jniRegisterNativeMethods android/opengl/EGL15
    jniRegisterNativeMethods android/opengl/EGLExt
    jniRegisterNativeMethods android/opengl/GLES10
09-19 00:10:54.211 766-766/? V/Riru: jniRegisterNativeMethods android/opengl/EGL14
    jniRegisterNativeMethods android/opengl/EGL15
    jniRegisterNativeMethods android/opengl/EGLExt
    jniRegisterNativeMethods android/opengl/GLES10
09-19 00:10:54.211 765-765/? V/Riru: jniRegisterNativeMethods android/opengl/GLES10Ext
    jniRegisterNativeMethods android/opengl/GLES11
    jniRegisterNativeMethods android/opengl/GLES11Ext
09-19 00:10:54.211 766-766/? V/Riru: jniRegisterNativeMethods android/opengl/GLES10Ext
    jniRegisterNativeMethods android/opengl/GLES11
09-19 00:10:54.211 765-765/? V/Riru: jniRegisterNativeMethods android/opengl/GLES20
09-19 00:10:54.211 766-766/? V/Riru: jniRegisterNativeMethods android/opengl/GLES11Ext
09-19 00:10:54.212 766-766/? V/Riru: jniRegisterNativeMethods android/opengl/GLES20
09-19 00:10:54.212 765-765/? V/Riru: jniRegisterNativeMethods android/opengl/GLES30
    jniRegisterNativeMethods android/opengl/GLES31
09-19 00:10:54.212 766-766/? V/Riru: jniRegisterNativeMethods android/opengl/GLES30
09-19 00:10:54.213 1001-1001/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:54.213 765-765/? V/Riru: jniRegisterNativeMethods android/opengl/GLES31Ext
    jniRegisterNativeMethods android/opengl/GLES32
    jniRegisterNativeMethods android/graphics/Bitmap
09-19 00:10:54.213 766-766/? V/Riru: jniRegisterNativeMethods android/opengl/GLES31
09-19 00:10:54.213 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/BitmapFactory
    jniRegisterNativeMethods android/graphics/BitmapRegionDecoder
    jniRegisterNativeMethods android/graphics/Camera
    jniRegisterNativeMethods android/graphics/CanvasProperty
    jniRegisterNativeMethods android/graphics/ColorFilter
    jniRegisterNativeMethods android/graphics/PorterDuffColorFilter
    jniRegisterNativeMethods android/graphics/BlendModeColorFilter
    jniRegisterNativeMethods android/graphics/LightingColorFilter
09-19 00:10:54.213 766-766/? V/Riru: jniRegisterNativeMethods android/opengl/GLES31Ext
09-19 00:10:54.213 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/ColorMatrixColorFilter
    jniRegisterNativeMethods android/graphics/DrawFilter
    jniRegisterNativeMethods android/graphics/PaintFlagsDrawFilter
    jniRegisterNativeMethods android/graphics/FontFamily
09-19 00:10:54.213 766-766/? V/Riru: jniRegisterNativeMethods android/opengl/GLES32
    jniRegisterNativeMethods android/graphics/Bitmap
    jniRegisterNativeMethods android/graphics/BitmapFactory
09-19 00:10:54.214 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/BitmapRegionDecoder
    jniRegisterNativeMethods android/graphics/Camera
    jniRegisterNativeMethods android/graphics/CanvasProperty
    jniRegisterNativeMethods android/graphics/ColorFilter
    jniRegisterNativeMethods android/graphics/PorterDuffColorFilter
    jniRegisterNativeMethods android/graphics/BlendModeColorFilter
    jniRegisterNativeMethods android/graphics/LightingColorFilter
    jniRegisterNativeMethods android/graphics/ColorMatrixColorFilter
    jniRegisterNativeMethods android/graphics/DrawFilter
    jniRegisterNativeMethods android/graphics/PaintFlagsDrawFilter
    jniRegisterNativeMethods android/graphics/FontFamily
09-19 00:10:54.214 1118-1118/? D/fpc_tac: 'modalias'='of:Nfingerprint_fpcT<NULL>Cfpc,' found on  path '/sys/bus/platform/devices/soc:fingerprint_fpc/'
09-19 00:10:54.214 1118-1118/? D/QSEECOMAPI: QSEECom_get_handle sb_length = 0x80
    App is not loaded in QSEE
09-19 00:10:54.214 1050-1050/? W//apex/com.android.media.swcodec/bin/mediaswcodec: Could not read additional policy file '/vendor/etc/seccomp_policy/mediaswcodec.policy'
09-19 00:10:54.215 1050-1050/? W//apex/com.android.media.swcodec/bin/mediaswcodec: libminijail[1050]: failed to get path of fd 5: No such file or directory
    libminijail[1050]: allowing syscall: connect
    libminijail[1050]: allowing syscall: fcntl
    libminijail[1050]: allowing syscall: sendto
    libminijail[1050]: allowing syscall: socket
    libminijail[1050]: allowing syscall: writev
09-19 00:10:54.216 1050-1050/? W//apex/com.android.media.swcodec/bin/mediaswcodec: libminijail[1050]: logging seccomp filter failures
09-19 00:10:54.216 1050-1050/? I/CodecServiceRegistrant: Creating software Codec2 service...
09-19 00:10:54.216 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/GraphicBuffer
    jniRegisterNativeMethods android/graphics/ImageDecoder
    jniRegisterNativeMethods android/graphics/drawable/AnimatedImageDrawable
    jniRegisterNativeMethods android/graphics/Interpolator
    jniRegisterNativeMethods android/graphics/MaskFilter
    jniRegisterNativeMethods android/graphics/BlurMaskFilter
09-19 00:10:54.217 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/EmbossMaskFilter
    jniRegisterNativeMethods android/graphics/TableMaskFilter
    jniRegisterNativeMethods android/graphics/Matrix
09-19 00:10:54.217 1118-1118/? D/QSEECOMAPI: app_arch = 1, total_files = 9
09-19 00:10:54.217 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/GraphicBuffer
09-19 00:10:54.217 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/Movie
    jniRegisterNativeMethods android/graphics/NinePatch
09-19 00:10:54.217 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/ImageDecoder
09-19 00:10:54.217 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/Paint
09-19 00:10:54.217 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/drawable/AnimatedImageDrawable
    jniRegisterNativeMethods android/graphics/Interpolator
    jniRegisterNativeMethods android/graphics/MaskFilter
    jniRegisterNativeMethods android/graphics/BlurMaskFilter
09-19 00:10:54.217 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/Path
09-19 00:10:54.217 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/EmbossMaskFilter
    jniRegisterNativeMethods android/graphics/TableMaskFilter
    jniRegisterNativeMethods android/graphics/Matrix
09-19 00:10:54.217 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/PathMeasure
    jniRegisterNativeMethods android/graphics/PathEffect
    jniRegisterNativeMethods android/graphics/ComposePathEffect
    jniRegisterNativeMethods android/graphics/SumPathEffect
    jniRegisterNativeMethods android/graphics/DashPathEffect
    jniRegisterNativeMethods android/graphics/PathDashPathEffect
    jniRegisterNativeMethods android/graphics/CornerPathEffect
    jniRegisterNativeMethods android/graphics/DiscretePathEffect
    jniRegisterNativeMethods android/graphics/Picture
09-19 00:10:54.217 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/Movie
09-19 00:10:54.217 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/Region
09-19 00:10:54.217 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/NinePatch
09-19 00:10:54.217 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/RegionIterator
    jniRegisterNativeMethods android/graphics/Color
09-19 00:10:54.217 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/Paint
09-19 00:10:54.217 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/Shader
    jniRegisterNativeMethods android/graphics/BitmapShader
    jniRegisterNativeMethods android/graphics/LinearGradient
    jniRegisterNativeMethods android/graphics/RadialGradient
    jniRegisterNativeMethods android/graphics/SweepGradient
    jniRegisterNativeMethods android/graphics/ComposeShader
09-19 00:10:54.217 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/Path
09-19 00:10:54.217 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/SurfaceTexture
    jniRegisterNativeMethods android/graphics/Typeface
    jniRegisterNativeMethods android/graphics/YuvImage
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/PathMeasure
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/drawable/AnimatedVectorDrawable
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/PathEffect
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/drawable/VectorDrawable
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/ComposePathEffect
    jniRegisterNativeMethods android/graphics/SumPathEffect
    jniRegisterNativeMethods android/graphics/DashPathEffect
    jniRegisterNativeMethods android/graphics/PathDashPathEffect
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/fonts/Font$Builder
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/CornerPathEffect
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/fonts/FontFamily$Builder
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/DiscretePathEffect
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/pdf/PdfDocument
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/Picture
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/pdf/PdfEditor
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/Region
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/pdf/PdfRenderer
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/RegionIterator
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/text/MeasuredText
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/Color
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/text/MeasuredText$Builder
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/Shader
09-19 00:10:54.218 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.media.c2@1.0::IComponentStore/default in either framework or device manifest.
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/graphics/text/LineBreaker
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/BitmapShader
    jniRegisterNativeMethods android/graphics/LinearGradient
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/database/CursorWindow
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/RadialGradient
    jniRegisterNativeMethods android/graphics/SweepGradient
    jniRegisterNativeMethods android/graphics/ComposeShader
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/database/sqlite/SQLiteConnection
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/SurfaceTexture
    jniRegisterNativeMethods android/graphics/Typeface
    jniRegisterNativeMethods android/graphics/YuvImage
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/database/sqlite/SQLiteGlobal
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/drawable/AnimatedVectorDrawable
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/database/sqlite/SQLiteDebug
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/drawable/VectorDrawable
09-19 00:10:54.218 1050-1050/? I/CodecServiceRegistrant: Preferred Codec2 store is defaulted to "software".
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/os/Debug
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/fonts/Font$Builder
09-19 00:10:54.218 1132-1132/? E/QMI_FW: QMUXD: WARNING qmi_qmux_if_pwr_up_init failed! rc=-6
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/fonts/FontFamily$Builder
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/os/FileObserver$ObserverThread
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/pdf/PdfDocument
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/os/GraphicsEnvironment
09-19 00:10:54.218 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/pdf/PdfEditor
09-19 00:10:54.218 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/os/MessageQueue
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/pdf/PdfRenderer
09-19 00:10:54.218 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/os/SELinux
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/text/MeasuredText
09-19 00:10:54.218 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/text/MeasuredText$Builder
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/os/Trace
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/graphics/text/LineBreaker
09-19 00:10:54.218 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/os/UEventObserver
09-19 00:10:54.218 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/database/CursorWindow
09-19 00:10:54.218 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/net/LocalSocketImpl
09-19 00:10:54.218 766-766/? V/Riru: jniRegisterNativeMethods android/database/sqlite/SQLiteConnection
09-19 00:10:54.218 765-765/? V/Riru: jniRegisterNativeMethods android/net/NetworkUtils
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods android/os/MemoryFile
    jniRegisterNativeMethods android/os/SharedMemory
09-19 00:10:54.219 766-766/? V/Riru: jniRegisterNativeMethods android/database/sqlite/SQLiteGlobal
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods com/android/internal/os/ClassLoaderFactory
09-19 00:10:54.219 766-766/? V/Riru: jniRegisterNativeMethods android/database/sqlite/SQLiteDebug
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods com/android/internal/os/Zygote
09-19 00:10:54.219 765-765/? I/Riru: replaced com.android.internal.os.Zygote#nativeForkAndSpecialize
    replaced com.android.internal.os.Zygote#nativeForkSystemServer
09-19 00:10:54.219 766-766/? V/Riru: jniRegisterNativeMethods android/os/Debug
09-19 00:10:54.219 765-765/? I/Riru: replaced com.android.internal.os.Zygote#nativeSpecializeAppProcess
09-19 00:10:54.219 766-766/? V/Riru: jniRegisterNativeMethods android/os/FileObserver$ObserverThread
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods com/android/internal/os/ZygoteInit
09-19 00:10:54.219 766-766/? V/Riru: jniRegisterNativeMethods android/os/GraphicsEnvironment
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods com/android/internal/util/VirtualRefBasePtr
09-19 00:10:54.219 766-766/? V/Riru: jniRegisterNativeMethods android/os/MessageQueue
    jniRegisterNativeMethods android/os/SELinux
    jniRegisterNativeMethods android/os/Trace
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods android/hardware/Camera
09-19 00:10:54.219 766-766/? V/Riru: jniRegisterNativeMethods android/os/UEventObserver
    jniRegisterNativeMethods android/net/LocalSocketImpl
    jniRegisterNativeMethods android/net/NetworkUtils
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods android/hardware/camera2/impl/CameraMetadataNative
09-19 00:10:54.219 1050-1050/? I/ServiceManagement: Registered android.hardware.media.c2@1.0::IComponentStore/software (start delay of 327ms)
09-19 00:10:54.219 766-766/? V/Riru: jniRegisterNativeMethods android/os/MemoryFile
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods android/hardware/camera2/legacy/LegacyCameraDevice
09-19 00:10:54.219 766-766/? V/Riru: jniRegisterNativeMethods android/os/SharedMemory
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods android/hardware/camera2/legacy/PerfMeasurement
09-19 00:10:54.219 766-766/? V/Riru: jniRegisterNativeMethods com/android/internal/os/ClassLoaderFactory
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods android/hardware/camera2/DngCreator
    jniRegisterNativeMethods android/hardware/HardwareBuffer
09-19 00:10:54.219 766-766/? V/Riru: jniRegisterNativeMethods com/android/internal/os/Zygote
09-19 00:10:54.219 1050-1050/? I/CodecServiceRegistrant: Software Codec2 service created.
09-19 00:10:54.219 766-766/? I/Riru: replaced com.android.internal.os.Zygote#nativeForkAndSpecialize
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods android/hardware/SystemSensorManager
09-19 00:10:54.219 766-766/? I/Riru: replaced com.android.internal.os.Zygote#nativeForkSystemServer
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods android/hardware/SystemSensorManager$BaseEventQueue
09-19 00:10:54.219 766-766/? I/Riru: replaced com.android.internal.os.Zygote#nativeSpecializeAppProcess
09-19 00:10:54.219 765-765/? V/Riru: jniRegisterNativeMethods android/hardware/SerialPort
09-19 00:10:54.219 766-766/? V/Riru: jniRegisterNativeMethods com/android/internal/os/ZygoteInit
    jniRegisterNativeMethods com/android/internal/util/VirtualRefBasePtr
09-19 00:10:54.220 765-765/? V/Riru: jniRegisterNativeMethods android/hardware/soundtrigger/SoundTrigger
    jniRegisterNativeMethods android/hardware/soundtrigger/SoundTriggerModule
09-19 00:10:54.220 766-766/? V/Riru: jniRegisterNativeMethods android/hardware/Camera
09-19 00:10:54.220 765-765/? V/Riru: jniRegisterNativeMethods android/hardware/usb/UsbDevice
    jniRegisterNativeMethods android/hardware/usb/UsbDeviceConnection
    jniRegisterNativeMethods android/hardware/usb/UsbRequest
    jniRegisterNativeMethods android/hardware/location/ActivityRecognitionHardware
    jniRegisterNativeMethods android/media/AudioSystem
09-19 00:10:54.220 766-766/? V/Riru: jniRegisterNativeMethods android/hardware/camera2/impl/CameraMetadataNative
    jniRegisterNativeMethods android/hardware/camera2/legacy/LegacyCameraDevice
    jniRegisterNativeMethods android/hardware/camera2/legacy/PerfMeasurement
    jniRegisterNativeMethods android/hardware/camera2/DngCreator
    jniRegisterNativeMethods android/hardware/HardwareBuffer
    jniRegisterNativeMethods android/hardware/SystemSensorManager
    jniRegisterNativeMethods android/hardware/SystemSensorManager$BaseEventQueue
    jniRegisterNativeMethods android/hardware/SerialPort
09-19 00:10:54.220 765-765/? V/Riru: jniRegisterNativeMethods android/media/AudioSystem
    jniRegisterNativeMethods android/media/AudioPortEventHandler
    jniRegisterNativeMethods android/media/AudioRecord
    jniRegisterNativeMethods android/media/AudioTrack
09-19 00:10:54.221 766-766/? V/Riru: jniRegisterNativeMethods android/hardware/soundtrigger/SoundTrigger
    jniRegisterNativeMethods android/hardware/soundtrigger/SoundTriggerModule
    jniRegisterNativeMethods android/hardware/usb/UsbDevice
09-19 00:10:54.221 765-765/? V/Riru: jniRegisterNativeMethods android/media/AudioAttributes
09-19 00:10:54.221 766-766/? V/Riru: jniRegisterNativeMethods android/hardware/usb/UsbDeviceConnection
09-19 00:10:54.221 765-765/? W/zygote64: JNI RegisterNativeMethods: attempt to register 0 native methods for android.media.AudioAttributes
09-19 00:10:54.221 766-766/? V/Riru: jniRegisterNativeMethods android/hardware/usb/UsbRequest
    jniRegisterNativeMethods android/hardware/location/ActivityRecognitionHardware
09-19 00:10:54.221 765-765/? V/Riru: jniRegisterNativeMethods android/media/audiopolicy/AudioProductStrategy
09-19 00:10:54.221 766-766/? V/Riru: jniRegisterNativeMethods android/media/AudioSystem
09-19 00:10:54.221 765-765/? V/Riru: jniRegisterNativeMethods android/media/audiopolicy/AudioVolumeGroup
    jniRegisterNativeMethods android/media/audiopolicy/AudioVolumeGroupChangeHandler
    jniRegisterNativeMethods android/media/JetPlayer
    jniRegisterNativeMethods android/media/RemoteDisplay
    jniRegisterNativeMethods android/media/ToneGenerator
    jniRegisterNativeMethods android/opengl/Matrix
    jniRegisterNativeMethods android/opengl/Visibility
    jniRegisterNativeMethods android/opengl/GLUtils
    jniRegisterNativeMethods android/opengl/ETC1
    jniRegisterNativeMethods com/android/server/NetworkManagementSocketTagger
    jniRegisterNativeMethods android/ddm/DdmHandleNativeHeap
    jniRegisterNativeMethods android/app/backup/BackupDataInput
    jniRegisterNativeMethods android/app/backup/BackupDataOutput
    jniRegisterNativeMethods android/app/backup/FileBackupHelperBase
    jniRegisterNativeMethods android/app/backup/BackupHelperDispatcher
    jniRegisterNativeMethods android/app/backup/FullBackup
    jniRegisterNativeMethods android/app/Activity
    jniRegisterNativeMethods android/app/ActivityThread
    jniRegisterNativeMethods android/app/NativeActivity
    jniRegisterNativeMethods android/util/jar/StrictJarFile
09-19 00:10:54.222 765-765/? V/Riru: jniRegisterNativeMethods android/view/InputChannel
    jniRegisterNativeMethods android/view/InputEventReceiver
    jniRegisterNativeMethods android/view/InputEventSender
    jniRegisterNativeMethods android/view/InputQueue
09-19 00:10:54.222 766-766/? V/Riru: jniRegisterNativeMethods android/media/AudioSystem
09-19 00:10:54.222 765-765/? V/Riru: jniRegisterNativeMethods android/view/KeyEvent
    jniRegisterNativeMethods android/view/MotionEvent
    jniRegisterNativeMethods android/view/VelocityTracker
09-19 00:10:54.222 766-766/? V/Riru: jniRegisterNativeMethods android/media/AudioPortEventHandler
09-19 00:10:54.222 765-765/? V/Riru: jniRegisterNativeMethods android/content/res/ObbScanner
    jniRegisterNativeMethods android/animation/PropertyValuesHolder
09-19 00:10:54.222 766-766/? V/Riru: jniRegisterNativeMethods android/media/AudioRecord
09-19 00:10:54.222 765-765/? V/Riru: jniRegisterNativeMethods android/security/Scrypt
    jniRegisterNativeMethods com/android/internal/content/NativeLibraryHelper
09-19 00:10:54.222 766-766/? V/Riru: jniRegisterNativeMethods android/media/AudioTrack
09-19 00:10:54.222 765-765/? V/Riru: jniRegisterNativeMethods com/android/internal/os/AtomicDirectory
    jniRegisterNativeMethods com/android/internal/os/FuseAppLoop
09-19 00:10:54.222 766-766/? V/Riru: jniRegisterNativeMethods android/media/AudioAttributes
09-19 00:10:54.223 766-766/? W/zygote: JNI RegisterNativeMethods: attempt to register 0 native methods for android.media.AudioAttributes
09-19 00:10:54.223 766-766/? V/Riru: jniRegisterNativeMethods android/media/audiopolicy/AudioProductStrategy
    jniRegisterNativeMethods android/media/audiopolicy/AudioVolumeGroup
    jniRegisterNativeMethods android/media/audiopolicy/AudioVolumeGroupChangeHandler
    jniRegisterNativeMethods android/media/JetPlayer
    jniRegisterNativeMethods android/media/RemoteDisplay
    jniRegisterNativeMethods android/media/ToneGenerator
    jniRegisterNativeMethods android/opengl/Matrix
    jniRegisterNativeMethods android/opengl/Visibility
    jniRegisterNativeMethods android/opengl/GLUtils
    jniRegisterNativeMethods android/opengl/ETC1
    jniRegisterNativeMethods com/android/server/NetworkManagementSocketTagger
    jniRegisterNativeMethods android/ddm/DdmHandleNativeHeap
    jniRegisterNativeMethods android/app/backup/BackupDataInput
    jniRegisterNativeMethods android/app/backup/BackupDataOutput
    jniRegisterNativeMethods android/app/backup/FileBackupHelperBase
    jniRegisterNativeMethods android/app/backup/BackupHelperDispatcher
    jniRegisterNativeMethods android/app/backup/FullBackup
09-19 00:10:54.224 766-766/? V/Riru: jniRegisterNativeMethods android/app/Activity
    jniRegisterNativeMethods android/app/ActivityThread
    jniRegisterNativeMethods android/app/NativeActivity
    jniRegisterNativeMethods android/util/jar/StrictJarFile
    jniRegisterNativeMethods android/view/InputChannel
    jniRegisterNativeMethods android/view/InputEventReceiver
    jniRegisterNativeMethods android/view/InputEventSender
    jniRegisterNativeMethods android/view/InputQueue
    jniRegisterNativeMethods android/view/KeyEvent
    jniRegisterNativeMethods android/view/MotionEvent
09-19 00:10:54.224 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:54.224 766-766/? V/Riru: jniRegisterNativeMethods android/view/VelocityTracker
09-19 00:10:54.225 766-766/? V/Riru: jniRegisterNativeMethods android/content/res/ObbScanner
    jniRegisterNativeMethods android/animation/PropertyValuesHolder
    jniRegisterNativeMethods android/security/Scrypt
    jniRegisterNativeMethods com/android/internal/content/NativeLibraryHelper
    jniRegisterNativeMethods com/android/internal/os/AtomicDirectory
    jniRegisterNativeMethods com/android/internal/os/FuseAppLoop
09-19 00:10:54.234 765-765/? D/Zygote: begin preload
09-19 00:10:54.234 765-765/? I/Zygote: Calling ZygoteHooks.beginPreload()
09-19 00:10:54.239 766-766/? I/zygote: Explicit concurrent copying GC freed 303(39KB) AllocSpace objects, 0(0B) LOS objects, 99% free, 24KB/24MB, paused 53us total 5.718ms
09-19 00:10:54.245 766-766/? I/zygote: Explicit concurrent copying GC freed 5(32KB) AllocSpace objects, 0(0B) LOS objects, 99% free, 24KB/24MB, paused 25us total 5.415ms
09-19 00:10:54.245 766-766/? D/Zygote32Timing: PostZygoteInitGC took to complete: 12ms
    ZygoteInit took to complete: 13ms
09-19 00:10:54.300 765-765/? D/Zygote64Timing: BeginPreload took to complete: 67ms
09-19 00:10:54.301 765-765/? I/Zygote: Preloading classes...
09-19 00:10:54.302 963-963/? E/MediaExtractorFactory: couldn't opendir(/system/lib64/extractors)
09-19 00:10:54.303 765-765/? W/Zygote: Class not found for preloading: android.app.-$$Lambda$ActivityThread$ZXDWm3IBeFmLnFVblhB-IOZCr9o
09-19 00:10:54.308 766-766/? I/Zygote: Accepting command socket connections
09-19 00:10:54.325 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:54.338 765-765/? W/Zygote: Class not found for preloading: android.bluetooth.BluetoothA2dp$2
09-19 00:10:54.341 765-765/? I/PackageBackwardCompatibility: Could not find android.content.pm.AndroidTestBaseUpdater, ignoring
09-19 00:10:54.366 1118-1118/? D/QSEECOMAPI: Loaded image: APP id = 262146
09-19 00:10:54.367 1118-1118/? D/fpc_tac: fpc_tee_print_build_info
09-19 00:10:54.373 1118-1118/? E/fpc_tac: fpc_tac_transfer send_cmd failed -11
    fpc_tee_print_build_info, fpc_tac_transfer failed -4.
09-19 00:10:54.374 1118-1118/? D/fpc_fingerprint_hal: fpc_hal_open, An error occured print build info.
09-19 00:10:54.384 1118-1118/? D/fpc_tac: 'modalias'='of:Nfingerprint_fpcT<NULL>Cfpc,' found on  path '/sys/bus/platform/devices/soc:fingerprint_fpc/'
09-19 00:10:54.387 1118-1118/? E/fpc_tac: fpc_tac_transfer send_cmd failed -11
    sensor_command, Failed to send command: 4 to TA, status code: -4
09-19 00:10:54.387 1118-1118/? E/fpc_fingerprint_hal: fpc_hal_open failed
09-19 00:10:54.387 1118-1118/? D/fpc_fingerprint_hal: fpc_hal_close
09-19 00:10:54.388 1118-1118/? D/fpc_tac: fpc_hw_resource_release OK
09-19 00:10:54.389 1118-1118/? D/fpc_fingerprint_hal: destroy_input_device fd: -1
09-19 00:10:54.389 1118-1118/? D/QSEECOMAPI: QSEECom_dealloc_memory 
    QSEECom_shutdown_app, app_id = 262146
09-19 00:10:54.390 1118-1118/? D/fpc_fingerprint_hal: fpc_module_close
    fpc_hal_close
09-19 00:10:54.390 1118-1118/? E/android.hardware.biometrics.fingerprint@2.1-service.xiaomi_msm8998: Can't open fingerprint methods, class fpc, error: -1
    Failed to load fpc fingerprint module
09-19 00:10:54.390 1118-1118/? D/vndksupport: Loading /vendor/lib64/hw/fingerprint.goodix.msm8998.so from current namespace instead of sphal namespace.
09-19 00:10:54.401 1118-1118/? E/[goodix][gf_hal]: [gf_hal_open] Android O Version
09-19 00:10:54.408 870-916/? I/adbd: USB event: FUNCTIONFS_ENABLE
09-19 00:10:54.425 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:54.428 1118-1118/? D/QSEECOMAPI: QSEECom_get_handle sb_length = 0x1000
    App is not loaded in QSEE
09-19 00:10:54.429 1118-1118/? D/QSEECOMAPI: app_arch = 1, total_files = 9
09-19 00:10:54.463 772-772/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: retry, retry_num 1
09-19 00:10:54.508 1118-1118/? D/QSEECOMAPI: Loaded image: APP id = 327682
09-19 00:10:54.510 1118-1118/? D/QSEECOMAPI: QSEECom_get_handle sb_length = 0x1000
    App is already loaded QSEE and app id = 65537
09-19 00:10:54.514 1118-1118/? D/QSEECOMAPI: QSEECom_dealloc_memory 
    QSEECom_shutdown_app, app_id = 65537
09-19 00:10:54.523 832-832/? D/RenderEngine: shader cache generated - 48 shaders in 584.106201 ms
09-19 00:10:54.525 832-832/? I/ServiceManagement: Registered android.frameworks.displayservice@1.0::IDisplayService/default (start delay of 1203ms)
09-19 00:10:54.525 832-832/? D/SurfaceFlinger: Setting power mode 2 on display 0
09-19 00:10:54.525 784-784/? I/SDM: DisplayBase::SetDisplayState: Set state = 1, display 0
09-19 00:10:54.526 832-832/? D/SurfaceFlinger: Finished setting power mode 2 on display 0
09-19 00:10:54.526 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:54.530 1118-1118/? I/[goodix][gf_hal_common]: [gf_hal_common_load_otp_info_from_sdcard] CRC8 check success
09-19 00:10:54.590 1118-1118/? I/[goodix][gf_hal_device]: [gf_hal_device_enable] g_netlink_route=25
09-19 00:10:54.590 1118-1118/? I/[goodix][gf_hal_milan_f_series]: [hal_milan_f_information_OTP] year=18, month=4, day=3, product_id=0x2a
09-19 00:10:54.604 1118-1118/? I/[goodix][gf_hal_milan_f_series]: setprop[persist.vendor.sys.fp.info] = 0x00000124032affff OK
09-19 00:10:54.614 1118-1118/? I/[goodix][gf_hal_milan_f_series]: setprop[persist.vendor.sys.fp.uid] = C868626-96F43AFA-A2BE5188-24E21F OK
09-19 00:10:54.626 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:54.633 1118-1118/? I/[goodix][gf_hal_milan_f_series]: setprop[persist.vendor.sys.fp.module] = QTech OK
09-19 00:10:54.674 1215-1215/? D/BootAnimation: BootAnimationStartTiming start time: 52812ms
    BootAnimationPreloadTiming start time: 52812ms
09-19 00:10:54.704 936-936/? I/cameraserver: ServiceManager: 0xecc231a0
09-19 00:10:54.704 936-936/? I/CameraService: CameraService started (pid=936)
09-19 00:10:54.705 936-936/? I/CameraService: CameraService process starting
09-19 00:10:54.705 936-936/? W/BatteryNotifier: batterystats service unavailable!
    batterystats service unavailable!
09-19 00:10:54.709 1215-1215/? D/BootAnimation: BootAnimationPreloadStopTiming start time: 52847ms
09-19 00:10:54.711 772-847/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: retry, retry_num 1
09-19 00:10:54.714 772-847/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: snd_card_name: msm8998-tasha-snd-card
09-19 00:10:54.714 772-847/? W/hardware_info: update_hardware_info_msm8998: Not a msm8998 device
09-19 00:10:54.715 772-847/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: Opened sound card:0
09-19 00:10:54.715 772-847/? D/msm8974_platform: platform_init: Opened sound card:0
09-19 00:10:54.715 772-847/? I/audio_hw_extn: audio_extn_set_snd_card_split: snd_card_name(msm8998-tasha-snd-card) device(msm8998) snd_card(tasha) form_factor(snd)
09-19 00:10:54.715 772-847/? W/hardware_info: update_hardware_info_msm8998: Not a msm8998 device
09-19 00:10:54.715 772-847/? D/msm8974_platform: platform_init: Loading mixer file: /vendor/etc/mixer_paths_tasha.xml
09-19 00:10:54.718 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.graphics.mapper@3.0::IMapper/default in either framework or device manifest.
09-19 00:10:54.718 832-876/? W/Gralloc3: mapper 3.x is not supported
09-19 00:10:54.719 936-936/? I/ServiceManagement: getService: Trying again for android.hardware.camera.provider@2.4::ICameraProvider/legacy/0...
09-19 00:10:54.721 765-765/? E/ActivityRecognitionHardware: activity_recognition HAL is deprecated. class_init is effectively a no-op
09-19 00:10:54.727 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:54.727 1215-1232/? D/libEGL: loaded /vendor/lib64/egl/libEGL_adreno.so
09-19 00:10:54.733 1215-1232/? D/libEGL: loaded /vendor/lib64/egl/libGLESv1_CM_adreno.so
09-19 00:10:54.735 1215-1232/? D/libEGL: loaded /vendor/lib64/egl/libGLESv2_adreno.so
09-19 00:10:54.747 1215-1232/? I/Adreno: QUALCOMM build                   : 2c6a1c7, I1490fecf6e
    Build Date                       : 02/04/19
    OpenGL ES Shader Compiler Version: EV031.25.03.02
    Local Branch                     : 
    Remote Branch                    : 
    Remote Branch                    : 
    Reconstruct Branch               : 
    Build Config                     : S L 6.0.7 AArch64
09-19 00:10:54.753 1215-1232/? I/Adreno: PFP: 0x005ff112, ME: 0x005ff066
09-19 00:10:54.754 1215-1232/? E/libEGL: Driver indicates EGL 1.5 support, but does not have a critical API
09-19 00:10:54.759 1215-1232/? D/BootAnimation: BootAnimationShownTiming start time: 52897ms
09-19 00:10:54.764 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.graphics.allocator@3.0::IAllocator/default in either framework or device manifest.
09-19 00:10:54.765 832-876/? W/Gralloc3: allocator 3.x is not supported
09-19 00:10:54.766 832-876/? I/Gralloc2: Adding additional valid usage bits: 0x202400
09-19 00:10:54.771 765-765/? V/Riru: jniRegisterNativeMethods android/media/ImageWriter
    jniRegisterNativeMethods android/media/ImageWriter$WriterSurfaceImage
    jniRegisterNativeMethods android/media/ImageReader
    jniRegisterNativeMethods android/media/ImageReader$SurfaceImage
    jniRegisterNativeMethods android/media/MediaPlayer
    jniRegisterNativeMethods android/media/MediaRecorder
    jniRegisterNativeMethods android/media/MediaScanner
    jniRegisterNativeMethods android/media/MediaMetadataRetriever
    jniRegisterNativeMethods android/media/ResampleInputStream
    jniRegisterNativeMethods android/media/EncoderCapabilities
    jniRegisterNativeMethods android/media/CamcorderProfile
    jniRegisterNativeMethods android/media/DecoderCapabilities
    jniRegisterNativeMethods android/media/CameraProfile
09-19 00:10:54.771 765-765/? I/zygote64: Thread[1,tid=765,Native,Thread*=0x75903a9c00,peer=0x12c022c0,"main"] recursive attempt to load library "libmedia_jni.so"
09-19 00:10:54.771 765-765/? V/Riru: jniRegisterNativeMethods android/mtp/MtpDatabase
    jniRegisterNativeMethods android/mtp/MtpPropertyGroup
09-19 00:10:54.771 765-765/? D/MtpDeviceJNI: register_android_mtp_MtpDevice
09-19 00:10:54.771 765-765/? I/zygote64: Thread[1,tid=765,Native,Thread*=0x75903a9c00,peer=0x12c022c0,"main"] recursive attempt to load library "libmedia_jni.so"
09-19 00:10:54.772 765-765/? V/Riru: jniRegisterNativeMethods android/mtp/MtpDevice
09-19 00:10:54.772 765-765/? I/zygote64: Thread[1,tid=765,Native,Thread*=0x75903a9c00,peer=0x12c022c0,"main"] recursive attempt to load library "libmedia_jni.so"
09-19 00:10:54.772 765-765/? V/Riru: jniRegisterNativeMethods android/mtp/MtpServer
    jniRegisterNativeMethods android/media/MediaCodec
    jniRegisterNativeMethods android/media/MediaSync
    jniRegisterNativeMethods android/media/MediaExtractor
    jniRegisterNativeMethods android/media/MediaMuxer
    jniRegisterNativeMethods android/media/MediaCodecList
    jniRegisterNativeMethods android/media/MediaCrypto
    jniRegisterNativeMethods android/media/MediaDrm
    jniRegisterNativeMethods android/media/MediaDescrambler
    jniRegisterNativeMethods android/media/MediaHTTPConnection
09-19 00:10:54.777 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.graphics.mapper@3.0::IMapper/default in either framework or device manifest.
09-19 00:10:54.777 1215-1232/? W/Gralloc3: mapper 3.x is not supported
09-19 00:10:54.778 792-1206/? E/qti_sensors_hal: processSingleSensorInfoResp: either handle is -1 or error is true or mSensors[handle] is NULL!
    processSingleSensorInfoResp: either handle_wakeup is -1 or error is true or mSensors[handle_wakeup] is NULL!
    processSingleSensorInfoResp: either handle is -1 or error is true or mSensors[handle] is NULL!
    processSingleSensorInfoResp: either handle_wakeup is -1 or error is true or mSensors[handle_wakeup] is NULL!
09-19 00:10:54.778 765-765/? V/Riru: jniRegisterNativeMethods android/media/SoundPool
09-19 00:10:54.779 765-765/? W/Zygote: Class not found for preloading: android.media.audiopolicy.AudioProductStrategies
    Class not found for preloading: android.media.audiopolicy.AudioVolumeGroups
09-19 00:10:54.780 792-1206/? E/qti_sensors_hal: processSingleSensorInfoResp: either handle is -1 or error is true or mSensors[handle] is NULL!
09-19 00:10:54.781 792-1206/? E/qti_sensors_hal: processSingleSensorInfoResp: either handle_wakeup is -1 or error is true or mSensors[handle_wakeup] is NULL!
    processSingleSensorInfoResp: either handle_wakeup is -1 or error is true or mSensors[handle_wakeup] is NULL!
09-19 00:10:54.781 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:739] qti_file_open():Could not open device file. Errno 2 error msg=No such file or directory
09-19 00:10:54.794 832-832/? I/SurfaceFlinger: Enter boot animation
09-19 00:10:54.827 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:54.833 792-792/? W/qti_sensors_hal: addSensor : Not supported sensor with handle 67!
09-19 00:10:54.835 765-765/? W/Zygote: Class not found for preloading: android.view.-$$Lambda$SurfaceView$Cs7TGTdA1lXf9qW8VOJAfEsMjdk
09-19 00:10:54.836 784-784/? D/qdutils: DEBUG_CALC_FPS: 0
    period: 10
    ignorethresh_us: 500000
09-19 00:10:54.837 765-765/? W/Zygote: Class not found for preloading: android.view.SurfaceView$3
09-19 00:10:54.839 765-765/? W/Zygote: Class not found for preloading: android.view.textclassifier.-$$Lambda$TextClassificationManager$JIaezIJbMig_-kVzN6oArzkTsJE
09-19 00:10:54.845 765-765/? W/Zygote: Class not found for preloading: com.android.internal.net.NetworkStatsFactory
09-19 00:10:54.847 792-792/? W/qti_sensors_hal: Oem5TaptapGesture: handle:77
09-19 00:10:54.849 765-765/? W/Zygote: Class not found for preloading: com.android.internal.telephony.-$$Lambda$PhoneSubInfoController$8HFbCDJDN1mrLJG980qYH5MGqMk
    Class not found for preloading: com.android.internal.telephony.-$$Lambda$PhoneSubInfoController$U28a_EGx2cvmQhDfRRgonMt5Zrc
    Class not found for preloading: com.android.internal.telephony.-$$Lambda$SubscriptionInfoUpdater$-zZXM9oMRZ3vZz7dJOG19J00Bmw
    Class not found for preloading: com.android.internal.telephony.-$$Lambda$SubscriptionInfoUpdater$D5yF1HbS4cvCyoAj3FESkPtA_0g
    Class not found for preloading: com.android.internal.telephony.-$$Lambda$SubscriptionInfoUpdater$MMx9iQX0JVqqMPLTUZhdBubFSzU
09-19 00:10:54.850 765-765/? W/Zygote: Class not found for preloading: com.android.internal.telephony.NewNitzStateMachine$1
09-19 00:10:54.851 765-765/? W/Zygote: Class not found for preloading: com.android.internal.telephony.NewNitzStateMachine
    Class not found for preloading: com.android.internal.telephony.NewTimeServiceHelper$1
    Class not found for preloading: com.android.internal.telephony.NewTimeServiceHelper$Listener
    Class not found for preloading: com.android.internal.telephony.NewTimeServiceHelper
    Class not found for preloading: com.android.internal.telephony.PhoneConfigurationModels
09-19 00:10:54.852 765-765/? W/Zygote: Class not found for preloading: com.android.internal.telephony.SubscriptionController$ScLocalLog
    Class not found for preloading: com.android.internal.telephony.UiccSmsController
    Class not found for preloading: com.android.internal.telephony.dataconnection.DcController$2
09-19 00:10:54.882 765-765/? I/Zygote: ...preloaded 7582 classes in 581ms.
09-19 00:10:54.882 765-765/? I/zygote64: VMRuntime.preloadDexCaches starting
09-19 00:10:54.884 792-792/? W/qti_sensors_hal: addSensor : Not supported sensor with handle 39!
09-19 00:10:54.894 792-792/? W/qti_sensors_hal: addSensor : Not supported sensor with handle 48!
    addSensor : Not supported sensor with handle 49!
09-19 00:10:54.897 1118-1118/? I/[goodix][gf_hal]: [gf_hal_open] init success
09-19 00:10:54.898 1118-1118/? I/ServiceManagement: Registered vendor.goodix.hardware.fingerprintextension@1.0::IGoodixBiometricsFingerprint/default (start delay of 906ms)
09-19 00:10:54.898 792-792/? W/qti_sensors_hal: addSensor : Not supported sensor with handle 53!
09-19 00:10:54.899 1118-1118/? I/goodixFingerprintHal: register GoodixFingerprintExtension hwbinder service successfully
09-19 00:10:54.900 1118-1118/? I/android.hardware.biometrics.fingerprint@2.1-service.xiaomi_msm8998: Loaded fingerprint module: class goodix
09-19 00:10:54.903 774-774/? E/mm-camera: <SENSOR><ERROR> 386: eebin_read: failed!
    <SENSOR><ERROR> 386: eebin_read: failed!
09-19 00:10:54.906 765-765/? I/zygote64: VMRuntime.preloadDexCaches strings total=332856 before=9849 after=9849
    VMRuntime.preloadDexCaches types total=36368 before=7357 after=7626
    VMRuntime.preloadDexCaches fields total=162783 before=8038 after=8239
    VMRuntime.preloadDexCaches methods total=285088 before=11193 after=11625
    VMRuntime.preloadDexCaches finished
09-19 00:10:54.906 765-765/? D/Zygote64Timing: PreloadClasses took to complete: 605ms
09-19 00:10:54.903 765-765/? W/main: type=1400 audit(0.0:29): avc: denied { write } for name="/" dev="tmpfs" ino=23802 scontext=u:r:zygote:s0 tcontext=u:object_r:system_file:s0 tclass=dir permissive=0
09-19 00:10:54.907 792-792/? W/qti_sensors_hal: addSensor : Not supported sensor with handle 68!
09-19 00:10:54.909 774-774/? E/mm-camera: <SENSOR><ERROR> 921: sensor_xml_util_get_camera_probe_config:  tmp chromatix_name = chiron_imx386_semco_chromatix
09-19 00:10:54.910 765-765/? I/zygote64: The ClassLoaderContext is a special shared library.
09-19 00:10:54.912 765-765/? D/ApplicationLoaders: Created zygote-cached class loader: /system/framework/android.hidl.base-V1.0-java.jar
09-19 00:10:54.910 765-765/? W/main: type=1400 audit(0.0:30): avc: denied { write } for name="/" dev="tmpfs" ino=23802 scontext=u:r:zygote:s0 tcontext=u:object_r:system_file:s0 tclass=dir permissive=0
09-19 00:10:54.915 765-765/? I/zygote64: The ClassLoaderContext is a special shared library.
09-19 00:10:54.916 765-765/? D/ApplicationLoaders: Created zygote-cached class loader: /system/framework/android.hidl.manager-V1.0-java.jar
09-19 00:10:54.916 765-765/? D/Zygote64Timing: CacheNonBootClasspathClassLoaders took to complete: 10ms
09-19 00:10:54.920 1118-1218/? I/[goodix][gf_hal_milan_f_series]: [hal_milan_f_series_irq] irq_type=INVALID_IRQ_TYPE, irq_type=0x0000
09-19 00:10:54.926 1118-1118/? I/ServiceManagement: Registered android.hardware.biometrics.fingerprint@2.1::IBiometricsFingerprint/default (start delay of 934ms)
    Removing namespace from process name android.hardware.biometrics.fingerprint@2.1-service.xiaomi_msm8998 to fingerprint@2.1-service.xiaomi_msm8998.
09-19 00:10:54.927 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:54.932 1118-1218/? I/[goodix][gf_hal_milan_f_series]: [hal_milan_f_series_irq] irq_type=INVALID_IRQ_TYPE, irq_type=0x0000
09-19 00:10:54.948 925-1074/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 43000 mC, weight[0] 2
09-19 00:10:54.949 925-1074/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:10:54.951 792-792/? I/ultrasound: ultrasound_is_supported: hwversion = 3.2.0
09-19 00:10:54.952 792-792/? I/Elliptic: Configuration.h(412) : I : Adding sensor Elliptic Proximity to Sensor List
    SensorHAL.cpp(80) : I : Elliptic SensorHAL. Version 1.4.40717.2
09-19 00:10:54.952 792-792/? E//vendor/bin/hw/android.hardware.sensors@1.0-service: HAL specifies version 1.4, but does not implement set_operation_mode()
09-19 00:10:54.953 792-792/? I/ServiceManagement: Registered android.hardware.sensors@1.0::ISensors/default (start delay of 1741ms)
    Removing namespace from process name android.hardware.sensors@1.0-service to sensors@1.0-service.
09-19 00:10:54.954 792-792/? I/android.hardware.sensors@1.0-service: Registration complete for android.hardware.sensors@1.0::ISensors/default.
09-19 00:10:54.971 774-774/? E/mm-camera: <SENSOR><ERROR> 921: sensor_xml_util_get_camera_probe_config:  tmp chromatix_name = chiron_ov5675_primax_chromatix
09-19 00:10:54.986 774-774/? E/mm-camera: <SENSOR><ERROR> 921: sensor_xml_util_get_camera_probe_config:  tmp chromatix_name = chiron_ov5675_qtech_chromatix
    <SENSOR><ERROR> 8040: set_sensor_module_info: back_main_camera=Sony_imx386_I;back_aux_camera=none;front_main_camera=OmniVision_ov5675_I;front_aux_camera=none,PROPERTY_VALUE_MAX=92
09-19 00:10:55.000 774-774/? E/mm-camera: <SENSOR><ERROR> chiron_imx386_semco_eeprom_open_lib: 577: chiron_imx386_semco_eeprom_open_lib Enter
09-19 00:10:55.001 774-774/? E/mm-camera: <SENSOR><ERROR> chiron_imx386_semco_format_afdata: 59: OTP: AF Macro DAC = 820, Infinity DAC = 366
    <SENSOR><ERROR> chiron_imx386_semco_format_afdata: 68: near margin 0.40, FAR_MARGIN -0.08
    <SENSOR><ERROR> chiron_imx386_semco_format_afdata: 71: With Margin: AF Macro DAC = 1001, Infinity DAC = 329
    <SENSOR><ERROR> chiron_imx386_semco_format_wbdata: 99: OTP:AWB: r_over_gr: 0.489258,b_over_gr: 0.569336,gr_over_gb: 0.999023
09-19 00:10:55.004 774-774/? E/mm-camera: <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[0]: addr: 0x7D4C, data: 0x49
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[1]: addr: 0x7D4D, data: 0x45
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[2]: addr: 0x7D4E, data: 0x3F
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[3]: addr: 0x7D4F, data: 0x3A
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[4]: addr: 0x7D50, data: 0x37
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[5]: addr: 0x7D51, data: 0x34
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[6]: addr: 0x7D52, data: 0x32
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[7]: addr: 0x7D53, data: 0x31
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[8]: addr: 0x7D54, data: 0x4C
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[9]: addr: 0x7D55, data: 0x46
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[10]: addr: 0x7D56, data: 0x40
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[11]: addr: 0x7D57, data: 0x3A
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[12]: addr: 0x7D58, data: 0x37
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[13]: addr: 0x7D59, data: 0x34
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[14]: addr: 0x7D5A, data: 0x32
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[15]: addr: 0x7D5B, data: 0x30
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[16]: addr: 0x7D5C, data: 0x4D
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[17]: addr: 0x7D5D, data: 0x47
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[18]: addr: 0x7D5E, data: 0x3F
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[19]: addr: 0x7D5F, data: 0x3A
09-19 00:10:55.005 774-774/? E/mm-camera: <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[20]: addr: 0x7D60, data: 0x38
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[21]: addr: 0x7D61, data: 0x35
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[22]: addr: 0x7D62, data: 0x32
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[23]: addr: 0x7D63, data: 0x30
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[24]: addr: 0x7D64, data: 0x4D
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[25]: addr: 0x7D65, data: 0x47
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[26]: addr: 0x7D66, data: 0x3F
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[27]: addr: 0x7D67, data: 0x3A
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[28]: addr: 0x7D68, data: 0x38
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[29]: addr: 0x7D69, data: 0x35
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[30]: addr: 0x7D6A, data: 0x33
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[31]: addr: 0x7D6B, data: 0x31
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[32]: addr: 0x7D6C, data: 0x4B
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[33]: addr: 0x7D6D, data: 0x46
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[34]: addr: 0x7D6E, data: 0x3F
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[35]: addr: 0x7D6F, data: 0x3A
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[36]: addr: 0x7D70, data: 0x37
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[37]: addr: 0x7D71, data: 0x35
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[38]: addr: 0x7D72, data: 0x33
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[39]: addr: 0x7D73, data: 0x31
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[40]: addr: 0x7D74, data: 0x48
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[41]: addr: 0x7D75, data: 0x44
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[42]: addr: 0x7D76, data: 0x3F
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[43]: addr: 0x7D77, data: 0x3A
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[44]: addr: 0x7D78, data: 0x37
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[45]: addr: 0x7D79, data: 0x35
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[46]: addr: 0x7D7A, data: 0x33
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[47]: addr: 0x7D7B, data: 0x31
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[48]: addr: 0x7D7C, data: 0x39
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[49]: addr: 0x7D7D, data: 0x3B
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[50]: addr: 0x7D7E, data: 0x3E
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[51]: addr: 0x7D7F, data: 0x43
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[52]: addr: 0x7D80, data: 0x47
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[53]: addr: 0x7D81, data: 0x4E
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[54]: addr: 0x7D82, data: 0x56
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[55]: addr: 0x7D83, data: 0x5E
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[56]: addr: 0x7D84, data: 0x39
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[57]: addr: 0x7D85, data: 0x3B
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[58]: addr: 0x7D86, data: 0x3E
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[59]: addr: 0x7D87, data: 0x43
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[60]: addr: 0x7D88, data: 0x47
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[61]: addr: 0x7D89, data: 0x4E
09-19 00:10:55.006 774-774/? E/mm-camera: <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[62]: addr: 0x7D8A, data: 0x58
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[63]: addr: 0x7D8B, data: 0x63
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[64]: addr: 0x7D8C, data: 0x39
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[65]: addr: 0x7D8D, data: 0x3B
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[66]: addr: 0x7D8E, data: 0x3F
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[67]: addr: 0x7D8F, data: 0x43
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[68]: addr: 0x7D90, data: 0x46
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[69]: addr: 0x7D91, data: 0x4D
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[70]: addr: 0x7D92, data: 0x59
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[71]: addr: 0x7D93, data: 0x64
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[72]: addr: 0x7D94, data: 0x39
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[73]: addr: 0x7D95, data: 0x3B
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[74]: addr: 0x7D96, data: 0x3F
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[75]: addr: 0x7D97, data: 0x43
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[76]: addr: 0x7D98, data: 0x46
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[77]: addr: 0x7D99, data: 0x4D
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[78]: addr: 0x7D9A, data: 0x59
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[79]: addr: 0x7D9B, data: 0x64
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[80]: addr: 0x7D9C, data: 0x3A
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[81]: addr: 0x7D9D, data: 0x3C
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[82]: addr: 0x7D9E, data: 0x3F
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[83]: addr: 0x7D9F, data: 0x43
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[84]: addr: 0x7DA0, data: 0x46
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[85]: addr: 0x7DA1, data: 0x4E
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[86]: addr: 0x7DA2, data: 0x57
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[87]: addr: 0x7DA3, data: 0x61
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[88]: addr: 0x7DA4, data: 0x3A
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[89]: addr: 0x7DA5, data: 0x3C
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[90]: addr: 0x7DA6, data: 0x3F
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[91]: addr: 0x7DA7, data: 0x43
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[92]: addr: 0x7DA8, data: 0x47
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[93]: addr: 0x7DA9, data: 0x4D
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[94]: addr: 0x7DAA, data: 0x55
    <SENSOR><ERROR> chiron_imx386_semco_format_spcdata: 422: OTP: SPCData[95]: addr: 0x7DAB, data: 0x5D
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[0]: u7.9: 0x7264, float: 57.195312
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[1]: u7.9: 0x55f6, float: 42.980469
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[2]: u7.9: 0x55f6, float: 42.980469
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[3]: u7.9: 0x5920, float: 44.562500
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[4]: u7.9: 0x59ad, float: 44.837891
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[5]: u7.9: 0x5895, float: 44.291016
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[6]: u7.9: 0x5e56, float: 47.167969
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[7]: u7.9: 0x7e54, float: 63.164062
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[8]: u7.9: 0x6431, float: 50.095703
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[9]: u7.9: 0x4d46, float: 38.636719
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[10]: u7.9: 0x56fe, float: 43.496094
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[11]: u7.9: 0x5bf3, float: 45.974609
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[12]: u7.9: 0x5e56, float: 47.167969
09-19 00:10:55.007 774-774/? E/mm-camera: <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[13]: u7.9: 0x59ad, float: 44.837891
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[14]: u7.9: 0x580c, float: 44.023438
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[15]: u7.9: 0x67c5, float: 51.884766
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[16]: u7.9: 0x55f6, float: 42.980469
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[17]: u7.9: 0x4c76, float: 38.230469
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[18]: u7.9: 0x5a3c, float: 45.117188
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[19]: u7.9: 0x5f94, float: 47.789062
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[20]: u7.9: 0x60da, float: 48.425781
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[21]: u7.9: 0x5c88, float: 46.265625
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[22]: u7.9: 0x5304, float: 41.507812
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[23]: u7.9: 0x6036, float: 48.105469
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[24]: u7.9: 0x56fe, float: 43.496094
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[25]: u7.9: 0x4baa, float: 37.832031
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[26]: u7.9: 0x5acc, float: 45.398438
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[27]: u7.9: 0x6036, float: 48.105469
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[28]: u7.9: 0x6229, float: 49.080078
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[29]: u7.9: 0x5d20, float: 46.562500
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[30]: u7.9: 0x50b6, float: 40.355469
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[31]: u7.9: 0x5ef4, float: 47.476562
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[32]: u7.9: 0x5d20, float: 46.562500
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[33]: u7.9: 0x4e87, float: 39.263672
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[34]: u7.9: 0x5679, float: 43.236328
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[35]: u7.9: 0x5bf3, float: 45.974609
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[36]: u7.9: 0x5dba, float: 46.863281
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[37]: u7.9: 0x5895, float: 44.291016
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[38]: u7.9: 0x54f5, float: 42.478516
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[39]: u7.9: 0x64e3, float: 50.443359
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[40]: u7.9: 0x6a0b, float: 53.021484
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[41]: u7.9: 0x59ad, float: 44.837891
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[42]: u7.9: 0x5575, float: 42.728516
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[43]: u7.9: 0x5895, float: 44.291016
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[44]: u7.9: 0x5920, float: 44.562500
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[45]: u7.9: 0x5920, float: 44.562500
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[46]: u7.9: 0x5bf3, float: 45.974609
    <SENSOR><ERROR> chiron_imx386_semco_format_dccdata: 453: OTP SlopeData[47]: u7.9: 0x7a15, float: 61.041016
09-19 00:10:55.009 774-774/? E/mm-camera: <SENSOR><ERROR> chiron_ov5675_primax_eeprom_format_module_info: 181: OTP: module id 37, lens id 2, sensor id 10, product id 16, mirror 0, flip 0
    <SENSOR><ERROR> chiron_ov5675_primax_eeprom_format_wbdata_table: 92: OTP: buffer[30] 2 20 2 5a
    <SENSOR><ERROR> chiron_ov5675_primax_eeprom_format_wbdata_table: 93: OTP: buffer 200 200
    <SENSOR><ERROR> chiron_ov5675_primax_eeprom_format_wbdata_table: 95: OTP:LightType[6]:awb_r_over_g: 0.531250,awb_b_over_g: 0.587891,awb_gr_over_gb: 1.000000
09-19 00:10:55.028 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:55.039 1081-1081/? I/Atfwd_Daemon: qmi_client_init_instance status retry : 1
     qmi_client_init_instance....
09-19 00:10:55.043 1081-1081/? I/Atfwd_Daemon: qmi_client_init_instance status: -3, num_retries: 2, retryCnt: 1
    result : -3 	 ,Init step :1 	 ,qmiErrorCode: 0
     Sleeping...
09-19 00:10:55.068 765-765/? I/Zygote: Preloading resources...
09-19 00:10:55.085 765-765/? W/Resources: Preloaded drawable resource #0x108027e (android:drawable/dialog_background_material) that varies with configuration!!
09-19 00:10:55.102 755-755/? I/Riru: found Riru in zygote64 (pid=765)
09-19 00:10:55.102 755-755/? V/Riru: check again after 1s, remaining 1 times
09-19 00:10:55.106 765-765/? I/Zygote: ...preloaded 64 resources in 38ms.
09-19 00:10:55.110 765-765/? I/Zygote: ...preloaded 41 resources in 3ms.
09-19 00:10:55.110 765-765/? D/Zygote64Timing: PreloadResources took to complete: 194ms
09-19 00:10:55.119 765-765/? D/libEGL: loaded /vendor/lib64/egl/libEGL_adreno.so
09-19 00:10:55.124 765-765/? D/libEGL: loaded /vendor/lib64/egl/libGLESv1_CM_adreno.so
09-19 00:10:55.126 765-765/? D/libEGL: loaded /vendor/lib64/egl/libGLESv2_adreno.so
09-19 00:10:55.128 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:55.139 765-765/? I/Zygote: Preloading shared libraries...
09-19 00:10:55.146 765-765/? I/Zygote: Called ZygoteHooks.endPreload()
09-19 00:10:55.147 765-765/? I/Zygote: Installed AndroidKeyStoreProvider in 0ms.
09-19 00:10:55.153 765-765/? I/Zygote: Warmed up JCA providers in 6ms.
09-19 00:10:55.153 765-765/? D/Zygote: end preload
09-19 00:10:55.153 765-765/? D/Zygote64Timing: ZygotePreload took to complete: 919ms
09-19 00:10:55.155 1135-1165/? E/LocSvc_LocIpc: sendData:193] cannot send to socket. reason:No such file or directory
09-19 00:10:55.172 765-765/? I/zygote64: Explicit concurrent copying GC freed 63565(3547KB) AllocSpace objects, 17(408KB) LOS objects, 90% free, 2571KB/26MB, paused 38us total 18.631ms
09-19 00:10:55.172 772-847/? E/audio_route: Control 'MultiMedia4 Mixer MI2S_TX' doesn't exist - skipping
    Control 'MultiMedia7 Mixer MI2S_TX' doesn't exist - skipping
09-19 00:10:55.173 772-847/? E/audio_route: Control 'MultiMedia10 Mixer MI2S_TX' doesn't exist - skipping
    Control 'MultiMedia11 Mixer MI2S_TX' doesn't exist - skipping
    Control 'MultiMedia12 Mixer MI2S_TX' doesn't exist - skipping
    Control 'MultiMedia13 Mixer MI2S_TX' doesn't exist - skipping
    Control 'MultiMedia14 Mixer MI2S_TX' doesn't exist - skipping
    Control 'MultiMedia15 Mixer MI2S_TX' doesn't exist - skipping
09-19 00:10:55.175 772-847/? E/audio_route: Control 'QUAT_MI2S_RX Audio Mixer MultiMedia9' doesn't exist - skipping
09-19 00:10:55.177 772-847/? E/audio_route: Control 'SpkrLeft COMP Switch' doesn't exist - skipping
    Control 'SpkrRight COMP Switch' doesn't exist - skipping
    Control 'SpkrLeft BOOST Switch' doesn't exist - skipping
    Control 'SpkrRight BOOST Switch' doesn't exist - skipping
    Control 'SpkrLeft VISENSE Switch' doesn't exist - skipping
    Control 'SpkrRight VISENSE Switch' doesn't exist - skipping
    Control 'SpkrLeft SWR DAC_Port Switch' doesn't exist - skipping
    Control 'SpkrRight SWR DAC_Port Switch' doesn't exist - skipping
09-19 00:10:55.181 772-847/? E/audio_route: Control 'SpkrLeft WSA PA Gain' doesn't exist - skipping
    Control 'LSM1 MUX' doesn't exist - skipping
09-19 00:10:55.182 772-847/? E/audio_route: Control 'LSM2 MUX' doesn't exist - skipping
    Control 'LSM3 MUX' doesn't exist - skipping
    Control 'LSM4 MUX' doesn't exist - skipping
    Control 'LSM5 MUX' doesn't exist - skipping
    Control 'LSM6 MUX' doesn't exist - skipping
    Control 'LSM7 MUX' doesn't exist - skipping
    Control 'LSM8 MUX' doesn't exist - skipping
09-19 00:10:55.185 772-847/? E/audio_route: unable to find sub path 'audio-ull-playback speaker-safe'
09-19 00:10:55.185 772-847/? I/chatty: uid=1041(audioserver) HwBinder:772_2 identical 3 lines
09-19 00:10:55.185 772-847/? E/audio_route: unable to find sub path 'audio-ull-playback speaker-safe'
09-19 00:10:55.188 765-765/? I/zygote64: Explicit concurrent copying GC freed 6272(213KB) AllocSpace objects, 0(0B) LOS objects, 91% free, 2389KB/26MB, paused 13us total 11.026ms
09-19 00:10:55.188 765-765/? D/Zygote64Timing: PostZygoteInitGC took to complete: 34ms
    ZygoteInit took to complete: 954ms
09-19 00:10:55.192 772-847/? E/audio_route: Control 'MultiMedia8 Mixer SLIM_8_TX' doesn't exist - skipping
09-19 00:10:55.193 772-847/? E/audio_route: Control 'AUX PCM SampleRate' doesn't exist - skipping
09-19 00:10:55.198 772-847/? E/audio_route: Control 'LSM1 MUX' doesn't exist - skipping
    Control 'LSM2 MUX' doesn't exist - skipping
    Control 'LSM3 MUX' doesn't exist - skipping
    Control 'LSM4 MUX' doesn't exist - skipping
09-19 00:10:55.199 772-847/? E/audio_route: Control 'LSM5 MUX' doesn't exist - skipping
    Control 'LSM6 MUX' doesn't exist - skipping
    Control 'LSM7 MUX' doesn't exist - skipping
    Control 'LSM8 MUX' doesn't exist - skipping
    Control 'SLIM_1_RX Channels' doesn't exist - skipping
09-19 00:10:55.200 772-847/? E/audio_route: Control 'SLIM_1_RX SampleRate' doesn't exist - skipping
    Control 'SLIM_1_TX SampleRate' doesn't exist - skipping
09-19 00:10:55.201 772-847/? E/audio_route: Control 'SpkrLeft COMP Switch' doesn't exist - skipping
09-19 00:10:55.202 772-847/? E/audio_route: Control 'SpkrLeft BOOST Switch' doesn't exist - skipping
    Control 'SpkrLeft VISENSE Switch' doesn't exist - skipping
    Control 'SpkrLeft SWR DAC_Port Switch' doesn't exist - skipping
09-19 00:10:55.204 772-847/? E/audio_route: Control 'SpkrLeft SWR DAC_Port Switch' doesn't exist - skipping
    Control 'SpkrLeft WSA PA Gain' doesn't exist - skipping
09-19 00:10:55.209 772-847/? E/audio_route: unable to find sub path 'audio-ull-playback speaker-safe'
09-19 00:10:55.216 774-774/? E/mm-camera: <IMGLIB><ERROR> 1347: frameproc_comp_reload_lib: Error opening frameproc library libmmcamera_llvd.so error dlopen failed: library "libllvd_smore.so" not found
09-19 00:10:55.217 774-774/? E/mm-camera: <IMGLIB><ERROR> 1213: frameproc_comp_load: frameproc_comp_load:1213] cannot load libmmcamera_llvd.so
    <IMGLIB><ERROR> 3475: module_imgbase_init: llvd] Error rc -7
09-19 00:10:55.223 772-847/? D/msm8974_platform: Opening /sys/class/thermal/thermal_zone0/type
    Opening /sys/class/thermal/thermal_zone1/type
    Opening /sys/class/thermal/thermal_zone2/type
09-19 00:10:55.224 772-847/? D/msm8974_platform: Opening /sys/class/thermal/thermal_zone3/type
    Opening /sys/class/thermal/thermal_zone4/type
    Opening /sys/class/thermal/thermal_zone5/type
    Opening /sys/class/thermal/thermal_zone6/type
    Opening /sys/class/thermal/thermal_zone7/type
    Opening /sys/class/thermal/thermal_zone8/type
    Opening /sys/class/thermal/thermal_zone9/type
    Opening /sys/class/thermal/thermal_zone10/type
    Opening /sys/class/thermal/thermal_zone11/type
    Opening /sys/class/thermal/thermal_zone12/type
    Opening /sys/class/thermal/thermal_zone13/type
    Opening /sys/class/thermal/thermal_zone14/type
    Opening /sys/class/thermal/thermal_zone15/type
    Opening /sys/class/thermal/thermal_zone16/type
    Opening /sys/class/thermal/thermal_zone17/type
    Opening /sys/class/thermal/thermal_zone18/type
09-19 00:10:55.225 772-847/? D/msm8974_platform: Opening /sys/class/thermal/thermal_zone19/type
    Opening /sys/class/thermal/thermal_zone20/type
    Opening /sys/class/thermal/thermal_zone21/type
    Opening /sys/class/thermal/thermal_zone22/type
    Opening /sys/class/thermal/thermal_zone23/type
    Opening /sys/class/thermal/thermal_zone24/type
    Opening /sys/class/thermal/thermal_zone25/type
    Opening /sys/class/thermal/thermal_zone26/type
    Opening /sys/class/thermal/thermal_zone27/type
    Opening /sys/class/thermal/thermal_zone28/type
    Opening /sys/class/thermal/thermal_zone29/type
    Opening /sys/class/thermal/thermal_zone30/type
    Opening /sys/class/thermal/thermal_zone31/type
    Opening /sys/class/thermal/thermal_zone32/type
    Opening /sys/class/thermal/thermal_zone33/type
    Opening /sys/class/thermal/thermal_zone34/type
09-19 00:10:55.226 772-847/? D/msm8974_platform: Opening /sys/class/thermal/thermal_zone35/type
    Opening /sys/class/thermal/thermal_zone36/type
    Opening /sys/class/thermal/thermal_zone37/type
09-19 00:10:55.226 772-847/? D/audio_hw_extn: audio_extn_can_use_vbat: vbat.enabled property is set to 0
    audio_extn_can_use_bcl: bcl.enabled property is set to 0
09-19 00:10:55.226 772-847/? D/msm8974_platform: Alac software decoder is available...removing alac from DSP decoder list
    APE software decoder is available...removing ape from DSP decoder list
09-19 00:10:55.226 772-847/? I/audio_hw_extn: audio_extn_set_snd_card_split: snd_card_name(msm8998-tasha-snd-card) device(msm8998) snd_card(tasha) form_factor(snd)
09-19 00:10:55.226 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_OUT_HEADPHONES_NATIVE_44_1
09-19 00:10:55.226 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_OUT_HEADPHONES_NATIVE_44_1 in platform info xml not found, no ACDB ID set!
09-19 00:10:55.226 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_OUT_HIFI_HEADPHONES
09-19 00:10:55.226 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_OUT_HIFI_HEADPHONES in platform info xml not found, no ACDB ID set!
09-19 00:10:55.226 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_OUT_HIFI_HEADPHONES_44_1
09-19 00:10:55.226 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_OUT_HIFI_HEADPHONES_44_1 in platform info xml not found, no ACDB ID set!
09-19 00:10:55.227 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_OUT_HIFI_HEADPHONES_NATIVE_44_1
09-19 00:10:55.227 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_OUT_HIFI_HEADPHONES_NATIVE_44_1 in platform info xml not found, no ACDB ID set!
09-19 00:10:55.227 774-774/? E/mm-camera: <IMGLIB><ERROR> 3895: module_qdc_common_init:  Algo Capabilities Crop caps 2,core type 2, access mode 1, exec mode 1
09-19 00:10:55.227 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_MAIN_MIC
09-19 00:10:55.227 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_MAIN_MIC in platform info xml not found, no ACDB ID set!
09-19 00:10:55.227 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_TOP_MIC
09-19 00:10:55.227 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_TOP_MIC in platform info xml not found, no ACDB ID set!
09-19 00:10:55.227 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_FRONT_MIC
09-19 00:10:55.227 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_FRONT_MIC in platform info xml not found, no ACDB ID set!
09-19 00:10:55.227 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_HANDSET_DMIC_MUSIC
09-19 00:10:55.227 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_HANDSET_DMIC_MUSIC in platform info xml not found, no ACDB ID set!
09-19 00:10:55.227 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_HANDSET_DMIC_VOICE
09-19 00:10:55.227 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_HANDSET_DMIC_VOICE in platform info xml not found, no ACDB ID set!
09-19 00:10:55.227 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_HANDSET_DMIC_INTERVIEW
09-19 00:10:55.227 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_HANDSET_DMIC_INTERVIEW in platform info xml not found, no ACDB ID set!
09-19 00:10:55.227 774-774/? E/mm-camera: <IMGLIB><ERROR> 2076: multi_frameproc_core_reload_lib: Error opening multi_frameproc library libmmcamera_sac_lib.so error dlopen failed: library "libmmcamera_sac_lib.so" not found
09-19 00:10:55.227 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_HANDSET_DMIC_HD
09-19 00:10:55.227 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_HANDSET_DMIC_HD in platform info xml not found, no ACDB ID set!
09-19 00:10:55.227 774-774/? E/mm-camera: <IMGLIB><ERROR> 2205: multi_frameproc_core_load: cannot load libmmcamera_sac_lib.so status -7
    <IMGLIB><ERROR> 3475: module_imgbase_init: sac] Error rc -7
    <IMGLIB><ERROR> 3869: module_qdc_common_init: mct module 0x0
09-19 00:10:55.227 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_VOICE_SPEAKER_TMIC_CONF
09-19 00:10:55.227 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_VOICE_SPEAKER_TMIC_CONF in platform info xml not found, no ACDB ID set!
09-19 00:10:55.227 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_CAMCORDER_DMIC
09-19 00:10:55.227 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_CAMCORDER_DMIC in platform info xml not found, no ACDB ID set!
09-19 00:10:55.227 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_CAMCORDER_TMIC
09-19 00:10:55.227 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_CAMCORDER_TMIC in platform info xml not found, no ACDB ID set!
09-19 00:10:55.227 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_CAMCORDER_TMIC_FAR_END
09-19 00:10:55.228 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_CAMCORDER_TMIC_FAR_END in platform info xml not found, no ACDB ID set!
09-19 00:10:55.228 772-847/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_CAMCORDER_TMIC_NEAR_END
09-19 00:10:55.228 772-847/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_CAMCORDER_TMIC_NEAR_END in platform info xml not found, no ACDB ID set!
09-19 00:10:55.228 772-847/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:10:55.228 772-847/? I/chatty: uid=1041(audioserver) HwBinder:772_2 identical 2 lines
09-19 00:10:55.228 772-847/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:10:55.228 772-847/? D/msm8974_platform: native_audio_set_params:napb updating mode (1) from XML
    platform_set_native_support:napb: native audio playback enabled in (SRC) mode
09-19 00:10:55.228 772-847/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:10:55.228 772-847/? D/msm8974_platform: native_audio_set_params:napb updating mode (1) from XML
    platform_set_native_support:napb: native audio playback enabled in (SRC) mode
09-19 00:10:55.228 772-847/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:10:55.228 772-847/? D/msm8974_platform: native_audio_set_params:napb updating mode (1) from XML
    platform_set_native_support:napb: native audio playback enabled in (SRC) mode
09-19 00:10:55.228 772-847/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:10:55.228 772-847/? D/msm8974_platform: native_audio_set_params:napb updating mode (1) from XML
    platform_set_native_support:napb: native audio playback enabled in (SRC) mode
09-19 00:10:55.228 772-847/? V/audio_hw_usb: usb_set_sidetone_gain: sidetone gain(35) decimal 3162
09-19 00:10:55.228 772-847/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:10:55.228 772-847/? D/msm8974_platform: native_audio_set_params:napb updating mode (1) from XML
    platform_set_native_support:napb: native audio playback enabled in (SRC) mode
09-19 00:10:55.228 772-847/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:10:55.228 772-847/? D/msm8974_platform: platform_set_snd_device_backend: backend_tag_table[headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[9] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[headphones-hifi-filter]: old = headphones-hifi-filter new = headphones
    platform_set_snd_device_backend: hw_interface_table[11] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[bt-sco-headset-wb]: old = bt-sco-wb new = bt-sco-wb
    platform_set_snd_device_backend: hw_interface_table[34] = SLIMBUS_7_RX
    platform_set_snd_device_backend: backend_tag_table[bt-sco-headset]: old = bt-sco new = bt-sco
    platform_set_snd_device_backend: hw_interface_table[33] = SLIMBUS_7_RX
    platform_set_snd_device_backend: backend_tag_table[bt-a2dp]: old = bt-a2dp new = bt-a2dp
    platform_set_snd_device_backend: hw_interface_table[36] = SLIMBUS_7_RX
    platform_set_snd_device_backend: backend_tag_table[line]: old = null new = headphones
09-19 00:10:55.229 772-847/? D/msm8974_platform: platform_set_snd_device_backend: hw_interface_table[8] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[anc-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[69] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[anc-fb-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[70] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[handset]: old = null new = receiver
    platform_set_snd_device_backend: hw_interface_table[1] = QUAT_MI2S_RX
    platform_set_snd_device_backend: backend_tag_table[voice-handset]: old = null new = receiver
    platform_set_snd_device_backend: hw_interface_table[20] = QUAT_MI2S_RX
    platform_set_snd_device_backend: backend_tag_table[speaker]: old = null new = speaker
    platform_set_snd_device_backend: hw_interface_table[2] = QUAT_MI2S_RX
    platform_set_snd_device_backend: backend_tag_table[voice-speaker]: old = null new = speaker
    platform_set_snd_device_backend: hw_interface_table[21] = QUAT_MI2S_RX
    platform_set_snd_device_backend: backend_tag_table[voice-speaker-2]: old = null new = speaker
    platform_set_snd_device_backend: hw_interface_table[24] = QUAT_MI2S_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-headphones]: old = null new = speaker-and-headphones
    platform_set_snd_device_backend: hw_interface_table[13] = QUAT_MI2S_RX-and-SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-headphones-hifi-filter]: old = speaker-and-headphones-hifi-filter new = speaker-and-headphones
    platform_set_snd_device_backend: hw_interface_table[14] = QUAT_MI2S_RX-and-SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-line]: old = null new = speaker-and-headphones
    platform_set_snd_device_backend: hw_interface_table[16] = QUAT_MI2S_RX-and-SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-anc-headphones]: old = null new = speaker-and-headphones
    platform_set_snd_device_backend: hw_interface_table[73] = QUAT_MI2S_RX-and-SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-anc-fb-headphones]: old = null new = speaker-and-headphones
    platform_set_snd_device_backend: hw_interface_table[74] = QUAT_MI2S_RX-and-SLIMBUS_6_RX
09-19 00:10:55.229 774-774/? E/mm-camera: <IMGLIB><ERROR> 3895: module_qdc_common_init:  Algo Capabilities Crop caps 0,core type 0, access mode 0, exec mode 0
09-19 00:10:55.229 772-847/? D/msm8974_platform: platform_set_snd_device_backend: backend_tag_table[speaker-and-hdmi]: old = speaker-and-hdmi new = speaker-and-hdmi
    platform_set_snd_device_backend: hw_interface_table[30] = QUAT_MI2S_RX-and-HDMI
    platform_set_snd_device_backend: backend_tag_table[speaker-and-display-port]: old = speaker-and-display-port new = speaker-and-display-port
    platform_set_snd_device_backend: hw_interface_table[32] = QUAT_MI2S_RX-and-DISPLAY_PORT
    platform_set_snd_device_backend: backend_tag_table[speaker-and-bt-a2dp]: old = speaker-and-bt-a2dp new = speaker-and-bt-a2dp
    platform_set_snd_device_backend: hw_interface_table[37] = QUAT_MI2S_RX-and-SLIMBUS_7_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-bt-sco]: old = null new = speaker-and-bt-sco
    platform_set_snd_device_backend: hw_interface_table[40] = QUAT_MI2S_RX-and-SLIMBUS_7_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-bt-sco-wb]: old = null new = speaker-and-bt-sco-wb
    platform_set_snd_device_backend: hw_interface_table[42] = QUAT_MI2S_RX-and-SLIMBUS_7_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-usb-headphones]: old = speaker-and-usb-headphones new = speaker-and-usb-headphones
    platform_set_snd_device_backend: hw_interface_table[63] = QUAT_MI2S_RX-and-USB_AUDIO_RX
    platform_set_snd_device_backend: backend_tag_table[voice-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[26] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[voice-anc-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[71] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[voice-anc-fb-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[72] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[voice-line]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[28] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[voice-tty-full-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[49] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[voice-tty-vco-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[51] = SLIMBUS_6_RX
09-19 00:10:55.230 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:55.231 772-847/? E/msm8974_platform: platform_init: soundcard: msm8998-tasha-snd-card supports only default sample rate
09-19 00:10:55.241 772-847/? E/msm8974_platform: platform_init: Could not find the symbol acdb_send_audio_cal_v4 from libacdbloader.so
    platform_init: dlsym error undefined symbol: acdb_loader_init_v4 for acdb_loader_init_v4
09-19 00:10:55.241 772-847/? I/audio_hw_extn: audio_extn_set_snd_card_split: snd_card_name(msm8998-tasha-snd-card) device(msm8998) snd_card(tasha) form_factor(snd)
09-19 00:10:55.242 772-847/? E/platform_info: param tag only supported with CONFIG_PARAMS section
09-19 00:10:55.242 772-847/? I/chatty: uid=1041(audioserver) HwBinder:772_2 identical 7 lines
09-19 00:10:55.242 772-847/? E/platform_info: param tag only supported with CONFIG_PARAMS section
09-19 00:10:55.243 772-847/? E/audio_hw_acdb: acdb_init_v2: dlsym error undefined symbol: acdb_loader_init_v4 for acdb_loader_init_v4
09-19 00:10:55.243 772-847/? D/ACDB-LOADER: ACDB -> Load file: /vendor/etc/acdbdata/adsp_avs_config.acdb
    ACDB -> found 1 form factor & soundcard independant files
09-19 00:10:55.243 772-847/? I/ACDB-LOADER: ACDB -> Info: ACDB file path is /vendor/etc/acdbdata/Forte
09-19 00:10:55.244 772-847/? D/ACDB-LOADER: ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_Bluetooth_cal.acdb
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_Speaker_cal.acdb
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_Handset_cal.acdb
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_Headset_cal.acdb
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_General_cal.acdb
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_workspaceFile.qwsp
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_Hdmi_cal.acdb
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_Global_cal.acdb
09-19 00:10:55.244 772-847/? I/ACDB-LOADER: ACDB -> Info: Loaded ForteMedia ACDB!
09-19 00:10:55.244 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_INITIALIZE_V2
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 3926799360, ACDB File Minor = 2335533130, ACDB File Revision = 0
09-19 00:10:55.240 765-765/? W/main: type=1400 audit(0.0:31): avc: denied { write } for name="/" dev="tmpfs" ino=23802 scontext=u:r:zygote:s0 tcontext=u:object_r:system_file:s0 tclass=dir permissive=0
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
09-19 00:10:55.246 774-774/? E/mm-camera: <IMGLIB><ERROR> 3895: module_qdc_common_init:  Algo Capabilities Crop caps 0,core type 2, access mode 1, exec mode 1
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
09-19 00:10:55.247 870-870/? I/adbd: UsbFfs: already offline
    Calling send_auth_request...
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
09-19 00:10:55.250 765-765/? W/main: type=1400 audit(0.0:32): avc: denied { write } for name="/" dev="tmpfs" ino=23802 scontext=u:r:zygote:s0 tcontext=u:object_r:system_file:s0 tclass=dir permissive=0
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
    ACDBFILE_MGR:Read the devices count as zero, please check the acdb file
09-19 00:10:55.253 772-847/? D/ACDB-LOADER: ACDB -> ACPH INIT
09-19 00:10:55.253 772-847/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    diag: In diagpkt_tbl_reg, service not initialized.
09-19 00:10:55.253 772-847/? D/ACDB-LOADER: ACDB -> RTAC INIT
09-19 00:10:55.254 772-847/? D/ACDB-LOADER: ACDB -> MCS, FTS INIT
09-19 00:10:55.254 772-847/? E/ACDB-MCS: acdb_mcs_init: /vendor/etc/audio_tuning_mixer_tasha.txt not present, using /vendor/etc/audio_tuning_mixer.txt config file
09-19 00:10:55.254 772-847/? E/MCS-RT-CTL: Can't open the configuration file /vendor/etc/audio_tuning_mixer.txt.
09-19 00:10:55.254 772-847/? E/ACDB-MCS: acdb_mcs_init: MCS routing control initialization failed.
09-19 00:10:55.254 772-847/? D/ACDB-LOADER: ACDB -> ADIE RTAC INIT
09-19 00:10:55.254 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_VOC_PROC_DYNAMIC_TABLE_SIZE
09-19 00:10:55.254 774-774/? E/mm-camera: <IMGLIB><ERROR> 570: fphwtw_tracker_load_fptrs: Loading HWTracker_ResetTracking error undefined symbol: HWTracker_ResetTracking
    <IMGLIB><ERROR> 1612: faceproc_hw_tracker_wrapper_load_library: Failed in loading Tracker function pointers
09-19 00:10:55.255 774-774/? E/mm-camera: <IMGLIB><ERROR> 5871: faceproc_hw_comp_load: Faceproc sw wrapper load failed
09-19 00:10:55.255 774-774/? W/mm-camera: <IMGLIB>< WARN> 1235: faceproc_dsp_comp_load: face detection dsp disabled , enable by set property
09-19 00:10:55.259 870-870/? I/adbd: Loading keys from /data/misc/adb/adb_keys
09-19 00:10:55.260 772-847/? D/ACDB-LOADER: ACDB -> send_common_custom_topology
    ACDB -> ACDB_CMD_GET_AVCS_CUSTOM_TOPO_INFO_SIZE
    ACDB -> ACDB_CMD_GET_AVCS_CUSTOM_TOPO_INFO
    ACDB -> ACDB_CMD_GET_AVCS_CUSTOM_TOPO_INFO: size:0x4ac ret=0 
    ACDB -> CORE_CUSTOM_TOPOLOGIES
09-19 00:10:55.260 870-870/? I/adbd: adb client authorized
09-19 00:10:55.263 772-847/? D/ACDB-LOADER: ACDB -> acdb_loader_send_common_custom_topology: Common custom topology in use
    ACDB -> init done!
09-19 00:10:55.263 772-847/? D/audio_hw_acdb: acdb_init_v2: ACDB Instance ID support after ACDB init:0
09-19 00:10:55.263 772-847/? D/msm8974_platform: ACDB initialized
    hw_util_open Opening device /dev/snd/hwC0D1000
09-19 00:10:55.264 772-847/? D/msm8974_platform: hw_util_open success
09-19 00:10:55.264 774-774/? E/mm-camera: <IMGLIB><ERROR> 1347: frameproc_comp_reload_lib: Error opening frameproc library libmmcamera_chromaflash_lib.so error dlopen failed: library "libchromaflash.so" not found
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:10:55.264 774-774/? E/mm-camera: <IMGLIB><ERROR> 1213: frameproc_comp_load: frameproc_comp_load:1213] cannot load libmmcamera_chromaflash_lib.so
    <IMGLIB><ERROR> 3475: module_imgbase_init: imglib_chroma_flash] Error rc -7
09-19 00:10:55.264 772-847/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:10:55.264 774-774/? W/mm-camera: <IMGLIB>< WARN> 743: module_imglib_create_topology: Can not init the module imglib_chroma_flash
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:10:55.264 772-847/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:10:55.264 772-847/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:10:55.264 772-847/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:10:55.264 772-847/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:10:55.264 772-847/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:10:55.264 772-847/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:10:55.264 772-847/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:10:55.264 772-847/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:10:55.264 772-847/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:10:55.264 772-847/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:10:55.264 772-847/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:10:55.264 772-847/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:10:55.264 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:10:55.265 772-847/? D/ACDB-LOADER: send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:10:55.265 772-847/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:10:55.265 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:10:55.265 772-847/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:10:55.265 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:10:55.265 772-847/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:10:55.265 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:10:55.265 772-847/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:10:55.265 772-847/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:10:55.265 772-847/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:10:55.265 772-847/? D/msm8974_platform: send_codec_cal: anc_cal cal sent successfully
09-19 00:10:55.265 772-847/? D/ACDB-LOADER: send mbhc data
    ACDB -> MBHC ACDB_PID_GENERAL_CONFIG
    ACDB -> MBHC ACDB_PID_PLUG_REMOVAL_DETECTION
    ACDB -> MBHC ACDB_PID_PLUG_TYPE_DETECTION
    ACDB -> MBHC ACDB_PID_BUTTON_PRESS_DETECTION
    ACDB -> MBHC ACDB_PID_IMPEDANCE_DETECTION
09-19 00:10:55.265 772-847/? D/msm8974_platform: send_codec_cal: mbhc_cal cal sent successfully
09-19 00:10:55.265 772-847/? D/ACDB-LOADER: send vbat data
    ACDB -> VBAT ACDB_PID_ADC_CAL
09-19 00:10:55.265 774-774/? E/mm-camera: <IMGLIB><ERROR> 1347: frameproc_comp_reload_lib: Error opening frameproc library libmmcamera_optizoom_lib.so error dlopen failed: library "liboptizoom.so" not found
09-19 00:10:55.265 772-847/? D/ACDB-LOADER: ACDB -> VBAT ACDB_PID_GAIN_PROC
    send vbat data, calling convert_vbat_data
09-19 00:10:55.265 774-774/? E/mm-camera: <IMGLIB><ERROR> 1213: frameproc_comp_load: frameproc_comp_load:1213] cannot load libmmcamera_optizoom_lib.so
09-19 00:10:55.265 772-847/? D/ACDB-LOADER: copied vbat cal size =72
09-19 00:10:55.265 774-774/? E/mm-camera: <IMGLIB><ERROR> 3475: module_imgbase_init: imglib_optizoom] Error rc -7
09-19 00:10:55.265 772-847/? D/msm8974_platform: send_codec_cal: vbat_cal cal sent successfully
09-19 00:10:55.265 774-774/? W/mm-camera: <IMGLIB>< WARN> 743: module_imglib_create_topology: Can not init the module imglib_optizoom
09-19 00:10:55.266 774-774/? E/mm-camera: <IMGLIB><ERROR> 1347: frameproc_comp_reload_lib: Error opening frameproc library libmmcamera_ubifocus_lib.so error dlopen failed: library "libmmcamera_ubifocus_lib.so" not found
    <IMGLIB><ERROR> 1213: frameproc_comp_load: frameproc_comp_load:1213] cannot load libmmcamera_ubifocus_lib.so
    <IMGLIB><ERROR> 3475: module_imgbase_init: imglib_ubifocus] Error rc -7
09-19 00:10:55.266 774-774/? W/mm-camera: <IMGLIB>< WARN> 743: module_imglib_create_topology: Can not init the module imglib_ubifocus
09-19 00:10:55.266 772-847/? W/msm8974_platform: init_be_dai_name_table: sound device  has no hw interface set
09-19 00:10:55.266 772-847/? D/msm8974_platform: init_be_dai_name_table: sound device speaker-and-headphones does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-and-headphones-hifi-filter does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-safe-and-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-and-line does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-safe-and-line does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-and-headphones-ext-1 does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-and-headphones-ext-2 does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-and-hdmi does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-HDMI
    init_be_dai_name_table: sound device speaker-and-display-port does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-DISPLAY_PORT
    init_be_dai_name_table: sound device speaker-and-bt-a2dp does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_7_RX
    init_be_dai_name_table: sound device speaker-safe-and-bt-a2dp does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_7_RX
    init_be_dai_name_table: sound device speaker-and-bt-sco does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_7_RX
    init_be_dai_name_table: sound device speaker-safe-and-bt-sco does not have a valid hw interface set (disregard for combo devices) QUAT_TDM_RX_0-and-SLIMBUS_7_RX
    init_be_dai_name_table: sound device speaker-and-bt-sco-wb does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_7_RX
09-19 00:10:55.266 774-774/? E/mm-camera: <IMGLIB><ERROR> 1347: frameproc_comp_reload_lib: Error opening frameproc library libmmcamera_ubifocus_lib.so error dlopen failed: library "libmmcamera_ubifocus_lib.so" not found
09-19 00:10:55.266 772-847/? D/msm8974_platform: init_be_dai_name_table: sound device speaker-safe-and-bt-sco-wb does not have a valid hw interface set (disregard for combo devices) QUAT_TDM_RX_0-and-SLIMBUS_7_RX
09-19 00:10:55.266 774-774/? E/mm-camera: <IMGLIB><ERROR> 1213: frameproc_comp_load: frameproc_comp_load:1213] cannot load libmmcamera_ubifocus_lib.so
09-19 00:10:55.266 772-847/? D/msm8974_platform: init_be_dai_name_table: sound device speaker-and-bt-sco-swb does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SEC_AUX_PCM_RX
09-19 00:10:55.266 774-774/? E/mm-camera: <IMGLIB><ERROR> 3475: module_imgbase_init: imglib_refocus] Error rc -7
09-19 00:10:55.266 772-847/? D/msm8974_platform: init_be_dai_name_table: sound device speaker-safe-and-bt-sco-swb does not have a valid hw interface set (disregard for combo devices) QUAT_TDM_RX_0-and-SLIMBUS_7_RX
09-19 00:10:55.266 774-774/? W/mm-camera: <IMGLIB>< WARN> 743: module_imglib_create_topology: Can not init the module imglib_refocus
09-19 00:10:55.266 772-847/? W/msm8974_platform: init_be_dai_name_table: sound device wsa-speaker-and-bt-sco has no hw interface set
    init_be_dai_name_table: sound device wsa-speaker-and-bt-sco-wb has no hw interface set
    init_be_dai_name_table: sound device wsa-speaker-and-bt-sco-wb has no hw interface set
09-19 00:10:55.266 772-847/? D/msm8974_platform: init_be_dai_name_table: sound device speaker-and-usb-headphones does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-USB_AUDIO_RX
    init_be_dai_name_table: sound device speaker-safe-and-usb-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-USB_AUDIO_RX
    init_be_dai_name_table: sound device speaker-and-anc-headphones does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-and-anc-fb-headphones does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_6_RX
09-19 00:10:55.266 772-847/? W/msm8974_platform: init_be_dai_name_table: sound device speaker-protected has no hw interface set
    init_be_dai_name_table: sound device speaker-protected-vbat has no hw interface set
09-19 00:10:55.266 772-847/? D/msm8974_platform: init_be_dai_name_table: sound device voice-speaker-and-voice-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device voice-speaker-and-voice-anc-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device voice-speaker-and-voice-anc-fb-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device voice-speaker-stereo-and-voice-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device voice-speaker-stereo-and-voice-anc-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device voice-speaker-stereo-and-voice-anc-fb-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device hearing-aid does not have a valid hw interface set (disregard for combo devices) BT_RX
    init_be_dai_name_table: sound device spdif-in does not have a valid hw interface set (disregard for combo devices) PRI_SPDIF_TX
    init_be_dai_name_table: sound device hdmi-arc-in does not have a valid hw interface set (disregard for combo devices) SEC_SPDIF_TX
09-19 00:10:55.266 772-847/? W/msm8974_platform: init_be_dai_name_table: sound device usb-headset-mic has no hw interface set
09-19 00:10:55.266 772-847/? I/chatty: uid=1041(audioserver) HwBinder:772_2 identical 1 line
09-19 00:10:55.266 772-847/? W/msm8974_platform: init_be_dai_name_table: sound device usb-headset-mic has no hw interface set
    init_be_dai_name_table: sound device handset-6mic has no hw interface set
    init_be_dai_name_table: sound device handset-8mic has no hw interface set
    init_be_dai_name_table: sound device (null) has no hw interface set
    init_be_dai_name_table: sound device (null) has no hw interface set
    init_be_dai_name_table: sound device incall-rec-rx-tx has no hw interface set
    init_be_dai_name_table: sound device ec-ref-loopback has no hw interface set
    init_be_dai_name_table: sound device handset-dmic-and-ec-ref-loopback has no hw interface set
09-19 00:10:55.267 772-847/? W/msm8974_platform: init_be_dai_name_table: sound device handset-qmic-and-ec-ref-loopback has no hw interface set
    init_be_dai_name_table: sound device handset-6mic-and-ec-ref-loopback has no hw interface set
    init_be_dai_name_table: sound device handset-8mic-and-ec-ref-loopback has no hw interface set
09-19 00:10:55.267 772-847/? D/audio_hw_extn: audio_extn_can_use_ras: ras.enabled property is set to 0
09-19 00:10:55.267 772-847/? D/msm8974_platform: platform_init: Fluence_Type(1) max_mic_count(4) mic_type(0xf) fluence_in_voice_call(1) fluence_in_voice_rec(0) fluence_in_spkr_mode(1) fluence_in_hfp_call(0)fluence_sb_enabled(0)
    platform_get_snd_device_backend_interface: hw_interface set for device SEC_MI2S_TX
09-19 00:10:55.267 774-774/? E/mm-camera: <IMGLIB><ERROR> 1347: frameproc_comp_reload_lib: Error opening frameproc library libmmcamera_trueportrait_lib.so error dlopen failed: library "libtrueportrait.so" not found
    <IMGLIB><ERROR> 1213: frameproc_comp_load: frameproc_comp_load:1213] cannot load libmmcamera_trueportrait_lib.so
    <IMGLIB><ERROR> 3475: module_imgbase_init: imglib_trueportrait] Error rc -7
09-19 00:10:55.268 774-774/? W/mm-camera: <IMGLIB>< WARN> 743: module_imglib_create_topology: Can not init the module imglib_trueportrait
09-19 00:10:55.269 774-774/? E/mm-camera: <IMGLIB><ERROR> 1347: frameproc_comp_reload_lib: Error opening frameproc library libmmcamera_stillmore_lib.so error dlopen failed: library "libseemore.so" not found
    <IMGLIB><ERROR> 1213: frameproc_comp_load: frameproc_comp_load:1213] cannot load libmmcamera_stillmore_lib.so
    <IMGLIB><ERROR> 3475: module_imgbase_init: imglib_stillmore] Error rc -7
09-19 00:10:55.269 774-774/? W/mm-camera: <IMGLIB>< WARN> 743: module_imglib_create_topology: Can not init the module imglib_stillmore
    <IMGLIB>< WARN> 743: module_imglib_create_topology: Can not init the module imglib_oem1
09-19 00:10:55.269 774-774/? I/QCamera: <MCI><INFO> get_num_of_cameras: 2766: dev_info[id=0,name='video4']
    <MCI><INFO> get_num_of_cameras: 2766: dev_info[id=1,name='video5']
09-19 00:10:55.270 774-774/? I/QCamera: <MCI><INFO> sort_camera_info: 2611: Camera id: 0 facing: 0, type: 1 is_yuv: 0
    <MCI><INFO> sort_camera_info: 2611: Camera id: 1 facing: 1, type: 1 is_yuv: 0
    <MCI><INFO> sort_camera_info: 2617: Number of cameras 2 sorted 2
    <MCI><INFO> get_num_of_cameras: 2784: num_cameras=2
09-19 00:10:55.270 774-774/? I/CamPrvdr@2.4-legacy: Loaded "QCamera Module" camera module
09-19 00:10:55.270 774-774/? I/QCamera: <HAL><INFO> getCameraInfo: 342: Camera id 0 API version 768
09-19 00:10:55.270 774-774/? D/QCamera: Debug log file is not enabled
09-19 00:10:55.267 765-765/? W/main: type=1400 audit(0.0:33): avc: denied { write } for name="/" dev="tmpfs" ino=23802 scontext=u:r:zygote:s0 tcontext=u:object_r:system_file:s0 tclass=dir permissive=0
09-19 00:10:55.277 774-1346/? E/libsensor1: check_sensors_enabled: Sensors enabled = true
09-19 00:10:55.277 774-1346/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:55.285 772-847/? D/msm8974_platform: platform_get_mixer_control: mixer ctl not obtained
09-19 00:10:55.285 772-847/? I/chatty: uid=1041(audioserver) HwBinder:772_2 identical 1 line
09-19 00:10:55.285 772-847/? D/msm8974_platform: platform_get_mixer_control: mixer ctl not obtained
09-19 00:10:55.286 765-765/? W/SandHook-Native: JNI Loaded
09-19 00:10:55.288 772-847/? D/msm8974_platform: platform_get_mixer_control: mixer ctl not obtained
09-19 00:10:55.288 772-847/? I/chatty: uid=1041(audioserver) HwBinder:772_2 identical 1 line
09-19 00:10:55.288 772-847/? D/msm8974_platform: platform_get_mixer_control: mixer ctl not obtained
09-19 00:10:55.288 772-847/? E/audio_hw_utils: audio_extn_utils_get_codec_variant: ERROR. cannot open /proc/asound/card0/codecs/wcd937x/variant
09-19 00:10:55.288 772-847/? D/audio_hw_utils: audio_extn_utils_get_codec_version: codec version WCD9335_2_0
09-19 00:10:55.292 772-847/? E/audio_hw_primary: Amplifier initialization failed
09-19 00:10:55.292 772-847/? D/ultrasound: us_init: enter
09-19 00:10:55.292 765-765/? W/zygote64: Core platform API violation: Ljava/lang/Class;->accessFlags:I from Lcom/elderdrivers/riru/edxp/sandhook/config/SandHookProvider; using JNI
09-19 00:10:55.294 772-847/? D/ultrasound: us_init: exit, status(0)
09-19 00:10:55.294 772-847/? D/audio_hw_utils: audio_extn_utils_update_streams_cfg_lists: failed to open io config file(/vendor/etc/audio_io_policy.conf), trying older config file
09-19 00:10:55.294 772-847/? I/audio_hw_utils: load_cfg_list: could not load input, node is NULL
09-19 00:10:55.295 772-847/? I/qc_adm: ADM buffering size (6) ms requested, defaulting to 3 ms
09-19 00:10:55.296 774-774/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:10:55.296 774-774/? I/chatty: uid=1047(cameraserver) android.hardwar identical 3 lines
09-19 00:10:55.296 774-774/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:10:55.297 772-847/? E/audio_hw_extn: audio_extn_perf_lock_init: Perf lock handles Success 
09-19 00:10:55.297 772-847/? I/soundtrigger: audio_extn_sound_trigger_init: Enter
    audio_extn_sound_trigger_init: DLOPEN successful for /vendor/lib/hw/sound_trigger.primary.msm8998.so
09-19 00:10:55.297 772-847/? D/soundtrigger: audio_extn_sound_trigger_init: sthal is using proprietary API version 0x0100
09-19 00:10:55.298 772-844/? W/DeviceHAL: Error from HAL Device in function get_master_volume: Function not implemented
    Error from HAL Device in function get_master_mute: Function not implemented
09-19 00:10:55.299 772-844/? W/DeviceHAL: Error from HAL Device in function set_master_volume: Function not implemented
09-19 00:10:55.299 774-1342/? E/mm-camera: <SENSOR><ERROR> chiron_imx386_semco_autofocus_calibration: 571: adjusted code_per_step: 165, qvalue: 128
09-19 00:10:55.299 772-844/? W/DeviceHAL: Error from HAL Device in function set_master_mute: Function not implemented
09-19 00:10:55.299 823-823/? I/AudioFlinger: loadHwModule() Loaded primary audio interface, handle 10
    openOutput() this 0x77c2829600, module 10 Device 0x2, SamplingRate 48000, Format 0x000001, Channels 0x3, flags 0x6
09-19 00:10:55.299 772-844/? D/audio_hw_primary: adev_open_output_stream: enter: format(0x1) sample_rate(48000) channel_mask(0x3) devices(0x2) flags(0x6)        stream_handle(0xe8853000) address()
09-19 00:10:55.299 772-844/? I/audio_hw_primary: adev_open_output_stream: dynamic qos voting not enabled for platform
09-19 00:10:55.299 772-844/? I/audio_hw_utils: audio_extn_utils_update_stream_output_app_type_cfg Allowing 24 and above bits playback on speaker ONLY at default sampling rate
09-19 00:10:55.299 772-844/? D/audio_hw_primary: adev_open_output_stream: Stream (0xe8853000) picks up usecase (low-latency-playback)
09-19 00:10:55.300 823-823/? I/AudioFlinger: HAL output buffer size 192 frames, normal sink buffer size 960 frames
09-19 00:10:55.306 765-765/? W/zygote64: Core platform API violation: Ljava/lang/ClassLoader;->parent:Ljava/lang/ClassLoader; from Lde/robv/android/xposed/XposedHelpers; using reflection
09-19 00:10:55.307 820-852/? D/PerMgrSrv: modem new state: is on-line
09-19 00:10:55.307 820-850/? D/PerMgrSrv: modem state: is on-line, add client cnss-daemon
    cnss-daemon registered
09-19 00:10:55.307 820-1141/? D/PerMgrSrv: modem state: is on-line, add client QCRIL
    QCRIL registered
09-19 00:10:55.307 820-1145/? D/PerMgrSrv: modem state: is on-line, add client QCRIL
    QCRIL registered
09-19 00:10:55.307 1091-1091/? D/PerMgrLib: cnss-daemon successfully registered for modem
    cnss-daemon voting for modem
09-19 00:10:55.307 820-852/? D/PerMgrSrv: cnss-daemon voting for modem
09-19 00:10:55.307 923-923/? D/PerMgrLib: QCRIL successfully registered for modem
09-19 00:10:55.307 1001-1001/? D/PerMgrLib: QCRIL successfully registered for modem
09-19 00:10:55.307 820-852/? D/PerMgrSrv: modem num voters is 2
09-19 00:10:55.309 1091-1371/? E/cnss-daemon: ro.baseband : [msm]
09-19 00:10:55.307 765-765/? W/main: type=1400 audit(0.0:34): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
    type=1400 audit(0.0:35): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.320 772-1366/? D/volume_listener: init_once Called 
09-19 00:10:55.321 772-1366/? D/volume_listener: init_once: using custome volume table
09-19 00:10:55.321 772-1366/? I/EffectDiracSound: DiracSoundLib_GetDescriptor() start
09-19 00:10:55.321 823-823/? I/BufferProvider: found effect "Multichannel Downmix To Stereo" from The Android Open Source Project
09-19 00:10:55.323 823-823/? I/AudioFlinger: Using module 10 as the primary audio interface
09-19 00:10:55.323 823-1385/? I/AudioFlinger: AudioFlinger's thread 0x77c28ecb80 tid=1385 ready to run
09-19 00:10:55.323 823-1385/? W/AudioFlinger: no wake lock to update, system not ready yet
09-19 00:10:55.323 772-1366/? D/audio_hw_primary: out_standby: enter: stream (0xe8853000) usecase(1: low-latency-playback)
    out_standby: exit
09-19 00:10:55.320 765-765/? W/main: type=1400 audit(0.0:36): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
    type=1400 audit(0.0:37): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.325 823-823/? V/APM_AudioPolicyManager: checkAndSetVolume cannot set volume group 3 volume with force use = 0 for comm
09-19 00:10:55.325 823-1385/? W/AudioFlinger: no wake lock to update, system not ready yet
09-19 00:10:55.328 823-823/? W/AudioFlinger: moveEffects() bad srcOutput 0
09-19 00:10:55.328 823-823/? V/APM_AudioPolicyManager: selectOutputForMusicEffects selected output 13
    setOutputDevices device {type:0x2,@:} delayMs 0
    setOutputDevices() prevDevice {type:0x2,@:}
    setOutputDevices changing device to {type:0x2,@:}
09-19 00:10:55.330 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:55.343 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.344 765-765/? W/zygote64: Core platform API violation: Ljava/lang/reflect/Executable;->accessFlags:I from Lcom/swift/sandhook/SandHook; using reflection
    Core platform API violation: Ljava/lang/Thread;->nativePeer:J from Lcom/swift/sandhook/SandHook; using reflection
    Core platform API violation: Ljava/lang/reflect/Executable;->artMethod:J from Lcom/swift/sandhook/SandHook; using reflection
    Core platform API violation: Ljava/lang/reflect/Executable;->dexMethodIndex:I from Lcom/swift/sandhook/SandHook; using reflection
    Core platform API violation: Ljava/lang/Class;->dexCache:Ljava/lang/Object; from Lcom/swift/sandhook/SandHook; using reflection
09-19 00:10:55.345 765-765/? W/zygote64: Core platform API violation: Ljava/lang/DexCache;->resolvedMethods:J from Lcom/swift/sandhook/SandHook; using reflection
09-19 00:10:55.346 765-765/? D/dlopen: 750ad4f000-750ae7c000 r--p 00000000 103:1d 309                           /apex/com.android.runtime/lib64/libart.so
09-19 00:10:55.346 765-765/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart.so loaded in Android at 0x750ad4f000
09-19 00:10:55.347 765-765/? I/nougat_dlfcn: _ZN3art3jit3Jit20jit_compiler_handle_E found at 0x750b312960
09-19 00:10:55.348 765-765/? D/dlopen: 7500e06000-7500ec8000 r--p 00000000 103:1d 306                           /apex/com.android.runtime/lib64/libart-compiler.so
09-19 00:10:55.348 765-765/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart-compiler.so loaded in Android at 0x7500e06000
    jit_compile_method found at 0x75010403dc
09-19 00:10:55.349 765-765/? D/dlopen: 7500e06000-7500ec8000 r--p 00000000 103:1d 306                           /apex/com.android.runtime/lib64/libart-compiler.so
09-19 00:10:55.349 765-765/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart-compiler.so loaded in Android at 0x7500e06000
09-19 00:10:55.350 765-765/? I/nougat_dlfcn: jit_load found at 0x7501040298
09-19 00:10:55.352 765-765/? D/dlopen: 750ad4f000-750ae7c000 r--p 00000000 103:1d 309                           /apex/com.android.runtime/lib64/libart.so
09-19 00:10:55.352 765-765/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart.so loaded in Android at 0x750ad4f000
09-19 00:10:55.353 765-765/? I/nougat_dlfcn: _ZN3art3Dbg9SuspendVMEv found at 0x750af0a3f4
09-19 00:10:55.353 772-1366/? D/audio_hw_primary: out_set_parameters: enter: usecase(1: low-latency-playback) kvpairs: routing=2
09-19 00:10:55.353 772-1366/? D/audio_hw_extn: audio_extn_fm_set_parameters: Enter
09-19 00:10:55.353 772-1366/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:10:55.353 823-823/? V/APM_AudioPolicyManager: setOutputDevices() AF::createAudioPatch returned 0 patchHandle 12 num_sources 1 num_sinks 1
09-19 00:10:55.354 823-823/? V/APM_AudioPolicyManager: checkAndSetVolume cannot set volume group 3 volume with force use = 0 for comm
09-19 00:10:55.354 765-765/? D/dlopen: 750ad4f000-750ae7c000 r--p 00000000 103:1d 309                           /apex/com.android.runtime/lib64/libart.so
09-19 00:10:55.354 765-765/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart.so loaded in Android at 0x750ad4f000
09-19 00:10:55.355 765-765/? I/nougat_dlfcn: _ZN3art3Dbg8ResumeVMEv found at 0x750af0a478
09-19 00:10:55.356 823-823/? I/AudioFlinger: openOutput() this 0x77c2829600, module 10 Device 0x2, SamplingRate 48000, Format 0x000001, Channels 0x3, flags 0x4
    res_idx = 0 chromatix_lib_name[1] = chiron_imx386_semco_snapshot
09-19 00:10:55.356 772-1366/? D/audio_hw_primary: adev_open_output_stream: enter: format(0x1) sample_rate(48000) channel_mask(0x3) devices(0x2) flags(0x4)        stream_handle(0xe88c6000) address()
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
09-19 00:10:55.356 772-1366/? I/audio_hw_primary: adev_open_output_stream: dynamic qos voting not enabled for platform
    res_idx = 0 chromatix_lib_name[5] = chiron_imx386_semco_cpp_snapshot
09-19 00:10:55.356 772-1366/? I/audio_hw_utils: audio_extn_utils_update_stream_output_app_type_cfg Allowing 24 and above bits playback on speaker ONLY at default sampling rate
09-19 00:10:55.356 772-1366/? E/audio_hw_primary: adev_open_output_stream: Primary output is already opened
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
09-19 00:10:55.356 772-1366/? D/audio_hw_primary: adev_open_output_stream: exit: ret -17
09-19 00:10:55.356 772-1366/? W/DeviceHAL: Error from HAL Device in function open_output_stream: File exists
    res_idx = 0 chromatix_lib_name[11] = chiron_imx386_semco_cpp_video
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
09-19 00:10:55.356 765-765/? D/dlopen: 750ad4f000-750ae7c000 r--p 00000000 103:1d 309                           /apex/com.android.runtime/lib64/libart.so
09-19 00:10:55.356 765-765/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart.so loaded in Android at 0x750ad4f000
09-19 00:10:55.356 823-823/? I/AudioHwDevice: openOutputStream(), HAL returned sampleRate 48000, Format 0x1, channelMask 0x3, status -61
09-19 00:10:55.357 823-823/? W/APM_AudioPolicyManager: Cannot open output stream for devices type:0x2,@: on hw module primary
09-19 00:10:55.357 823-823/? I/AudioFlinger: openOutput() this 0x77c2829600, module 10 Device 0x2, SamplingRate 48000, Format 0x000001, Channels 0x3, flags 0x8
09-19 00:10:55.357 772-1366/? D/audio_hw_primary: adev_open_output_stream: enter: format(0x1) sample_rate(48000) channel_mask(0x3) devices(0x2) flags(0x8)        stream_handle(0xe88c6000) address()
09-19 00:10:55.357 772-1366/? I/audio_hw_utils: audio_extn_utils_update_stream_output_app_type_cfg Allowing 24 and above bits playback on speaker ONLY at default sampling rate
09-19 00:10:55.357 772-1366/? D/audio_hw_primary: adev_open_output_stream: Stream (0xe88c6000) picks up usecase (deep-buffer-playback)
09-19 00:10:55.357 765-765/? I/nougat_dlfcn: _ZN3art9JavaVMExt16AddWeakGlobalRefEPNS_6ThreadENS_6ObjPtrINS_6mirror6ObjectEEE found at 0x750b0c3380
09-19 00:10:55.358 823-823/? I/AudioFlinger: HAL output buffer size 1920 frames, normal sink buffer size 1920 frames
09-19 00:10:55.358 823-1392/? I/AudioFlinger: AudioFlinger's thread 0x7735495380 tid=1392 ready to run
09-19 00:10:55.359 823-1392/? W/AudioFlinger: no wake lock to update, system not ready yet
09-19 00:10:55.359 765-765/? D/dlopen: 750ad4f000-750ae7c000 r--p 00000000 103:1d 309                           /apex/com.android.runtime/lib64/libart.so
09-19 00:10:55.359 765-765/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart.so loaded in Android at 0x750ad4f000
09-19 00:10:55.359 772-1366/? D/audio_hw_primary: out_standby: enter: stream (0xe88c6000) usecase(0: deep-buffer-playback)
    out_standby: exit
09-19 00:10:55.359 823-823/? V/APM_AudioPolicyManager: checkAndSetVolume cannot set volume group 3 volume with force use = 0 for comm
09-19 00:10:55.360 823-1392/? W/AudioFlinger: no wake lock to update, system not ready yet
09-19 00:10:55.361 765-765/? D/dlopen: 750ad4f000-750ae7c000 r--p 00000000 103:1d 309                           /apex/com.android.runtime/lib64/libart.so
09-19 00:10:55.361 765-765/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart.so loaded in Android at 0x750ad4f000
    _ZN3art12ProfileSaver20ForceProcessProfilesEv found at 0x750b097084
09-19 00:10:55.364 823-823/? V/APM_AudioPolicyManager: selectOutputForMusicEffects selected output 13
    setOutputDevices device {type:0x2,@:} delayMs 0
    setOutputDevices() prevDevice {type:0x2,@:}
09-19 00:10:55.365 823-823/? V/APM_AudioPolicyManager: setOutputDevices changing device to {type:0x2,@:}
09-19 00:10:55.366 765-765/? E/nougat_dlfcn: /system/lib64/libsandhook-native.so not found in my userspace
09-19 00:10:55.371 765-765/? E/nougat_dlfcn: /odm/lib64/libsandhook-native.so not found in my userspace
09-19 00:10:55.372 774-1399/? E/mm-camera: <IMGLIB><ERROR> 328: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Nothing allocated or already freed!
09-19 00:10:55.375 765-765/? E/nougat_dlfcn: /vendor/lib64/libsandhook-native.so not found in my userspace
09-19 00:10:55.379 765-765/? E/nougat_dlfcn: libsandhook-native.so not found in my userspace
09-19 00:10:55.379 765-765/? D/SandHook: method <public static android.app.ActivityThread android.app.ActivityThread.systemMain()> hook <replacement> success!
09-19 00:10:55.380 765-765/? W/main: type=1400 audit(0.0:38): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
    type=1400 audit(0.0:39): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.387 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.388 765-765/? D/SandHook: method <private void android.app.ActivityThread.handleBindApplication(android.app.ActivityThread$AppBindData)> hook <replacement> success!
09-19 00:10:55.387 765-765/? W/main: type=1400 audit(0.0:40): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
    type=1400 audit(0.0:41): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.397 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.398 765-765/? D/SandHook: method <public android.app.LoadedApk(android.app.ActivityThread,android.content.pm.ApplicationInfo,android.content.res.CompatibilityInfo,java.lang.ClassLoader,boolean,boolean,boolean)> hook <replacement> success!
09-19 00:10:55.400 765-765/? W/main: type=1400 audit(0.0:42): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
    type=1400 audit(0.0:43): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.405 1001-1001/? I/ServiceManagement: Registered vendor.qti.hardware.radio.am@1.0::IQcRilAudio/slot1 (start delay of 1553ms)
09-19 00:10:55.405 772-1366/? D/audio_hw_primary: out_set_parameters: enter: usecase(0: deep-buffer-playback) kvpairs: routing=2
09-19 00:10:55.406 823-823/? V/APM_AudioPolicyManager: setOutputDevices() AF::createAudioPatch returned 0 patchHandle 20 num_sources 1 num_sinks 1
09-19 00:10:55.408 823-823/? V/APM_AudioPolicyManager: checkAndSetVolume cannot set volume group 3 volume with force use = 0 for comm
09-19 00:10:55.409 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.410 765-765/? D/SandHook: method <public android.content.res.Resources android.app.ApplicationPackageManager.getResourcesForApplication(android.content.pm.ApplicationInfo) throws android.content.pm.PackageManager$NameNotFoundException> hook <replacement> success!
09-19 00:10:55.410 765-765/? W/main: type=1400 audit(0.0:44): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
    type=1400 audit(0.0:45): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.412 1001-1001/? I/ServiceManagement: Registered android.hardware.radio@1.1::IRadio/slot1 (start delay of 1561ms)
09-19 00:10:55.413 1001-1001/? I/ServiceManagement: Registered android.hardware.radio.deprecated@1.0::IOemHook/slot1 (start delay of 1561ms)
09-19 00:10:55.414 810-810/? I/vendor.rmt_storage: rmt_storage_connect_cb: clnt_h=0x1 conn_h=0x7aae805010
    rmt_storage_open_cb: /boot/modem_fs1: req_h=0x1 msg_id=1: Client found
    rmt_storage_open_cb: /boot/modem_fs1: req_h=0x1 msg_id=1: Send response: res=0 err=0
09-19 00:10:55.414 810-1408/? I/vendor.rmt_storage: rmt_storage_client_thread: /boot/modem_fs1: Worker thread started
    wake lock name: rmt_storage_526907297104, name creation success: 24
09-19 00:10:55.415 823-823/? W/APM_AudioPolicyManager: Output profile contains no device on module primary
09-19 00:10:55.415 810-810/? I/vendor.rmt_storage: rmt_storage_disconnect_cb: clnt_h=0x1 conn_h=0x7aae805010
    rmt_storage_connect_cb: clnt_h=0x2 conn_h=0x7aae805010
09-19 00:10:55.415 823-823/? I/AudioFlinger: openOutput() this 0x77c2829600, module 10 Device 0x10000, SamplingRate 48000, Format 0x000001, Channels 0x3, flags 0
09-19 00:10:55.415 810-810/? I/vendor.rmt_storage: rmt_storage_open_cb: /boot/modem_fs2: req_h=0x2 msg_id=1: Client found
    rmt_storage_open_cb: /boot/modem_fs2: req_h=0x2 msg_id=1: Send response: res=0 err=0
09-19 00:10:55.415 772-844/? D/audio_hw_primary: adev_open_output_stream: enter: format(0x1) sample_rate(48000) channel_mask(0x3) devices(0x10000) flags(0)        stream_handle(0xe8855800) address()
    adev_open_output_stream: Stream (0xe8855800) picks up usecase (afe-proxy-playback)
09-19 00:10:55.416 810-810/? I/vendor.rmt_storage: rmt_storage_connect_cb: clnt_h=0x3 conn_h=0x7aae805020
    rmt_storage_open_cb: /boot/modem_fsg: req_h=0x3 msg_id=1: Client found
    rmt_storage_open_cb: /boot/modem_fsg: req_h=0x3 msg_id=1: Send response: res=0 err=0
    rmt_storage_disconnect_cb: clnt_h=0x2 conn_h=0x7aae805010
09-19 00:10:55.416 1001-1121/? D/PerMgrLib: QCRIL voting for modem
09-19 00:10:55.420 765-765/? W/main: type=1400 audit(0.0:46): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
    type=1400 audit(0.0:47): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.416 810-810/? I/vendor.rmt_storage: rmt_storage_disconnect_cb: clnt_h=0x3 conn_h=0x7aae805020
09-19 00:10:55.416 820-852/? D/PerMgrSrv: QCRIL voting for modem
    modem num voters is 3
09-19 00:10:55.417 810-1409/? I/vendor.rmt_storage: rmt_storage_client_thread: /boot/modem_fs2: Worker thread started
09-19 00:10:55.417 810-810/? I/vendor.rmt_storage: rmt_storage_connect_cb: clnt_h=0x4 conn_h=0x7aae805020
    rmt_storage_open_cb: /boot/modem_fsc: req_h=0x4 msg_id=1: Client found
    rmt_storage_open_cb: /boot/modem_fsc: req_h=0x4 msg_id=1: Send response: res=0 err=0
09-19 00:10:55.417 810-1409/? I/vendor.rmt_storage: wake lock name: rmt_storage_526889483600, name creation success: 24
09-19 00:10:55.418 1001-1121/? E/QMI_FW: QMUXD: WARNING qmi_qmux_if_pwr_up_init failed! rc=-6
09-19 00:10:55.418 810-1411/? I/vendor.rmt_storage: rmt_storage_client_thread: /boot/modem_fsc: Worker thread started
    wake lock name: rmt_storage_526870633808, name creation success: 24
09-19 00:10:55.418 810-810/? I/vendor.rmt_storage: rmt_storage_disconnect_cb: clnt_h=0x4 conn_h=0x7aae805020
09-19 00:10:55.419 810-810/? I/vendor.rmt_storage: rmt_storage_connect_cb: clnt_h=0x5 conn_h=0x7aae805020
09-19 00:10:55.427 765-765/? W/main: type=1400 audit(0.0:48): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.419 810-810/? I/vendor.rmt_storage: rmt_storage_open_cb: Unable to open /boot/modem_fsg_oem_1
    rmt_storage_open_cb: : req_h=0x5 msg_id=1: Send response: res=1 err=3
09-19 00:10:55.419 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.419 810-810/? I/vendor.rmt_storage: rmt_storage_disconnect_cb: clnt_h=0x5 conn_h=0x7aae805020
09-19 00:10:55.427 765-765/? W/main: type=1400 audit(0.0:49): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.419 810-1410/? I/vendor.rmt_storage: rmt_storage_client_thread: /boot/modem_fsg: Worker thread started
    wake lock name: rmt_storage_526888447312, name creation success: 24
09-19 00:10:55.419 823-823/? I/AudioFlinger: HAL output buffer size 768 frames, normal sink buffer size 1152 frames
09-19 00:10:55.420 765-765/? D/SandHook: method <private android.content.res.Resources android.app.ResourcesManager.getOrCreateResources(android.os.IBinder,android.content.res.ResourcesKey,java.lang.ClassLoader)> hook <replacement> success!
09-19 00:10:55.420 810-810/? I/vendor.rmt_storage: rmt_storage_connect_cb: clnt_h=0x6 conn_h=0x7aae805020
    rmt_storage_open_cb: Unable to open /boot/modem_fsg_oem_2
    rmt_storage_open_cb: : req_h=0x6 msg_id=1: Send response: res=1 err=3
    rmt_storage_disconnect_cb: clnt_h=0x6 conn_h=0x7aae805020
09-19 00:10:55.421 810-810/? I/vendor.rmt_storage: rmt_storage_connect_cb: clnt_h=0x7 conn_h=0x7aae805020
    rmt_storage_alloc_buff_cb: /boot/modem_fs1: req_h=0x7 msg_id=4: Alloc request received: Size: 0
    rmt_storage_alloc_buff_cb: /boot/modem_fs1: req_h=0x7 msg_id=4: New client making a dummy request with buffer req size 0
    rmt_storage_alloc_buff_cb: /boot/modem_fs1: req_h=0x7 msg_id=4: Send response: res=0 err=0
    rmt_storage_disconnect_cb: clnt_h=0x7 conn_h=0x7aae805020
    rmt_storage_connect_cb: clnt_h=0x8 conn_h=0x7aae805020
    rmt_storage_rw_iovec_cb: /boot/modem_fs1: req_h=0x8 msg_id=3: R/W request received
    wakelock acquired: 1, error no: 42
09-19 00:10:55.421 810-1408/? I/vendor.rmt_storage: rmt_storage_client_thread: /boot/modem_fs1: Unblock worker thread (th_id: 526907297104)
09-19 00:10:55.422 823-823/? V/APM_AudioPolicyManager: checkAndSetVolume cannot set volume group 3 volume with force use = 0 for comm
09-19 00:10:55.422 810-1408/? I/vendor.rmt_storage: rmt_storage_client_thread: /boot/modem_fs1: req_h=0x8 msg_id=3: Bytes read = 512
    rmt_storage_client_thread: /boot/modem_fs1: req_h=0x8 msg_id=3: Send response: res=0 err=0
    rmt_storage_client_thread: /boot/modem_fs1: About to block rmt_storage client thread (th_id: 526907297104) wakelock released: 1, error no: 0
09-19 00:10:55.422 823-1414/? I/AudioFlinger: AudioFlinger's thread 0x77354e6100 tid=1414 ready to run
09-19 00:10:55.423 810-810/? I/vendor.rmt_storage: rmt_storage_connect_cb: clnt_h=0x9 conn_h=0x7aae805010
    rmt_storage_rw_iovec_cb: /boot/modem_fs2: req_h=0x9 msg_id=3: R/W request received
    wakelock acquired: 1, error no: 42
    rmt_storage_disconnect_cb: clnt_h=0x8 conn_h=0x7aae805020
09-19 00:10:55.423 810-1409/? I/vendor.rmt_storage: rmt_storage_client_thread: /boot/modem_fs2: Unblock worker thread (th_id: 526889483600)
    rmt_storage_client_thread: /boot/modem_fs2: req_h=0x9 msg_id=3: Bytes read = 512
    rmt_storage_client_thread: /boot/modem_fs2: req_h=0x9 msg_id=3: Send response: res=0 err=0
    rmt_storage_client_thread: /boot/modem_fs2: About to block rmt_storage client thread (th_id: 526889483600) wakelock released: 1, error no: 0
09-19 00:10:55.424 810-810/? I/vendor.rmt_storage: rmt_storage_disconnect_cb: clnt_h=0x9 conn_h=0x7aae805010
09-19 00:10:55.424 823-1414/? W/AudioFlinger: no wake lock to update, system not ready yet
09-19 00:10:55.424 772-844/? D/audio_hw_primary: out_standby: enter: stream (0xe8855800) usecase(51: afe-proxy-playback)
    out_standby: exit
09-19 00:10:55.424 823-1414/? W/AudioFlinger: no wake lock to update, system not ready yet
09-19 00:10:55.425 810-810/? I/vendor.rmt_storage: rmt_storage_connect_cb: clnt_h=0xa conn_h=0x7aae805010
    rmt_storage_rw_iovec_cb: /boot/modem_fs2: req_h=0xa msg_id=3: R/W request received
    wakelock acquired: 1, error no: 42
09-19 00:10:55.425 810-1409/? I/vendor.rmt_storage: rmt_storage_client_thread: /boot/modem_fs2: Unblock worker thread (th_id: 526889483600)
09-19 00:10:55.426 823-823/? V/APM_AudioPolicyManager: selectOutputForMusicEffects selected output 13
09-19 00:10:55.427 823-823/? V/APM_AudioPolicyManager: setOutputDevices device {type:0x10000,@:} delayMs 0
    setOutputDevices() prevDevice {type:0x10000,@:}
09-19 00:10:55.437 765-765/? W/main: type=1400 audit(0.0:50): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.427 823-823/? V/APM_AudioPolicyManager: setOutputDevices changing device to {type:0x10000,@:}
09-19 00:10:55.428 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.437 765-765/? W/main: type=1400 audit(0.0:51): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.429 765-765/? D/SandHook: method <static android.content.res.TypedArray android.content.res.TypedArray.obtain(android.content.res.Resources,int)> hook <replacement> success!
09-19 00:10:55.430 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:55.430 810-1409/? I/vendor.rmt_storage: rmt_storage_client_thread: /boot/modem_fs2: req_h=0xa msg_id=3: Bytes read = 2096128
    rmt_storage_client_thread: /boot/modem_fs2: req_h=0xa msg_id=3: Send response: res=0 err=0
09-19 00:10:55.431 810-1409/? I/vendor.rmt_storage: rmt_storage_client_thread: /boot/modem_fs2: About to block rmt_storage client thread (th_id: 526889483600) wakelock released: 1, error no: 0
09-19 00:10:55.431 810-810/? I/vendor.rmt_storage: rmt_storage_disconnect_cb: clnt_h=0xa conn_h=0x7aae805010
09-19 00:10:55.438 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.438 765-765/? D/SandHook: method <public android.view.View android.view.LayoutInflater.inflate(org.xmlpull.v1.XmlPullParser,android.view.ViewGroup,boolean)> hook <replacement> success!
09-19 00:10:55.446 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.447 765-765/? D/SandHook: method <private void android.view.LayoutInflater.parseInclude(org.xmlpull.v1.XmlPullParser,android.content.Context,android.view.View,android.util.AttributeSet) throws org.xmlpull.v1.XmlPullParserException,java.io.IOException> hook <replacement> success!
09-19 00:10:55.449 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/com.bigsing.fakemap-N6PbN7a22Ns4jlp2fADtxg==/base.apk
09-19 00:10:55.451 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:55.463 772-772/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: retry, retry_num 2
09-19 00:10:55.465 772-772/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: snd_card_name: msm8998-tasha-snd-card
09-19 00:10:55.465 772-772/? W/hardware_info: update_hardware_info_msm8998: Not a msm8998 device
09-19 00:10:55.465 772-772/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: Opened sound card:0
09-19 00:10:55.483 772-844/? D/audio_hw_primary: out_set_parameters: enter: usecase(51: afe-proxy-playback) kvpairs: routing=65536
09-19 00:10:55.484 823-823/? V/APM_AudioPolicyManager: setOutputDevices() AF::createAudioPatch returned 0 patchHandle 28 num_sources 1 num_sinks 1
    checkAndSetVolume cannot set volume group 3 volume with force use = 0 for comm
09-19 00:10:55.485 772-844/? D/audio_hw_primary: adev_open_input_stream: enter: sample_rate(48000) channel_mask(0xc) devices(0x80000004)        stream_handle(0xe88a3a00) io_handle(14) source(1) format 1
09-19 00:10:55.485 772-844/? W/audio_hw_utils: audio_extn_utils_update_stream_input_app_type_cfg: App type could not be selected. Falling back to default
09-19 00:10:55.492 823-1416/? I/AudioFlinger: AudioFlinger's thread 0x77355cfa80 tid=1416 ready to run
09-19 00:10:55.492 772-844/? D/audio_hw_primary: adev_open_input_stream: enter: sample_rate(192000) channel_mask(0x8000000f) devices(0x80000004)        stream_handle(0xe88a3c80) io_handle(22) source(1) format 5
    adev_open_input_stream: enter: sample_rate(48000) channel_mask(0x8000000f) devices(0x80000004)        stream_handle(0xe88a3c80) io_handle(22) source(1) format 1
09-19 00:10:55.492 772-844/? W/audio_hw_utils: audio_extn_utils_update_stream_input_app_type_cfg: App type could not be selected. Falling back to default
09-19 00:10:55.493 772-844/? D/audio_hw_primary: adev_close_input_stream: enter:stream_handle(0xe88a3a00)
09-19 00:10:55.493 772-844/? D/soundtrigger: audio_extn_sound_trigger_check_ec_ref_enable: EC Reference is disabled
09-19 00:10:55.493 772-844/? W/sound_trigger_hw: sound_trigger_hw_call_back: Unknown event 16
09-19 00:10:55.493 772-844/? D/soundtrigger: audio_extn_sound_trigger_update_ec_ref_status: update audio echo ref status false
09-19 00:10:55.493 772-844/? D/audio_hw_primary: in_standby: enter: stream (0xe88a3a00) usecase(20: audio-record)
09-19 00:10:55.496 823-1418/? I/AudioFlinger: AudioFlinger's thread 0x7735642b00 tid=1418 ready to run
09-19 00:10:55.496 772-844/? D/audio_hw_primary: adev_open_input_stream: enter: sample_rate(48000) channel_mask(0xc) devices(0x80000040)        stream_handle(0xe88a3a00) io_handle(30) source(1) format 1
09-19 00:10:55.496 772-844/? W/audio_hw_utils: audio_extn_utils_update_stream_input_app_type_cfg: App type could not be selected. Falling back to default
09-19 00:10:55.498 772-844/? D/audio_hw_primary: adev_close_input_stream: enter:stream_handle(0xe88a3c80)
09-19 00:10:55.498 772-844/? D/soundtrigger: audio_extn_sound_trigger_check_ec_ref_enable: EC Reference is disabled
09-19 00:10:55.498 772-844/? W/sound_trigger_hw: sound_trigger_hw_call_back: Unknown event 16
09-19 00:10:55.498 772-844/? D/soundtrigger: audio_extn_sound_trigger_update_ec_ref_status: update audio echo ref status false
09-19 00:10:55.498 772-844/? D/audio_hw_primary: in_standby: enter: stream (0xe88a3c80) usecase(20: audio-record)
09-19 00:10:55.499 823-1420/? I/AudioFlinger: AudioFlinger's thread 0x77355c9b40 tid=1420 ready to run
09-19 00:10:55.499 772-844/? D/audio_hw_primary: adev_open_input_stream: enter: sample_rate(48000) channel_mask(0x80000007) devices(0x80000004)        stream_handle(0xe88a3c80) io_handle(38) source(1) format 1
09-19 00:10:55.499 772-844/? W/audio_hw_utils: audio_extn_utils_update_stream_input_app_type_cfg: App type could not be selected. Falling back to default
09-19 00:10:55.501 772-844/? D/audio_hw_primary: adev_close_input_stream: enter:stream_handle(0xe88a3a00)
09-19 00:10:55.501 772-844/? D/soundtrigger: audio_extn_sound_trigger_check_ec_ref_enable: EC Reference is disabled
09-19 00:10:55.501 772-844/? W/sound_trigger_hw: sound_trigger_hw_call_back: Unknown event 16
09-19 00:10:55.502 772-844/? D/soundtrigger: audio_extn_sound_trigger_update_ec_ref_status: update audio echo ref status false
09-19 00:10:55.502 772-844/? D/audio_hw_primary: in_standby: enter: stream (0xe88a3a00) usecase(52: afe-proxy-record)
09-19 00:10:55.502 823-1422/? I/AudioFlinger: AudioFlinger's thread 0x773563ca00 tid=1422 ready to run
09-19 00:10:55.502 772-844/? D/audio_hw_primary: adev_close_input_stream: enter:stream_handle(0xe88a3c80)
09-19 00:10:55.502 772-844/? D/soundtrigger: audio_extn_sound_trigger_check_ec_ref_enable: EC Reference is disabled
09-19 00:10:55.503 772-844/? W/sound_trigger_hw: sound_trigger_hw_call_back: Unknown event 16
09-19 00:10:55.503 823-823/? E/APM_AudioPolicyManager: initialize: Input device list is empty!
09-19 00:10:55.503 772-844/? D/soundtrigger: audio_extn_sound_trigger_update_ec_ref_status: update audio echo ref status false
09-19 00:10:55.503 772-844/? D/audio_hw_primary: in_standby: enter: stream (0xe88a3c80) usecase(20: audio-record)
09-19 00:10:55.515 823-823/? I/bt_a2dp_hw: adev_open:  adev_open in A2dp_hw module
09-19 00:10:55.515 823-823/? I/AudioFlinger: loadHwModule() Loaded a2dp audio interface, handle 18
09-19 00:10:55.515 823-823/? E/APM_AudioPolicyManager: initialize: Input device list is empty!
09-19 00:10:55.516 772-1366/? D/vndksupport: Loading /vendor/lib/hw/audio.usb.default.so from current namespace instead of sphal namespace.
09-19 00:10:55.519 772-1366/? W/DeviceHAL: Error from HAL Device in function set_master_volume: Function not implemented
09-19 00:10:55.519 823-823/? I/AudioFlinger: loadHwModule() Loaded usb audio interface, handle 26
09-19 00:10:55.519 772-1366/? D/vndksupport: Loading /vendor/lib/hw/audio.r_submix.default.so from current namespace instead of sphal namespace.
09-19 00:10:55.522 772-1366/? I/r_submix: adev_open(name=audio_hw_if)
09-19 00:10:55.523 772-1366/? I/r_submix: adev_init_check()
09-19 00:10:55.523 772-1366/? W/DeviceHAL: Error from HAL Device in function set_master_volume: Function not implemented
    Error from HAL Device in function set_master_mute: Function not implemented
09-19 00:10:55.523 823-823/? I/AudioFlinger: loadHwModule() Loaded r_submix audio interface, handle 34
09-19 00:10:55.523 772-1366/? D/r_submix: adev_open_input_stream(addr=0)
    submix_audio_device_create_pipe_l(addr=0, idx=9)
      now using address 0 for route 9
09-19 00:10:55.526 823-1424/? I/AudioFlinger: AudioFlinger's thread 0x77355ca780 tid=1424 ready to run
09-19 00:10:55.527 823-823/? D/AudioPolicyManagerCustom: USE_XML_AUDIO_POLICY_CONF is TRUE
09-19 00:10:55.528 772-1366/? D/r_submix: adev_close_input_stream()
    submix_audio_device_release_pipe_l(idx=9) addr=0
    submix_audio_device_destroy_pipe_l(): pipe destroyed
09-19 00:10:55.531 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:55.547 924-983/? D/QC-time-services: Daemon:time_service_modem_serv_notify_cb: QMI service is up 
09-19 00:10:55.547 924-987/? D/QC-time-services: Daemon:genoff_modem_qmi_service_handle_cb: QMI service handle cb called 
09-19 00:10:55.548 925-1003/? I/ThermalEngine: MODEM thermal mitigation available.
    Mitigation:modem[MODEM]:0 pending QMI request succeded
    Mitigation:vdd_restriction[MODEM]:0 pending QMI request succeded
09-19 00:10:55.549 925-1003/? I/ThermalEngine: Mitigation:modem_proc[MODEM]:0 pending QMI request succeded
    Mitigation:modem_proc_current[MODEM]:0 pending QMI request succeded
09-19 00:10:55.550 925-1003/? I/ThermalEngine: Mitigation:cpr_band[MODEM]:0 pending QMI request succeded
09-19 00:10:55.622 774-774/? E/mm-camera: <MCT   ><ERROR> 179: stop_sof_check_thread: Returning as SOF timer thread not yet initialized
09-19 00:10:55.623 774-774/? E/CamComm1.0-MD: Update metadata entry: Unknown tag -2145976319
    Update metadata entry: Unknown tag -2145976317
09-19 00:10:55.623 774-774/? I/QCamera: <HAL><INFO> getCamInfo: 9565: camera 0 resource cost is 100
    <HAL><INFO> openLegacy: 503: openLegacy halVersion: 256 cameraId = 0
09-19 00:10:55.624 774-774/? D/vndksupport: Loading /vendor/lib/hw/power.default.so from current namespace instead of sphal namespace.
09-19 00:10:55.631 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:55.656 812-812/? I/tftp_server: pid=812 tid=812 tftp-server : INF :[tftp_server.c, 659] rcvd request [1] [72] [2] [0] [41]
09-19 00:10:55.658 812-1432/? I/tftp_server: pid=812 tid=1432 tftp-server : INF :[tftp_server_utils.c, 113] file [readwrite/server_check.txt] : [/vendor/rfs/msm/mpss/readwrite/server_check.txt]
    pid=812 tid=1432 tftp-server : INF :[tftp_server.c, 1202] OACK options : [7680, 200, 10, 0, 0, 0, 0, 0]
    pid=812 tid=1432 tftp-server : INF :[tftp_os_la.c, 63] open : [-1] [-1] [384] [577] [/vendor/rfs/msm/mpss/readwrite/server_check.txt]
09-19 00:10:55.661 812-1432/? I/tftp_server: pid=812 tid=1432 tftp-server : INF :[tftp_server.c, 1465] WRQ stats : total-blocks = 1 : total-bytes = 5 : 5 timedout-pkts = 0, wrong-pkts = 0
09-19 00:10:55.661 812-812/? I/tftp_server: pid=812 tid=812 tftp-server : INF :[tftp_server.c, 659] rcvd request [1] [84] [1] [0] [42]
09-19 00:10:55.662 812-1432/? I/tftp_server: pid=812 tid=1432 tftp-server : INF :[tftp_server.c, 1469] WRQ time stats : Total : [TX, RX] = [111, 708, 10]
    pid=812 tid=1432 tftp-server : INF :[tftp_server.c, 1473] WRQ time stats : Tx [Min, Max] = [55, 56]
    pid=812 tid=1432 tftp-server : INF :[tftp_server.c, 1477] WRQ time stats : Rx [Min, Max] = [241, 467]
09-19 00:10:55.670 812-1433/? I/tftp_server: pid=812 tid=1433 tftp-server : INF :[tftp_server_utils.c, 113] file [readwrite/ota_firewall/ruleset] : [/vendor/rfs/msm/mpss/readwrite/ota_firewall/ruleset]
    pid=812 tid=1433 tftp-server : INF :[tftp_server.c, 1202] OACK options : [7680, 200, 10, 4, 0, 0, 0, 0]
    pid=812 tid=1433 tftp-server : INF :[tftp_os_la.c, 63] open : [-1] [-1] [384] [0] [/vendor/rfs/msm/mpss/readwrite/ota_firewall/ruleset]
09-19 00:10:55.670 812-1433/? E/tftp_server: pid=812 tid=1433 tftp-server : ERR :[tftp_os_la.c, 70] open failed: [2] [No such file or directory]
    pid=812 tid=1433 tftp-server : ERR :[tftp_server.c, 1698] open failed : [-2] [Unknown error -2]
    pid=812 tid=1433 tftp-server : ERR :[tftp_protocol.c, 1229] sending error-pkt. Code = 1, Msg = Err=2 String=No such file or directory
09-19 00:10:55.671 812-812/? I/tftp_server: pid=812 tid=812 tftp-server : INF :[tftp_server.c, 659] rcvd request [1] [84] [1] [0] [44]
09-19 00:10:55.672 812-1434/? I/tftp_server: pid=812 tid=1434 tftp-server : INF :[tftp_server_utils.c, 113] file [readwrite/ota_firewall/ruleset] : [/vendor/rfs/msm/mpss/readwrite/ota_firewall/ruleset]
    pid=812 tid=1434 tftp-server : INF :[tftp_server.c, 1202] OACK options : [7680, 200, 0, 10, 0, 0, 0, 0]
    pid=812 tid=1434 tftp-server : INF :[tftp_os_la.c, 63] open : [-1] [-1] [384] [0] [/vendor/rfs/msm/mpss/readwrite/ota_firewall/ruleset]
09-19 00:10:55.672 812-1434/? E/tftp_server: pid=812 tid=1434 tftp-server : ERR :[tftp_os_la.c, 70] open failed: [2] [No such file or directory]
    pid=812 tid=1434 tftp-server : ERR :[tftp_server.c, 1698] open failed : [-2] [Unknown error -2]
    pid=812 tid=1434 tftp-server : ERR :[tftp_protocol.c, 1229] sending error-pkt. Code = 1, Msg = Err=2 String=No such file or directory
09-19 00:10:55.704 774-774/? E/Watermark: getFontData Font file does not exist!
    getFontData Get file status failed
    getFontData Font file does not exist!
    getFontData Get file status failed
09-19 00:10:55.704 774-774/? I/QCamera: <HAL><INFO> openCamera: 1923: [KPI Perf]: E PROFILE_OPEN_CAMERA camera id 0
09-19 00:10:55.706 774-774/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:10:55.706 774-774/? D/QCamera: Debug log file is not enabled
09-19 00:10:55.719 936-936/? W/ServiceManagement: Waited one second for android.hardware.camera.provider@2.4::ICameraProvider/legacy/0
09-19 00:10:55.720 936-936/? I/ServiceManagement: getService: Trying again for android.hardware.camera.provider@2.4::ICameraProvider/legacy/0...
09-19 00:10:55.731 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:55.737 774-774/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:10:55.737 774-774/? I/chatty: uid=1047(cameraserver) android.hardwar identical 3 lines
09-19 00:10:55.737 774-774/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:10:55.740 774-1430/? E/QCamera: <HAL><ERROR> calcThermalLevel: 10178: level: 0, preview minfps 7000.000000, preview maxfpS 30000.000000, video minfps 7000.000000, video maxfps 30000.000000
    <HAL><ERROR> calcThermalLevel: 10183: level change to -> 0
    <HAL><ERROR> calcThermalLevel: 10262: Adjusted preview minfps 7.000000, preview maxfpS 30.000000, video minfps 7.000000, video maxfps 30.000000
09-19 00:10:55.741 774-1430/? E/QCameraParameters: setOISValue9690 OISEnabled=1 
    res_idx = 0 chromatix_lib_name[1] = chiron_imx386_semco_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_imx386_semco_common
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[9] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[10] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[11] = chiron_imx386_semco_cpp_video
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_imx386_semco_zsl_preview
    res_idx = 0 chromatix_lib_name[1] = chiron_imx386_semco_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_imx386_semco_common
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[9] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[10] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[11] = chiron_imx386_semco_cpp_video
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_imx386_semco_zsl_preview
09-19 00:10:55.743 774-1441/? E/mm-camera: <SENSOR><ERROR> chiron_imx386_semco_autofocus_calibration: 571: adjusted code_per_step: 165, qvalue: 128
    res_idx = 0 chromatix_lib_name[1] = chiron_imx386_semco_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_imx386_semco_common
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[9] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[10] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[11] = chiron_imx386_semco_cpp_video
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_imx386_semco_zsl_preview
09-19 00:10:55.747 774-774/? I/Thermal-Lib: Thermal-Lib-Client: Registration successful for camera with handle:1
09-19 00:10:55.747 774-774/? I/QCamera: <HAL><INFO> openCamera: 1938: [KPI Perf]: X PROFILE_OPEN_CAMERA camera id 0, rc: 0
09-19 00:10:55.750 925-1078/? I/ThermalEngine: Thermal-Server: Adding thermal event listener on fd 78
09-19 00:10:55.750 774-1463/? I/Thermal-Lib: Thermal-Lib-Client: Client received msg camera 0
09-19 00:10:55.750 774-1429/? E/QCamera: <HAL><ERROR> calcThermalLevel: 10178: level: 0, preview minfps 7000.000000, preview maxfpS 30000.000000, video minfps 7000.000000, video maxfps 30000.000000
    <HAL><ERROR> calcThermalLevel: 10183: level change to -> 0
    <HAL><ERROR> calcThermalLevel: 10262: Adjusted preview minfps 7.000000, preview maxfpS 30.000000, video minfps 7.000000, video maxfps 30.000000
09-19 00:10:55.751 774-1463/? I/Thermal-Lib: Thermal-Lib-Client: Client received msg camcorder 0
09-19 00:10:55.751 774-1463/? E/Thermal-Lib: Thermal-Lib-Client: No Callback registered for camcorder
09-19 00:10:55.756 774-774/? I/QCamera: <HAL><INFO> close_camera_device: 1571: [KPI Perf]: E camera id 0
09-19 00:10:55.760 774-774/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:10:55.761 774-774/? I/QCamera: <HAL><INFO> closeCamera: 2351: E
    <HAL><INFO> closeCamera: 2356: [KPI Perf]: E PROFILE_CLOSE_CAMERA camera id 0
09-19 00:10:55.761 774-1436/? E/mm-camera: <SENSOR><ERROR> 711: sensor_pick_resolution: res_idx: 1
09-19 00:10:55.761 774-1310/? E/mm-camera: <IMGLIB><ERROR> 297: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Invalid dimensions 0x0
    <IMGLIB><ERROR> 197: int img_algo_preload(img_base_ops_t *, void *): Preload: Failed to allocate buffer, rc -4
    <IMGLIB><ERROR> 119: module_imgbase_client_preload_exec: IMG_CORE_PRELOAD failed -4
09-19 00:10:55.762 925-1078/? I/ThermalEngine: Thermal-Server: removing client on fd 78
09-19 00:10:55.762 774-774/? I/Thermal-Lib: Thermal-Lib-Client: Unregisteration is successfull for handle:1
09-19 00:10:55.777 765-765/? I/EdXposed-Bridge:   Loading class com.bigsing.fakemap.MainHook
09-19 00:10:55.778 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/com.lanyus.blocksecureflag-QkgSXuv3JtDkgn3BXLv7VA==/base.apk
09-19 00:10:55.780 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:55.781 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:739] qti_file_open():Could not open device file. Errno 2 error msg=No such file or directory
09-19 00:10:55.803 774-1468/? E/mm-camera: <IMGLIB><ERROR> 328: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Nothing allocated or already freed!
09-19 00:10:55.832 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:55.869 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:55.877 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:10:55.877 765-765/? I/EdXposed-Bridge:   Loading class com.lanyus.blocksecureflag.XposedMain
09-19 00:10:55.878 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/com.df.callblocker-LNcAKCNcPT-cSh6jxYZPSQ==/base.apk
09-19 00:10:55.879 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:55.887 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:55.889 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:10:55.889 765-765/? I/EdXposed-Bridge:   Loading class com.droidmate.xposed.PermissionMod
09-19 00:10:55.893 765-765/? E/EdXposed-Bridge: de.robv.android.xposed.XposedHelpers$ClassNotFoundError: java.lang.ClassNotFoundException: com.android.server.pm.PackageManagerService
        at de.robv.android.xposed.XposedHelpers.findClass(XposedHelpers.java:71)
        at com.droidmate.xposed.PermissionMod.alterPermissions(Unknown Source:8)
        at com.droidmate.xposed.PermissionMod.initZygote(Unknown Source:43)
        at de.robv.android.xposed.XposedInit.loadModule(XposedInit.java:479)
        at de.robv.android.xposed.XposedInit.loadModules(XposedInit.java:345)
        at com.elderdrivers.riru.edxp.proxy.BaseRouter.loadModulesSafely(BaseRouter.java:78)
        at com.elderdrivers.riru.edxp.proxy.NormalProxy.forkSystemServerPre(NormalProxy.java:50)
        at com.elderdrivers.riru.edxp.core.Main.forkSystemServerPre(Main.java:108)
        at com.android.internal.os.Zygote.nativeForkSystemServer(Native Method)
        at com.android.internal.os.Zygote.forkSystemServer(Zygote.java:355)
        at com.android.internal.os.ZygoteInit.forkSystemServer(ZygoteInit.java:780)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:913)
     Caused by: java.lang.ClassNotFoundException: com.android.server.pm.PackageManagerService
        at java.lang.Class.classForName(Native Method)
        at java.lang.Class.forName(Class.java:454)
        at external.org.apache.commons.lang3.ClassUtils.getClass(ClassUtils.java:823)
        at de.robv.android.xposed.XposedHelpers.findClass(XposedHelpers.java:69)
        at com.droidmate.xposed.PermissionMod.alterPermissions(Unknown Source:8) 
        at com.droidmate.xposed.PermissionMod.initZygote(Unknown Source:43) 
        at de.robv.android.xposed.XposedInit.loadModule(XposedInit.java:479) 
        at de.robv.android.xposed.XposedInit.loadModules(XposedInit.java:345) 
        at com.elderdrivers.riru.edxp.proxy.BaseRouter.loadModulesSafely(BaseRouter.java:78) 
        at com.elderdrivers.riru.edxp.proxy.NormalProxy.forkSystemServerPre(NormalProxy.java:50) 
        at com.elderdrivers.riru.edxp.core.Main.forkSystemServerPre(Main.java:108) 
        at com.android.internal.os.Zygote.nativeForkSystemServer(Native Method) 
        at com.android.internal.os.Zygote.forkSystemServer(Zygote.java:355) 
        at com.android.internal.os.ZygoteInit.forkSystemServer(ZygoteInit.java:780) 
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:913) 
     Caused by: java.lang.ClassNotFoundException: Didn't find class "com.android.server.pm.PackageManagerService" on path: DexPathList[[zip file "/data/app/com.df.callblocker-LNcAKCNcPT-cSh6jxYZPSQ==/base.apk"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at java.lang.Class.classForName(Native Method) 
        at java.lang.Class.forName(Class.java:454) 
        at external.org.apache.commons.lang3.ClassUtils.getClass(ClassUtils.java:823) 
        at de.robv.android.xposed.XposedHelpers.findClass(XposedHelpers.java:69) 
        at com.droidmate.xposed.PermissionMod.alterPermissions(Unknown Source:8) 
        at com.droidmate.xposed.PermissionMod.initZygote(Unknown Source:43) 
        at de.robv.android.xposed.XposedInit.loadModule(XposedInit.java:479) 
        at de.robv.android.xposed.XposedInit.loadModules(XposedInit.java:345) 
        at com.elderdrivers.riru.edxp.proxy.BaseRouter.loadModulesSafely(BaseRouter.java:78) 
        at com.elderdrivers.riru.edxp.proxy.NormalProxy.forkSystemServerPre(NormalProxy.java:50) 
        at com.elderdrivers.riru.edxp.core.Main.forkSystemServerPre(Main.java:108) 
        at com.android.internal.os.Zygote.nativeForkSystemServer(Native Method) 
        at com.android.internal.os.Zygote.forkSystemServer(Zygote.java:355) 
        at com.android.internal.os.ZygoteInit.forkSystemServer(ZygoteInit.java:780) 
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:913) 
09-19 00:10:55.893 765-765/? W/main: type=1400 audit(0.0:52): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.902 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.903 765-765/? D/SandHook: method <public int android.app.AppOpsManager.checkOp(int,int,java.lang.String)> hook <replacement> success!
09-19 00:10:55.903 765-765/? W/main: type=1400 audit(0.0:54): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.910 772-772/? W/sound_trigger_platform: load_acdb: acdb_loader_send_listen_device_cal_v1 not found. undefined symbol: acdb_loader_send_listen_device_cal_v1
    load_acdb: acdb_loader_send_listen_lsm_cal_v1 not found. undefined symbol: acdb_loader_send_listen_lsm_cal_v1
09-19 00:10:55.910 772-772/? I/audio_hw_extn: audio_extn_set_snd_card_split: snd_card_name(msm8998-tasha-snd-card) device(msm8998) snd_card(tasha) form_factor(snd)
09-19 00:10:55.911 772-772/? E/platform_info: param tag only supported with CONFIG_PARAMS section
09-19 00:10:55.911 772-772/? I/chatty: uid=1041(audioserver) audio@2.0-servi identical 7 lines
09-19 00:10:55.911 772-772/? E/platform_info: param tag only supported with CONFIG_PARAMS section
09-19 00:10:55.912 772-772/? E/audio_hw_acdb: acdb_init_v2: dlsym error undefined symbol: acdb_loader_init_v4 for acdb_loader_init_v4
09-19 00:10:55.912 772-772/? D/ACDB-LOADER: ACDB -> already initialized, exit
09-19 00:10:55.912 772-772/? D/audio_hw_acdb: acdb_init_v2: ACDB Instance ID support after ACDB init:0
09-19 00:10:55.913 772-772/? D/sound_trigger_platform: platform_stdev_init: Opening device /dev/snd/hwC0D1000
    get_codec_version: codec version WCD9335_2_0
09-19 00:10:55.913 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.913 772-772/? I/SoundTriggerHw: onFirstRef() mModuleName primary mHwDevice 0xea04b000
09-19 00:10:55.914 765-765/? D/SandHook: method <public int android.app.AppOpsManager.checkOpNoThrow(int,int,java.lang.String)> hook <replacement> success!
09-19 00:10:55.915 772-772/? I/ServiceManagement: Registered android.hardware.soundtrigger@2.2::ISoundTriggerHw/default (start delay of 2743ms)
09-19 00:10:55.915 772-772/? I/audiohalservice: Registration complete for android.hardware.soundtrigger@2.2::ISoundTriggerHw/default.
09-19 00:10:55.915 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.bluetooth.audio@2.0::IBluetoothAudioProvidersFactory/default in either framework or device manifest.
09-19 00:10:55.916 772-772/? E/audiohalservice: Could not get passthrough implementation for android.hardware.bluetooth.audio@2.0::IBluetoothAudioProvidersFactory/default.
09-19 00:10:55.916 772-772/? W/audiohalservice: Could not register Bluetooth Audio API 2.0
09-19 00:10:55.913 765-765/? W/main: type=1400 audit(0.0:56): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.916 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.bluetooth.a2dp@1.0::IBluetoothAudioOffload/default in either framework or device manifest.
09-19 00:10:55.916 772-772/? E/audiohalservice: Could not get passthrough implementation for android.hardware.bluetooth.a2dp@1.0::IBluetoothAudioOffload/default.
09-19 00:10:55.916 772-772/? W/audiohalservice: Could not register Bluetooth audio offload 1.0
09-19 00:10:55.924 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.925 765-765/? D/SandHook: method <public int android.app.AppOpsManager.noteOp(int,int,java.lang.String)> hook <replacement> success!
09-19 00:10:55.923 765-765/? W/main: type=1400 audit(0.0:58): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.932 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:55.933 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.934 765-765/? D/SandHook: method <public int android.app.AppOpsManager.noteOpNoThrow(int,int,java.lang.String)> hook <replacement> success!
09-19 00:10:55.933 765-765/? W/main: type=1400 audit(0.0:60): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.942 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.943 765-765/? D/SandHook: method <public int android.app.AppOpsManager.startOp(int,int,java.lang.String)> hook <replacement> success!
09-19 00:10:55.940 765-765/? W/main: type=1400 audit(0.0:62): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:55.951 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:55.951 925-1074/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 43000 mC, weight[0] 2
09-19 00:10:55.951 765-765/? D/SandHook: method <public int android.app.AppOpsManager.startOpNoThrow(int,int,java.lang.String)> hook <replacement> success!
09-19 00:10:55.952 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/com.devin.islowramdevice-ey8WMdZp-IUDY3h4qPbIYA==/base.apk
09-19 00:10:55.952 925-1074/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:10:55.952 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:55.978 925-1080/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 43000 mC, weight[0] 2
09-19 00:10:55.981 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:55.981 925-1080/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:10:55.982 765-765/? I/EdXposed-Bridge:   Loading class com.devin.islowramdevice.XIsLowRamDevice
    Loading modules from /data/app/ma.wanam.wanamkit-mDFL8N9RpaVfGiQy4SjMXA==/base.apk
09-19 00:10:55.983 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:56.000 812-812/? I/tftp_server: pid=812 tid=812 tftp-server : INF :[tftp_server.c, 659] rcvd request [1] [90] [1] [0] [77]
09-19 00:10:56.001 812-1476/? I/tftp_server: pid=812 tid=1476 tftp-server : INF :[tftp_server_utils.c, 113] file [readonly/firmware/image/wlanmdsp.mbn] : [/vendor/rfs/msm/mpss/readonly/firmware/image/wl
09-19 00:10:56.009 1132-1186/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:56.010 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:56.012 812-1476/? I/tftp_server: pid=812 tid=1476 tftp-server : INF :[tftp_server.c, 1202] OACK options : [7680, 200, 2744992, 10, 0, 0, 0, 0]
    pid=812 tid=1476 tftp-server : INF :[tftp_os_la.c, 63] open : [-1] [-1] [384] [0] [/vendor/rfs/msm/mpss/readonly/firmware/image/wlanmdsp.mbn]
09-19 00:10:56.013 812-1476/? I/tftp_server: pid=812 tid=1476 tftp-server : INF :[tftp_protocol.c, 742] Recd END OF TRANSFER pkt. Code = 9, Msg = End of Transfer
    pid=812 tid=1476 tftp-server : INF :[tftp_server.c, 1310] RRQ stats : sent_size = 0 total-blocks = 0 total-bytes = 0 timedout-pkts = 0, wrong-pkts = 0
    pid=812 tid=1476 tftp-server : INF :[tftp_server.c, 1314] RRQ time stats : Total : [TX, RX] = [40, 178]
    pid=812 tid=1476 tftp-server : INF :[tftp_server.c, 1320] RRQ time stats : Tx/Rx [Min, Max] = [40, 40, 178, 178]
    pid=812 tid=1476 tftp-server : INF :[tftp_server.c, 1336] RRQ was successfully processed.
09-19 00:10:56.014 812-812/? I/tftp_server: pid=812 tid=812 tftp-server : INF :[tftp_server.c, 659] rcvd request [1] [90] [1] [0] [80]
09-19 00:10:56.014 812-1482/? I/tftp_server: pid=812 tid=1482 tftp-server : INF :[tftp_server_utils.c, 113] file [readonly/firmware/image/wlanmdsp.mbn] : [/vendor/rfs/msm/mpss/readonly/firmware/image/wl
    pid=812 tid=1482 tftp-server : INF :[tftp_server.c, 1202] OACK options : [7680, 200, 2744992, 10, 0, 0, 0, 0]
    pid=812 tid=1482 tftp-server : INF :[tftp_os_la.c, 63] open : [-1] [-1] [384] [0] [/vendor/rfs/msm/mpss/readonly/firmware/image/wlanmdsp.mbn]
    pid=812 tid=1482 tftp-server : INF :[tftp_protocol.c, 742] Recd END OF TRANSFER pkt. Code = 9, Msg = End of Transfer
    pid=812 tid=1482 tftp-server : INF :[tftp_server.c, 1310] RRQ stats : sent_size = 0 total-blocks = 0 total-bytes = 0 timedout-pkts = 0, wrong-pkts = 0
09-19 00:10:56.015 812-1482/? I/tftp_server: pid=812 tid=1482 tftp-server : INF :[tftp_server.c, 1314] RRQ time stats : Total : [TX, RX] = [31, 191]
    pid=812 tid=1482 tftp-server : INF :[tftp_server.c, 1320] RRQ time stats : Tx/Rx [Min, Max] = [31, 31, 191, 191]
    pid=812 tid=1482 tftp-server : INF :[tftp_server.c, 1336] RRQ was successfully processed.
09-19 00:10:56.015 812-812/? I/tftp_server: pid=812 tid=812 tftp-server : INF :[tftp_server.c, 659] rcvd request [1] [96] [1] [0] [81]
09-19 00:10:56.015 812-1483/? I/tftp_server: pid=812 tid=1483 tftp-server : INF :[tftp_server_utils.c, 113] file [readonly/firmware/image/wlanmdsp.mbn] : [/vendor/rfs/msm/mpss/readonly/firmware/image/wl
    pid=812 tid=1483 tftp-server : INF :[tftp_server.c, 1202] OACK options : [7680, 200, 10, 2744992, 0, 0, 0, 0]
    pid=812 tid=1483 tftp-server : INF :[tftp_os_la.c, 63] open : [-1] [-1] [384] [0] [/vendor/rfs/msm/mpss/readonly/firmware/image/wlanmdsp.mbn]
09-19 00:10:56.019 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:56.032 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:56.058 774-774/? E/mm-camera: <MCT   ><ERROR> 179: stop_sof_check_thread: Returning as SOF timer thread not yet initialized
09-19 00:10:56.060 774-774/? I/QCamera: <HAL><INFO> closeCamera: 2431: [KPI Perf]: X PROFILE_CLOSE_CAMERA camera id 0, rc: 0
09-19 00:10:56.060 774-774/? D/MIPreview: stopAnalyzeThread: stopAnalyzeThread BEGIN
    stopAnalyzeThread: stopAnalyzeThread END
09-19 00:10:56.061 774-774/? I/QCamera: <HAL><INFO> close_camera_device: 1573: [KPI Perf]: X
09-19 00:10:56.062 774-774/? I/QCamera: <HAL><INFO> getCameraInfo: 342: Camera id 1 API version 768
09-19 00:10:56.062 774-774/? D/QCamera: Debug log file is not enabled
09-19 00:10:56.089 774-774/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:10:56.089 774-774/? I/chatty: uid=1047(cameraserver) android.hardwar identical 3 lines
09-19 00:10:56.089 774-774/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:10:56.101 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:56.102 812-1483/? I/tftp_server: pid=812 tid=1483 tftp-server : INF :[tftp_server.c, 1310] RRQ stats : sent_size = 2744992 total-blocks = 358 total-bytes = 2744992 timedout-pkts = 0, wrong-p
    pid=812 tid=1483 tftp-server : INF :[tftp_server.c, 1314] RRQ time stats : Total : [TX, RX] = [60735, 14812]
    pid=812 tid=1483 tftp-server : INF :[tftp_server.c, 1320] RRQ time stats : Tx/Rx [Min, Max] = [16, 1145, 253, 1291]
    pid=812 tid=1483 tftp-server : INF :[tftp_server.c, 1336] RRQ was successfully processed.
    res_idx = 0 chromatix_lib_name[1] = chiron_ov5675_primax_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_ov5675_primax_common
    res_idx = 0 chromatix_lib_name[3] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[8] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[9] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[10] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[11] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[12] = chiron_ov5675_primax_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_ov5675_primax_zsl_preview
09-19 00:10:56.108 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:10:56.108 765-765/? I/EdXposed-Bridge:   Loading class ma.wanam.wanamkit.Xposed
09-19 00:10:56.110 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/org.meowcat.edxposed.manager-vV43FdjgRSKoaRvjzrhayQ==/base.apk
09-19 00:10:56.111 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:56.115 774-1518/? E/mm-camera: <IMGLIB><ERROR> 328: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Nothing allocated or already freed!
09-19 00:10:56.115 774-774/? E/mm-camera: <MCT   ><ERROR> 179: stop_sof_check_thread: Returning as SOF timer thread not yet initialized
09-19 00:10:56.116 774-774/? E/CamComm1.0-MD: Update metadata entry: Unknown tag -2145976319
    Update metadata entry: Unknown tag -2145976317
09-19 00:10:56.116 774-774/? I/QCamera: <HAL><INFO> getCamInfo: 9565: camera 1 resource cost is 100
    <HAL><INFO> openLegacy: 503: openLegacy halVersion: 256 cameraId = 1
09-19 00:10:56.116 774-774/? D/vndksupport: Loading /vendor/lib/hw/power.default.so from current namespace instead of sphal namespace.
09-19 00:10:56.124 774-774/? E/Watermark: getFontData Font file does not exist!
    getFontData Get file status failed
    getFontData Font file does not exist!
    getFontData Get file status failed
09-19 00:10:56.124 774-774/? I/QCamera: <HAL><INFO> openCamera: 1923: [KPI Perf]: E PROFILE_OPEN_CAMERA camera id 1
09-19 00:10:56.126 774-774/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:10:56.126 774-774/? D/QCamera: Debug log file is not enabled
09-19 00:10:56.132 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:56.138 755-755/? I/Riru: found Riru in zygote64 (pid=765)
09-19 00:10:56.148 774-774/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:10:56.148 774-774/? I/chatty: uid=1047(cameraserver) android.hardwar identical 3 lines
09-19 00:10:56.148 774-774/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:10:56.151 774-774/? I/Thermal-Lib: Thermal-Lib-Client: Registration successful for camera with handle:1
09-19 00:10:56.151 774-774/? I/QCamera: <HAL><INFO> openCamera: 1938: [KPI Perf]: X PROFILE_OPEN_CAMERA camera id 1, rc: 0
09-19 00:10:56.153 774-774/? I/QCamera: <HAL><INFO> close_camera_device: 1571: [KPI Perf]: E camera id 1
09-19 00:10:56.154 774-1521/? E/QCamera: <HAL><ERROR> calcThermalLevel: 10178: level: 0, preview minfps 7000.000000, preview maxfpS 30000.000000, video minfps 7000.000000, video maxfps 30000.000000
    <HAL><ERROR> calcThermalLevel: 10183: level change to -> 0
    <HAL><ERROR> calcThermalLevel: 10262: Adjusted preview minfps 7.000000, preview maxfpS 30.000000, video minfps 7.000000, video maxfps 30.000000
09-19 00:10:56.155 774-1521/? E/QCameraParameters: setOISValue9690 OISEnabled=1 
    res_idx = 0 chromatix_lib_name[1] = chiron_ov5675_primax_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_ov5675_primax_common
    res_idx = 0 chromatix_lib_name[3] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[8] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[9] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[10] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[11] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[12] = chiron_ov5675_primax_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_ov5675_primax_zsl_preview
    res_idx = 0 chromatix_lib_name[1] = chiron_ov5675_primax_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_ov5675_primax_common
    res_idx = 0 chromatix_lib_name[3] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[8] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[9] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[10] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[11] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[12] = chiron_ov5675_primax_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_ov5675_primax_zsl_preview
    res_idx = 0 chromatix_lib_name[1] = chiron_ov5675_primax_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_ov5675_primax_common
    res_idx = 0 chromatix_lib_name[3] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[8] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[9] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[10] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[11] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[12] = chiron_ov5675_primax_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_ov5675_primax_zsl_preview
09-19 00:10:56.158 1091-1372/? I/cnss-daemon: WLFW service connected
    wlfw_read_file: No such file /data/vendor/wifi/wlfw_cal_00.bin
09-19 00:10:56.158 1091-1372/? E/cnss-daemon: wlfw_build_cal_table: not read /data/vendor/wifi/wlfw_cal_00.bin
09-19 00:10:56.158 1091-1372/? I/cnss-daemon: wlfw_read_file: No such file /data/vendor/wifi/wlfw_cal_01.bin
09-19 00:10:56.158 1091-1372/? E/cnss-daemon: wlfw_build_cal_table: not read /data/vendor/wifi/wlfw_cal_01.bin
09-19 00:10:56.158 1091-1372/? I/cnss-daemon: wlfw_read_file: No such file /data/vendor/wifi/wlfw_cal_02.bin
09-19 00:10:56.158 1091-1372/? E/cnss-daemon: wlfw_build_cal_table: not read /data/vendor/wifi/wlfw_cal_02.bin
09-19 00:10:56.158 1091-1372/? I/cnss-daemon: wlfw_read_file: No such file /data/vendor/wifi/wlfw_cal_03.bin
09-19 00:10:56.159 1091-1372/? E/cnss-daemon: wlfw_build_cal_table: not read /data/vendor/wifi/wlfw_cal_03.bin
09-19 00:10:56.159 1091-1372/? I/cnss-daemon: wlfw_read_file: No such file /data/vendor/wifi/wlfw_cal_04.bin
09-19 00:10:56.159 1091-1372/? E/cnss-daemon: wlfw_build_cal_table: not read /data/vendor/wifi/wlfw_cal_04.bin
09-19 00:10:56.164 774-774/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:10:56.164 774-774/? I/QCamera: <HAL><INFO> closeCamera: 2351: E
    <HAL><INFO> closeCamera: 2356: [KPI Perf]: E PROFILE_CLOSE_CAMERA camera id 1
09-19 00:10:56.164 774-1522/? E/mm-camera: <SENSOR><ERROR> 711: sensor_pick_resolution: res_idx: 2
09-19 00:10:56.164 774-1310/? E/mm-camera: <IMGLIB><ERROR> 297: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Invalid dimensions 0x0
    <IMGLIB><ERROR> 197: int img_algo_preload(img_base_ops_t *, void *): Preload: Failed to allocate buffer, rc -4
    <IMGLIB><ERROR> 119: module_imgbase_client_preload_exec: IMG_CORE_PRELOAD failed -4
09-19 00:10:56.165 925-1078/? I/ThermalEngine: Thermal-Server: Adding thermal event listener on fd 78
    Thermal-Server: removing client on fd 78
09-19 00:10:56.165 774-774/? I/Thermal-Lib: Thermal-Lib-Client: Unregisteration is successfull for handle:1
09-19 00:10:56.181 774-1554/? E/mm-camera: <IMGLIB><ERROR> 328: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Nothing allocated or already freed!
09-19 00:10:56.182 774-774/? E/mm-camera: <MCT   ><ERROR> 179: stop_sof_check_thread: Returning as SOF timer thread not yet initialized
09-19 00:10:56.183 774-774/? I/QCamera: <HAL><INFO> closeCamera: 2431: [KPI Perf]: X PROFILE_CLOSE_CAMERA camera id 1, rc: 0
09-19 00:10:56.183 774-774/? D/MIPreview: stopAnalyzeThread: stopAnalyzeThread BEGIN
    stopAnalyzeThread: stopAnalyzeThread END
09-19 00:10:56.184 774-774/? I/QCamera: <HAL><INFO> close_camera_device: 1573: [KPI Perf]: X
09-19 00:10:56.187 936-936/? I/CameraProviderManager: Connecting to new camera provider: legacy/0, isRemote? 1
09-19 00:10:56.188 936-936/? I/CameraProviderManager: Enumerating new camera device: device@1.0/legacy/0
09-19 00:10:56.188 774-774/? I/ServiceManagement: Registered android.hardware.camera.provider@2.4::ICameraProvider/legacy/0 (start delay of 3015ms)
    Removing namespace from process name android.hardware.camera.provider@2.4-service to provider@2.4-service.
09-19 00:10:56.189 774-774/? I/android.hardware.camera.provider@2.4-service: Registration complete for android.hardware.camera.provider@2.4::ICameraProvider/legacy/0.
09-19 00:10:56.191 774-1437/? I/CamDev@1.0-impl: Opening camera 0
09-19 00:10:56.191 774-1437/? I/QCamera: <HAL><INFO> openLegacy: 503: openLegacy halVersion: 256 cameraId = 0
09-19 00:10:56.191 774-1437/? D/vndksupport: Loading /vendor/lib/hw/power.default.so from current namespace instead of sphal namespace.
09-19 00:10:56.198 774-1437/? E/Watermark: getFontData Font file does not exist!
    getFontData Get file status failed
    getFontData Font file does not exist!
    getFontData Get file status failed
09-19 00:10:56.198 774-1437/? I/QCamera: <HAL><INFO> openCamera: 1923: [KPI Perf]: E PROFILE_OPEN_CAMERA camera id 0
09-19 00:10:56.199 774-1437/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:10:56.199 936-936/? W/CameraProviderManager: Camera provider legacy/0 says an unknown camera device@1.0/legacy/0 now has torch status 0. Curious.
    Camera provider legacy/0 says an unknown camera device@3.3/legacy/0 now has torch status 0. Curious.
09-19 00:10:56.199 774-1437/? D/QCamera: Debug log file is not enabled
09-19 00:10:56.211 1091-1372/? I/cnss-daemon: wlfw_send_cap_req: chip_id: 0x30214, chip_family 0x4001, board_id: 0xff, soc_id: 0x40010002, fw_version: 0x100382c4, fw_build_timestamp: 2019-07-07 19:01
09-19 00:10:56.222 774-1437/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:10:56.222 774-1437/? I/chatty: uid=1047(cameraserver) HwBinder:774_2 identical 3 lines
09-19 00:10:56.222 774-1437/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:10:56.225 774-1437/? I/Thermal-Lib: Thermal-Lib-Client: Registration successful for camera with handle:1
09-19 00:10:56.225 774-1437/? I/QCamera: <HAL><INFO> openCamera: 1938: [KPI Perf]: X PROFILE_OPEN_CAMERA camera id 0, rc: 0
09-19 00:10:56.226 774-1437/? I/CamDev@1.0-impl: could not cast ICameraDeviceCallback to IQCameraDeviceCallback
09-19 00:10:56.227 774-1558/? E/QCamera: <HAL><ERROR> calcThermalLevel: 10178: level: 0, preview minfps 7000.000000, preview maxfpS 30000.000000, video minfps 7000.000000, video maxfps 30000.000000
    <HAL><ERROR> calcThermalLevel: 10183: level change to -> 0
    <HAL><ERROR> calcThermalLevel: 10262: Adjusted preview minfps 7.000000, preview maxfpS 30.000000, video minfps 7.000000, video maxfps 30.000000
09-19 00:10:56.228 774-1558/? E/QCameraParameters: setOISValue9690 OISEnabled=1 
    res_idx = 0 chromatix_lib_name[1] = chiron_imx386_semco_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_imx386_semco_common
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[9] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[10] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[11] = chiron_imx386_semco_cpp_video
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_imx386_semco_zsl_preview
    res_idx = 0 chromatix_lib_name[0] = chiron_imx386_semco_snapshot
    res_idx = 0 chromatix_lib_name[1] = chiron_imx386_semco_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_imx386_semco_common
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[9] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[10] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[11] = chiron_imx386_semco_cpp_video
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_imx386_semco_zsl_preview
09-19 00:10:56.230 774-1563/? E/mm-camera: <SENSOR><ERROR> chiron_imx386_semco_autofocus_calibration: 571: adjusted code_per_step: 165, qvalue: 128
    res_idx = 0 chromatix_lib_name[1] = chiron_imx386_semco_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_imx386_semco_common
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[9] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[10] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[11] = chiron_imx386_semco_cpp_video
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_imx386_semco_zsl_preview
09-19 00:10:56.233 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:56.234 774-774/? I/CamDev@1.0-impl: Closing camera 0
09-19 00:10:56.234 774-774/? I/QCamera: <HAL><INFO> close_camera_device: 1571: [KPI Perf]: E camera id 0
09-19 00:10:56.238 774-774/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:10:56.239 774-774/? I/QCamera: <HAL><INFO> closeCamera: 2351: E
    <HAL><INFO> closeCamera: 2356: [KPI Perf]: E PROFILE_CLOSE_CAMERA camera id 0
09-19 00:10:56.239 774-1559/? E/mm-camera: <SENSOR><ERROR> 711: sensor_pick_resolution: res_idx: 1
09-19 00:10:56.239 774-1310/? E/mm-camera: <IMGLIB><ERROR> 297: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Invalid dimensions 0x0
    <IMGLIB><ERROR> 197: int img_algo_preload(img_base_ops_t *, void *): Preload: Failed to allocate buffer, rc -4
    <IMGLIB><ERROR> 119: module_imgbase_client_preload_exec: IMG_CORE_PRELOAD failed -4
09-19 00:10:56.242 925-1078/? I/ThermalEngine: Thermal-Server: Adding thermal event listener on fd 78
    Thermal-Server: removing client on fd 78
09-19 00:10:56.242 774-774/? I/Thermal-Lib: Thermal-Lib-Client: Unregisteration is successfull for handle:1
09-19 00:10:56.295 774-1590/? E/mm-camera: <IMGLIB><ERROR> 328: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Nothing allocated or already freed!
09-19 00:10:56.305 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:56.309 765-765/? W/zygote64: Found duplicate classes, falling back to extracting from APK : /data/app/org.meowcat.edxposed.manager-vV43FdjgRSKoaRvjzrhayQ==/base.apk
09-19 00:10:56.310 765-765/? W/zygote64: NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /data/app/org.meowcat.edxposed.manager-vV43FdjgRSKoaRvjzrhayQ==/base.apk and /system/framework/edxp.jar
09-19 00:10:56.315 923-923/? I/ServiceManagement: Registered vendor.qti.hardware.radio.am@1.0::IQcRilAudio/slot2 (start delay of 2583ms)
09-19 00:10:56.318 923-1036/? D/PerMgrLib: QCRIL voting for modem
09-19 00:10:56.318 820-852/? D/PerMgrSrv: QCRIL voting for modem
    modem num voters is 4
09-19 00:10:56.319 923-923/? I/ServiceManagement: Registered android.hardware.radio@1.1::IRadio/slot2 (start delay of 2587ms)
09-19 00:10:56.320 923-923/? I/ServiceManagement: Registered android.hardware.radio.deprecated@1.0::IOemHook/slot2 (start delay of 2588ms)
09-19 00:10:56.320 923-1036/? E/QMI_FW: QMUXD: WARNING qmi_qmux_if_pwr_up_init failed! rc=-6
09-19 00:10:56.322 870-870/? W/adbd: timeout expired while flushing socket, closing
09-19 00:10:56.333 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:56.350 923-1036/? I/ServiceManagement: Registered vendor.qti.hardware.radio.ims@1.0::IImsRadio/imsradio1 (start delay of 2618ms)
09-19 00:10:56.357 923-923/? W/rild: type=1400 audit(0.0:64): avc: denied { read } for name="u:object_r:system_prop:s0" dev="tmpfs" ino=19426 scontext=u:r:rild:s0 tcontext=u:object_r:system_prop:s0 tclass=file permissive=0
09-19 00:10:56.359 923-1036/? E/libc: Access denied finding property "persist.sys.labtest_flag"
09-19 00:10:56.360 923-923/? W/rild: type=1400 audit(0.0:65): avc: denied { read } for name="u:object_r:default_prop:s0" dev="tmpfs" ino=19331 scontext=u:r:rild:s0 tcontext=u:object_r:default_prop:s0 tclass=file permissive=0
09-19 00:10:56.363 923-1036/? E/libc: Access denied finding property "ro.carrier.name"
    Access denied finding property "ro.miui.cust_variant"
09-19 00:10:56.380 923-923/? W/rild: type=1400 audit(0.0:67): avc: denied { read } for name="u:object_r:default_prop:s0" dev="tmpfs" ino=19331 scontext=u:r:rild:s0 tcontext=u:object_r:default_prop:s0 tclass=file permissive=0
09-19 00:10:56.383 923-1036/? E/libc: Access denied finding property "ro.product.mod_device"
    Access denied finding property "persist.sys.labtest_flag"
09-19 00:10:56.405 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:56.406 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:56.406 1132-1132/? I/chatty: uid=1001(radio) /vendor/bin/imsdatadaemon identical 1 line
09-19 00:10:56.407 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:56.419 923-1036/? I/ServiceManagement: Registered vendor.qti.hardware.radio.uim_remote_server@1.0::IUimRemoteServiceServer/uimRemoteServer1 (start delay of 2687ms)
09-19 00:10:56.421 923-1036/? I/ServiceManagement: Registered vendor.qti.hardware.radio.uim@1.1::IUim/Uim1 (start delay of 2689ms)
09-19 00:10:56.428 923-1615/? I/ServiceManagement: Registered android.hardware.secure_element@1.0::ISecureElement/SIM2 (start delay of 2697ms)
09-19 00:10:56.431 923-1036/? I/ServiceManagement: Registered vendor.qti.hardware.radio.uim_remote_client@1.0::IUimRemoteServiceClient/uimRemoteClient1 (start delay of 2699ms)
09-19 00:10:56.432 923-1036/? I/ServiceManagement: Registered vendor.qti.hardware.radio.lpa@1.0::IUimLpa/UimLpa1 (start delay of 2701ms)
09-19 00:10:56.433 923-1036/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:56.434 923-1036/? I/chatty: uid=1001(radio) /vendor/bin/hw/rild identical 1 line
09-19 00:10:56.434 923-1036/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:56.436 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:56.438 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:56.439 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:56.454 1001-1121/? I/ServiceManagement: Registered vendor.qti.hardware.radio.ims@1.0::IImsRadio/imsradio0 (start delay of 2602ms)
09-19 00:10:56.455 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:10:56.456 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:56.457 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:56.458 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:56.458 1001-1121/? W/libc: Unable to set property "ro.vendor.ril.svlte1x" to "false": error code: 0xb
    Unable to set property "ro.vendor.ril.svdo" to "false": error code: 0xb
09-19 00:10:56.465 1001-1121/? E/libc: Access denied finding property "persist.sys.labtest_flag"
09-19 00:10:56.460 1001-1001/? W/rild: type=1400 audit(0.0:69): avc: denied { read } for name="u:object_r:system_prop:s0" dev="tmpfs" ino=19426 scontext=u:r:rild:s0 tcontext=u:object_r:system_prop:s0 tclass=file permissive=0
09-19 00:10:56.468 1001-1121/? E/libc: Access denied finding property "ro.carrier.name"
09-19 00:10:56.467 1001-1001/? W/rild: type=1400 audit(0.0:70): avc: denied { read } for name="u:object_r:default_prop:s0" dev="tmpfs" ino=19331 scontext=u:r:rild:s0 tcontext=u:object_r:default_prop:s0 tclass=file permissive=0
09-19 00:10:56.468 1001-1121/? E/libc: Access denied finding property "ro.miui.cust_variant"
09-19 00:10:56.470 923-1036/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:56.476 923-1036/? I/ServiceManagement: Registered vendor.qti.hardware.radio.qcrilhook@1.0::IQtiOemHook/oemhook1 (start delay of 2744ms)
09-19 00:10:56.477 923-1036/? I/ServiceManagement: Registered vendor.qti.hardware.radio.qtiradio@1.0::IQtiRadio/slot2 (start delay of 2745ms)
09-19 00:10:56.482 923-1036/? E/libc: Access denied finding property "ro.cust.test"
09-19 00:10:56.480 923-923/? W/rild: type=1400 audit(0.0:72): avc: denied { read } for name="u:object_r:default_prop:s0" dev="tmpfs" ino=19331 scontext=u:r:rild:s0 tcontext=u:object_r:default_prop:s0 tclass=file permissive=0
09-19 00:10:56.483 1632-1632/? I/imsrcsd: Uce Service HAL  is starting up...
    getAndroidPropValue : vendor.ims.DATA_DAEMON_STATUS[1]
09-19 00:10:56.485 765-765/? I/EdXposed-Bridge:   Loading class org.meowcat.edxposed.manager.xposed.Enhancement
09-19 00:10:56.486 1001-1121/? D/qmi_nv_api: XIAOMI_QMI_NV: qmi_client_get_service_list() returned 0 num_services = 1
    XIAOMI_QMI_NV: qmi_client_get_service_list() returned 0 num_entries = 1 num_services = 1
    XIAOMI_QMI_NV: NV Read with nv index 2824 index 0.
09-19 00:10:56.486 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-8y2xge8uLmrhBt8pzNcgVA==/base.apk
09-19 00:10:56.486 1001-1121/? D/qmi_nv_api: XIAOMI_QMI_NV: qmi_client_send_msg_async returned 0
09-19 00:10:56.487 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:56.487 1001-1651/? D/qmi_nv_api: XIAOMI_QMI_NV: Read NV2824 Response: 0, Length: 0
09-19 00:10:56.490 1001-1121/? D/qmi_nv_api: XIAOMI_QMI_NV: qmi_client_get_service_list() returned 0 num_services = 1
    XIAOMI_QMI_NV: qmi_client_get_service_list() returned 0 num_entries = 1 num_services = 1
    XIAOMI_QMI_NV: NV Read with nv index 2497 index 0.
    XIAOMI_QMI_NV: qmi_client_send_msg_async returned 0
09-19 00:10:56.490 1001-1652/? D/qmi_nv_api: XIAOMI_QMI_NV: Read NV2497 Response: 0, Length: 0
09-19 00:10:56.490 1001-1001/? W/rild: type=1400 audit(0.0:73): avc: denied { read } for name="u:object_r:default_prop:s0" dev="tmpfs" ino=19331 scontext=u:r:rild:s0 tcontext=u:object_r:default_prop:s0 tclass=file permissive=0
    type=1400 audit(0.0:74): avc: denied { read } for name="u:object_r:system_prop:s0" dev="tmpfs" ino=19426 scontext=u:r:rild:s0 tcontext=u:object_r:system_prop:s0 tclass=file permissive=0
09-19 00:10:56.493 1001-1121/? E/libc: Access denied finding property "ro.product.mod_device"
09-19 00:10:56.494 1001-1121/? E/libc: Access denied finding property "persist.sys.labtest_flag"
09-19 00:10:56.503 1001-1121/? I/ServiceManagement: Registered vendor.qti.hardware.radio.uim_remote_server@1.0::IUimRemoteServiceServer/uimRemoteServer0 (start delay of 2651ms)
09-19 00:10:56.504 1001-1121/? I/ServiceManagement: Registered vendor.qti.hardware.radio.uim@1.1::IUim/Uim0 (start delay of 2652ms)
09-19 00:10:56.505 1001-1121/? I/ServiceManagement: Registered android.hardware.radio.config@1.0::IRadioConfig/default (start delay of 2653ms)
09-19 00:10:56.506 1001-1656/? I/ServiceManagement: Registered android.hardware.secure_element@1.0::ISecureElement/SIM1 (start delay of 2654ms)
09-19 00:10:56.509 1001-1121/? I/ServiceManagement: Registered vendor.qti.hardware.radio.uim_remote_client@1.0::IUimRemoteServiceClient/uimRemoteClient0 (start delay of 2657ms)
    Registered vendor.qti.hardware.radio.lpa@1.0::IUimLpa/UimLpa0 (start delay of 2658ms)
09-19 00:10:56.510 1001-1121/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:56.511 1001-1121/? I/chatty: uid=1001(radio) /vendor/bin/hw/rild identical 2 lines
09-19 00:10:56.535 1001-1121/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:56.536 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:56.541 1001-1121/? I/ServiceManagement: Registered vendor.qti.hardware.radio.qcrilhook@1.0::IQtiOemHook/oemhook0 (start delay of 2689ms)
09-19 00:10:56.542 1001-1121/? I/ServiceManagement: Registered vendor.qti.hardware.radio.qtiradio@1.0::IQtiRadio/slot1 (start delay of 2690ms)
09-19 00:10:56.547 1001-1121/? E/libc: Access denied finding property "ro.cust.test"
09-19 00:10:56.543 1001-1001/? W/rild: type=1400 audit(0.0:75): avc: denied { read } for name="u:object_r:default_prop:s0" dev="tmpfs" ino=19331 scontext=u:r:rild:s0 tcontext=u:object_r:default_prop:s0 tclass=file permissive=0
09-19 00:10:56.554 774-774/? E/mm-camera: <MCT   ><ERROR> 179: stop_sof_check_thread: Returning as SOF timer thread not yet initialized
09-19 00:10:56.555 936-936/? W/CameraProviderManager: Camera provider legacy/0 says an unknown camera device@1.0/legacy/0 now has torch status 1. Curious.
    Camera provider legacy/0 says an unknown camera device@3.3/legacy/0 now has torch status 1. Curious.
09-19 00:10:56.555 774-774/? I/QCamera: <HAL><INFO> closeCamera: 2431: [KPI Perf]: X PROFILE_CLOSE_CAMERA camera id 0, rc: 0
09-19 00:10:56.555 774-774/? D/MIPreview: stopAnalyzeThread: stopAnalyzeThread BEGIN
    stopAnalyzeThread: stopAnalyzeThread END
09-19 00:10:56.558 774-774/? I/QCamera: <HAL><INFO> close_camera_device: 1573: [KPI Perf]: X
09-19 00:10:56.558 936-936/? I/CameraProviderManager: Enumerating new camera device: device@3.3/legacy/0
09-19 00:10:56.559 936-936/? E/CameraProviderManager: DeviceInfo3: Converted ICameraDevice instance to nullptr
09-19 00:10:56.559 936-936/? I/CameraProviderManager: Enumerating new camera device: device@1.0/legacy/1
09-19 00:10:56.561 774-1435/? I/CamDev@1.0-impl: Opening camera 1
09-19 00:10:56.561 774-1435/? I/QCamera: <HAL><INFO> openLegacy: 503: openLegacy halVersion: 256 cameraId = 1
09-19 00:10:56.562 774-1435/? D/vndksupport: Loading /vendor/lib/hw/power.default.so from current namespace instead of sphal namespace.
09-19 00:10:56.568 774-1435/? E/Watermark: getFontData Font file does not exist!
    getFontData Get file status failed
09-19 00:10:56.569 774-1435/? E/Watermark: getFontData Font file does not exist!
    getFontData Get file status failed
09-19 00:10:56.569 774-1435/? I/QCamera: <HAL><INFO> openCamera: 1923: [KPI Perf]: E PROFILE_OPEN_CAMERA camera id 1
09-19 00:10:56.569 774-1435/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:10:56.570 774-1435/? D/QCamera: Debug log file is not enabled
09-19 00:10:56.593 774-1435/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:10:56.593 774-1435/? I/chatty: uid=1047(cameraserver) HwBinder:774_1 identical 3 lines
09-19 00:10:56.593 774-1435/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:10:56.597 774-1435/? I/Thermal-Lib: Thermal-Lib-Client: Registration successful for camera with handle:1
09-19 00:10:56.597 774-1435/? I/QCamera: <HAL><INFO> openCamera: 1938: [KPI Perf]: X PROFILE_OPEN_CAMERA camera id 1, rc: 0
09-19 00:10:56.600 774-1677/? E/QCamera: <HAL><ERROR> calcThermalLevel: 10178: level: 0, preview minfps 7000.000000, preview maxfpS 30000.000000, video minfps 7000.000000, video maxfps 30000.000000
    <HAL><ERROR> calcThermalLevel: 10183: level change to -> 0
    <HAL><ERROR> calcThermalLevel: 10262: Adjusted preview minfps 7.000000, preview maxfpS 30.000000, video minfps 7.000000, video maxfps 30.000000
09-19 00:10:56.600 774-1435/? I/CamDev@1.0-impl: could not cast ICameraDeviceCallback to IQCameraDeviceCallback
09-19 00:10:56.601 774-1677/? E/QCameraParameters: setOISValue9690 OISEnabled=1 
    res_idx = 0 chromatix_lib_name[1] = chiron_ov5675_primax_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_ov5675_primax_common
    res_idx = 0 chromatix_lib_name[3] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[8] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[9] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[10] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[11] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[12] = chiron_ov5675_primax_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_ov5675_primax_zsl_preview
    res_idx = 0 chromatix_lib_name[0] = chiron_ov5675_primax_snapshot
    res_idx = 0 chromatix_lib_name[1] = chiron_ov5675_primax_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_ov5675_primax_common
    res_idx = 0 chromatix_lib_name[3] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[8] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[9] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[10] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[12] = chiron_ov5675_primax_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_ov5675_primax_zsl_preview
    res_idx = 0 chromatix_lib_name[1] = chiron_ov5675_primax_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_ov5675_primax_common
    res_idx = 0 chromatix_lib_name[3] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[8] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[9] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[10] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[11] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[12] = chiron_ov5675_primax_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_ov5675_primax_zsl_preview
09-19 00:10:56.606 774-1435/? I/CamDev@1.0-impl: Closing camera 1
09-19 00:10:56.606 774-1435/? I/QCamera: <HAL><INFO> close_camera_device: 1571: [KPI Perf]: E camera id 1
09-19 00:10:56.610 774-1435/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:10:56.610 925-1078/? I/ThermalEngine: Thermal-Server: Adding thermal event listener on fd 78
09-19 00:10:56.611 774-1435/? I/QCamera: <HAL><INFO> closeCamera: 2351: E
    <HAL><INFO> closeCamera: 2356: [KPI Perf]: E PROFILE_CLOSE_CAMERA camera id 1
09-19 00:10:56.611 774-1678/? E/mm-camera: <SENSOR><ERROR> 711: sensor_pick_resolution: res_idx: 2
09-19 00:10:56.611 774-1310/? E/mm-camera: <IMGLIB><ERROR> 297: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Invalid dimensions 0x0
    <IMGLIB><ERROR> 197: int img_algo_preload(img_base_ops_t *, void *): Preload: Failed to allocate buffer, rc -4
09-19 00:10:56.612 774-1310/? E/mm-camera: <IMGLIB><ERROR> 119: module_imgbase_client_preload_exec: IMG_CORE_PRELOAD failed -4
09-19 00:10:56.612 774-1705/? I/Thermal-Lib: Thermal-Lib-Client: Client received msg camera 0
    Thermal-Lib-Client: Client received msg camcorder 0
09-19 00:10:56.612 774-1705/? E/Thermal-Lib: Thermal-Lib-Client: No Callback registered for camcorder
09-19 00:10:56.613 925-1078/? I/ThermalEngine: Thermal-Server: removing client on fd 78
09-19 00:10:56.613 774-1435/? I/Thermal-Lib: Thermal-Lib-Client: Unregisteration is successfull for handle:1
09-19 00:10:56.622 774-1711/? E/mm-camera: <IMGLIB><ERROR> 328: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Nothing allocated or already freed!
09-19 00:10:56.622 774-1435/? E/mm-camera: <MCT   ><ERROR> 179: stop_sof_check_thread: Returning as SOF timer thread not yet initialized
09-19 00:10:56.623 774-1435/? I/QCamera: <HAL><INFO> closeCamera: 2431: [KPI Perf]: X PROFILE_CLOSE_CAMERA camera id 1, rc: 0
09-19 00:10:56.623 774-1435/? D/MIPreview: stopAnalyzeThread: stopAnalyzeThread BEGIN
    stopAnalyzeThread: stopAnalyzeThread END
09-19 00:10:56.624 774-1435/? I/QCamera: <HAL><INFO> close_camera_device: 1573: [KPI Perf]: X
09-19 00:10:56.624 936-936/? I/CameraProviderManager: Enumerating new camera device: device@3.3/legacy/1
09-19 00:10:56.625 936-936/? E/CameraProviderManager: DeviceInfo3: Converted ICameraDevice instance to nullptr
09-19 00:10:56.625 936-936/? I/CameraProviderManager: Camera provider legacy/0 ready with 4 camera devices
09-19 00:10:56.625 936-936/? I/CameraService: onDeviceStatusChanged: Status changed for cameraId=1, newStatus=1
    onDeviceStatusChanged: Unknown camera ID 1, a new camera is added
09-19 00:10:56.626 936-936/? I/CameraService: onDeviceStatusChanged: Status changed for cameraId=0, newStatus=1
    onDeviceStatusChanged: Unknown camera ID 0, a new camera is added
09-19 00:10:56.626 936-1231/? W/CameraProviderManager: addProviderLocked: Camera provider HAL with name 'legacy/0' already registered
09-19 00:10:56.637 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:56.738 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:56.781 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:739] qti_file_open():Could not open device file. Errno 2 error msg=No such file or directory
09-19 00:10:56.839 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:56.871 765-765/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
      Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
09-19 00:10:56.872 765-765/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v0
    Loading modules from /data/app/com.oranav.ditheredholobackground-WGw3w1Oj7KB1upluOt6Kqw==/base.apk
09-19 00:10:56.873 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:56.888 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:56.889 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:10:56.890 765-765/? I/EdXposed-Bridge:   Loading class com.oranav.ditheredholobackground.DitheredHoloBackground
09-19 00:10:56.893 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/com.jy.xposed.web-0cFiSLP-t5GVpgMJ1Zv9lw==/base.apk
09-19 00:10:56.894 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:56.912 765-765/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:56.913 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Hierarchies don't match'
09-19 00:10:56.913 765-765/? I/EdXposed-Bridge:   Loading class com.jy.xposed.web.core.Main
09-19 00:10:56.916 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/z.houbin.skip-ALbC9SZ8n0lVdbMmAc5fQQ==/base.apk
09-19 00:10:56.916 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:56.939 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:56.954 925-1074/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 43000 mC, weight[0] 2
09-19 00:10:56.955 925-1074/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:10:56.967 765-765/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
    Found duplicate classes, falling back to extracting from APK : /data/app/z.houbin.skip-ALbC9SZ8n0lVdbMmAc5fQQ==/base.apk
    NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /data/app/z.houbin.skip-ALbC9SZ8n0lVdbMmAc5fQQ==/base.apk and /system/framework/edxp.jar
09-19 00:10:57.008 765-765/? I/EdXposed-Bridge:   Loading class z.houbin.skip.MainHook
09-19 00:10:57.010 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/xyz.joas.forcedarkmodeoreo-PGC5RmNRt7E7ivwzrfliMQ==/base.apk
09-19 00:10:57.011 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:57.039 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:57.070 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:57.072 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:10:57.072 765-765/? I/EdXposed-Bridge:   Loading class xyz.joas.forcedarkmodeoreo.ForceDarkMode
09-19 00:10:57.073 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/ml.pyshivam.imeimasker-kBZTMKUVVbE3p0YdbIrmSw==/base.apk
09-19 00:10:57.073 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:57.101 882-882/? I/QC-NETMGR-LIB: NetmgrNetdClientInit(): Looking for Netd service
09-19 00:10:57.102 882-882/? D/QC-NETMGR-LIB: registerServerNotification(): Successfully registered for Netd HAL service
09-19 00:10:57.104 882-1736/? I/QC-NETMGR-LIB: onRegistration(): Starting Netd getService thread
09-19 00:10:57.105 882-1740/? I/QC-NETMGR-LIB: getServiceImpl(): INetd discovered
09-19 00:10:57.106 882-1740/? I/QC-NETMGR-LIB: registerLinkToDeath(): Success registerLinkToDeath!
09-19 00:10:57.106 882-1736/? I/QC-NETMGR-LIB: onRegistration(): Service exists, not a restart
09-19 00:10:57.106 882-882/? I/QC-NETMGR-LIB: NetmgrNetdClientInit(): Created netd client
09-19 00:10:57.140 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:57.156 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:57.156 882-882/? I/QC-NETMGR-LIB: NetmgrNetdClientRegisterNetwork(): Looking for Netd service
    NetmgrNetdClientRegisterNetwork(): register to create new OEM network
    registerNetwork(): Attempting createOemNetwork
09-19 00:10:57.156 764-1123/? D/TcpSocketMonitor: suspending tcpinfo polling
09-19 00:10:57.157 882-882/? I/QC-NETMGR-LIB: registerNetwork(): command completed!
    registerNetwork(): createOemNetwork succeeded [packet mark : 0xf0001] [net id : 1] [network handle : 0x1cafed00d]
    NetmgrNetdClientRegisterNetwork(): [packet mark : 0xf0001] [network handle : 0x1cafed00d]
09-19 00:10:57.159 765-765/? W/zygote64: Found duplicate classes, falling back to extracting from APK : /data/app/ml.pyshivam.imeimasker-kBZTMKUVVbE3p0YdbIrmSw==/base.apk
    NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /system/framework/edxp.jar and /data/app/ml.pyshivam.imeimasker-kBZTMKUVVbE3p0YdbIrmSw==/base.apk
09-19 00:10:57.228 765-765/? I/EdXposed-Bridge:   Loading class ml.pyshivam.imeimasker.IMEIMasker
09-19 00:10:57.229 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/com.xloger.exlink.app-k4miYHCp7k_RBO4_2BxjHg==/base.apk
09-19 00:10:57.230 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:57.240 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:57.254 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:57.256 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:10:57.256 765-765/? I/EdXposed-Bridge:   Loading class com.xloger.exlink.app.HookMain
09-19 00:10:57.258 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/louis.baseapk-Nb3bv9DiXpVlLtzRL5xIdQ==/base.apk
09-19 00:10:57.258 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:57.317 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:57.320 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:10:57.321 765-765/? I/EdXposed-Bridge:   Loading class louis.ʹ
    Loading modules from /data/app/io.alcatraz.noapplet-eIitfHwR5bBcjeYqx3rDpA==/base.apk
09-19 00:10:57.322 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:57.340 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:57.407 765-765/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:57.409 765-765/? W/zygote64: Found duplicate classes, falling back to extracting from APK : /data/app/io.alcatraz.noapplet-eIitfHwR5bBcjeYqx3rDpA==/base.apk
09-19 00:10:57.410 765-765/? W/zygote64: NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /data/app/io.alcatraz.noapplet-eIitfHwR5bBcjeYqx3rDpA==/base.apk and /system/framework/edxp.jar
09-19 00:10:57.440 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:57.480 765-765/? I/EdXposed-Bridge:   Loading class io.alcatraz.noapplet.ModuleMain
09-19 00:10:57.481 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/li.lingfeng.ltweaks-wp3kMW3n45fUnDO4mVLXAg==/base.apk
09-19 00:10:57.482 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:57.541 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:57.637 765-765/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:57.641 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:57.645 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Hierarchies don't match'
09-19 00:10:57.645 765-765/? I/EdXposed-Bridge:   Loading class li.lingfeng.ltweaks.xposed.XposedLoader
09-19 00:10:57.658 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/ru.bluecat.android.xposed.mods.appsettings-VYHj687WS3roYgko83SRXg==/base.apk
09-19 00:10:57.659 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:57.668 765-765/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
    Found duplicate classes, falling back to extracting from APK : /data/app/ru.bluecat.android.xposed.mods.appsettings-VYHj687WS3roYgko83SRXg==/base.apk
    NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /system/framework/edxp.jar and /data/app/ru.bluecat.android.xposed.mods.appsettings-VYHj687WS3roYgko83SRXg==/base.apk
09-19 00:10:57.672 765-765/? I/EdXposed-Bridge:   Loading class ru.bluecat.android.xposed.mods.appsettings.hooks.XposedMod
09-19 00:10:57.677 765-765/? W/main: type=1400 audit(0.0:76): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:57.684 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:57.684 765-765/? D/SandHook: method <private void android.view.Display.updateDisplayInfoLocked()> hook <replacement> success!
09-19 00:10:57.687 765-765/? W/main: type=1400 audit(0.0:78): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:57.694 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:57.695 765-765/? D/SandHook: method <protected android.view.ViewGroup com.android.internal.policy.PhoneWindow.generateLayout(com.android.internal.policy.DecorView)> hook <replacement> success!
09-19 00:10:57.693 765-765/? W/main: type=1400 audit(0.0:80): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:57.704 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:57.704 765-765/? D/SandHook: method <public void android.view.Window.setFlags(int,int)> hook <replacement> success!
09-19 00:10:57.703 765-765/? W/main: type=1400 audit(0.0:82): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:57.713 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:57.714 765-765/? D/SandHook: method <public void android.view.ViewRootImpl.dispatchSystemUiVisibilityChanged(int,int,int,int)> hook <replacement> success!
09-19 00:10:57.721 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:57.713 765-765/? W/main: type=1400 audit(0.0:84): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:57.722 765-765/? D/SandHook: method <public void android.app.Activity.setRequestedOrientation(int)> hook <replacement> success!
09-19 00:10:57.720 765-765/? W/main: type=1400 audit(0.0:86): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:57.730 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:57.730 765-765/? D/SandHook: method <void android.inputmethodservice.InputMethodService.doStartInput(android.view.inputmethod.InputConnection,android.view.inputmethod.EditorInfo,boolean)> hook <replacement> success!
09-19 00:10:57.731 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/top.imlk.confesstalk-nX7zXQm5XMtH6SjG9zammA==/base.apk
09-19 00:10:57.731 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:57.741 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:57.748 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:57.749 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:10:57.750 765-765/? I/EdXposed-Bridge:   Loading class top.imlk.confesstalk.hooker.Injecter
    Loading modules from /data/app/hdfg159.qqsendpoke-oK-fuqejo1vRTTkNDpO7iw==/base.apk
09-19 00:10:57.751 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:57.756 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:57.757 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:10:57.757 765-765/? I/EdXposed-Bridge:   Loading class hdfg159.qqsendpoke.hook.PokeMsgHook
    Loading modules from /data/app/com.arjerine.textxposed-wwEDo2OIEu6Gyza_qvGUUA==/base.apk
09-19 00:10:57.758 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:57.781 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:739] qti_file_open():Could not open device file. Errno 2 error msg=No such file or directory
09-19 00:10:57.831 882-882/? I/QC-NETMGR-LIB: NetmgrNetdClientRegisterNetwork(): Looking for Netd service
    NetmgrNetdClientRegisterNetwork(): register to create new OEM network
    registerNetwork(): Attempting createOemNetwork
09-19 00:10:57.831 764-1123/? D/TcpSocketMonitor: suspending tcpinfo polling
09-19 00:10:57.831 882-882/? I/QC-NETMGR-LIB: registerNetwork(): command completed!
    registerNetwork(): createOemNetwork succeeded [packet mark : 0xf0002] [net id : 2] [network handle : 0x2cafed00d]
    NetmgrNetdClientRegisterNetwork(): [packet mark : 0xf0002] [network handle : 0x2cafed00d]
09-19 00:10:57.842 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:57.878 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:57.885 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:10:57.886 765-765/? I/EdXposed-Bridge:   Loading class com.arjerine.textxposed.xposed.Xposed
09-19 00:10:57.895 765-765/? I/EdXposed-Bridge:   Loading class com.arjerine.textxposed.xposed.XposedDetect
      Loading class com.arjerine.textxposed.macro.Xposed
09-19 00:10:57.896 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:10:57.897 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:57.930 765-765/? W/zygote64: Method La/b/m/a/b;.b is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:10:57.931 765-765/? W/zygote64: Method La/i/f/j;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/f/j;.b is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/l/u$c;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/l/u$c;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/l/d/n;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.b is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.e is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.g is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.h is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:10:57.932 765-765/? W/zygote64: Method Lb/c/a/a/f0/d;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.g is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.h is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.i is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.j is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.m is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.o is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.p is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.s is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/f/k/c;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/f/k/c;.setTintList is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:10:57.942 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:57.944 765-765/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
    Found duplicate classes, falling back to extracting from APK : /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk and /system/framework/edxp.jar
09-19 00:10:57.957 925-1074/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 44000 mC, weight[0] 2
09-19 00:10:57.958 925-1074/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:10:57.959 925-1079/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 44000 mC, weight[0] 2
09-19 00:10:57.960 925-1079/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
    handle_thresh_sig: TM Id SKIN-BATTERY-MONITOR Sensor SKIN-VIRTUAL-SENSOR Temp 41333
    TM Id 'SKIN-BATTERY-MONITOR' Sensor 'SKIN-VIRTUAL-SENSOR' - alarm  raised 3 at 41.3 degC
    j=0 i=2 TM Id SKIN-BATTERY-MONITOR Sensor SKIN-VIRTUAL-SENSOR: Action battery value 2
    ACTION: BATTERY - Setting battery charging mitigation to 2
    Mitigation:Battery:2
09-19 00:10:57.961 925-1079/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 44000 mC, weight[0] 2
09-19 00:10:57.962 925-1079/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
    handle_thresh_sig: TM Id CPU7_HOTPLUG_MONITOR Sensor SKIN-VIRTUAL-SENSOR Temp 41333
    TM Id 'CPU7_HOTPLUG_MONITOR' Sensor 'SKIN-VIRTUAL-SENSOR' - alarm  raised 1 at 41.3 degC
    j=0 i=0 TM Id CPU7_HOTPLUG_MONITOR Sensor SKIN-VIRTUAL-SENSOR: Action hotplug_7 value 1
    ACTION: Hotplugged OFF CPU[7]
09-19 00:10:57.963 765-765/? W/zygote64: Method La/b/m/a/b;.b is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/f/j;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/f/j;.b is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/l/u$c;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/l/u$c;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:10:57.964 765-765/? W/zygote64: Method La/l/d/n;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.b is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.e is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.g is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.h is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/f0/d;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:10:57.965 765-765/? W/zygote64: Method Lb/c/a/a/z/e;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.g is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.h is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.i is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.j is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.m is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.o is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.p is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.s is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/f/k/c;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/f/k/c;.setTintList is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:10:57.975 765-765/? I/EdXposed-Bridge:   Loading class com.modosa.unblockdarkmode.util.XModule
09-19 00:10:57.977 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/tk.navideju.darkthemefixer-n5QMTRQLRxmyDjunCSs9-Q==/base.apk
09-19 00:10:57.978 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:57.982 925-1080/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 44000 mC, weight[0] 2
09-19 00:10:57.983 925-1080/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:10:58.043 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:58.067 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:58.069 765-765/? I/EdXposed-Bridge:   Loading class tk.navideju.darkthemefixer.Main
09-19 00:10:58.089 765-765/? I/EdXposed-Bridge: [DarkThemeFixer] From zygote: true can read?: false
    Loading modules from /data/app/ru.uMcSebxc.QziYqbJtk-gLoMearDmswr_Yiwmy4c9g==/base.apk
09-19 00:10:58.090 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:58.143 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:58.208 765-765/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:58.212 765-765/? W/zygote64: Found duplicate classes, falling back to extracting from APK : /data/app/ru.uMcSebxc.QziYqbJtk-gLoMearDmswr_Yiwmy4c9g==/base.apk
    NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /data/app/ru.uMcSebxc.QziYqbJtk-gLoMearDmswr_Yiwmy4c9g==/base.apk and /system/framework/edxp.jar
09-19 00:10:58.243 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:58.312 765-765/? I/EdXposed-Bridge:   Loading class com.xposed.XSupport
09-19 00:10:58.313 765-765/? W/main: type=1400 audit(0.0:88): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:58.323 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:58.324 765-765/? D/SandHook: method <protected boolean com.android.org.conscrypt.OpenSSLSignature.engineVerify(byte[]) throws java.security.SignatureException> hook <replacement> success!
09-19 00:10:58.323 765-765/? W/main: type=1400 audit(0.0:90): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:58.332 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:58.332 765-765/? D/SandHook: method <public static boolean java.security.MessageDigest.isEqual(byte[],byte[])> hook <replacement> success!
09-19 00:10:58.330 765-765/? W/main: type=1400 audit(0.0:92): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:58.340 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:58.340 765-765/? D/SandHook: method <public final boolean java.security.Signature.verify(byte[]) throws java.security.SignatureException> hook <replacement> success!
09-19 00:10:58.340 765-765/? W/main: type=1400 audit(0.0:94): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:10:58.343 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:58.349 765-765/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:10:58.350 765-765/? D/SandHook: method <public final boolean java.security.Signature.verify(byte[],int,int) throws java.security.SignatureException> hook <replacement> success!
09-19 00:10:58.350 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/fi.veetipaananen.android.disableflagsecure-vph3x2wEvvnXRoJcUJAdmQ==/base.apk
09-19 00:10:58.351 765-765/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:10:58.356 765-765/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:10:58.357 765-765/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:10:58.357 765-765/? I/EdXposed-Bridge:   Loading class fi.veetipaananen.android.disableflagsecure.DisableFlagSecureModule
09-19 00:10:58.358 817-817/? I/MSM-irqbalance: Discovered a new IRQ: 36
    Discovered a new IRQ: 39
09-19 00:10:58.359 817-817/? I/MSM-irqbalance: Discovered a new IRQ: 119
    Discovered a new IRQ: 123
    Discovered a new IRQ: 128
    Discovered a new IRQ: 143
    Discovered a new IRQ: 144
    Discovered a new IRQ: 154
09-19 00:10:58.360 817-817/? E/MSM-irqbalance: WARNING: Cannot find matching virq for hwirq(22).
09-19 00:10:58.363 817-817/? E/MSM-irqbalance: WARNING: Cannot find matching virq for hwirq(446).
09-19 00:10:58.363 765-765/? D/Zygote: Forked child process 1841
09-19 00:10:58.363 765-765/? I/Zygote: System server process 1841 has been created
09-19 00:10:58.363 817-817/? E/MSM-irqbalance: WARNING: Cannot find matching virq for hwirq(455).
09-19 00:10:58.364 817-817/? E/MSM-irqbalance: WARNING: Cannot find matching virq for hwirq(456).
09-19 00:10:58.365 765-765/? I/Zygote: Accepting command socket connections
09-19 00:10:58.389 1841-1841/? I/system_server: The ClassLoaderContext is a special shared library.
09-19 00:10:58.426 1841-1841/? I/chatty: uid=1000 system_server identical 2 lines
09-19 00:10:58.438 1841-1841/? I/system_server: The ClassLoaderContext is a special shared library.
09-19 00:10:58.444 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:58.448 1841-1841/? I/system_server: The ClassLoaderContext is a special shared library.
09-19 00:10:58.465 1841-1841/? V/Riru: edxp: forkSystemServerPost
09-19 00:10:58.550 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:58.589 1841-1841/? I/SystemServer: InitBeforeStartServices
09-19 00:10:58.591 1841-1841/? I/SystemServer: Entered the Android system server!
09-19 00:10:58.650 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:58.654 926-944/? E//vendor/bin/adsprpcd: vendor/qcom/proprietary/commonsys-intf/adsprpc/src/apps_std_imp.c:745:Error 0x2: fopen failed for .//lowi//lowi_lp.conf. (No such file or directory)
09-19 00:10:58.738 1841-1841/? E/UsbAlsaJackDetectorJNI: Can't register UsbAlsaJackDetector native methods
09-19 00:10:58.742 1841-1841/system_process V/Riru: jniRegisterNativeMethods com/android/server/storage/AppFuseBridge
09-19 00:10:58.750 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:58.751 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.754 1841-1841/system_process D/SandHook: method <private void com.android.server.SystemServer.startBootstrapServices()> hook <replacement> success!
09-19 00:10:58.759 1841-1841/system_process D/SystemServerTiming: InitBeforeStartServices took to complete: 170ms
09-19 00:10:58.759 1841-1841/system_process I/SystemServer: StartServices
09-19 00:10:58.760 1841-1841/system_process I/Xposed: Load li.lingfeng.ltweaks.xposed.system.XposedTrustAgentWifi for android, with prefs []
09-19 00:10:58.767 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.768 1841-1841/system_process D/SandHook: method <public int com.android.server.pm.PackageManagerService.checkPermission(java.lang.String,java.lang.String,int)> hook <replacement> success!
09-19 00:10:58.770 1841-1841/system_process I/Xposed: Load li.lingfeng.ltweaks.xposed.system.XposedPreventWakeLock for android, with prefs []
09-19 00:10:58.771 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.773 1841-1841/system_process D/SandHook: method <final void com.android.server.am.ActivityManagerService.finishBooting()> hook <replacement> success!
09-19 00:10:58.773 1841-1841/system_process I/Xposed: Load li.lingfeng.ltweaks.xposed.system.XposedPreventExactAlarm for android, with prefs []
    Load li.lingfeng.ltweaks.xposed.system.XposedPreventForegroundService for android, with prefs []
    Load li.lingfeng.ltweaks.xposed.system.XposedTextActions for all packages (exclude 1), with prefs []
09-19 00:10:58.774 1841-1841/system_process I/Xposed: Load li.lingfeng.ltweaks.xposed.system.XposedPreventReceiver for android, with prefs []
    Load li.lingfeng.ltweaks.xposed.system.XposedShareFilter for android, with prefs []
09-19 00:10:58.776 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.778 1841-1841/system_process D/SandHook: method <private java.util.List com.android.server.pm.PackageManagerService.queryIntentActivitiesInternal(android.content.Intent,java.lang.String,int,int)> hook <replacement> success!
09-19 00:10:58.778 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.780 1841-1841/system_process D/SandHook: method <private java.util.List com.android.server.pm.PackageManagerService.queryIntentActivitiesInternal(android.content.Intent,java.lang.String,int,int,int,boolean,boolean)> hook <replacement> success!
09-19 00:10:58.781 1841-1841/system_process I/Xposed: Load li.lingfeng.ltweaks.xposed.system.XposedSetInactive for android, with prefs []
09-19 00:10:58.782 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:739] qti_file_open():Could not open device file. Errno 2 error msg=No such file or directory
09-19 00:10:58.783 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.785 1841-1841/system_process D/SandHook: method <public android.content.pm.ApplicationInfo com.android.server.pm.PackageManagerService.getApplicationInfo(java.lang.String,int,int)> hook <replacement> success!
09-19 00:10:58.787 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.789 1841-1841/system_process D/SandHook: method <public android.content.pm.PackageInfo com.android.server.pm.PackageManagerService.getPackageInfo(java.lang.String,int,int)> hook <replacement> success!
09-19 00:10:58.792 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.794 1841-1841/system_process D/SandHook: method <int com.android.server.am.ActivityManagerService.appRestrictedInBackgroundLocked(int,java.lang.String,int)> hook <replacement> success!
09-19 00:10:58.796 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.798 1841-1841/system_process D/SandHook: method <int com.android.server.am.ActivityManagerService.appServicesRestrictedInBackgroundLocked(int,java.lang.String,int)> hook <replacement> success!
09-19 00:10:58.800 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.801 1907-1907/? E/RTPServiceImpl: qpLogDiagInit <== result : 1; log_write_mutex is Initialized
    [IMS_AP_RTP]"RTP Daemon main entry : 3e9"
    [IMS_AP_RTP]"RTP Daemon bLogRTPMsgs 1, bLogRTPDataMsgs 2, bLogAdbMsgs 0"
09-19 00:10:58.801 1907-1907/? E/Diag_Lib: [IMS_AP_RTP]"qvp_rtp_task_init"
09-19 00:10:58.802 1907-1907/? E/RTPServiceImpl: [IMS_AP_RTP]"ims-rtp-daemon listen done"
09-19 00:10:58.802 1841-1841/system_process D/SandHook: method <int com.android.server.am.ActivityManagerService.getAppStartModeLocked(int,java.lang.String,int,int,boolean,boolean,boolean)> hook <replacement> success!
09-19 00:10:58.802 1907-1907/? E/RTPServiceImpl: [IMS_AP_RTP]"ims-rtp-daemon qmi_rtp_register_service >"
09-19 00:10:58.802 1907-1915/? E/Diag_Lib: DPL : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0 gIsDebugDataPathDisabled = 0
    [IMS_AP_RTP]"qvp_rtp_handle_signals call ret qpDplInitTaskInfo 1"
    [IMS_FATAL]| 1915 |qpNetSetReadFds - DataD IPC socket not available
09-19 00:10:58.803 1907-1915/? E/Diag_Lib: [IMS_FATAL]| 1915 |qpCheckSockEventsOnNetConnProfiles : pNetConnProfileArray NULL
09-19 00:10:58.803 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:10:58.803 1907-1907/? E/RTPServiceImpl: [IMS_AP_RTP]"ims-rtp-daemon qmi_rtp_register_service rc : 0"
09-19 00:10:58.803 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.803 1907-1907/? E/RTPServiceImpl: [IMS_AP_RTP]"ims-rtp-daemon qmi_rtp_register_service service_cookie.service_handle : 0x1"
09-19 00:10:58.803 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.803 1907-1907/? E/RTPServiceImpl: [IMS_AP_RTP]"HIDL Service is starting."
09-19 00:10:58.803 1907-1907/? E/Diag_Lib: bLogRTPMSgs =1,rtpdata=2,adblog=0
09-19 00:10:58.803 1907-1907/? E/RTPServiceImpl: [IMS_AP_RTP]"RTPService callback Registraton"
09-19 00:10:58.803 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.804 1907-1907/? I/ServiceManagement: Registered vendor.qti.imsrtpservice@1.0::IRTPService/imsrtpservice (start delay of 51ms)
09-19 00:10:58.804 1907-1916/? E/RTPServiceImpl: [IMS_AP_RTP]"ms-rtp-daemon ims_rtp_qmi_handler_thread_func >"
09-19 00:10:58.805 1841-1841/system_process D/SandHook: method <public void android.view.SurfaceView.setSecure(boolean)> hook <replacement> success!
09-19 00:10:58.806 1907-1907/? E/RTPServiceImpl: [IMS_AP_RTP]"[ION_RTP]Device open success"
09-19 00:10:58.806 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.808 1841-1841/system_process D/SandHook: method <com.android.server.pm.SharedUserSetting com.android.server.pm.Settings.addSharedUserLPw(java.lang.String,int,int,int)> hook <replacement> success!
09-19 00:10:58.809 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.811 1841-1841/system_process D/SandHook: method <public boolean android.content.ContextWrapper.bindService(android.content.Intent,int,java.util.concurrent.Executor,android.content.ServiceConnection)> hook <replacement> success!
09-19 00:10:58.811 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.813 1841-1841/system_process D/SandHook: method <public boolean android.content.ContextWrapper.bindService(android.content.Intent,android.content.ServiceConnection,int)> hook <replacement> success!
09-19 00:10:58.813 1907-1915/? E/Diag_Lib: [IMS_FATAL]| 1915 |qpCheckSockEventsOnNetConnProfiles : pNetConnProfileArray NULL
    [IMS_AP_RTP]"rtp_register :: active num_users 1 "
09-19 00:10:58.814 1907-1921/? E/QMI_FW: QMUXD: WARNING qmi_qmux_if_pwr_up_init failed! rc=-6
09-19 00:10:58.814 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.816 1841-1841/system_process D/SandHook: method <public android.content.Intent android.content.Intent.setPackage(java.lang.String)> hook <replacement> success!
09-19 00:10:58.817 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.820 1841-1841/system_process D/SandHook: method <public com.android.server.pm.PackageManagerService(android.content.Context,com.android.server.pm.Installer,boolean,boolean)> hook <replacement> success!
09-19 00:10:58.823 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.823 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.823 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.824 927-927/? E/QMI_FW: QMUXD: WARNING qmi_qmux_if_pwr_up_init failed! rc=-6
09-19 00:10:58.824 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.825 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.825 1841-1841/system_process D/SandHook: method <private android.content.pm.PackageParser$Package com.android.server.pm.PackageManagerService.scanPackageLI(java.io.File,int,int,long,android.os.UserHandle) throws com.android.server.pm.PackageManagerException> hook <replacement> success!
09-19 00:10:58.827 927-1927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.827 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.827 927-1927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.828 927-1927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.829 927-1927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:10:58.829 1841-1841/system_process D/SandHook: method <public boolean android.content.pm.PackageParser$SigningDetails.checkCapability(android.content.pm.PackageParser$SigningDetails,int)> hook <replacement> success!
09-19 00:10:58.829 927-1927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.829 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.829 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.829 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.830 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:10:58.831 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:10:58.831 1841-1841/system_process D/SandHook: method <public boolean android.content.pm.PackageParser$SigningDetails.checkCapability(java.lang.String,int)> hook <replacement> success!
09-19 00:10:58.831 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.832 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:58.832 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.832 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:10:58.833 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:58.833 1841-1841/system_process D/SandHook: method <public static int com.android.server.pm.PackageManagerServiceUtils.compareSignatures(android.content.pm.Signature[],android.content.pm.Signature[])> hook <replacement> success!
09-19 00:10:58.833 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:10:58.835 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:58.836 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.836 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.836 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.837 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:58.838 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.838 1841-1841/system_process D/SandHook: method <void com.android.server.pm.PackageManagerService.installStage(com.android.server.pm.PackageManagerService$ActiveInstallSession)> hook <replacement> success!
09-19 00:10:58.838 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.839 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.839 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.840 1841-1841/system_process D/SandHook: method <void com.android.server.pm.PackageManagerService.installStage(java.util.List) throws com.android.server.pm.PackageManagerException> hook <replacement> success!
09-19 00:10:58.841 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.844 1841-1841/system_process D/SandHook: method <private static void com.android.server.pm.PackageManagerService.checkDowngrade(android.content.pm.PackageParser$Package,android.content.pm.PackageInfoLite) throws com.android.server.pm.PackageManagerException> hook <replacement> success!
09-19 00:10:58.847 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.849 1841-1841/system_process D/SandHook: method <private android.content.pm.PackageInfo com.android.server.pm.PackageManagerService.generatePackageInfo(com.android.server.pm.PackageSetting,int,int)> hook <replacement> success!
09-19 00:10:58.851 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:58.851 1132-1629/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.851 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.851 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:58.852 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.853 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.853 1841-1841/system_process D/SandHook: method <public android.content.pm.ParceledListSlice com.android.server.pm.PackageManagerService.getInstalledApplications(int,int)> hook <replacement> success!
09-19 00:10:58.853 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.854 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.855 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.857 1841-1841/system_process D/SandHook: method <public android.content.pm.ParceledListSlice com.android.server.pm.PackageManagerService.getInstalledPackages(int,int)> hook <replacement> success!
09-19 00:10:58.859 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.860 1841-1841/system_process D/SandHook: method <protected android.app.ApplicationPackageManager(android.app.ContextImpl,android.content.pm.IPackageManager)> hook <replacement> success!
09-19 00:10:58.862 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.863 1841-1841/system_process D/SandHook: method <public android.content.pm.PackageInfo android.app.ApplicationPackageManager.getPackageInfo(android.content.pm.VersionedPackage,int) throws android.content.pm.PackageManager$NameNotFoundException> hook <replacement> success!
09-19 00:10:58.864 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.865 1841-1841/system_process D/SandHook: method <public android.content.pm.PackageInfo android.app.ApplicationPackageManager.getPackageInfo(java.lang.String,int) throws android.content.pm.PackageManager$NameNotFoundException> hook <replacement> success!
09-19 00:10:58.866 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.867 1841-1841/system_process D/SandHook: method <public android.content.pm.ApplicationInfo android.app.ApplicationPackageManager.getApplicationInfo(java.lang.String,int) throws android.content.pm.PackageManager$NameNotFoundException> hook <replacement> success!
09-19 00:10:58.868 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.870 1841-1841/system_process D/SandHook: method <public java.util.List android.app.ApplicationPackageManager.getInstalledApplications(int)> hook <replacement> success!
09-19 00:10:58.870 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.871 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:10:58.872 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.872 1841-1841/system_process D/SandHook: method <public java.util.List android.app.ApplicationPackageManager.getInstalledPackages(int)> hook <replacement> success!
09-19 00:10:58.873 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.874 1841-1841/system_process D/SandHook: method <public java.util.List android.app.ApplicationPackageManager.getPreferredPackages(int)> hook <replacement> success!
09-19 00:10:58.877 1132-1627/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.877 882-979/? I/QC-NETMGR-LIB: NetmgrNetdClientAddInterfaceToOemNetwork(): Looking for Netd service
    NetmgrNetdClientAddInterfaceToOemNetwork(): starting command
    addInterfaceToOemNetwork(): Attempting addInterfaceToOemNetwork
09-19 00:10:58.880 1841-1841/system_process E/EdXposed-Bridge: java.lang.NoSuchMethodError: android.app.WallpaperManager$Globals#getWallpaperColors(int,int)#exact
        at de.robv.android.xposed.XposedHelpers.findMethodExact(XposedHelpers.java:344)
        at de.robv.android.xposed.XposedHelpers.findAndHookMethod(XposedHelpers.java:185)
        at de.robv.android.xposed.XposedHelpers.findAndHookMethod(XposedHelpers.java:260)
        at xyz.joas.forcedarkmodeoreo.ForceDarkMode.handleLoadPackage(ForceDarkMode.java:102)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-19 00:10:58.880 882-979/? I/QC-NETMGR-LIB: NetmgrNetdClientAddInterfaceToOemNetwork(): completed command
09-19 00:10:58.880 1841-1841/system_process E/EdXposed-Bridge: java.lang.NullPointerException: Attempt to read from field 'int android.content.pm.ApplicationInfo.flags' on a null object reference
        at com.jy.xposed.web.core.Main.handleLoadPackage(Unknown Source:2)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-19 00:10:58.881 1841-1841/system_process E/EdXposed-Bridge: java.io.FileNotFoundException: /data/data/com.xloger.exlink.app/files/AppData: open failed: ENOENT (No such file or directory)
        at libcore.io.IoBridge.open(IoBridge.java:496)
        at java.io.FileInputStream.<init>(FileInputStream.java:159)
        at java.io.FileInputStream.<init>(FileInputStream.java:115)
        at com.xloger.exlink.app.c.c.b(Unknown Source:20)
        at com.xloger.exlink.app.c.b.a(Unknown Source:8)
        at com.xloger.exlink.app.HookMain.handleLoadPackage(Unknown Source:13)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
     Caused by: android.system.ErrnoException: open failed: ENOENT (No such file or directory)
        at libcore.io.Linux.open(Native Method)
        at libcore.io.ForwardingOs.open(ForwardingOs.java:167)
        at libcore.io.BlockGuardOs.open(BlockGuardOs.java:252)
        at libcore.io.IoBridge.open(IoBridge.java:482)
        at java.io.FileInputStream.<init>(FileInputStream.java:159) 
        at java.io.FileInputStream.<init>(FileInputStream.java:115) 
        at com.xloger.exlink.app.c.c.b(Unknown Source:20) 
        at com.xloger.exlink.app.c.b.a(Unknown Source:8) 
        at com.xloger.exlink.app.HookMain.handleLoadPackage(Unknown Source:13) 
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37) 
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61) 
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117) 
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36) 
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51) 
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357) 
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46) 
        at com.android.server.SystemServer.run(SystemServer.java:527) 
        at com.android.server.SystemServer.main(SystemServer.java:356) 
        at java.lang.reflect.Method.invoke(Native Method) 
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491) 
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918) 
09-19 00:10:58.881 1841-1841/system_process W/System.err: java.io.FileNotFoundException: /data/data/com.xloger.exlink.app/files/AppData: open failed: ENOENT (No such file or directory)
        at libcore.io.IoBridge.open(IoBridge.java:496)
        at java.io.FileInputStream.<init>(FileInputStream.java:159)
        at java.io.FileInputStream.<init>(FileInputStream.java:115)
        at com.xloger.exlink.app.c.c.b(Unknown Source:20)
        at com.xloger.exlink.app.c.b.a(Unknown Source:8)
        at com.xloger.exlink.app.HookMain.handleLoadPackage(Unknown Source:13)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
09-19 00:10:58.882 1841-1841/system_process W/System.err:     at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
    Caused by: android.system.ErrnoException: open failed: ENOENT (No such file or directory)
        at libcore.io.Linux.open(Native Method)
        at libcore.io.ForwardingOs.open(ForwardingOs.java:167)
        at libcore.io.BlockGuardOs.open(BlockGuardOs.java:252)
        at libcore.io.IoBridge.open(IoBridge.java:482)
    	... 17 more
09-19 00:10:58.882 1841-1841/system_process E/EdXposed-Bridge: java.lang.AbstractMethodError: abstract method "void de.robv.android.xposed.IXposedHookLoadPackage.handleLoadPackage(de.robv.android.xposed.callbacks.XC_LoadPackage$LoadPackageParam)"
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-19 00:10:58.883 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.884 1132-1627/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.884 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:58.885 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:58.885 1841-1841/system_process D/SandHook: method <public java.lang.String android.telephony.TelephonyManager.getImei()> hook <replacement> success!
09-19 00:10:58.885 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.885 882-979/? I/QC-NETMGR-LIB: NetmgrNetdClientGetNetworkHandle(): [network handle : 7700664333] [network type : LINK_LOCAL]
09-19 00:10:58.885 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.886 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:10:58.887 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.887 1841-1841/system_process D/SandHook: method <public java.lang.String android.telephony.TelephonyManager.getDeviceId()> hook <replacement> success!
09-19 00:10:58.887 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.887 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.887 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.888 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:10:58.889 1841-1841/system_process D/SandHook: method <public java.lang.String android.telephony.TelephonyManager.getImei(int)> hook <replacement> success!
09-19 00:10:58.889 1907-1915/? E/Diag_Lib: [IMS_AP_RTP]"qvp_rtp_sl_register_cb : app data = -559038737"
    qvp_rtp_media_init
09-19 00:10:58.890 1907-1915/? E/Diag_Lib: [IMS_AP_RTP]"qvp_rtp_notify_dpl_init_pvt : DPL initialized \r\n"
09-19 00:10:58.890 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.890 1907-1915/? E/Diag_Lib: DPL : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0 gIsDebugDataPathDisabled = 0
09-19 00:10:58.891 1841-1841/system_process D/SandHook: method <public java.lang.String android.telephony.TelephonyManager.getDeviceId(int)> hook <replacement> success!
09-19 00:10:58.893 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.894 1841-1841/system_process D/SandHook: method <public android.widget.TextView(android.content.Context)> hook <replacement> success!
09-19 00:10:58.895 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.896 1841-1841/system_process D/SandHook: method <public android.widget.TextView(android.content.Context,android.util.AttributeSet)> hook <replacement> success!
09-19 00:10:58.896 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.897 1841-1841/system_process D/SandHook: method <public android.widget.TextView(android.content.Context,android.util.AttributeSet,int)> hook <replacement> success!
09-19 00:10:58.898 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.899 1841-1841/system_process D/SandHook: method <public android.widget.TextView(android.content.Context,android.util.AttributeSet,int,int)> hook <replacement> success!
09-19 00:10:58.901 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.902 1841-1841/system_process D/SandHook: method <protected void android.widget.TextView.onFocusChanged(boolean,int,android.graphics.Rect)> hook <replacement> success!
09-19 00:10:58.903 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.905 1841-1841/system_process D/SandHook: method <public boolean android.widget.Editor$TextActionModeCallback.onCreateActionMode(android.view.ActionMode,android.view.Menu)> hook <replacement> success!
09-19 00:10:58.906 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.907 1841-1841/system_process D/SandHook: method <public boolean android.widget.Editor$TextActionModeCallback.onActionItemClicked(android.view.ActionMode,android.view.MenuItem)> hook <replacement> success!
09-19 00:10:58.907 1841-1841/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "android.content.pm.PackageParser.Package" on path: DexPathList[[zip file "/system/framework/org.lineageos.platform.jar", zip file "/system/framework/services.jar", zip file "/system/framework/ethernet-service.jar", zip file "/system/framework/wifi-service.jar", zip file "/system/framework/com.android.location.provider.jar"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at ai.lazero.lazero.HookTest_v0.handleLoadPackage(HookTest_v0.java:35)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-19 00:10:58.909 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.911 1841-1841/system_process D/SandHook: method <com.android.server.am.ProcessRecord(com.android.server.am.ActivityManagerService,android.content.pm.ApplicationInfo,java.lang.String,int)> hook <replacement> success!
09-19 00:10:58.911 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.913 1841-1841/system_process D/SandHook: method <boolean com.android.server.wm.ActivityStackSupervisor.realStartActivityLocked(com.android.server.wm.ActivityRecord,com.android.server.wm.WindowProcessController,boolean,boolean) throws android.os.RemoteException> hook <replacement> success!
09-19 00:10:58.914 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.916 1841-1841/system_process D/SandHook: method <com.android.server.wm.ActivityRecord(com.android.server.wm.ActivityTaskManagerService,com.android.server.wm.WindowProcessController,int,int,java.lang.String,android.content.Intent,java.lang.String,android.content.pm.ActivityInfo,android.content.res.Configuration,com.android.server.wm.ActivityRecord,java.lang.String,int,boolean,boolean,com.android.server.wm.ActivityStackSupervisor,android.app.ActivityOptions,com.android.server.wm.ActivityRecord)> hook <replacement> success!
09-19 00:10:58.917 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.918 1841-1841/system_process D/SandHook: method <boolean com.android.server.wm.ActivityTaskManagerService.isGetTasksAllowed(java.lang.String,int,int)> hook <replacement> success!
09-19 00:10:58.920 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.922 1841-1841/system_process D/SandHook: method <public void com.android.server.pm.PackageManagerService.systemReady()> hook <replacement> success!
09-19 00:10:58.922 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.924 1841-1841/system_process D/SandHook: method <com.android.server.pm.permission.PermissionManagerService(android.content.Context,java.lang.Object)> hook <replacement> success!
09-19 00:10:58.925 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.927 1841-1841/system_process D/SandHook: method <private void com.android.server.pm.permission.PermissionManagerService.restorePermissionState(android.content.pm.PackageParser$Package,boolean,java.lang.String,com.android.server.pm.permission.PermissionManagerServiceInternal$PermissionCallback)> hook <replacement> success!
09-19 00:10:58.928 1841-1841/system_process W/system_server: Unsupported class loader
09-19 00:10:58.929 1841-1841/system_process D/SandHook: method <void com.android.server.notification.NotificationManagerService.enqueueNotificationInternal(java.lang.String,java.lang.String,int,int,java.lang.String,int,android.app.Notification,int)> hook <replacement> success!
09-19 00:10:58.933 1841-1841/system_process E/EdXposed-Bridge: de.robv.android.xposed.XposedHelpers$ClassNotFoundError: java.lang.ClassNotFoundException: com.android.internal.policy.impl.GlobalActions
        at de.robv.android.xposed.XposedHelpers.findClass(XposedHelpers.java:71)
        at ma.wanam.wanamkit.XGlobalActions.doHook(XGlobalActions.java:108)
        at ma.wanam.wanamkit.Xposed.handleLoadPackage(Xposed.java:58)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
     Caused by: java.lang.ClassNotFoundException: com.android.internal.policy.impl.GlobalActions
        at java.lang.Class.classForName(Native Method)
        at java.lang.Class.forName(Class.java:454)
        at external.org.apache.commons.lang3.ClassUtils.getClass(ClassUtils.java:823)
        at de.robv.android.xposed.XposedHelpers.findClass(XposedHelpers.java:69)
        at ma.wanam.wanamkit.XGlobalActions.doHook(XGlobalActions.java:108) 
        at ma.wanam.wanamkit.Xposed.handleLoadPackage(Xposed.java:58) 
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37) 
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61) 
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117) 
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36) 
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51) 
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357) 
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46) 
        at com.android.server.SystemServer.run(SystemServer.java:527) 
        at com.android.server.SystemServer.main(SystemServer.java:356) 
        at java.lang.reflect.Method.invoke(Native Method) 
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491) 
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918) 
     Caused by: java.lang.ClassNotFoundException: Didn't find class "com.android.internal.policy.impl.GlobalActions" on path: DexPathList[[zip file "/system/framework/org.lineageos.platform.jar", zip file "/system/framework/services.jar", zip file "/system/framework/ethernet-service.jar", zip file "/system/framework/wifi-service.jar", zip file "/system/framework/com.android.location.provider.jar"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at java.lang.Class.classForName(Native Method) 
        at java.lang.Class.forName(Class.java:454) 
        at external.org.apache.commons.lang3.ClassUtils.getClass(ClassUtils.java:823) 
        at de.robv.android.xposed.XposedHelpers.findClass(XposedHelpers.java:69) 
        at ma.wanam.wanamkit.XGlobalActions.doHook(XGlobalActions.java:108) 
        at ma.wanam.wanamkit.Xposed.handleLoadPackage(Xposed.java:58) 
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37) 
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61) 
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117) 
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36) 
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51) 
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357) 
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46) 
        at com.android.server.SystemServer.run(SystemServer.java:527) 
        at com.android.server.SystemServer.main(SystemServer.java:356) 
        at java.lang.reflect.Method.invoke(Native Method) 
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491) 
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918) 
09-19 00:10:58.938 1841-1841/system_process I/SystemServer: StartWatchdog
09-19 00:10:58.943 1841-1841/system_process D/SystemServerTiming: StartWatchdog took to complete: 5ms
09-19 00:10:58.943 1841-1841/system_process I/SystemServer: Reading configuration...
    ReadingSystemConfig
09-19 00:10:58.943 1841-1841/system_process D/SystemServerTiming: ReadingSystemConfig took to complete: 0ms
09-19 00:10:58.943 1841-1841/system_process I/SystemServer: StartInstaller
09-19 00:10:58.943 1841-1841/system_process I/SystemServiceManager: Starting com.android.server.pm.Installer
09-19 00:10:58.944 1841-1947/system_process D/SystemServerInitThreadPool: Started executing ReadingSystemConfig
09-19 00:10:58.946 956-1022/? D/installd: Found quota mount /dev/block/bootdevice/by-name/userdata at /data
09-19 00:10:58.955 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:58.960 925-1074/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 44000 mC, weight[0] 2
09-19 00:10:58.961 925-1074/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:10:58.964 1091-1137/? I/cnss-daemon: WLPS service connected
09-19 00:10:58.973 1841-1841/system_process D/SystemServerTiming: StartInstaller took to complete: 30ms
09-19 00:10:58.973 1841-1841/system_process I/SystemServer: DeviceIdentifiersPolicyService
09-19 00:10:58.973 1841-1841/system_process I/SystemServiceManager: Starting com.android.server.os.DeviceIdentifiersPolicyService
09-19 00:10:58.974 1841-1841/system_process D/SystemServerTiming: DeviceIdentifiersPolicyService took to complete: 1ms
09-19 00:10:58.974 1841-1841/system_process I/SystemServer: UriGrantsManagerService
09-19 00:10:58.974 1841-1841/system_process I/SystemServiceManager: Starting com.android.server.uri.UriGrantsManagerService$Lifecycle
09-19 00:10:58.975 1841-1841/system_process D/SystemServerTiming: UriGrantsManagerService took to complete: 1ms
09-19 00:10:58.975 1841-1841/system_process I/SystemServer: StartActivityManager
09-19 00:10:58.975 1841-1841/system_process I/SystemServiceManager: Starting com.android.server.wm.ActivityTaskManagerService$Lifecycle
09-19 00:10:59.001 1841-1841/system_process I/SystemServiceManager: Starting com.android.server.am.ActivityManagerService$Lifecycle
09-19 00:10:59.008 1841-1841/system_process I/ActivityManager: Memory class: 192
09-19 00:10:59.013 1841-1841/system_process E/libpsi: No kernel psi monitor support (errno=2)
09-19 00:10:59.013 1841-1841/system_process E/LowMemDetector: Failed to register psi trigger
09-19 00:10:59.020 1841-1841/system_process D/BatteryStatsImpl: Reading daily items from /data/system/batterystats-daily.xml
09-19 00:10:59.030 1841-1947/system_process W/SystemConfig: No directory /product_services/etc/sysconfig, skipping
    No directory /product_services/etc/permissions, skipping
09-19 00:10:59.030 1841-1947/system_process D/SystemServerInitThreadPool: Finished executing ReadingSystemConfig
09-19 00:10:59.046 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.power.stats@1.0::IPowerStats/default in either framework or device manifest.
09-19 00:10:59.048 1841-1959/system_process I/BatteryStatsService: Using power HAL
09-19 00:10:59.048 1841-1959/system_process E/BatteryStatsService: Unable to load Power.Stats.HAL. Setting rail availability to false
09-19 00:10:59.048 1841-1959/system_process E/BluetoothAdapter: Bluetooth binder is null
09-19 00:10:59.049 1841-1959/system_process E/BatteryExternalStatsWorker: no controller energy info supplied for telephony
09-19 00:10:59.052 1841-1959/system_process I/KernelCpuUidFreqTimeReader: mPerClusterTimesAvailable=true
09-19 00:10:59.055 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:59.066 1841-1959/system_process I/PowerManagerService-JNI: Loaded power HAL 1.0 service
    Loaded power HAL 1.1 service
09-19 00:10:59.101 1841-1841/system_process I/IntentFirewall: Read new rules (A:0 B:0 S:0)
09-19 00:10:59.108 1841-1841/system_process E/libprocessgroup: Failed to open /dev/memcg/apps: Permission denied
09-19 00:10:59.109 1841-1841/system_process D/AppOps: AppOpsService published
09-19 00:10:59.110 1841-1841/system_process D/SystemServerTiming: StartActivityManager took to complete: 135ms
09-19 00:10:59.110 1841-1841/system_process I/SystemServer: StartPowerManager
09-19 00:10:59.110 1841-1841/system_process I/SystemServiceManager: Starting com.android.server.power.PowerManagerService
09-19 00:10:59.119 791-791/? E/QTI PowerHAL: Failed to acquire lock for hint_id: 1041.
09-19 00:10:59.121 1841-1841/system_process D/SystemServerTiming: StartPowerManager took to complete: 11ms
09-19 00:10:59.121 1841-1841/system_process I/SystemServer: StartThermalManager
09-19 00:10:59.121 1841-1841/system_process I/SystemServiceManager: Starting com.android.server.power.ThermalManagerService
09-19 00:10:59.121 1841-1841/system_process D/SystemServerTiming: StartThermalManager took to complete: 1ms
09-19 00:10:59.122 1841-1841/system_process I/SystemServer: InitPowerManagement
09-19 00:10:59.122 1841-1841/system_process D/SystemServerTiming: InitPowerManagement took to complete: 0ms
09-19 00:10:59.122 1841-1841/system_process I/SystemServer: StartRecoverySystemService
09-19 00:10:59.122 1841-1841/system_process I/SystemServiceManager: Starting com.android.server.RecoverySystemService
09-19 00:10:59.124 1841-1841/system_process D/SystemServerTiming: StartRecoverySystemService took to complete: 3ms
09-19 00:10:59.125 1841-1841/system_process V/RescueParty: Disabled because of active USB connection
09-19 00:10:59.125 1841-1841/system_process I/SystemServer: StartLightsService
09-19 00:10:59.125 1841-1841/system_process I/SystemServiceManager: Starting com.android.server.lights.LightsService
09-19 00:10:59.127 1841-1841/system_process D/SystemServerTiming: StartLightsService took to complete: 2ms
09-19 00:10:59.127 1841-1841/system_process I/SystemServer: StartSidekickService
09-19 00:10:59.127 1841-1841/system_process D/SystemServerTiming: StartSidekickService took to complete: 0ms
09-19 00:10:59.127 1841-1841/system_process I/SystemServer: StartDisplayManager
09-19 00:10:59.127 1841-1841/system_process I/SystemServiceManager: Starting com.android.server.display.DisplayManagerService
09-19 00:10:59.133 1841-1841/system_process D/SystemServerTiming: StartDisplayManager took to complete: 6ms
09-19 00:10:59.133 1841-1841/system_process I/SystemServer: WaitForDisplay
09-19 00:10:59.133 1841-1841/system_process I/SystemServiceManager: Starting phase 100
09-19 00:10:59.135 784-784/? I/SDM: HWCDisplay::GetColorModeCount: Supported color mode count = 0
09-19 00:10:59.142 1841-1943/system_process I/DisplayManagerService: Display device added: DisplayDeviceInfo{"Built-in Screen": uniqueId="local:0", 1080 x 2160, modeId 1, defaultModeId 1, supportedModes [{id=1, width=1080, height=2160, fps=60.000004}], colorMode 0, supportedColorModes [0], HdrCapabilities android.view.Display$HdrCapabilities@40f16308, density 400, 403.411 x 403.411 dpi, appVsyncOff 2000000, presDeadline 11666666, touch INTERNAL, rotation 0, type BUILT_IN, address {port=0}, state UNKNOWN, FLAG_DEFAULT_DISPLAY, FLAG_ROTATES_WITH_CONTENT, FLAG_SECURE, FLAG_SUPPORTS_PROTECTED_BUFFERS}
09-19 00:10:59.143 832-832/? D/SurfaceFlinger: Setting power mode 2 on display 0
09-19 00:10:59.146 1841-1943/system_process I/DisplayManagerService: Display device changed state: "Built-in Screen", ON
09-19 00:10:59.147 1841-1841/system_process D/SystemServerTiming: WaitForDisplay took to complete: 14ms
09-19 00:10:59.147 1841-1841/system_process I/SystemServer: StartPackageManagerService
09-19 00:10:59.147 1841-1841/system_process I/Watchdog: Pausing HandlerChecker: main thread for reason: packagemanagermain. Pause count: 1
09-19 00:10:59.156 971-1125/? W/ServiceManager: Service package_native didn't start. Returning NULL
09-19 00:10:59.156 971-1125/? E/storaged: getService package_native failed
09-19 00:10:59.159 971-1125/? I/storaged: storaged: Start
09-19 00:10:59.161 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:59.169 1841-1841/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.system
    PM has Hooked!
09-19 00:10:59.171 1841-1841/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
    Permission UID method has Hooked! android.uid.phone
    Permission UID method has Hooked! android.uid.log
    Permission UID method has Hooked! android.uid.nfc
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! android.uid.shell
    Permission UID method has Hooked! android.uid.se
    Permission UID method has Hooked! android.uid.networkstack
09-19 00:10:59.175 1841-1841/system_process D/SELinuxMMAC: Using policy file /system/etc/selinux/plat_mac_permissions.xml
09-19 00:10:59.176 1841-1841/system_process D/SELinuxMMAC: Using policy file /vendor/etc/selinux/vendor_mac_permissions.xml
09-19 00:10:59.179 1841-1841/system_process D/FallbackCategoryProvider: Found 1 fallback categories
09-19 00:10:59.262 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:59.263 1841-1841/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.media
09-19 00:10:59.264 1841-1841/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.networkstack
    Permission UID method has Hooked! android.uid.systemui
09-19 00:10:59.265 1841-1841/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.nfc
09-19 00:10:59.266 1841-1841/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.se
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! ai.lazero.lazero
09-19 00:10:59.266 1841-1841/system_process E/PackageManager: Adding duplicate shared user, keeping first: ai.lazero.lazero
09-19 00:10:59.268 1841-1841/system_process E/PackageManager: Occurred while parsing settings at START_TAG <shared-user name='ai.lazero.lazero' userId='10171'>@7454:57 in java.io.InputStreamReader@d4ff718
09-19 00:10:59.269 1841-1841/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.shared
    Permission UID method has Hooked! android.uid.system
    PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-19 00:10:59.270 1841-1841/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.phone
09-19 00:10:59.271 1841-1841/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.shell
09-19 00:10:59.272 1841-1841/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.calendar
    Permission UID method has Hooked! com.termux
09-19 00:10:59.273 1841-1841/system_process I/EdXposed-Bridge: Permission UID method has Hooked! com.android.emergency.uid
09-19 00:10:59.277 1841-1841/system_process E/PackageManager: Bad package setting: package ai.lazero.lazero has shared uid 10171 that is not defined
09-19 00:10:59.279 1841-1841/system_process W/PackageManager: No package known for stopped package ai.lazero.lazero
09-19 00:10:59.313 1841-1841/system_process D/PackageManager: Keeping known cache e923b92d3c96d64a19be89d4f4846aad93752eb7
09-19 00:10:59.363 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:59.416 1841-1841/system_process I/System.out: Update settings xposed
09-19 00:10:59.417 1841-1841/system_process W/System.err: java.io.FileNotFoundException: /data/local/tmp/xposed: open failed: EACCES (Permission denied)
        at libcore.io.IoBridge.open(IoBridge.java:496)
        at java.io.RandomAccessFile.<init>(RandomAccessFile.java:289)
        at com.chelpus.ˆ.ˆ(Utils.java:7086)
        at com.chelpus.ˆ.ᐧ(Utils.java:10063)
        at com.xposed.XSupport.ʻ(XSupport.java:1249)
        at com.xposed.XSupport$9.beforeHookedMethod(XSupport.java:466)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_2nkqvsp0pjs3mavtk6arhdmkc0.hook(Unknown Source:55)
        at com.android.server.pm.PackageManagerService.applyPolicy(PackageManagerService.java:11795)
09-19 00:10:59.418 1841-1841/system_process W/System.err:     at com.android.server.pm.PackageManagerService.scanPackageNewLI(PackageManagerService.java:11071)
        at com.android.server.pm.PackageManagerService.addForInitLI(PackageManagerService.java:9609)
        at com.android.server.pm.PackageManagerService.scanPackageChildLI(PackageManagerService.java:9331)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9154)
        at com.android.server.pm.PackageManagerService.scanDirTracedLI(PackageManagerService.java:9108)
        at com.android.server.pm.PackageManagerService.<init>(PackageManagerService.java:2671)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_2ptsr6rbsnc7sqphenvn7nghm3.hook(Unknown Source:70)
        at com.android.server.pm.PackageManagerService.main(PackageManagerService.java:2318)
        at com.android.server.SystemServer.startBootstrapServices(SystemServer.java:753)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
    Caused by: android.system.ErrnoException: open failed: EACCES (Permission denied)
        at libcore.io.Linux.open(Native Method)
        at libcore.io.ForwardingOs.open(ForwardingOs.java:167)
        at libcore.io.BlockGuardOs.open(BlockGuardOs.java:252)
        at libcore.io.IoBridge.open(IoBridge.java:482)
    	... 30 more
09-19 00:10:59.413 1841-1841/system_process W/system_server: type=1400 audit(0.0:96): avc: denied { open } for path="/data/local/tmp/xposed" dev="sda17" ino=7077893 scontext=u:r:system_server:s0 tcontext=u:object_r:shell_data_file:s0 tclass=file permissive=0
09-19 00:10:59.418 1841-1841/system_process W/System.err: org.json.JSONException: Value ���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� of type java.lang.String cannot be converted to JSONObject
09-19 00:10:59.419 1841-1841/system_process W/System.err:     at org.json.JSON.typeMismatch(JSON.java:112)
        at org.json.JSONObject.<init>(JSONObject.java:168)
        at org.json.JSONObject.<init>(JSONObject.java:181)
        at com.chelpus.ˆ.ᐧ(Utils.java:10063)
        at com.xposed.XSupport.ʻ(XSupport.java:1249)
        at com.xposed.XSupport$9.beforeHookedMethod(XSupport.java:466)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_2nkqvsp0pjs3mavtk6arhdmkc0.hook(Unknown Source:55)
        at com.android.server.pm.PackageManagerService.applyPolicy(PackageManagerService.java:11795)
        at com.android.server.pm.PackageManagerService.scanPackageNewLI(PackageManagerService.java:11071)
        at com.android.server.pm.PackageManagerService.addForInitLI(PackageManagerService.java:9609)
        at com.android.server.pm.PackageManagerService.scanPackageChildLI(PackageManagerService.java:9331)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9154)
        at com.android.server.pm.PackageManagerService.scanDirTracedLI(PackageManagerService.java:9108)
        at com.android.server.pm.PackageManagerService.<init>(PackageManagerService.java:2671)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_2ptsr6rbsnc7sqphenvn7nghm3.hook(Unknown Source:70)
        at com.android.server.pm.PackageManagerService.main(PackageManagerService.java:2318)
        at com.android.server.SystemServer.startBootstrapServices(SystemServer.java:753)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-19 00:10:59.463 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:59.479 1841-1841/system_process D/PackageManager: No files in app dir /product_services/overlay
    No files in app dir /odm/overlay
    No files in app dir /oem/overlay
09-19 00:10:59.483 1841-1841/system_process W/PackageManager: Failed to parse /system/framework/oat: Missing base APK in /system/framework/oat
    Failed to parse /system/framework/arm64: Missing base APK in /system/framework/arm64
09-19 00:10:59.485 1841-1841/system_process W/PackageManager: Failed to parse /system/framework/arm: Missing base APK in /system/framework/arm
09-19 00:10:59.559 1841-1841/system_process W/PackageManager: Package ai.lazero.lazero shared user changed from <nothing> to ai.lazero.lazero; replacing with new
09-19 00:10:59.563 1841-1841/system_process I/System.out: SetPmContext
09-19 00:10:59.563 1841-1841/system_process I/Watchdog: Resuming HandlerChecker: main thread for reason: packagemanagermain. Pause count: 0
09-19 00:10:59.563 1841-1841/system_process E/System: ******************************************
09-19 00:10:59.564 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:59.564 1841-1841/system_process E/System: ************ Failure starting system services
    java.lang.NullPointerException: Attempt to read from field 'long com.android.server.pm.PackageSettingBase.versionCode' on a null object reference
        at com.android.server.pm.PackageManagerService.addForInitLI(PackageManagerService.java:9538)
        at com.android.server.pm.PackageManagerService.scanPackageChildLI(PackageManagerService.java:9331)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9154)
        at com.android.server.pm.PackageManagerService.scanDirTracedLI(PackageManagerService.java:9108)
        at com.android.server.pm.PackageManagerService.<init>(PackageManagerService.java:2725)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_2ptsr6rbsnc7sqphenvn7nghm3.hook(Unknown Source:70)
        at com.android.server.pm.PackageManagerService.main(PackageManagerService.java:2318)
        at com.android.server.SystemServer.startBootstrapServices(SystemServer.java:753)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
    	Suppressed: java.lang.IllegalStateException: Not all tasks finished before calling close: [java.util.concurrent.FutureTask@94f2a1f, java.util.concurrent.FutureTask@884916c, java.util.concurrent.FutureTask@a490335, java.util.concurrent.FutureTask@eb3ca, java.util.concurrent.FutureTask@946493b, java.util.concurrent.FutureTask@bdf5858, java.util.concurrent.FutureTask@7139db1, java.util.concurrent.FutureTask@54c4296, java.util.concurrent.FutureTask@3c63e17, java.util.concurrent.FutureTask@f1da204]
        at com.android.server.pm.ParallelPackageParser.close(ParallelPackageParser.java:145)
        at com.android.server.pm.PackageManagerService.$closeResource(PackageManagerService.java:3561)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9178)
        		... 17 more
09-19 00:10:59.564 1841-1841/? D/SystemServerTiming: StartPackageManagerService took to complete: 417ms
09-19 00:10:59.564 1841-1841/? E/Zygote: System zygote died with exception
    java.lang.NullPointerException: Attempt to read from field 'long com.android.server.pm.PackageSettingBase.versionCode' on a null object reference
        at com.android.server.pm.PackageManagerService.addForInitLI(PackageManagerService.java:9538)
        at com.android.server.pm.PackageManagerService.scanPackageChildLI(PackageManagerService.java:9331)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9154)
        at com.android.server.pm.PackageManagerService.scanDirTracedLI(PackageManagerService.java:9108)
        at com.android.server.pm.PackageManagerService.<init>(PackageManagerService.java:2725)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_2ptsr6rbsnc7sqphenvn7nghm3.hook(Unknown Source:70)
        at com.android.server.pm.PackageManagerService.main(PackageManagerService.java:2318)
        at com.android.server.SystemServer.startBootstrapServices(SystemServer.java:753)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
    	Suppressed: java.lang.IllegalStateException: Not all tasks finished before calling close: [java.util.concurrent.FutureTask@94f2a1f, java.util.concurrent.FutureTask@884916c, java.util.concurrent.FutureTask@a490335, java.util.concurrent.FutureTask@eb3ca, java.util.concurrent.FutureTask@946493b, java.util.concurrent.FutureTask@bdf5858, java.util.concurrent.FutureTask@7139db1, java.util.concurrent.FutureTask@54c4296, java.util.concurrent.FutureTask@3c63e17, java.util.concurrent.FutureTask@f1da204]
        at com.android.server.pm.ParallelPackageParser.close(ParallelPackageParser.java:145)
        at com.android.server.pm.PackageManagerService.$closeResource(PackageManagerService.java:3561)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9178)
        		... 17 more
09-19 00:10:59.564 1841-1841/? D/AndroidRuntime: Shutting down VM
    
    
    --------- beginning of crash
09-19 00:10:59.565 1841-1841/? E/AndroidRuntime: *** FATAL EXCEPTION IN SYSTEM PROCESS: main
    java.lang.NullPointerException: Attempt to read from field 'long com.android.server.pm.PackageSettingBase.versionCode' on a null object reference
        at com.android.server.pm.PackageManagerService.addForInitLI(PackageManagerService.java:9538)
        at com.android.server.pm.PackageManagerService.scanPackageChildLI(PackageManagerService.java:9331)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9154)
        at com.android.server.pm.PackageManagerService.scanDirTracedLI(PackageManagerService.java:9108)
        at com.android.server.pm.PackageManagerService.<init>(PackageManagerService.java:2725)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_2ptsr6rbsnc7sqphenvn7nghm3.hook(Unknown Source:70)
        at com.android.server.pm.PackageManagerService.main(PackageManagerService.java:2318)
        at com.android.server.SystemServer.startBootstrapServices(SystemServer.java:753)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
    	Suppressed: java.lang.IllegalStateException: Not all tasks finished before calling close: [java.util.concurrent.FutureTask@94f2a1f, java.util.concurrent.FutureTask@884916c, java.util.concurrent.FutureTask@a490335, java.util.concurrent.FutureTask@eb3ca, java.util.concurrent.FutureTask@946493b, java.util.concurrent.FutureTask@bdf5858, java.util.concurrent.FutureTask@7139db1, java.util.concurrent.FutureTask@54c4296, java.util.concurrent.FutureTask@3c63e17, java.util.concurrent.FutureTask@f1da204]
        at com.android.server.pm.ParallelPackageParser.close(ParallelPackageParser.java:145)
        at com.android.server.pm.PackageManagerService.$closeResource(PackageManagerService.java:3561)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9178)
        		... 17 more
09-19 00:10:59.566 1841-1841/? E/AndroidRuntime: Error reporting crash
    java.lang.NullPointerException: Attempt to invoke interface method 'void android.app.IActivityManager.handleApplicationCrash(android.os.IBinder, android.app.ApplicationErrorReport$ParcelableCrashInfo)' on a null object reference
        at com.android.internal.os.RuntimeInit$KillApplicationHandler.uncaughtException(RuntimeInit.java:147)
        at java.lang.ThreadGroup.uncaughtException(ThreadGroup.java:1073)
        at java.lang.ThreadGroup.uncaughtException(ThreadGroup.java:1068)
        at java.lang.Thread.dispatchUncaughtException(Thread.java:2187)
09-19 00:10:59.566 1841-1841/? I/Process: Sending signal. PID: 1841 SIG: 9
09-19 00:10:59.590 584-584/? I/ServiceManager: service 'batterystats' died
09-19 00:10:59.591 584-584/? I/ServiceManager: service 'appops' died
    service 'power' died
    service 'thermalservice' died
    service 'recovery' died
    service 'display' died
    service 'device_identifiers' died
    service 'uri_grants' died
    service 'activity_task' died
09-19 00:10:59.594 765-765/? I/Zygote: Process 1841 exited due to signal 9 (Killed)
09-19 00:10:59.594 765-765/? E/Zygote: Exit zygote because system server (pid 1841) has terminated
09-19 00:10:59.627 584-584/? I/ServiceManager: service 'media.audio_flinger' died
09-19 00:10:59.627 772-844/? I/r_submix: adev_close()
09-19 00:10:59.627 772-1366/? D/audio_hw_primary: adev_close_output_stream: enter:stream_handle(low-latency-playback)
    out_standby: enter: stream (0xe8853000) usecase(1: low-latency-playback)
    out_standby: exit
09-19 00:10:59.628 772-1366/? D/audio_hw_primary: adev_close_output_stream: enter:stream_handle(deep-buffer-playback)
    out_standby: enter: stream (0xe88c6000) usecase(0: deep-buffer-playback)
    out_standby: exit
    adev_close_output_stream: enter:stream_handle(afe-proxy-playback)
    out_standby: enter: stream (0xe8855800) usecase(51: afe-proxy-playback)
    out_standby: exit
09-19 00:10:59.628 772-1366/? I/soundtrigger: audio_extn_sound_trigger_deinit: Enter
09-19 00:10:59.640 772-1366/? D/ACDB-LOADER: ACDB -> deallocate_ADIE
09-19 00:10:59.640 772-1366/? D/ACDB-LOADER: ACDB -> deallocate_ACDB
    [ACPH]->acph_deinit->is called
    g_pCmdTbl is not NULL, g_pCmdTbl->pNodeHead is not NULL
    Node1 is not empty, address[0xe7a85520]
    Node2 is not empty, address[0xe7a85440]
    g_pCmdTbl->pNodeTail is not NULL, address[0xe7a85440]
    Free first node, pNodeHead[0xe7a85440],pCur[0xe7a85520],pNext[0xe7a85440]
    [ACPH]->Online service Unregistered with ACPH
09-19 00:10:59.648 584-584/? I/ServiceManager: service 'media.player' died
    service 'media.resource_manager' died
09-19 00:10:59.649 772-1366/? D/ACDB-LOADER: ACDB -> deallocate_ACDB done!
09-19 00:10:59.649 772-1366/? D/ultrasound: us_deinit: enter
    us_deinit: exit
09-19 00:10:59.657 882-1736/? E/QC-NETMGR-LIB: serviceDied(): Netd service died
09-19 00:10:59.657 584-584/? I/ServiceManager: service 'dnsresolver' died
    service 'netd' died
09-19 00:10:59.662 584-584/? I/ServiceManager: service 'wificond' died
09-19 00:10:59.664 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:59.772 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:59.782 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:739] qti_file_open():Could not open device file. Errno 2 error msg=No such file or directory
09-19 00:10:59.785 1988-1988/? I/wificond: wificond is starting up...
09-19 00:10:59.814 1989-1989/? D/vndksupport: Loading /vendor/lib/hw/android.hardware.audio@5.0-impl.so from current namespace instead of sphal namespace.
09-19 00:10:59.820 1989-1989/? I/ServiceManagement: Registered android.hardware.audio@5.0::IDevicesFactory/default (start delay of 58ms)
    Removing namespace from process name android.hardware.audio@2.0-service to audio@2.0-service.
09-19 00:10:59.820 1989-1989/? I/audiohalservice: Registration complete for android.hardware.audio@5.0::IDevicesFactory/default.
09-19 00:10:59.820 1987-1987/? I/netdClient: Skipping libnetd_client init since *we* are netd
09-19 00:10:59.821 1989-1989/? D/vndksupport: Loading /vendor/lib/hw/android.hardware.audio.effect@5.0-impl.so from current namespace instead of sphal namespace.
09-19 00:10:59.822 1987-1987/? I/netd: netd 1.0 starting
09-19 00:10:59.825 1987-1987/? I/Netd: Loaded resolver library from /apex/com.android.resolv/lib64/libnetd_resolv.so
09-19 00:10:59.825 1987-1987/? D/TetherController: Setting IP forward enable = 0
09-19 00:10:59.827 1987-1987/? D/FirewallController: Could not read /proc/self/uid_map, max uid defaulting to 4294967294
09-19 00:10:59.830 1989-1989/? I/ServiceManagement: Registered android.hardware.audio.effect@5.0::IEffectsFactory/default (start delay of 68ms)
09-19 00:10:59.830 1989-1989/? I/audiohalservice: Registration complete for android.hardware.audio.effect@5.0::IEffectsFactory/default.
09-19 00:10:59.830 1989-1989/? D/vndksupport: Loading /vendor/lib/hw/android.hardware.soundtrigger@2.2-impl.so from current namespace instead of sphal namespace.
09-19 00:10:59.833 1989-1989/? D/vndksupport: Loading /vendor/lib/hw/sound_trigger.primary.msm8998.so from current namespace instead of sphal namespace.
09-19 00:10:59.836 1989-1989/? D/sound_trigger_hw: stdev_open: Enter
09-19 00:10:59.843 1989-1989/? D/sound_trigger_hw: load_audio_hal: ahal is using proprietary API version 0x0101
09-19 00:10:59.844 1989-1989/? I/sound_trigger_platform: platform_stdev_init: Enter
09-19 00:10:59.845 1989-1989/? W/sound_trigger_platform: load_smlib: generate_sound_trigger_phrase_recognition_event_v3 not found. undefined symbol: generate_sound_trigger_phrase_recognition_event_v3
09-19 00:10:59.848 1989-1989/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: snd_card_name: msm8998-tasha-snd-card
09-19 00:10:59.849 1989-1989/? W/hardware_info: update_hardware_info_msm8998: Not a msm8998 device
09-19 00:10:59.849 1989-1989/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: Opened sound card:0
09-19 00:10:59.860 1982-1982/? I/Riru: Riru v21.3 (36) in zygote64
    config dir is /data/misc/riru
    system version 10 (api 29, preview_sdk 0)
09-19 00:10:59.861 1987-1987/? I/netd: Creating child chains: 20.5ms
    Setting up OEM hooks: 0.1ms
09-19 00:10:59.863 1982-1982/? I/Riru: hook installed
09-19 00:10:59.865 1982-1982/? I/Riru: module loaded: edxp (api 4)
09-19 00:10:59.865 1982-1982/? V/Riru: edxp: onModuleLoaded
09-19 00:10:59.865 1982-1982/? I/EdXposed: onModuleLoaded: welcome to EdXposed!
    Start to install inline hooks
    Using api level 29
    Start to install Riru hook
09-19 00:10:59.869 1987-1987/? I/netd: Setting up FirewallController hooks: 8.6ms
09-19 00:10:59.872 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:59.873 1987-1987/? I/netd: Setting up TetherController hooks: 3.3ms
09-19 00:10:59.877 1987-1987/? I/netd: Setting up BandwidthController hooks: 4.2ms
    Setting up IdletimerController hooks: 0.1ms
09-19 00:10:59.878 1982-1982/? I/EdXposed: Riru hooks installed
09-19 00:10:59.879 1984-1984/? I/FastMixerState: sMaxFastTracks = 8
09-19 00:10:59.881 1984-1984/? V/MediaUtils: physMem: 6004461568
    requested limit: 536870912
09-19 00:10:59.881 1984-1984/? I/libc: malloc_limit: Allocation limit enabled, max size 536870912 bytes
09-19 00:10:59.881 1984-1984/? I/audioserver: ServiceManager: 0x72a9c1edc0
09-19 00:10:59.881 1984-1984/? W/BatteryNotifier: batterystats service unavailable!
09-19 00:10:59.883 1987-1987/? I/netd: Setting up StrictController hooks: 5.8ms
09-19 00:10:59.883 1987-1987/? I/ClatdController: Pre-4.9 kernel or pre-P api shipping level - disabling clat ebpf.
09-19 00:10:59.883 1987-1987/? I/netd: Initializing ClatdController: 0.0ms
    Initializing traffic control: 0.0ms
09-19 00:10:59.884 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.audio@5.0::IDevicesFactory/msd in either framework or device manifest.
09-19 00:10:59.885 1982-1982/? D/AndroidRuntime: >>>>>> START com.android.internal.os.ZygoteInit uid 0 <<<<<<
09-19 00:10:59.885 1983-1983/? I/Riru: Riru v21.3 (36) in zygote
    config dir is /data/misc/riru
    system version 10 (api 29, preview_sdk 0)
09-19 00:10:59.888 1986-1986/? I/mediaserver: ServiceManager: 0xe8c232a0
09-19 00:10:59.888 1986-1986/? W/BatteryNotifier: batterystats service unavailable!
    batterystats service unavailable!
09-19 00:10:59.888 1983-1983/? I/Riru: hook installed
09-19 00:10:59.888 1984-1984/? I/AudioFlinger: Using default 3000 mSec as standby time.
09-19 00:10:59.889 1982-1982/? I/EdXposed: ART hooks installed
09-19 00:10:59.889 1982-1982/? I/AndroidRuntime: Using default boot image
    Leaving lock profiling enabled
09-19 00:10:59.889 1982-1982/? I/EdXposed: system_property_get: dalvik.vm.dex2oat-filter -> quicken
    system_property_get: dalvik.vm.dex2oat-flags -> --inline-max-code-units=0
09-19 00:10:59.890 1982-1982/? I/zygote64: option[0]=-Xzygote
    option[1]=exit
    option[2]=vfprintf
    option[3]=sensitiveThread
    option[4]=-verbose:gc
    option[5]=-Xms8m
    option[6]=-Xmx512m
    option[7]=-XX:HeapGrowthLimit=192m
    option[8]=-XX:HeapMinFree=8m
    option[9]=-XX:HeapMaxFree=16m
    option[10]=-XX:HeapTargetUtilization=0.6
    option[11]=-Xusejit:true
    option[12]=-Xjitsaveprofilinginfo
    option[13]=-XjdwpOptions:suspend=n,server=y
    option[14]=-XjdwpProvider:default
    option[15]=-Xlockprofthreshold:500
    option[16]=-Ximage-compiler-option
    option[17]=--runtime-arg
    option[18]=-Ximage-compiler-option
    option[19]=-Xms64m
    option[20]=-Ximage-compiler-option
    option[21]=--runtime-arg
    option[22]=-Ximage-compiler-option
    option[23]=-Xmx64m
    option[24]=-Ximage-compiler-option
    option[25]=--profile-file=/system/etc/boot-image.prof
    option[26]=-Ximage-compiler-option
    option[27]=--compiler-filter=speed-profile
    option[28]=-Xcompiler-option
    option[29]=--runtime-arg
    option[30]=-Xcompiler-option
    option[31]=-Xms64m
    option[32]=-Xcompiler-option
    option[33]=--runtime-arg
    option[34]=-Xcompiler-option
    option[35]=-Xmx512m
    option[36]=-Xcompiler-option
    option[37]=--compiler-filter=quicken
    option[38]=-Ximage-compiler-option
    option[39]=--instruction-set-variant=cortex-a73
    option[40]=-Xcompiler-option
    option[41]=--instruction-set-variant=cortex-a73
    option[42]=-Ximage-compiler-option
09-19 00:10:59.890 1984-1984/? E/APM::Serializer: deserialize: Could not parse /odm/etc/audio_policy_configuration.xml document.
09-19 00:10:59.890 1982-1982/? I/zygote64: option[43]=--instruction-set-features=default
    option[44]=-Xcompiler-option
    option[45]=--instruction-set-features=default
09-19 00:10:59.891 1982-1982/? I/zygote64: option[46]=-Xcompiler-option
    option[47]=--inline-max-code-units=0
09-19 00:10:59.891 1984-1984/? E/APM::Serializer: deserialize: Could not parse /vendor/etc/audio/audio_policy_configuration.xml document.
09-19 00:10:59.891 1982-1982/? I/zygote64: option[48]=-Duser.locale=en-US
    option[49]=--cpu-abilist=arm64-v8a
    option[50]=-Xcompiler-option
    option[51]=--generate-mini-debug-info
    option[52]=-Xcore-platform-api-policy:just-warn
    option[53]=-Xfingerprint:Xiaomi/chiron/chiron:8.0.0/OPR1.170623.027/V9.5.4.0.ODEMIFA:user/release-keys
09-19 00:10:59.891 1983-1983/? I/Riru: module loaded: edxp (api 4)
09-19 00:10:59.891 1983-1983/? V/Riru: edxp: onModuleLoaded
09-19 00:10:59.891 1983-1983/? I/EdXposed: onModuleLoaded: welcome to EdXposed!
    Start to install inline hooks
    Using api level 29
    Start to install Riru hook
09-19 00:10:59.892 1982-1982/? I/zygote64: Core platform API reporting enabled, enforcing=false
09-19 00:10:59.898 1987-1987/? I/netd: Enabling bandwidth control: 14.9ms
09-19 00:10:59.900 1987-1987/? E/Netd: Error adding route 0.0.0.0/0 -> (null) dummy0 to table 1003: File exists
09-19 00:10:59.900 1987-1987/? I/netd: Initializing RouteController: 2.5ms
09-19 00:10:59.900 1987-1987/? D/XfrmController: XfrmController::ipSecAddXfrmInterface, line=1379
09-19 00:10:59.901 1987-1987/? D/XfrmController: XfrmController::ipSecRemoveTunnelInterface, line=1592
    deviceName=ipsec_test
    Sending Netlink XFRM Message: XFRM_MSG_FLUSHSA
    Sending Netlink XFRM Message: XFRM_MSG_FLUSHPOLICY
09-19 00:10:59.901 1987-1987/? I/netd: Initializing XfrmController: 0.8ms
09-19 00:10:59.901 1987-1987/? E/Netd: Unable to create netlink socket for family 5: Protocol not supported
09-19 00:10:59.901 1987-1987/? W/Netd: Unable to open qlog quota socket, check if xt_quota2 can send via UeventHandler
09-19 00:10:59.902 1987-1987/? I/libnetd_resolv: resolv_init: Initializing resolver
09-19 00:10:59.903 1984-1984/? E/APM::AudioPolicyEngine/Config: parse: Could not parse document /vendor/etc/audio_policy_engine_configuration.xml
09-19 00:10:59.903 1984-1984/? W/APM::AudioPolicyEngine/Base: loadAudioPolicyEngineConfig: No configuration found, using default matching phone experience.
09-19 00:10:59.904 1984-1984/? E/APM::AudioPolicyEngine/Config: parseLegacyVolumeFile: Could not parse document /odm/etc/audio_policy_configuration.xml
09-19 00:10:59.906 1987-1987/? D/MDnsDS: MDnsSdListener::Hander starting up
09-19 00:10:59.907 1987-2009/? D/MDnsDS: MDnsSdListener starting to monitor
    Going to poll with pollCount 1
09-19 00:10:59.907 1987-1987/? I/netd: Registering NetdNativeService: 0.2ms
09-19 00:10:59.908 1989-1993/? D/vndksupport: Loading /vendor/lib/hw/audio.primary.msm8998.so from current namespace instead of sphal namespace.
09-19 00:10:59.908 1989-1993/? D/audio_hw_primary: adev_open: enter
09-19 00:10:59.909 1989-1993/? W/audio_hw_utils: vndk_fwk_init: failed to dlopen VNDK_FWK_LIB No such file or directory
    audio_extn_utils_get_vendor_enhanced_info: default to vendor_enhanced_info 0x0
09-19 00:10:59.909 1989-1993/? D/audio_hw_extn: snd_mon_feature_init: Called with feature NOT Enabled
09-19 00:10:59.909 1989-1993/? W/audio_hw_extn: :: snd_mon_feature_init: ---- Feature SND_MONITOR is disabled ----
    :: compr_cap_feature_init: ---- Feature COMPRESS_CAPTURE is disabled ----
09-19 00:10:59.909 1989-1993/? D/audio_hw_extn: dsm_feedback_feature_init: Called with feature NOT Enabled
09-19 00:10:59.909 1989-1993/? W/audio_hw_extn: :: dsm_feedback_feature_init: ---- Feature DSM_FEEDBACK is disabled ----
    :: ssrec_feature_init: ---- Feature SSREC is disabled ----
09-19 00:10:59.909 1989-1993/? D/audio_hw_extn: src_trkn_feature_init:: ---- Feature SOURCE_TRACKING is Enabled ----
    hdmi_edid_feature_init: HDMI_EDID feature NOT Enabled
09-19 00:10:59.909 1989-1993/? W/audio_hw_extn: :: hdmi_edid_feature_init: ---- Feature HDMI_EDID is disabled ----
09-19 00:10:59.909 1989-1993/? D/audio_hw_extn: :: keep_alive_feature_init: ---- Feature KEEP_ALIVE is  NOT ENABLED ----
    :: hifi_audio_feature_init: ---- Feature HIFI_AUDIO is  NOT ENABLED ----
    :: ras_feature_init: ---- Feature RAS_FEATURE is ENABLED ----
    :: kpi_optimize_feature_init: ---- Feature KPI_OPTIMIZE is ENABLED ----
    usb_offload_feature_init: Called with feature Enabled
    usb_offload_burst_mode_feature_init: Called with feature NOT Enabled
    usb_offload_sidetone_volume_feature_init: Called with feature NOT Enabled
    a2dp_offload_feature_init: Called with feature NOT Enabled
09-19 00:10:59.909 1989-1993/? W/audio_hw_extn: :: a2dp_offload_feature_init: ---- Feature A2DP_OFFLOAD is disabled ----
09-19 00:10:59.909 1989-1993/? D/audio_hw_extn: :: vbat_feature_init: ---- Feature VBAT is ENABLED ----
    :: display_port_feature_init: ---- Feature DISPLAY_PORT is ENABLED ----
    :: fluence_feature_init: ---- Feature FLUENCE is ENABLED ----
    :: custom_stereo_feature_init: ---- Feature CUSTOM_STEREO is ENABLED ----
    :: anc_headset_feature_init: ---- Feature ANC_HEADSET is ENABLED----
    spkr_prot_feature_init: Called with feature NOT Enabled, vendor_enhanced_info 0x0
09-19 00:10:59.909 1989-1993/? W/audio_hw_extn: :: spkr_prot_feature_init: ---- Feature SPKR_PROT is disabled ----
09-19 00:10:59.909 1989-1993/? D/audio_hw_extn: fm_feature_init: ---- Feature FM_POWER_OPT is ENABLED----
    external_qdsp_feature_init: Called with feature NOT Enabled
09-19 00:10:59.909 1989-1993/? W/audio_hw_extn: :: external_qdsp_feature_init: ---- Feature EXTERNAL_QDSP is disabled ----
09-19 00:10:59.909 1989-1993/? D/audio_hw_extn: external_speaker_feature_init: Called with feature NOT Enabled
09-19 00:10:59.909 1989-1993/? W/audio_hw_extn: :: external_speaker_feature_init: ---- Feature EXTERNAL_SPKR is disabled ----
09-19 00:10:59.909 1989-1993/? D/audio_hw_extn: external_speaker_tfa_feature_init: Called with feature NOT Enabled
09-19 00:10:59.909 1989-1993/? W/audio_hw_extn: :: external_speaker_tfa_feature_init: ---- Feature EXTERNAL_SPKR_TFA is disabled ----
09-19 00:10:59.909 1989-1993/? D/audio_hw_extn: hwdep_cal_feature_init: Called with feature NOT Enabled
09-19 00:10:59.909 1989-1993/? W/audio_hw_extn: :: hwdep_cal_feature_init: ---- Feature HWDEP_CAL is disabled ----
09-19 00:10:59.909 1989-1993/? D/audio_hw_extn: hfp_feature_init: Called with feature Enabled
09-19 00:10:59.910 1989-1993/? D/audio_hw_extn: hfp_feature_init:: ---- Feature HFP is Enabled ----
    ext_hw_plugin_feature_init: Called with feature NOT Enabled
09-19 00:10:59.910 1989-1993/? W/audio_hw_extn: :: ext_hw_plugin_feature_init: ---- Feature EXT_HW_PLUGIN is disabled ----
09-19 00:10:59.910 1989-1993/? D/audio_hw_extn: record_play_concurency_feature_init: ---- Feature RECORD_PLAY_CONCURRENCY is NOT ENABLED----
    hdmi_passthrough_feature_init: Called with feature NOT Enabled
09-19 00:10:59.910 1989-1993/? W/audio_hw_extn: :: hdmi_passthrough_feature_init: ---- Feature HDMI_PASSTHROUGH is disabled ----
09-19 00:10:59.910 1989-1993/? D/audio_hw_extn: concurrent_capture_feature_init: ---- Feature CONCURRENT_CAPTURE is NOT ENABLED----
    compress_in_feature_init: ---- Feature COMPRESS_IN is NOT ENABLED----
09-19 00:10:59.910 1989-1993/? W/audio_hw_extn: :: battery_listener_feature_init: ---- Feature BATTERY_LISTENER is disabled ----
09-19 00:10:59.910 1989-1993/? D/audio_hw_extn: maxx_audio_feature_init: Called with feature NOT Enabled
09-19 00:10:59.910 1989-1993/? W/audio_hw_extn: :: maxx_audio_feature_init: ---- Feature MAXX_AUDIO is disabled ----
09-19 00:10:59.910 1989-1993/? D/audio_hw_extn: audiozoom_feature_init: Called with feature NOT Enabled
09-19 00:10:59.910 1989-1993/? W/audio_hw_extn: :: audiozoom_feature_init: ---- Feature AUDIOZOOM is disabled ----
09-19 00:10:59.910 1989-1993/? D/voice_extn: :: dynamic_ecns_feature_init: ---- Feature DYNAMIC_ECNS is NOT ENABLED ----
09-19 00:10:59.910 882-1736/? I/QC-NETMGR-LIB: onRegistration(): Starting Netd getService thread
09-19 00:10:59.910 1987-1987/? I/ServiceManagement: Registered android.system.net.netd@1.1::INetd/default (start delay of 159ms)
09-19 00:10:59.910 1983-1983/? I/EdXposed: Riru hooks installed
09-19 00:10:59.911 1987-1987/? I/netd: Registering NetdHwService: 4.1ms
    Netd started in 89ms
09-19 00:10:59.912 1989-1993/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: snd_card_name: msm8998-tasha-snd-card
09-19 00:10:59.912 1989-1993/? W/hardware_info: update_hardware_info_msm8998: Not a msm8998 device
09-19 00:10:59.912 1989-1993/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: Opened sound card:0
09-19 00:10:59.912 1989-1993/? D/msm8974_platform: platform_init: Opened sound card:0
09-19 00:10:59.912 1989-1993/? I/audio_hw_extn: audio_extn_set_snd_card_split: snd_card_name(msm8998-tasha-snd-card) device(msm8998) snd_card(tasha) form_factor(snd)
09-19 00:10:59.912 1989-1993/? W/hardware_info: update_hardware_info_msm8998: Not a msm8998 device
09-19 00:10:59.912 1989-1993/? D/msm8974_platform: platform_init: Loading mixer file: /vendor/etc/mixer_paths_tasha.xml
09-19 00:10:59.914 882-2015/? I/QC-NETMGR-LIB: getServiceImpl(): INetd discovered
    registerLinkToDeath(): Success registerLinkToDeath!
09-19 00:10:59.914 882-1736/? D/QC-NETMGR-LIB: onRegistration(): netd restart detected
09-19 00:10:59.914 882-979/? I/QC-NETMGR-LIB: NetmgrNetdClientRegisterNetwork(): Looking for Netd service
    NetmgrNetdClientRegisterNetwork(): register to create new OEM network
    registerNetwork(): Attempting createOemNetwork
09-19 00:10:59.915 1987-2014/? D/TcpSocketMonitor: suspending tcpinfo polling
09-19 00:10:59.915 882-979/? I/QC-NETMGR-LIB: registerNetwork(): command completed!
    registerNetwork(): createOemNetwork succeeded [packet mark : 0xf0001] [net id : 1] [network handle : 0x1cafed00d]
    NetmgrNetdClientRegisterNetwork(): [packet mark : 0xf0001] [network handle : 0x1cafed00d]
09-19 00:10:59.917 1983-1983/? D/AndroidRuntime: >>>>>> START com.android.internal.os.ZygoteInit uid 0 <<<<<<
09-19 00:10:59.920 1983-1983/? I/EdXposed: ART hooks installed
09-19 00:10:59.921 1983-1983/? I/AndroidRuntime: Using default boot image
    Leaving lock profiling enabled
09-19 00:10:59.921 1983-1983/? I/EdXposed: system_property_get: dalvik.vm.dex2oat-filter -> quicken
    system_property_get: dalvik.vm.dex2oat-flags -> --inline-max-code-units=0
09-19 00:10:59.922 1983-1983/? I/zygote: option[0]=-Xzygote
    option[1]=exit
    option[2]=vfprintf
    option[3]=sensitiveThread
    option[4]=-verbose:gc
    option[5]=-Xms8m
    option[6]=-Xmx512m
    option[7]=-XX:HeapGrowthLimit=192m
    option[8]=-XX:HeapMinFree=8m
    option[9]=-XX:HeapMaxFree=16m
    option[10]=-XX:HeapTargetUtilization=0.6
    option[11]=-Xusejit:true
    option[12]=-Xjitsaveprofilinginfo
    option[13]=-XjdwpOptions:suspend=n,server=y
    option[14]=-XjdwpProvider:default
    option[15]=-Xlockprofthreshold:500
    option[16]=-Ximage-compiler-option
    option[17]=--runtime-arg
    option[18]=-Ximage-compiler-option
    option[19]=-Xms64m
    option[20]=-Ximage-compiler-option
    option[21]=--runtime-arg
    option[22]=-Ximage-compiler-option
    option[23]=-Xmx64m
    option[24]=-Ximage-compiler-option
    option[25]=--profile-file=/system/etc/boot-image.prof
    option[26]=-Ximage-compiler-option
    option[27]=--compiler-filter=speed-profile
    option[28]=-Xcompiler-option
    option[29]=--runtime-arg
    option[30]=-Xcompiler-option
    option[31]=-Xms64m
    option[32]=-Xcompiler-option
    option[33]=--runtime-arg
    option[34]=-Xcompiler-option
09-19 00:10:59.923 1983-1983/? I/zygote: option[35]=-Xmx512m
    option[36]=-Xcompiler-option
    option[37]=--compiler-filter=quicken
    option[38]=-Ximage-compiler-option
    option[39]=--instruction-set-variant=cortex-a73
    option[40]=-Xcompiler-option
    option[41]=--instruction-set-variant=cortex-a73
    option[42]=-Ximage-compiler-option
    option[43]=--instruction-set-features=default
    option[44]=-Xcompiler-option
    option[45]=--instruction-set-features=default
    option[46]=-Xcompiler-option
    option[47]=--inline-max-code-units=0
    option[48]=-Duser.locale=en-US
    option[49]=--cpu-abilist=armeabi-v7a,armeabi
    option[50]=-Xcompiler-option
    option[51]=--generate-mini-debug-info
    option[52]=-Xcore-platform-api-policy:just-warn
    option[53]=-Xfingerprint:Xiaomi/chiron/chiron:8.0.0/OPR1.170623.027/V9.5.4.0.ODEMIFA:user/release-keys
09-19 00:10:59.925 1983-1983/? I/zygote: Core platform API reporting enabled, enforcing=false
09-19 00:10:59.946 1982-1982/? I/EdXposed: using installer org.meowcat.edxposed.manager
    data path prefix: /data/user_de/0/
      application list mode: false
        using whitelist: false
      dynamic modules mode: false
      resources hook: true
      deopt boot image: false
      no module log: false
09-19 00:10:59.963 925-1074/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 44000 mC, weight[0] 2
09-19 00:10:59.964 925-1074/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:10:59.971 1983-1983/? I/EdXposed: using installer org.meowcat.edxposed.manager
    data path prefix: /data/user_de/0/
      application list mode: false
09-19 00:10:59.971 1985-1985/? I/cameraserver: ServiceManager: 0xf17231a0
09-19 00:10:59.971 1983-1983/? I/EdXposed:     using whitelist: false
      dynamic modules mode: false
      resources hook: true
      deopt boot image: false
      no module log: false
09-19 00:10:59.971 1985-1985/? I/CameraService: CameraService started (pid=1985)
    CameraService process starting
09-19 00:10:59.971 1985-1985/? W/BatteryNotifier: batterystats service unavailable!
    batterystats service unavailable!
09-19 00:10:59.973 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:10:59.974 1985-1985/? I/CameraProviderManager: Connecting to new camera provider: legacy/0, isRemote? 1
09-19 00:10:59.975 1985-1985/? I/CameraProviderManager: Enumerating new camera device: device@1.0/legacy/0
09-19 00:10:59.977 774-774/? I/CamDev@1.0-impl: Opening camera 0
09-19 00:10:59.978 774-774/? I/QCamera: <HAL><INFO> openLegacy: 503: openLegacy halVersion: 256 cameraId = 0
09-19 00:10:59.979 774-774/? D/vndksupport: Loading /vendor/lib/hw/power.default.so from current namespace instead of sphal namespace.
09-19 00:10:59.982 1982-1982/? D/ICU: Time zone APEX file found: /apex/com.android.tzdata/etc/icu/icu_tzdata.dat
09-19 00:10:59.984 925-1080/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 44000 mC, weight[0] 2
09-19 00:10:59.985 925-1080/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:10:59.986 774-774/? E/Watermark: getFontData Font file does not exist!
    getFontData Get file status failed
    getFontData Font file does not exist!
    getFontData Get file status failed
09-19 00:10:59.986 774-774/? I/QCamera: <HAL><INFO> openCamera: 1923: [KPI Perf]: E PROFILE_OPEN_CAMERA camera id 0
09-19 00:10:59.987 774-774/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:10:59.988 1985-1985/? W/CameraProviderManager: Camera provider legacy/0 says an unknown camera device@1.0/legacy/0 now has torch status 0. Curious.
    Camera provider legacy/0 says an unknown camera device@3.3/legacy/0 now has torch status 0. Curious.
09-19 00:10:59.988 774-774/? D/QCamera: Debug log file is not enabled
09-19 00:10:59.992 1982-1982/? V/Riru: jniRegisterNativeMethods com/android/internal/os/RuntimeInit
    jniRegisterNativeMethods com/android/internal/os/ZygoteInit
    jniRegisterNativeMethods android/os/SystemClock
09-19 00:10:59.993 1982-1982/? V/Riru: jniRegisterNativeMethods android/util/EventLog
    jniRegisterNativeMethods android/util/Log
    jniRegisterNativeMethods android/util/MemoryIntArray
    jniRegisterNativeMethods android/util/PathParser
    jniRegisterNativeMethods android/util/StatsLog
    jniRegisterNativeMethods android/util/StatsLogInternal
09-19 00:10:59.994 1982-1982/? V/Riru: jniRegisterNativeMethods android/app/admin/SecurityLog
    jniRegisterNativeMethods android/content/res/AssetManager
09-19 00:10:59.995 1982-1982/? V/Riru: jniRegisterNativeMethods android/content/res/StringBlock
    jniRegisterNativeMethods android/content/res/XmlBlock
    jniRegisterNativeMethods android/content/res/ApkAssets
    jniRegisterNativeMethods android/text/AndroidCharacter
    jniRegisterNativeMethods android/text/Hyphenator
    jniRegisterNativeMethods android/view/KeyCharacterMap
    jniRegisterNativeMethods android/os/Process
    jniRegisterNativeMethods android/os/SystemProperties
09-19 00:10:59.995 1982-1982/? I/Riru: replaced android.os.SystemProperties#native_set
09-19 00:10:59.995 1982-1982/? V/Riru: jniRegisterNativeMethods android/os/Binder
09-19 00:10:59.996 1982-1982/? V/Riru: jniRegisterNativeMethods com/android/internal/os/BinderInternal
    jniRegisterNativeMethods android/os/BinderProxy
09-19 00:10:59.997 1982-1982/? V/Riru: jniRegisterNativeMethods android/os/Parcel
    jniRegisterNativeMethods android/os/HidlSupport
    jniRegisterNativeMethods android/os/HwBinder
    jniRegisterNativeMethods android/os/HwBlob
    jniRegisterNativeMethods android/os/HwParcel
    jniRegisterNativeMethods android/os/HwRemoteBinder
    jniRegisterNativeMethods android/os/VintfObject
    jniRegisterNativeMethods android/os/VintfRuntimeInfo
    jniRegisterNativeMethods android/graphics/Canvas
    jniRegisterNativeMethods android/graphics/BaseCanvas
    jniRegisterNativeMethods android/graphics/BaseRecordingCanvas
    jniRegisterNativeMethods android/graphics/ColorSpace$Rgb
09-19 00:10:59.998 1982-1982/? V/Riru: jniRegisterNativeMethods android/view/DisplayEventReceiver
    jniRegisterNativeMethods android/graphics/RenderNode
    jniRegisterNativeMethods android/view/RenderNodeAnimator
    jniRegisterNativeMethods android/graphics/RecordingCanvas
    jniRegisterNativeMethods android/view/InputApplicationHandle
    jniRegisterNativeMethods android/view/InputWindowHandle
    jniRegisterNativeMethods android/view/TextureLayer
    jniRegisterNativeMethods android/graphics/HardwareRenderer
09-19 00:10:59.999 1982-1982/? V/Riru: jniRegisterNativeMethods android/view/Surface
    jniRegisterNativeMethods android/view/SurfaceControl
    jniRegisterNativeMethods android/view/SurfaceSession
    jniRegisterNativeMethods android/view/CompositionSamplingListener
    jniRegisterNativeMethods android/view/TextureView
    jniRegisterNativeMethods com/android/internal/view/animation/NativeInterpolatorFactoryHelper
    jniRegisterNativeMethods com/google/android/gles_jni/EGLImpl
    jniRegisterNativeMethods com/google/android/gles_jni/GLImpl
09-19 00:11:00.000 1982-1982/? V/Riru: jniRegisterNativeMethods android/opengl/EGL14
    jniRegisterNativeMethods android/opengl/EGL15
    jniRegisterNativeMethods android/opengl/EGLExt
    jniRegisterNativeMethods android/opengl/GLES10
    jniRegisterNativeMethods android/opengl/GLES10Ext
    jniRegisterNativeMethods android/opengl/GLES11
    jniRegisterNativeMethods android/opengl/GLES11Ext
09-19 00:11:00.001 1982-1982/? V/Riru: jniRegisterNativeMethods android/opengl/GLES20
    jniRegisterNativeMethods android/opengl/GLES30
09-19 00:11:00.002 1982-1982/? V/Riru: jniRegisterNativeMethods android/opengl/GLES31
    jniRegisterNativeMethods android/opengl/GLES31Ext
    jniRegisterNativeMethods android/opengl/GLES32
    jniRegisterNativeMethods android/graphics/Bitmap
    jniRegisterNativeMethods android/graphics/BitmapFactory
    jniRegisterNativeMethods android/graphics/BitmapRegionDecoder
    jniRegisterNativeMethods android/graphics/Camera
    jniRegisterNativeMethods android/graphics/CanvasProperty
    jniRegisterNativeMethods android/graphics/ColorFilter
09-19 00:11:00.003 1982-1982/? V/Riru: jniRegisterNativeMethods android/graphics/PorterDuffColorFilter
    jniRegisterNativeMethods android/graphics/BlendModeColorFilter
    jniRegisterNativeMethods android/graphics/LightingColorFilter
    jniRegisterNativeMethods android/graphics/ColorMatrixColorFilter
    jniRegisterNativeMethods android/graphics/DrawFilter
    jniRegisterNativeMethods android/graphics/PaintFlagsDrawFilter
    jniRegisterNativeMethods android/graphics/FontFamily
09-19 00:11:00.006 1982-1982/? V/Riru: jniRegisterNativeMethods android/graphics/GraphicBuffer
    jniRegisterNativeMethods android/graphics/ImageDecoder
    jniRegisterNativeMethods android/graphics/drawable/AnimatedImageDrawable
    jniRegisterNativeMethods android/graphics/Interpolator
    jniRegisterNativeMethods android/graphics/MaskFilter
    jniRegisterNativeMethods android/graphics/BlurMaskFilter
    jniRegisterNativeMethods android/graphics/EmbossMaskFilter
    jniRegisterNativeMethods android/graphics/TableMaskFilter
    jniRegisterNativeMethods android/graphics/Matrix
    jniRegisterNativeMethods android/graphics/Movie
    jniRegisterNativeMethods android/graphics/NinePatch
    jniRegisterNativeMethods android/graphics/Paint
    jniRegisterNativeMethods android/graphics/Path
    jniRegisterNativeMethods android/graphics/PathMeasure
    jniRegisterNativeMethods android/graphics/PathEffect
    jniRegisterNativeMethods android/graphics/ComposePathEffect
    jniRegisterNativeMethods android/graphics/SumPathEffect
    jniRegisterNativeMethods android/graphics/DashPathEffect
    jniRegisterNativeMethods android/graphics/PathDashPathEffect
    jniRegisterNativeMethods android/graphics/CornerPathEffect
    jniRegisterNativeMethods android/graphics/DiscretePathEffect
09-19 00:11:00.007 1982-1982/? V/Riru: jniRegisterNativeMethods android/graphics/Picture
    jniRegisterNativeMethods android/graphics/Region
    jniRegisterNativeMethods android/graphics/RegionIterator
    jniRegisterNativeMethods android/graphics/Color
    jniRegisterNativeMethods android/graphics/Shader
    jniRegisterNativeMethods android/graphics/BitmapShader
    jniRegisterNativeMethods android/graphics/LinearGradient
    jniRegisterNativeMethods android/graphics/RadialGradient
    jniRegisterNativeMethods android/graphics/SweepGradient
    jniRegisterNativeMethods android/graphics/ComposeShader
    jniRegisterNativeMethods android/graphics/SurfaceTexture
    jniRegisterNativeMethods android/graphics/Typeface
    jniRegisterNativeMethods android/graphics/YuvImage
    jniRegisterNativeMethods android/graphics/drawable/AnimatedVectorDrawable
    jniRegisterNativeMethods android/graphics/drawable/VectorDrawable
    jniRegisterNativeMethods android/graphics/fonts/Font$Builder
    jniRegisterNativeMethods android/graphics/fonts/FontFamily$Builder
    jniRegisterNativeMethods android/graphics/pdf/PdfDocument
    jniRegisterNativeMethods android/graphics/pdf/PdfEditor
    jniRegisterNativeMethods android/graphics/pdf/PdfRenderer
    jniRegisterNativeMethods android/graphics/text/MeasuredText
    jniRegisterNativeMethods android/graphics/text/MeasuredText$Builder
    jniRegisterNativeMethods android/graphics/text/LineBreaker
    jniRegisterNativeMethods android/database/CursorWindow
    jniRegisterNativeMethods android/database/sqlite/SQLiteConnection
    jniRegisterNativeMethods android/database/sqlite/SQLiteGlobal
    jniRegisterNativeMethods android/database/sqlite/SQLiteDebug
    jniRegisterNativeMethods android/os/Debug
    jniRegisterNativeMethods android/os/FileObserver$ObserverThread
    jniRegisterNativeMethods android/os/GraphicsEnvironment
09-19 00:11:00.008 1982-1982/? V/Riru: jniRegisterNativeMethods android/os/MessageQueue
    jniRegisterNativeMethods android/os/SELinux
    jniRegisterNativeMethods android/os/Trace
    jniRegisterNativeMethods android/os/UEventObserver
    jniRegisterNativeMethods android/net/LocalSocketImpl
    jniRegisterNativeMethods android/net/NetworkUtils
    jniRegisterNativeMethods android/os/MemoryFile
    jniRegisterNativeMethods android/os/SharedMemory
    jniRegisterNativeMethods com/android/internal/os/ClassLoaderFactory
    jniRegisterNativeMethods com/android/internal/os/Zygote
09-19 00:11:00.008 1982-1982/? I/Riru: replaced com.android.internal.os.Zygote#nativeForkAndSpecialize
    replaced com.android.internal.os.Zygote#nativeForkSystemServer
    replaced com.android.internal.os.Zygote#nativeSpecializeAppProcess
09-19 00:11:00.008 1982-1982/? V/Riru: jniRegisterNativeMethods com/android/internal/os/ZygoteInit
    jniRegisterNativeMethods com/android/internal/util/VirtualRefBasePtr
    jniRegisterNativeMethods android/hardware/Camera
    jniRegisterNativeMethods android/hardware/camera2/impl/CameraMetadataNative
    jniRegisterNativeMethods android/hardware/camera2/legacy/LegacyCameraDevice
09-19 00:11:00.008 1983-1983/? D/ICU: Time zone APEX file found: /apex/com.android.tzdata/etc/icu/icu_tzdata.dat
09-19 00:11:00.009 1982-1982/? V/Riru: jniRegisterNativeMethods android/hardware/camera2/legacy/PerfMeasurement
    jniRegisterNativeMethods android/hardware/camera2/DngCreator
    jniRegisterNativeMethods android/hardware/HardwareBuffer
    jniRegisterNativeMethods android/hardware/SystemSensorManager
    jniRegisterNativeMethods android/hardware/SystemSensorManager$BaseEventQueue
    jniRegisterNativeMethods android/hardware/SerialPort
    jniRegisterNativeMethods android/hardware/soundtrigger/SoundTrigger
    jniRegisterNativeMethods android/hardware/soundtrigger/SoundTriggerModule
    jniRegisterNativeMethods android/hardware/usb/UsbDevice
    jniRegisterNativeMethods android/hardware/usb/UsbDeviceConnection
    jniRegisterNativeMethods android/hardware/usb/UsbRequest
    jniRegisterNativeMethods android/hardware/location/ActivityRecognitionHardware
    jniRegisterNativeMethods android/media/AudioSystem
09-19 00:11:00.010 1982-1982/? V/Riru: jniRegisterNativeMethods android/media/AudioSystem
    jniRegisterNativeMethods android/media/AudioPortEventHandler
    jniRegisterNativeMethods android/media/AudioRecord
    jniRegisterNativeMethods android/media/AudioTrack
    jniRegisterNativeMethods android/media/AudioAttributes
09-19 00:11:00.010 1982-1982/? W/zygote64: JNI RegisterNativeMethods: attempt to register 0 native methods for android.media.AudioAttributes
09-19 00:11:00.010 1982-1982/? V/Riru: jniRegisterNativeMethods android/media/audiopolicy/AudioProductStrategy
    jniRegisterNativeMethods android/media/audiopolicy/AudioVolumeGroup
    jniRegisterNativeMethods android/media/audiopolicy/AudioVolumeGroupChangeHandler
    jniRegisterNativeMethods android/media/JetPlayer
    jniRegisterNativeMethods android/media/RemoteDisplay
    jniRegisterNativeMethods android/media/ToneGenerator
    jniRegisterNativeMethods android/opengl/Matrix
    jniRegisterNativeMethods android/opengl/Visibility
    jniRegisterNativeMethods android/opengl/GLUtils
    jniRegisterNativeMethods android/opengl/ETC1
    jniRegisterNativeMethods com/android/server/NetworkManagementSocketTagger
    jniRegisterNativeMethods android/ddm/DdmHandleNativeHeap
09-19 00:11:00.011 1982-1982/? V/Riru: jniRegisterNativeMethods android/app/backup/BackupDataInput
    jniRegisterNativeMethods android/app/backup/BackupDataOutput
    jniRegisterNativeMethods android/app/backup/FileBackupHelperBase
    jniRegisterNativeMethods android/app/backup/BackupHelperDispatcher
    jniRegisterNativeMethods android/app/backup/FullBackup
    jniRegisterNativeMethods android/app/Activity
    jniRegisterNativeMethods android/app/ActivityThread
    jniRegisterNativeMethods android/app/NativeActivity
    jniRegisterNativeMethods android/util/jar/StrictJarFile
    jniRegisterNativeMethods android/view/InputChannel
    jniRegisterNativeMethods android/view/InputEventReceiver
    jniRegisterNativeMethods android/view/InputEventSender
    jniRegisterNativeMethods android/view/InputQueue
    jniRegisterNativeMethods android/view/KeyEvent
    jniRegisterNativeMethods android/view/MotionEvent
    jniRegisterNativeMethods android/view/VelocityTracker
    jniRegisterNativeMethods android/content/res/ObbScanner
    jniRegisterNativeMethods android/animation/PropertyValuesHolder
    jniRegisterNativeMethods android/security/Scrypt
    jniRegisterNativeMethods com/android/internal/content/NativeLibraryHelper
    jniRegisterNativeMethods com/android/internal/os/AtomicDirectory
    jniRegisterNativeMethods com/android/internal/os/FuseAppLoop
09-19 00:11:00.013 1982-1982/? D/Zygote: begin preload
09-19 00:11:00.013 1982-1982/? I/Zygote: Calling ZygoteHooks.beginPreload()
09-19 00:11:00.018 1982-1982/? D/Zygote64Timing: BeginPreload took to complete: 5ms
09-19 00:11:00.018 1982-1982/? I/Zygote: Preloading classes...
09-19 00:11:00.019 1982-1982/? W/Zygote: Class not found for preloading: android.app.-$$Lambda$ActivityThread$ZXDWm3IBeFmLnFVblhB-IOZCr9o
09-19 00:11:00.019 1983-1983/? V/Riru: jniRegisterNativeMethods com/android/internal/os/RuntimeInit
    jniRegisterNativeMethods com/android/internal/os/ZygoteInit
    jniRegisterNativeMethods android/os/SystemClock
09-19 00:11:00.020 1983-1983/? V/Riru: jniRegisterNativeMethods android/util/EventLog
    jniRegisterNativeMethods android/util/Log
    jniRegisterNativeMethods android/util/MemoryIntArray
    jniRegisterNativeMethods android/util/PathParser
    jniRegisterNativeMethods android/util/StatsLog
    jniRegisterNativeMethods android/util/StatsLogInternal
09-19 00:11:00.020 774-2029/? E/mm-camera: <SENSOR><ERROR> chiron_imx386_semco_autofocus_calibration: 571: adjusted code_per_step: 165, qvalue: 128
09-19 00:11:00.021 1983-1983/? V/Riru: jniRegisterNativeMethods android/app/admin/SecurityLog
    jniRegisterNativeMethods android/content/res/AssetManager
    jniRegisterNativeMethods android/content/res/StringBlock
    jniRegisterNativeMethods android/content/res/XmlBlock
    jniRegisterNativeMethods android/content/res/ApkAssets
    jniRegisterNativeMethods android/text/AndroidCharacter
    jniRegisterNativeMethods android/text/Hyphenator
    jniRegisterNativeMethods android/view/KeyCharacterMap
09-19 00:11:00.022 1983-1983/? V/Riru: jniRegisterNativeMethods android/os/Process
    jniRegisterNativeMethods android/os/SystemProperties
09-19 00:11:00.022 1983-1983/? I/Riru: replaced android.os.SystemProperties#native_set
09-19 00:11:00.022 1983-1983/? V/Riru: jniRegisterNativeMethods android/os/Binder
    jniRegisterNativeMethods com/android/internal/os/BinderInternal
    jniRegisterNativeMethods android/os/BinderProxy
    jniRegisterNativeMethods android/os/Parcel
    jniRegisterNativeMethods android/os/HidlSupport
    jniRegisterNativeMethods android/os/HwBinder
    jniRegisterNativeMethods android/os/HwBlob
09-19 00:11:00.023 1983-1983/? V/Riru: jniRegisterNativeMethods android/os/HwParcel
    jniRegisterNativeMethods android/os/HwRemoteBinder
    jniRegisterNativeMethods android/os/VintfObject
    jniRegisterNativeMethods android/os/VintfRuntimeInfo
    jniRegisterNativeMethods android/graphics/Canvas
    jniRegisterNativeMethods android/graphics/BaseCanvas
    jniRegisterNativeMethods android/graphics/BaseRecordingCanvas
    jniRegisterNativeMethods android/graphics/ColorSpace$Rgb
09-19 00:11:00.023 774-774/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:11:00.024 774-774/? I/chatty: uid=1047(cameraserver) provider@2.4-se identical 3 lines
09-19 00:11:00.024 774-774/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:11:00.024 1983-1983/? V/Riru: jniRegisterNativeMethods android/view/DisplayEventReceiver
    jniRegisterNativeMethods android/graphics/RenderNode
    jniRegisterNativeMethods android/view/RenderNodeAnimator
    jniRegisterNativeMethods android/graphics/RecordingCanvas
    jniRegisterNativeMethods android/view/InputApplicationHandle
    jniRegisterNativeMethods android/view/InputWindowHandle
    jniRegisterNativeMethods android/view/TextureLayer
    jniRegisterNativeMethods android/graphics/HardwareRenderer
    jniRegisterNativeMethods android/view/Surface
    jniRegisterNativeMethods android/view/SurfaceControl
09-19 00:11:00.025 1983-1983/? V/Riru: jniRegisterNativeMethods android/view/SurfaceSession
    jniRegisterNativeMethods android/view/CompositionSamplingListener
    jniRegisterNativeMethods android/view/TextureView
    jniRegisterNativeMethods com/android/internal/view/animation/NativeInterpolatorFactoryHelper
    jniRegisterNativeMethods com/google/android/gles_jni/EGLImpl
    jniRegisterNativeMethods com/google/android/gles_jni/GLImpl
09-19 00:11:00.026 1983-1983/? V/Riru: jniRegisterNativeMethods android/opengl/EGL14
    jniRegisterNativeMethods android/opengl/EGL15
    jniRegisterNativeMethods android/opengl/EGLExt
    jniRegisterNativeMethods android/opengl/GLES10
09-19 00:11:00.026 774-774/? I/Thermal-Lib: Thermal-Lib-Client: Registration successful for camera with handle:1
09-19 00:11:00.026 774-774/? I/QCamera: <HAL><INFO> openCamera: 1938: [KPI Perf]: X PROFILE_OPEN_CAMERA camera id 0, rc: 0
09-19 00:11:00.026 1983-1983/? V/Riru: jniRegisterNativeMethods android/opengl/GLES10Ext
    jniRegisterNativeMethods android/opengl/GLES11
09-19 00:11:00.027 1983-1983/? V/Riru: jniRegisterNativeMethods android/opengl/GLES11Ext
    jniRegisterNativeMethods android/opengl/GLES20
09-19 00:11:00.028 1983-1983/? V/Riru: jniRegisterNativeMethods android/opengl/GLES30
09-19 00:11:00.028 774-774/? I/CamDev@1.0-impl: could not cast ICameraDeviceCallback to IQCameraDeviceCallback
09-19 00:11:00.028 1983-1983/? V/Riru: jniRegisterNativeMethods android/opengl/GLES31
    jniRegisterNativeMethods android/opengl/GLES31Ext
    jniRegisterNativeMethods android/opengl/GLES32
09-19 00:11:00.029 1983-1983/? V/Riru: jniRegisterNativeMethods android/graphics/Bitmap
    jniRegisterNativeMethods android/graphics/BitmapFactory
    jniRegisterNativeMethods android/graphics/BitmapRegionDecoder
    jniRegisterNativeMethods android/graphics/Camera
    jniRegisterNativeMethods android/graphics/CanvasProperty
    jniRegisterNativeMethods android/graphics/ColorFilter
    jniRegisterNativeMethods android/graphics/PorterDuffColorFilter
    jniRegisterNativeMethods android/graphics/BlendModeColorFilter
    jniRegisterNativeMethods android/graphics/LightingColorFilter
    jniRegisterNativeMethods android/graphics/ColorMatrixColorFilter
    jniRegisterNativeMethods android/graphics/DrawFilter
    jniRegisterNativeMethods android/graphics/PaintFlagsDrawFilter
    jniRegisterNativeMethods android/graphics/FontFamily
09-19 00:11:00.030 774-2020/? E/QCamera: <HAL><ERROR> calcThermalLevel: 10178: level: 0, preview minfps 7000.000000, preview maxfpS 30000.000000, video minfps 7000.000000, video maxfps 30000.000000
    <HAL><ERROR> calcThermalLevel: 10183: level change to -> 0
    <HAL><ERROR> calcThermalLevel: 10262: Adjusted preview minfps 7.000000, preview maxfpS 30.000000, video minfps 7.000000, video maxfps 30.000000
09-19 00:11:00.030 774-2020/? E/QCameraParameters: setOISValue9690 OISEnabled=1 
    res_idx = 0 chromatix_lib_name[1] = chiron_imx386_semco_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_imx386_semco_common
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[9] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[10] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[11] = chiron_imx386_semco_cpp_video
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_imx386_semco_zsl_preview
    res_idx = 0 chromatix_lib_name[1] = chiron_imx386_semco_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_imx386_semco_common
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_imx386_semco_cpp_snapshot
09-19 00:11:00.032 1983-1983/? V/Riru: jniRegisterNativeMethods android/graphics/GraphicBuffer
    res_idx = 0 chromatix_lib_name[6] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[9] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[10] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[11] = chiron_imx386_semco_cpp_video
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_imx386_semco_zsl_preview
09-19 00:11:00.032 1983-1983/? V/Riru: jniRegisterNativeMethods android/graphics/ImageDecoder
    jniRegisterNativeMethods android/graphics/drawable/AnimatedImageDrawable
    jniRegisterNativeMethods android/graphics/Interpolator
    jniRegisterNativeMethods android/graphics/MaskFilter
    jniRegisterNativeMethods android/graphics/BlurMaskFilter
    jniRegisterNativeMethods android/graphics/EmbossMaskFilter
    jniRegisterNativeMethods android/graphics/TableMaskFilter
    jniRegisterNativeMethods android/graphics/Matrix
    jniRegisterNativeMethods android/graphics/Movie
    jniRegisterNativeMethods android/graphics/NinePatch
    jniRegisterNativeMethods android/graphics/Paint
    jniRegisterNativeMethods android/graphics/Path
    jniRegisterNativeMethods android/graphics/PathMeasure
    jniRegisterNativeMethods android/graphics/PathEffect
    jniRegisterNativeMethods android/graphics/ComposePathEffect
    jniRegisterNativeMethods android/graphics/SumPathEffect
09-19 00:11:00.033 1983-1983/? V/Riru: jniRegisterNativeMethods android/graphics/DashPathEffect
    jniRegisterNativeMethods android/graphics/PathDashPathEffect
    jniRegisterNativeMethods android/graphics/CornerPathEffect
    jniRegisterNativeMethods android/graphics/DiscretePathEffect
    jniRegisterNativeMethods android/graphics/Picture
    jniRegisterNativeMethods android/graphics/Region
    jniRegisterNativeMethods android/graphics/RegionIterator
    jniRegisterNativeMethods android/graphics/Color
    jniRegisterNativeMethods android/graphics/Shader
    jniRegisterNativeMethods android/graphics/BitmapShader
    jniRegisterNativeMethods android/graphics/LinearGradient
    jniRegisterNativeMethods android/graphics/RadialGradient
    jniRegisterNativeMethods android/graphics/SweepGradient
    jniRegisterNativeMethods android/graphics/ComposeShader
    jniRegisterNativeMethods android/graphics/SurfaceTexture
    jniRegisterNativeMethods android/graphics/Typeface
    jniRegisterNativeMethods android/graphics/YuvImage
    jniRegisterNativeMethods android/graphics/drawable/AnimatedVectorDrawable
    jniRegisterNativeMethods android/graphics/drawable/VectorDrawable
    jniRegisterNativeMethods android/graphics/fonts/Font$Builder
    jniRegisterNativeMethods android/graphics/fonts/FontFamily$Builder
    jniRegisterNativeMethods android/graphics/pdf/PdfDocument
    jniRegisterNativeMethods android/graphics/pdf/PdfEditor
    jniRegisterNativeMethods android/graphics/pdf/PdfRenderer
    jniRegisterNativeMethods android/graphics/text/MeasuredText
09-19 00:11:00.033 1983-1983/? V/Riru: jniRegisterNativeMethods android/graphics/text/MeasuredText$Builder
09-19 00:11:00.033 1983-1983/? V/Riru: jniRegisterNativeMethods android/graphics/text/LineBreaker
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
09-19 00:11:00.033 1983-1983/? V/Riru: jniRegisterNativeMethods android/database/CursorWindow
    res_idx = 0 chromatix_lib_name[5] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[9] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[10] = chiron_imx386_semco_cpp_snapshot
09-19 00:11:00.033 1983-1983/? V/Riru: jniRegisterNativeMethods android/database/sqlite/SQLiteConnection
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_imx386_semco_zsl_preview
09-19 00:11:00.033 1983-1983/? V/Riru: jniRegisterNativeMethods android/database/sqlite/SQLiteGlobal
    jniRegisterNativeMethods android/database/sqlite/SQLiteDebug
    jniRegisterNativeMethods android/os/Debug
09-19 00:11:00.034 1983-1983/? V/Riru: jniRegisterNativeMethods android/os/FileObserver$ObserverThread
    jniRegisterNativeMethods android/os/GraphicsEnvironment
    jniRegisterNativeMethods android/os/MessageQueue
    jniRegisterNativeMethods android/os/SELinux
    jniRegisterNativeMethods android/os/Trace
    jniRegisterNativeMethods android/os/UEventObserver
    jniRegisterNativeMethods android/net/LocalSocketImpl
    jniRegisterNativeMethods android/net/NetworkUtils
    jniRegisterNativeMethods android/os/MemoryFile
    jniRegisterNativeMethods android/os/SharedMemory
    jniRegisterNativeMethods com/android/internal/os/ClassLoaderFactory
    jniRegisterNativeMethods com/android/internal/os/Zygote
09-19 00:11:00.034 1983-1983/? I/Riru: replaced com.android.internal.os.Zygote#nativeForkAndSpecialize
    replaced com.android.internal.os.Zygote#nativeForkSystemServer
    replaced com.android.internal.os.Zygote#nativeSpecializeAppProcess
09-19 00:11:00.034 1983-1983/? V/Riru: jniRegisterNativeMethods com/android/internal/os/ZygoteInit
    jniRegisterNativeMethods com/android/internal/util/VirtualRefBasePtr
    jniRegisterNativeMethods android/hardware/Camera
    jniRegisterNativeMethods android/hardware/camera2/impl/CameraMetadataNative
    jniRegisterNativeMethods android/hardware/camera2/legacy/LegacyCameraDevice
    jniRegisterNativeMethods android/hardware/camera2/legacy/PerfMeasurement
    jniRegisterNativeMethods android/hardware/camera2/DngCreator
    jniRegisterNativeMethods android/hardware/HardwareBuffer
    jniRegisterNativeMethods android/hardware/SystemSensorManager
    jniRegisterNativeMethods android/hardware/SystemSensorManager$BaseEventQueue
09-19 00:11:00.035 1983-1983/? V/Riru: jniRegisterNativeMethods android/hardware/SerialPort
    jniRegisterNativeMethods android/hardware/soundtrigger/SoundTrigger
    jniRegisterNativeMethods android/hardware/soundtrigger/SoundTriggerModule
    jniRegisterNativeMethods android/hardware/usb/UsbDevice
    jniRegisterNativeMethods android/hardware/usb/UsbDeviceConnection
    jniRegisterNativeMethods android/hardware/usb/UsbRequest
    jniRegisterNativeMethods android/hardware/location/ActivityRecognitionHardware
    jniRegisterNativeMethods android/media/AudioSystem
09-19 00:11:00.035 774-1675/? I/CamDev@1.0-impl: Closing camera 0
09-19 00:11:00.035 774-1675/? I/QCamera: <HAL><INFO> close_camera_device: 1571: [KPI Perf]: E camera id 0
09-19 00:11:00.035 1983-1983/? V/Riru: jniRegisterNativeMethods android/media/AudioSystem
    jniRegisterNativeMethods android/media/AudioPortEventHandler
09-19 00:11:00.036 1983-1983/? V/Riru: jniRegisterNativeMethods android/media/AudioRecord
    jniRegisterNativeMethods android/media/AudioTrack
    jniRegisterNativeMethods android/media/AudioAttributes
09-19 00:11:00.036 1983-1983/? W/zygote: JNI RegisterNativeMethods: attempt to register 0 native methods for android.media.AudioAttributes
09-19 00:11:00.036 1983-1983/? V/Riru: jniRegisterNativeMethods android/media/audiopolicy/AudioProductStrategy
    jniRegisterNativeMethods android/media/audiopolicy/AudioVolumeGroup
    jniRegisterNativeMethods android/media/audiopolicy/AudioVolumeGroupChangeHandler
    jniRegisterNativeMethods android/media/JetPlayer
    jniRegisterNativeMethods android/media/RemoteDisplay
    jniRegisterNativeMethods android/media/ToneGenerator
    jniRegisterNativeMethods android/opengl/Matrix
    jniRegisterNativeMethods android/opengl/Visibility
    jniRegisterNativeMethods android/opengl/GLUtils
    jniRegisterNativeMethods android/opengl/ETC1
    jniRegisterNativeMethods com/android/server/NetworkManagementSocketTagger
    jniRegisterNativeMethods android/ddm/DdmHandleNativeHeap
    jniRegisterNativeMethods android/app/backup/BackupDataInput
    jniRegisterNativeMethods android/app/backup/BackupDataOutput
09-19 00:11:00.037 1983-1983/? V/Riru: jniRegisterNativeMethods android/app/backup/FileBackupHelperBase
    jniRegisterNativeMethods android/app/backup/BackupHelperDispatcher
    jniRegisterNativeMethods android/app/backup/FullBackup
    jniRegisterNativeMethods android/app/Activity
    jniRegisterNativeMethods android/app/ActivityThread
    jniRegisterNativeMethods android/app/NativeActivity
    jniRegisterNativeMethods android/util/jar/StrictJarFile
    jniRegisterNativeMethods android/view/InputChannel
    jniRegisterNativeMethods android/view/InputEventReceiver
    jniRegisterNativeMethods android/view/InputEventSender
    jniRegisterNativeMethods android/view/InputQueue
    jniRegisterNativeMethods android/view/KeyEvent
    jniRegisterNativeMethods android/view/MotionEvent
09-19 00:11:00.038 1983-1983/? V/Riru: jniRegisterNativeMethods android/view/VelocityTracker
    jniRegisterNativeMethods android/content/res/ObbScanner
    jniRegisterNativeMethods android/animation/PropertyValuesHolder
    jniRegisterNativeMethods android/security/Scrypt
    jniRegisterNativeMethods com/android/internal/content/NativeLibraryHelper
    jniRegisterNativeMethods com/android/internal/os/AtomicDirectory
    jniRegisterNativeMethods com/android/internal/os/FuseAppLoop
09-19 00:11:00.039 774-1675/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:11:00.040 774-1675/? I/QCamera: <HAL><INFO> closeCamera: 2351: E
    <HAL><INFO> closeCamera: 2356: [KPI Perf]: E PROFILE_CLOSE_CAMERA camera id 0
09-19 00:11:00.040 774-2023/? E/mm-camera: <SENSOR><ERROR> 711: sensor_pick_resolution: res_idx: 1
09-19 00:11:00.040 774-1310/? E/mm-camera: <IMGLIB><ERROR> 297: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Invalid dimensions 0x0
    <IMGLIB><ERROR> 197: int img_algo_preload(img_base_ops_t *, void *): Preload: Failed to allocate buffer, rc -4
    <IMGLIB><ERROR> 119: module_imgbase_client_preload_exec: IMG_CORE_PRELOAD failed -4
09-19 00:11:00.041 774-1675/? E/Thermal-Lib: pipe write error:9
09-19 00:11:00.041 774-1675/? I/Thermal-Lib: Thermal-Lib-Client: Unregisteration is successfull for handle:1
09-19 00:11:00.043 1983-1983/? I/zygote: Explicit concurrent copying GC freed 303(39KB) AllocSpace objects, 0(0B) LOS objects, 99% free, 24KB/24MB, paused 29us total 2.577ms
09-19 00:11:00.044 1081-1081/? I/Atfwd_Daemon:  Out of sleep...
     TrtyInit: retryCnt: 2
09-19 00:11:00.046 1982-1982/? W/Zygote: Class not found for preloading: android.bluetooth.BluetoothA2dp$2
09-19 00:11:00.047 1983-1983/? I/zygote: Explicit concurrent copying GC freed 5(32KB) AllocSpace objects, 0(0B) LOS objects, 99% free, 24KB/24MB, paused 25us total 3.259ms
09-19 00:11:00.047 1983-1983/? D/Zygote32Timing: PostZygoteInitGC took to complete: 6ms
    ZygoteInit took to complete: 6ms
09-19 00:11:00.048 1982-1982/? I/PackageBackwardCompatibility: Could not find android.content.pm.AndroidTestBaseUpdater, ignoring
09-19 00:11:00.073 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:00.079 1983-1983/? I/Zygote: Accepting command socket connections
09-19 00:11:00.084 774-2066/? E/mm-camera: <IMGLIB><ERROR> 328: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Nothing allocated or already freed!
09-19 00:11:00.160 1982-1982/? E/ActivityRecognitionHardware: activity_recognition HAL is deprecated. class_init is effectively a no-op
09-19 00:11:00.173 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:00.184 1982-1982/? V/Riru: jniRegisterNativeMethods android/media/ImageWriter
    jniRegisterNativeMethods android/media/ImageWriter$WriterSurfaceImage
    jniRegisterNativeMethods android/media/ImageReader
    jniRegisterNativeMethods android/media/ImageReader$SurfaceImage
    jniRegisterNativeMethods android/media/MediaPlayer
    jniRegisterNativeMethods android/media/MediaRecorder
    jniRegisterNativeMethods android/media/MediaScanner
    jniRegisterNativeMethods android/media/MediaMetadataRetriever
    jniRegisterNativeMethods android/media/ResampleInputStream
    jniRegisterNativeMethods android/media/EncoderCapabilities
    jniRegisterNativeMethods android/media/CamcorderProfile
    jniRegisterNativeMethods android/media/DecoderCapabilities
    jniRegisterNativeMethods android/media/CameraProfile
09-19 00:11:00.184 1982-1982/? I/zygote64: Thread[1,tid=1982,Native,Thread*=0x7683e92c00,peer=0x12c022c0,"main"] recursive attempt to load library "libmedia_jni.so"
09-19 00:11:00.184 1982-1982/? V/Riru: jniRegisterNativeMethods android/mtp/MtpDatabase
    jniRegisterNativeMethods android/mtp/MtpPropertyGroup
09-19 00:11:00.184 1982-1982/? D/MtpDeviceJNI: register_android_mtp_MtpDevice
09-19 00:11:00.184 1982-1982/? I/zygote64: Thread[1,tid=1982,Native,Thread*=0x7683e92c00,peer=0x12c022c0,"main"] recursive attempt to load library "libmedia_jni.so"
09-19 00:11:00.184 1982-1982/? V/Riru: jniRegisterNativeMethods android/mtp/MtpDevice
09-19 00:11:00.184 1982-1982/? I/zygote64: Thread[1,tid=1982,Native,Thread*=0x7683e92c00,peer=0x12c022c0,"main"] recursive attempt to load library "libmedia_jni.so"
09-19 00:11:00.184 1982-1982/? V/Riru: jniRegisterNativeMethods android/mtp/MtpServer
    jniRegisterNativeMethods android/media/MediaCodec
09-19 00:11:00.185 1982-1982/? V/Riru: jniRegisterNativeMethods android/media/MediaSync
    jniRegisterNativeMethods android/media/MediaExtractor
    jniRegisterNativeMethods android/media/MediaMuxer
    jniRegisterNativeMethods android/media/MediaCodecList
    jniRegisterNativeMethods android/media/MediaCrypto
    jniRegisterNativeMethods android/media/MediaDrm
    jniRegisterNativeMethods android/media/MediaDescrambler
    jniRegisterNativeMethods android/media/MediaHTTPConnection
09-19 00:11:00.190 1982-1982/? V/Riru: jniRegisterNativeMethods android/media/SoundPool
09-19 00:11:00.191 1982-1982/? W/Zygote: Class not found for preloading: android.media.audiopolicy.AudioProductStrategies
    Class not found for preloading: android.media.audiopolicy.AudioVolumeGroups
09-19 00:11:00.234 1982-1982/? W/Zygote: Class not found for preloading: android.view.-$$Lambda$SurfaceView$Cs7TGTdA1lXf9qW8VOJAfEsMjdk
09-19 00:11:00.237 1982-1982/? W/Zygote: Class not found for preloading: android.view.SurfaceView$3
09-19 00:11:00.239 1982-1982/? W/Zygote: Class not found for preloading: android.view.textclassifier.-$$Lambda$TextClassificationManager$JIaezIJbMig_-kVzN6oArzkTsJE
09-19 00:11:00.245 1982-1982/? W/Zygote: Class not found for preloading: com.android.internal.net.NetworkStatsFactory
09-19 00:11:00.247 1982-1982/? W/Zygote: Class not found for preloading: com.android.internal.telephony.-$$Lambda$PhoneSubInfoController$8HFbCDJDN1mrLJG980qYH5MGqMk
    Class not found for preloading: com.android.internal.telephony.-$$Lambda$PhoneSubInfoController$U28a_EGx2cvmQhDfRRgonMt5Zrc
    Class not found for preloading: com.android.internal.telephony.-$$Lambda$SubscriptionInfoUpdater$-zZXM9oMRZ3vZz7dJOG19J00Bmw
    Class not found for preloading: com.android.internal.telephony.-$$Lambda$SubscriptionInfoUpdater$D5yF1HbS4cvCyoAj3FESkPtA_0g
    Class not found for preloading: com.android.internal.telephony.-$$Lambda$SubscriptionInfoUpdater$MMx9iQX0JVqqMPLTUZhdBubFSzU
09-19 00:11:00.249 1982-1982/? W/Zygote: Class not found for preloading: com.android.internal.telephony.NewNitzStateMachine$1
    Class not found for preloading: com.android.internal.telephony.NewNitzStateMachine
    Class not found for preloading: com.android.internal.telephony.NewTimeServiceHelper$1
    Class not found for preloading: com.android.internal.telephony.NewTimeServiceHelper$Listener
    Class not found for preloading: com.android.internal.telephony.NewTimeServiceHelper
    Class not found for preloading: com.android.internal.telephony.PhoneConfigurationModels
09-19 00:11:00.250 1982-1982/? W/Zygote: Class not found for preloading: com.android.internal.telephony.SubscriptionController$ScLocalLog
    Class not found for preloading: com.android.internal.telephony.UiccSmsController
    Class not found for preloading: com.android.internal.telephony.dataconnection.DcController$2
09-19 00:11:00.273 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:00.275 1982-1982/? I/Zygote: ...preloaded 7582 classes in 257ms.
09-19 00:11:00.275 1982-1982/? I/zygote64: VMRuntime.preloadDexCaches starting
09-19 00:11:00.297 1982-1982/? I/zygote64: VMRuntime.preloadDexCaches strings total=332856 before=9849 after=9849
    VMRuntime.preloadDexCaches types total=36368 before=7357 after=7626
    VMRuntime.preloadDexCaches fields total=162783 before=8038 after=8239
    VMRuntime.preloadDexCaches methods total=285088 before=11193 after=11625
    VMRuntime.preloadDexCaches finished
09-19 00:11:00.297 1982-1982/? D/Zygote64Timing: PreloadClasses took to complete: 280ms
09-19 00:11:00.293 1982-1982/? W/main: type=1400 audit(0.0:97): avc: denied { write } for name="/" dev="tmpfs" ino=23802 scontext=u:r:zygote:s0 tcontext=u:object_r:system_file:s0 tclass=dir permissive=0
09-19 00:11:00.299 1982-1982/? I/zygote64: The ClassLoaderContext is a special shared library.
09-19 00:11:00.300 1982-1982/? D/ApplicationLoaders: Created zygote-cached class loader: /system/framework/android.hidl.base-V1.0-java.jar
09-19 00:11:00.297 1982-1982/? W/main: type=1400 audit(0.0:98): avc: denied { write } for name="/" dev="tmpfs" ino=23802 scontext=u:r:zygote:s0 tcontext=u:object_r:system_file:s0 tclass=dir permissive=0
09-19 00:11:00.301 1982-1982/? I/zygote64: The ClassLoaderContext is a special shared library.
09-19 00:11:00.303 1982-1982/? D/ApplicationLoaders: Created zygote-cached class loader: /system/framework/android.hidl.manager-V1.0-java.jar
09-19 00:11:00.303 1982-1982/? D/Zygote64Timing: CacheNonBootClasspathClassLoaders took to complete: 5ms
09-19 00:11:00.335 774-1675/? E/mm-camera: <MCT   ><ERROR> 179: stop_sof_check_thread: Returning as SOF timer thread not yet initialized
09-19 00:11:00.335 1985-1985/? W/CameraProviderManager: Camera provider legacy/0 says an unknown camera device@1.0/legacy/0 now has torch status 1. Curious.
09-19 00:11:00.336 1985-1985/? W/CameraProviderManager: Camera provider legacy/0 says an unknown camera device@3.3/legacy/0 now has torch status 1. Curious.
09-19 00:11:00.336 774-1675/? I/QCamera: <HAL><INFO> closeCamera: 2431: [KPI Perf]: X PROFILE_CLOSE_CAMERA camera id 0, rc: 0
09-19 00:11:00.336 774-1675/? D/MIPreview: stopAnalyzeThread: stopAnalyzeThread BEGIN
    stopAnalyzeThread: stopAnalyzeThread END
09-19 00:11:00.337 774-1675/? I/QCamera: <HAL><INFO> close_camera_device: 1573: [KPI Perf]: X
09-19 00:11:00.337 1985-1985/? I/CameraProviderManager: Enumerating new camera device: device@3.3/legacy/0
09-19 00:11:00.338 1985-1985/? E/CameraProviderManager: DeviceInfo3: Converted ICameraDevice instance to nullptr
09-19 00:11:00.338 1985-1985/? I/CameraProviderManager: Enumerating new camera device: device@1.0/legacy/1
09-19 00:11:00.339 774-774/? I/CamDev@1.0-impl: Opening camera 1
09-19 00:11:00.339 774-774/? I/QCamera: <HAL><INFO> openLegacy: 503: openLegacy halVersion: 256 cameraId = 1
09-19 00:11:00.340 774-774/? D/vndksupport: Loading /vendor/lib/hw/power.default.so from current namespace instead of sphal namespace.
09-19 00:11:00.346 774-774/? E/Watermark: getFontData Font file does not exist!
    getFontData Get file status failed
    getFontData Font file does not exist!
    getFontData Get file status failed
09-19 00:11:00.346 774-774/? I/QCamera: <HAL><INFO> openCamera: 1923: [KPI Perf]: E PROFILE_OPEN_CAMERA camera id 1
09-19 00:11:00.347 774-774/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:11:00.347 774-774/? D/QCamera: Debug log file is not enabled
09-19 00:11:00.366 1982-1982/? I/Zygote: Preloading resources...
09-19 00:11:00.369 774-774/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:11:00.369 774-774/? I/chatty: uid=1047(cameraserver) provider@2.4-se identical 3 lines
09-19 00:11:00.369 774-774/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:11:00.371 1982-1982/? W/Resources: Preloaded drawable resource #0x108027e (android:drawable/dialog_background_material) that varies with configuration!!
09-19 00:11:00.372 774-2082/? E/QCamera: <HAL><ERROR> calcThermalLevel: 10178: level: 0, preview minfps 7000.000000, preview maxfpS 30000.000000, video minfps 7000.000000, video maxfps 30000.000000
    <HAL><ERROR> calcThermalLevel: 10183: level change to -> 0
    <HAL><ERROR> calcThermalLevel: 10262: Adjusted preview minfps 7.000000, preview maxfpS 30.000000, video minfps 7.000000, video maxfps 30.000000
09-19 00:11:00.373 774-2082/? E/QCameraParameters: setOISValue9690 OISEnabled=1 
    res_idx = 0 chromatix_lib_name[1] = chiron_ov5675_primax_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_ov5675_primax_common
    res_idx = 0 chromatix_lib_name[4] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[8] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[9] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[10] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[11] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[12] = chiron_ov5675_primax_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_ov5675_primax_zsl_preview
    res_idx = 0 chromatix_lib_name[0] = chiron_ov5675_primax_snapshot
    res_idx = 0 chromatix_lib_name[1] = chiron_ov5675_primax_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_ov5675_primax_common
    res_idx = 0 chromatix_lib_name[3] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[8] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[9] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[10] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[11] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[12] = chiron_ov5675_primax_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_ov5675_primax_zsl_preview
09-19 00:11:00.374 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
    res_idx = 0 chromatix_lib_name[1] = chiron_ov5675_primax_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_ov5675_primax_common
    res_idx = 0 chromatix_lib_name[4] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_ov5675_primax_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[8] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[9] = chiron_ov5675_primax_cpp_ds_chromatix
    res_idx = 0 chromatix_lib_name[10] = chiron_ov5675_primax_cpp_us_chromatix
    res_idx = 0 chromatix_lib_name[11] = chiron_ov5675_primax_cpp_preview
    res_idx = 0 chromatix_lib_name[12] = chiron_ov5675_primax_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_ov5675_primax_zsl_preview
09-19 00:11:00.377 774-774/? I/Thermal-Lib: Thermal-Lib-Client: Registration successful for camera with handle:1
09-19 00:11:00.377 774-774/? I/QCamera: <HAL><INFO> openCamera: 1938: [KPI Perf]: X PROFILE_OPEN_CAMERA camera id 1, rc: 0
09-19 00:11:00.379 774-774/? I/CamDev@1.0-impl: could not cast ICameraDeviceCallback to IQCameraDeviceCallback
09-19 00:11:00.380 774-1675/? I/CamDev@1.0-impl: Closing camera 1
09-19 00:11:00.381 774-1675/? I/QCamera: <HAL><INFO> close_camera_device: 1571: [KPI Perf]: E camera id 1
09-19 00:11:00.381 1982-1982/? I/Zygote: ...preloaded 64 resources in 14ms.
09-19 00:11:00.384 774-1675/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:11:00.384 1982-1982/? I/Zygote: ...preloaded 41 resources in 3ms.
09-19 00:11:00.384 1982-1982/? D/Zygote64Timing: PreloadResources took to complete: 81ms
09-19 00:11:00.384 774-1675/? I/QCamera: <HAL><INFO> closeCamera: 2351: E
    <HAL><INFO> closeCamera: 2356: [KPI Perf]: E PROFILE_CLOSE_CAMERA camera id 1
09-19 00:11:00.385 774-2084/? E/mm-camera: <SENSOR><ERROR> 711: sensor_pick_resolution: res_idx: 2
09-19 00:11:00.385 774-1310/? E/mm-camera: <IMGLIB><ERROR> 297: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Invalid dimensions 0x0
    <IMGLIB><ERROR> 197: int img_algo_preload(img_base_ops_t *, void *): Preload: Failed to allocate buffer, rc -4
    <IMGLIB><ERROR> 119: module_imgbase_client_preload_exec: IMG_CORE_PRELOAD failed -4
09-19 00:11:00.385 774-1675/? E/Thermal-Lib: pipe write error:9
09-19 00:11:00.386 774-1675/? I/Thermal-Lib: Thermal-Lib-Client: Unregisteration is successfull for handle:1
09-19 00:11:00.393 1982-1982/? D/libEGL: loaded /vendor/lib64/egl/libEGL_adreno.so
09-19 00:11:00.396 774-2116/? E/mm-camera: <IMGLIB><ERROR> 328: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Nothing allocated or already freed!
09-19 00:11:00.396 774-1675/? E/mm-camera: <MCT   ><ERROR> 179: stop_sof_check_thread: Returning as SOF timer thread not yet initialized
09-19 00:11:00.397 774-1675/? I/QCamera: <HAL><INFO> closeCamera: 2431: [KPI Perf]: X PROFILE_CLOSE_CAMERA camera id 1, rc: 0
09-19 00:11:00.397 774-1675/? D/MIPreview: stopAnalyzeThread: stopAnalyzeThread BEGIN
    stopAnalyzeThread: stopAnalyzeThread END
09-19 00:11:00.398 1982-1982/? D/libEGL: loaded /vendor/lib64/egl/libGLESv1_CM_adreno.so
09-19 00:11:00.399 774-1675/? I/QCamera: <HAL><INFO> close_camera_device: 1573: [KPI Perf]: X
09-19 00:11:00.399 1985-1985/? I/CameraProviderManager: Enumerating new camera device: device@3.3/legacy/1
09-19 00:11:00.400 1985-1985/? E/CameraProviderManager: DeviceInfo3: Converted ICameraDevice instance to nullptr
09-19 00:11:00.400 1985-1985/? I/CameraProviderManager: Camera provider legacy/0 ready with 4 camera devices
09-19 00:11:00.400 1985-1985/? I/CameraService: onDeviceStatusChanged: Status changed for cameraId=1, newStatus=1
    onDeviceStatusChanged: Unknown camera ID 1, a new camera is added
09-19 00:11:00.401 1982-1982/? D/libEGL: loaded /vendor/lib64/egl/libGLESv2_adreno.so
09-19 00:11:00.401 1985-1985/? I/CameraService: onDeviceStatusChanged: Status changed for cameraId=0, newStatus=1
    onDeviceStatusChanged: Unknown camera ID 0, a new camera is added
09-19 00:11:00.401 1985-2018/? W/CameraProviderManager: addProviderLocked: Camera provider HAL with name 'legacy/0' already registered
09-19 00:11:00.412 1982-1982/? I/Zygote: Preloading shared libraries...
09-19 00:11:00.415 1982-1982/? I/Zygote: Called ZygoteHooks.endPreload()
09-19 00:11:00.416 1982-1982/? I/Zygote: Installed AndroidKeyStoreProvider in 0ms.
09-19 00:11:00.420 1982-1982/? I/Zygote: Warmed up JCA providers in 4ms.
09-19 00:11:00.420 1982-1982/? D/Zygote: end preload
09-19 00:11:00.420 1982-1982/? D/Zygote64Timing: ZygotePreload took to complete: 407ms
09-19 00:11:00.437 1982-1982/? I/zygote64: Explicit concurrent copying GC freed 63564(3547KB) AllocSpace objects, 17(408KB) LOS objects, 90% free, 2571KB/26MB, paused 35us total 17.095ms
09-19 00:11:00.453 1982-1982/? I/zygote64: Explicit concurrent copying GC freed 6272(213KB) AllocSpace objects, 0(0B) LOS objects, 91% free, 2389KB/26MB, paused 16us total 11.029ms
09-19 00:11:00.453 1982-1982/? D/Zygote64Timing: PostZygoteInitGC took to complete: 33ms
    ZygoteInit took to complete: 440ms
09-19 00:11:00.474 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:00.484 1989-1989/? W/sound_trigger_platform: load_acdb: acdb_loader_send_listen_device_cal_v1 not found. undefined symbol: acdb_loader_send_listen_device_cal_v1
    load_acdb: acdb_loader_send_listen_lsm_cal_v1 not found. undefined symbol: acdb_loader_send_listen_lsm_cal_v1
09-19 00:11:00.484 1989-1989/? I/audio_hw_extn: audio_extn_set_snd_card_split: snd_card_name(msm8998-tasha-snd-card) device(msm8998) snd_card(tasha) form_factor(snd)
09-19 00:11:00.485 1989-1989/? E/platform_info: param tag only supported with CONFIG_PARAMS section
09-19 00:11:00.485 1989-1989/? I/chatty: uid=1041(audioserver) audio@2.0-servi identical 7 lines
09-19 00:11:00.485 1989-1989/? E/platform_info: param tag only supported with CONFIG_PARAMS section
09-19 00:11:00.486 1989-1989/? E/audio_hw_acdb: acdb_init_v2: dlsym error undefined symbol: acdb_loader_init_v4 for acdb_loader_init_v4
09-19 00:11:00.486 1989-1989/? D/ACDB-LOADER: ACDB -> Load file: /vendor/etc/acdbdata/adsp_avs_config.acdb
    ACDB -> found 1 form factor & soundcard independant files
09-19 00:11:00.486 1989-1989/? I/ACDB-LOADER: ACDB -> Info: ACDB file path is /vendor/etc/acdbdata/Forte
09-19 00:11:00.487 1989-1989/? D/ACDB-LOADER: ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_Bluetooth_cal.acdb
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_Speaker_cal.acdb
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_Handset_cal.acdb
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_Headset_cal.acdb
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_General_cal.acdb
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_workspaceFile.qwsp
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_Hdmi_cal.acdb
    ACDB -> Load file: /vendor/etc/acdbdata/Forte/Forte_Global_cal.acdb
09-19 00:11:00.487 1989-1989/? I/ACDB-LOADER: ACDB -> Info: Loaded ForteMedia ACDB!
09-19 00:11:00.487 1989-1989/? D/ACDB-LOADER: ACDB -> ACDB_CMD_INITIALIZE_V2
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 4074175488, ACDB File Minor = 2492629821, ACDB File Revision = 0
    [ACDB Command]->SW Minor/Major/Revision version info for /vendor/etc/acdbdata/Forte/Forte_Bluetooth_cal.acdb
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
    [ACDB Command]->SW Minor/Major/Revision version info for /vendor/etc/acdbdata/Forte/Forte_Speaker_cal.acdb
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
    [ACDB Command]->SW Minor/Major/Revision version info for /vendor/etc/acdbdata/Forte/Forte_Headset_cal.acdb
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
    [ACDB Command]->SW Minor/Major/Revision version info for /vendor/etc/acdbdata/Forte/Forte_General_cal.acdb
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
    [ACDB Command]->SW Minor/Major/Revision version info for /vendor/etc/acdbdata/Forte/Forte_workspaceFile.qwsp
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
    [ACDB Command]->SW Minor/Major/Revision version info for /vendor/etc/acdbdata/Forte/Forte_Hdmi_cal.acdb
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
    [ACDB Command]->SW Minor/Major/Revision version info for /vendor/etc/acdbdata/Forte/Forte_Global_cal.acdb
    [ACDB Command]->ACDB Sw Major = 9, ACDB Sw Minor = 0, ACDB Sw Revision = 4, ACDB Sw Cpl Number = 0
    [ACDB Command]->ACDB File Major = 9, ACDB File Minor = 0, ACDB File Revision = 10
09-19 00:11:00.489 1989-1989/? D/ACDB-LOADER: ACDB -> ACPH INIT
09-19 00:11:00.489 1989-1989/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    diag: In diagpkt_tbl_reg, service not initialized.
09-19 00:11:00.489 1989-1989/? D/ACDB-LOADER: ACDB -> RTAC INIT
09-19 00:11:00.489 1989-1989/? D/ACDB-LOADER: ACDB -> MCS, FTS INIT
09-19 00:11:00.489 1989-1989/? E/ACDB-MCS: acdb_mcs_init: /vendor/etc/audio_tuning_mixer_tasha.txt not present, using /vendor/etc/audio_tuning_mixer.txt config file
09-19 00:11:00.489 1989-1989/? E/MCS-RT-CTL: Can't open the configuration file /vendor/etc/audio_tuning_mixer.txt.
09-19 00:11:00.489 1989-1989/? E/ACDB-MCS: acdb_mcs_init: MCS routing control initialization failed.
09-19 00:11:00.489 1989-1989/? D/ACDB-LOADER: ACDB -> ADIE RTAC INIT
09-19 00:11:00.489 1989-1989/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_VOC_PROC_DYNAMIC_TABLE_SIZE
09-19 00:11:00.495 1989-1989/? D/ACDB-LOADER: ACDB -> send_common_custom_topology
    ACDB -> ACDB_CMD_GET_AVCS_CUSTOM_TOPO_INFO_SIZE
    ACDB -> ACDB_CMD_GET_AVCS_CUSTOM_TOPO_INFO
    ACDB -> ACDB_CMD_GET_AVCS_CUSTOM_TOPO_INFO: size:0x4ac ret=0 
    ACDB -> CORE_CUSTOM_TOPOLOGIES
09-19 00:11:00.499 1989-1989/? D/ACDB-LOADER: ACDB -> acdb_loader_send_common_custom_topology: Common custom topology in use
    ACDB -> init done!
09-19 00:11:00.499 1989-1989/? D/audio_hw_acdb: acdb_init_v2: ACDB Instance ID support after ACDB init:0
09-19 00:11:00.499 1989-1989/? D/sound_trigger_platform: platform_stdev_init: Opening device /dev/snd/hwC0D1000
    get_codec_version: codec version WCD9335_2_0
09-19 00:11:00.500 1989-1989/? I/SoundTriggerHw: onFirstRef() mModuleName primary mHwDevice 0xf2d82000
09-19 00:11:00.501 1989-1989/? I/ServiceManagement: Registered android.hardware.soundtrigger@2.2::ISoundTriggerHw/default (start delay of 739ms)
09-19 00:11:00.501 1989-1989/? I/audiohalservice: Registration complete for android.hardware.soundtrigger@2.2::ISoundTriggerHw/default.
09-19 00:11:00.501 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.bluetooth.audio@2.0::IBluetoothAudioProvidersFactory/default in either framework or device manifest.
09-19 00:11:00.501 1989-1989/? E/audiohalservice: Could not get passthrough implementation for android.hardware.bluetooth.audio@2.0::IBluetoothAudioProvidersFactory/default.
09-19 00:11:00.502 1989-1989/? W/audiohalservice: Could not register Bluetooth Audio API 2.0
09-19 00:11:00.502 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.bluetooth.a2dp@1.0::IBluetoothAudioOffload/default in either framework or device manifest.
09-19 00:11:00.502 1989-1989/? E/audiohalservice: Could not get passthrough implementation for android.hardware.bluetooth.a2dp@1.0::IBluetoothAudioOffload/default.
09-19 00:11:00.502 1989-1989/? W/audiohalservice: Could not register Bluetooth audio offload 1.0
09-19 00:11:00.508 882-979/? I/QC-NETMGR-LIB: NetmgrNetdClientRegisterNetwork(): Looking for Netd service
    NetmgrNetdClientRegisterNetwork(): register to create new OEM network
    registerNetwork(): Attempting createOemNetwork
09-19 00:11:00.508 1987-2014/? D/TcpSocketMonitor: suspending tcpinfo polling
09-19 00:11:00.509 882-979/? I/QC-NETMGR-LIB: registerNetwork(): command completed!
    registerNetwork(): createOemNetwork succeeded [packet mark : 0xf0002] [net id : 2] [network handle : 0x2cafed00d]
    NetmgrNetdClientRegisterNetwork(): [packet mark : 0xf0002] [network handle : 0x2cafed00d]
09-19 00:11:00.507 1982-1982/? W/main: type=1400 audit(0.0:99): avc: denied { write } for name="/" dev="tmpfs" ino=23802 scontext=u:r:zygote:s0 tcontext=u:object_r:system_file:s0 tclass=dir permissive=0
09-19 00:11:00.513 1982-1982/? W/main: type=1400 audit(0.0:100): avc: denied { write } for name="/" dev="tmpfs" ino=23802 scontext=u:r:zygote:s0 tcontext=u:object_r:system_file:s0 tclass=dir permissive=0
09-19 00:11:00.530 1982-1982/? W/main: type=1400 audit(0.0:101): avc: denied { write } for name="/" dev="tmpfs" ino=23802 scontext=u:r:zygote:s0 tcontext=u:object_r:system_file:s0 tclass=dir permissive=0
09-19 00:11:00.544 1982-1982/? W/SandHook-Native: JNI Loaded
09-19 00:11:00.549 1982-1982/? W/zygote64: Core platform API violation: Ljava/lang/Class;->accessFlags:I from Lcom/elderdrivers/riru/edxp/sandhook/config/SandHookProvider; using JNI
09-19 00:11:00.552 1989-1993/? E/audio_route: Control 'MultiMedia4 Mixer MI2S_TX' doesn't exist - skipping
    Control 'MultiMedia7 Mixer MI2S_TX' doesn't exist - skipping
    Control 'MultiMedia10 Mixer MI2S_TX' doesn't exist - skipping
    Control 'MultiMedia11 Mixer MI2S_TX' doesn't exist - skipping
    Control 'MultiMedia12 Mixer MI2S_TX' doesn't exist - skipping
    Control 'MultiMedia13 Mixer MI2S_TX' doesn't exist - skipping
    Control 'MultiMedia14 Mixer MI2S_TX' doesn't exist - skipping
09-19 00:11:00.553 1989-1993/? E/audio_route: Control 'MultiMedia15 Mixer MI2S_TX' doesn't exist - skipping
09-19 00:11:00.554 1989-1993/? E/audio_route: Control 'QUAT_MI2S_RX Audio Mixer MultiMedia9' doesn't exist - skipping
09-19 00:11:00.556 1989-1993/? E/audio_route: Control 'SpkrLeft COMP Switch' doesn't exist - skipping
    Control 'SpkrRight COMP Switch' doesn't exist - skipping
    Control 'SpkrLeft BOOST Switch' doesn't exist - skipping
    Control 'SpkrRight BOOST Switch' doesn't exist - skipping
09-19 00:11:00.557 1989-1993/? E/audio_route: Control 'SpkrLeft VISENSE Switch' doesn't exist - skipping
    Control 'SpkrRight VISENSE Switch' doesn't exist - skipping
    Control 'SpkrLeft SWR DAC_Port Switch' doesn't exist - skipping
    Control 'SpkrRight SWR DAC_Port Switch' doesn't exist - skipping
09-19 00:11:00.560 1989-1993/? E/audio_route: Control 'SpkrLeft WSA PA Gain' doesn't exist - skipping
09-19 00:11:00.561 1989-1993/? E/audio_route: Control 'LSM1 MUX' doesn't exist - skipping
    Control 'LSM2 MUX' doesn't exist - skipping
    Control 'LSM3 MUX' doesn't exist - skipping
    Control 'LSM4 MUX' doesn't exist - skipping
    Control 'LSM5 MUX' doesn't exist - skipping
    Control 'LSM6 MUX' doesn't exist - skipping
    Control 'LSM7 MUX' doesn't exist - skipping
    Control 'LSM8 MUX' doesn't exist - skipping
09-19 00:11:00.561 1982-1982/? W/zygote64: Core platform API violation: Ljava/lang/ClassLoader;->parent:Ljava/lang/ClassLoader; from Lde/robv/android/xposed/XposedHelpers; using reflection
09-19 00:11:00.564 1989-1993/? E/audio_route: unable to find sub path 'audio-ull-playback speaker-safe'
09-19 00:11:00.564 1989-1993/? I/chatty: uid=1041(audioserver) HwBinder:1989_2 identical 3 lines
09-19 00:11:00.564 1989-1993/? E/audio_route: unable to find sub path 'audio-ull-playback speaker-safe'
09-19 00:11:00.563 1982-1982/? W/main: type=1400 audit(0.0:102): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:00.572 1989-1993/? E/audio_route: Control 'MultiMedia8 Mixer SLIM_8_TX' doesn't exist - skipping
09-19 00:11:00.573 1989-1993/? E/audio_route: Control 'AUX PCM SampleRate' doesn't exist - skipping
09-19 00:11:00.575 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:00.573 1982-1982/? W/main: type=1400 audit(0.0:104): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:00.577 1989-1993/? E/audio_route: Control 'LSM1 MUX' doesn't exist - skipping
09-19 00:11:00.578 1989-1993/? E/audio_route: Control 'LSM2 MUX' doesn't exist - skipping
    Control 'LSM3 MUX' doesn't exist - skipping
    Control 'LSM4 MUX' doesn't exist - skipping
    Control 'LSM5 MUX' doesn't exist - skipping
    Control 'LSM6 MUX' doesn't exist - skipping
    Control 'LSM7 MUX' doesn't exist - skipping
09-19 00:11:00.579 1989-1993/? E/audio_route: Control 'LSM8 MUX' doesn't exist - skipping
    Control 'SLIM_1_RX Channels' doesn't exist - skipping
    Control 'SLIM_1_RX SampleRate' doesn't exist - skipping
    Control 'SLIM_1_TX SampleRate' doesn't exist - skipping
09-19 00:11:00.581 1989-1993/? E/audio_route: Control 'SpkrLeft COMP Switch' doesn't exist - skipping
    Control 'SpkrLeft BOOST Switch' doesn't exist - skipping
    Control 'SpkrLeft VISENSE Switch' doesn't exist - skipping
    Control 'SpkrLeft SWR DAC_Port Switch' doesn't exist - skipping
09-19 00:11:00.583 1989-1993/? E/audio_route: Control 'SpkrLeft SWR DAC_Port Switch' doesn't exist - skipping
    Control 'SpkrLeft WSA PA Gain' doesn't exist - skipping
09-19 00:11:00.588 1989-1993/? E/audio_route: unable to find sub path 'audio-ull-playback speaker-safe'
09-19 00:11:00.591 1989-1993/? D/msm8974_platform: Opening /sys/class/thermal/thermal_zone0/type
    Opening /sys/class/thermal/thermal_zone1/type
    Opening /sys/class/thermal/thermal_zone2/type
    Opening /sys/class/thermal/thermal_zone3/type
    Opening /sys/class/thermal/thermal_zone4/type
    Opening /sys/class/thermal/thermal_zone5/type
09-19 00:11:00.592 1989-1993/? D/msm8974_platform: Opening /sys/class/thermal/thermal_zone6/type
    Opening /sys/class/thermal/thermal_zone7/type
    Opening /sys/class/thermal/thermal_zone8/type
    Opening /sys/class/thermal/thermal_zone9/type
    Opening /sys/class/thermal/thermal_zone10/type
    Opening /sys/class/thermal/thermal_zone11/type
    Opening /sys/class/thermal/thermal_zone12/type
    Opening /sys/class/thermal/thermal_zone13/type
    Opening /sys/class/thermal/thermal_zone14/type
    Opening /sys/class/thermal/thermal_zone15/type
    Opening /sys/class/thermal/thermal_zone16/type
    Opening /sys/class/thermal/thermal_zone17/type
    Opening /sys/class/thermal/thermal_zone18/type
    Opening /sys/class/thermal/thermal_zone19/type
    Opening /sys/class/thermal/thermal_zone20/type
    Opening /sys/class/thermal/thermal_zone21/type
    Opening /sys/class/thermal/thermal_zone22/type
09-19 00:11:00.593 1989-1993/? D/msm8974_platform: Opening /sys/class/thermal/thermal_zone23/type
    Opening /sys/class/thermal/thermal_zone24/type
    Opening /sys/class/thermal/thermal_zone25/type
    Opening /sys/class/thermal/thermal_zone26/type
    Opening /sys/class/thermal/thermal_zone27/type
    Opening /sys/class/thermal/thermal_zone28/type
    Opening /sys/class/thermal/thermal_zone29/type
    Opening /sys/class/thermal/thermal_zone30/type
    Opening /sys/class/thermal/thermal_zone31/type
    Opening /sys/class/thermal/thermal_zone32/type
    Opening /sys/class/thermal/thermal_zone33/type
    Opening /sys/class/thermal/thermal_zone34/type
    Opening /sys/class/thermal/thermal_zone35/type
    Opening /sys/class/thermal/thermal_zone36/type
    Opening /sys/class/thermal/thermal_zone37/type
09-19 00:11:00.593 1989-1993/? D/audio_hw_extn: audio_extn_can_use_vbat: vbat.enabled property is set to 0
    audio_extn_can_use_bcl: bcl.enabled property is set to 0
09-19 00:11:00.593 1989-1993/? D/msm8974_platform: Alac software decoder is available...removing alac from DSP decoder list
    APE software decoder is available...removing ape from DSP decoder list
09-19 00:11:00.593 1989-1993/? I/audio_hw_extn: audio_extn_set_snd_card_split: snd_card_name(msm8998-tasha-snd-card) device(msm8998) snd_card(tasha) form_factor(snd)
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_OUT_HEADPHONES_NATIVE_44_1
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_OUT_HEADPHONES_NATIVE_44_1 in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_OUT_HIFI_HEADPHONES
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_OUT_HIFI_HEADPHONES in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_OUT_HIFI_HEADPHONES_44_1
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_OUT_HIFI_HEADPHONES_44_1 in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_OUT_HIFI_HEADPHONES_NATIVE_44_1
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_OUT_HIFI_HEADPHONES_NATIVE_44_1 in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_MAIN_MIC
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_MAIN_MIC in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_TOP_MIC
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_TOP_MIC in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_FRONT_MIC
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_FRONT_MIC in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_HANDSET_DMIC_MUSIC
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_HANDSET_DMIC_MUSIC in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_HANDSET_DMIC_VOICE
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_HANDSET_DMIC_VOICE in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_HANDSET_DMIC_INTERVIEW
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_HANDSET_DMIC_INTERVIEW in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_HANDSET_DMIC_HD
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_HANDSET_DMIC_HD in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_VOICE_SPEAKER_TMIC_CONF
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_VOICE_SPEAKER_TMIC_CONF in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_CAMCORDER_DMIC
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_CAMCORDER_DMIC in platform info xml not found, no ACDB ID set!
09-19 00:11:00.594 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_CAMCORDER_TMIC
09-19 00:11:00.594 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_CAMCORDER_TMIC in platform info xml not found, no ACDB ID set!
09-19 00:11:00.595 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_CAMCORDER_TMIC_FAR_END
09-19 00:11:00.595 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_CAMCORDER_TMIC_FAR_END in platform info xml not found, no ACDB ID set!
09-19 00:11:00.595 1989-1993/? E/msm8974_platform: find_index: Could not find index for name = SND_DEVICE_IN_CAMCORDER_TMIC_NEAR_END
09-19 00:11:00.595 1989-1993/? E/platform_info: process_acdb_id: Device SND_DEVICE_IN_CAMCORDER_TMIC_NEAR_END in platform info xml not found, no ACDB ID set!
09-19 00:11:00.595 1989-1993/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:11:00.595 1989-1993/? I/chatty: uid=1041(audioserver) HwBinder:1989_2 identical 2 lines
09-19 00:11:00.595 1989-1993/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:11:00.595 1989-1993/? D/msm8974_platform: native_audio_set_params:napb updating mode (1) from XML
    platform_set_native_support:napb: native audio playback enabled in (SRC) mode
09-19 00:11:00.595 1989-1993/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:11:00.595 1989-1993/? D/msm8974_platform: native_audio_set_params:napb updating mode (1) from XML
    platform_set_native_support:napb: native audio playback enabled in (SRC) mode
09-19 00:11:00.595 1989-1993/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:11:00.595 1989-1993/? D/msm8974_platform: native_audio_set_params:napb updating mode (1) from XML
    platform_set_native_support:napb: native audio playback enabled in (SRC) mode
09-19 00:11:00.595 1989-1993/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:11:00.595 1989-1993/? D/msm8974_platform: native_audio_set_params:napb updating mode (1) from XML
    platform_set_native_support:napb: native audio playback enabled in (SRC) mode
09-19 00:11:00.595 1989-1993/? V/audio_hw_usb: usb_set_sidetone_gain: sidetone gain(35) decimal 3162
09-19 00:11:00.595 1989-1993/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:11:00.595 1989-1993/? D/msm8974_platform: native_audio_set_params:napb updating mode (1) from XML
    platform_set_native_support:napb: native audio playback enabled in (SRC) mode
09-19 00:11:00.595 1989-1993/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:11:00.595 1989-1993/? D/msm8974_platform: platform_set_snd_device_backend: backend_tag_table[headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[9] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[headphones-hifi-filter]: old = headphones-hifi-filter new = headphones
    platform_set_snd_device_backend: hw_interface_table[11] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[bt-sco-headset-wb]: old = bt-sco-wb new = bt-sco-wb
    platform_set_snd_device_backend: hw_interface_table[34] = SLIMBUS_7_RX
    platform_set_snd_device_backend: backend_tag_table[bt-sco-headset]: old = bt-sco new = bt-sco
    platform_set_snd_device_backend: hw_interface_table[33] = SLIMBUS_7_RX
    platform_set_snd_device_backend: backend_tag_table[bt-a2dp]: old = bt-a2dp new = bt-a2dp
    platform_set_snd_device_backend: hw_interface_table[36] = SLIMBUS_7_RX
    platform_set_snd_device_backend: backend_tag_table[line]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[8] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[anc-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[69] = SLIMBUS_6_RX
09-19 00:11:00.596 1989-1993/? D/msm8974_platform: platform_set_snd_device_backend: backend_tag_table[anc-fb-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[70] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[handset]: old = null new = receiver
    platform_set_snd_device_backend: hw_interface_table[1] = QUAT_MI2S_RX
    platform_set_snd_device_backend: backend_tag_table[voice-handset]: old = null new = receiver
    platform_set_snd_device_backend: hw_interface_table[20] = QUAT_MI2S_RX
    platform_set_snd_device_backend: backend_tag_table[speaker]: old = null new = speaker
    platform_set_snd_device_backend: hw_interface_table[2] = QUAT_MI2S_RX
    platform_set_snd_device_backend: backend_tag_table[voice-speaker]: old = null new = speaker
    platform_set_snd_device_backend: hw_interface_table[21] = QUAT_MI2S_RX
    platform_set_snd_device_backend: backend_tag_table[voice-speaker-2]: old = null new = speaker
    platform_set_snd_device_backend: hw_interface_table[24] = QUAT_MI2S_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-headphones]: old = null new = speaker-and-headphones
    platform_set_snd_device_backend: hw_interface_table[13] = QUAT_MI2S_RX-and-SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-headphones-hifi-filter]: old = speaker-and-headphones-hifi-filter new = speaker-and-headphones
    platform_set_snd_device_backend: hw_interface_table[14] = QUAT_MI2S_RX-and-SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-line]: old = null new = speaker-and-headphones
    platform_set_snd_device_backend: hw_interface_table[16] = QUAT_MI2S_RX-and-SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-anc-headphones]: old = null new = speaker-and-headphones
    platform_set_snd_device_backend: hw_interface_table[73] = QUAT_MI2S_RX-and-SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-anc-fb-headphones]: old = null new = speaker-and-headphones
    platform_set_snd_device_backend: hw_interface_table[74] = QUAT_MI2S_RX-and-SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-hdmi]: old = speaker-and-hdmi new = speaker-and-hdmi
    platform_set_snd_device_backend: hw_interface_table[30] = QUAT_MI2S_RX-and-HDMI
    platform_set_snd_device_backend: backend_tag_table[speaker-and-display-port]: old = speaker-and-display-port new = speaker-and-display-port
    platform_set_snd_device_backend: hw_interface_table[32] = QUAT_MI2S_RX-and-DISPLAY_PORT
    platform_set_snd_device_backend: backend_tag_table[speaker-and-bt-a2dp]: old = speaker-and-bt-a2dp new = speaker-and-bt-a2dp
    platform_set_snd_device_backend: hw_interface_table[37] = QUAT_MI2S_RX-and-SLIMBUS_7_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-bt-sco]: old = null new = speaker-and-bt-sco
    platform_set_snd_device_backend: hw_interface_table[40] = QUAT_MI2S_RX-and-SLIMBUS_7_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-bt-sco-wb]: old = null new = speaker-and-bt-sco-wb
    platform_set_snd_device_backend: hw_interface_table[42] = QUAT_MI2S_RX-and-SLIMBUS_7_RX
    platform_set_snd_device_backend: backend_tag_table[speaker-and-usb-headphones]: old = speaker-and-usb-headphones new = speaker-and-usb-headphones
    platform_set_snd_device_backend: hw_interface_table[63] = QUAT_MI2S_RX-and-USB_AUDIO_RX
    platform_set_snd_device_backend: backend_tag_table[voice-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[26] = SLIMBUS_6_RX
09-19 00:11:00.596 1982-1982/? W/zygote64: Unsupported class loader
09-19 00:11:00.596 1989-1993/? D/msm8974_platform: platform_set_snd_device_backend: backend_tag_table[voice-anc-headphones]: old = null new = headphones
09-19 00:11:00.596 1982-1982/? W/zygote64: Could not establish class loader context
09-19 00:11:00.596 1989-1993/? D/msm8974_platform: platform_set_snd_device_backend: hw_interface_table[71] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[voice-anc-fb-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[72] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[voice-line]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[28] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[voice-tty-full-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[49] = SLIMBUS_6_RX
    platform_set_snd_device_backend: backend_tag_table[voice-tty-vco-headphones]: old = null new = headphones
    platform_set_snd_device_backend: hw_interface_table[51] = SLIMBUS_6_RX
09-19 00:11:00.598 1982-1982/? W/zygote64: Core platform API violation: Ljava/lang/reflect/Executable;->accessFlags:I from Lcom/swift/sandhook/SandHook; using reflection
    Core platform API violation: Ljava/lang/Thread;->nativePeer:J from Lcom/swift/sandhook/SandHook; using reflection
09-19 00:11:00.598 1989-1993/? E/msm8974_platform: platform_init: soundcard: msm8998-tasha-snd-card supports only default sample rate
09-19 00:11:00.598 1982-1982/? W/zygote64: Core platform API violation: Ljava/lang/reflect/Executable;->artMethod:J from Lcom/swift/sandhook/SandHook; using reflection
    Core platform API violation: Ljava/lang/reflect/Executable;->dexMethodIndex:I from Lcom/swift/sandhook/SandHook; using reflection
    Core platform API violation: Ljava/lang/Class;->dexCache:Ljava/lang/Object; from Lcom/swift/sandhook/SandHook; using reflection
    Core platform API violation: Ljava/lang/DexCache;->resolvedMethods:J from Lcom/swift/sandhook/SandHook; using reflection
09-19 00:11:00.598 1989-1993/? E/msm8974_platform: platform_init: Could not find the symbol acdb_send_audio_cal_v4 from libacdbloader.so
    platform_init: dlsym error undefined symbol: acdb_loader_init_v4 for acdb_loader_init_v4
09-19 00:11:00.598 1989-1993/? I/audio_hw_extn: audio_extn_set_snd_card_split: snd_card_name(msm8998-tasha-snd-card) device(msm8998) snd_card(tasha) form_factor(snd)
09-19 00:11:00.599 1989-1993/? E/platform_info: param tag only supported with CONFIG_PARAMS section
09-19 00:11:00.599 1989-1993/? I/chatty: uid=1041(audioserver) HwBinder:1989_2 identical 7 lines
09-19 00:11:00.599 1989-1993/? E/platform_info: param tag only supported with CONFIG_PARAMS section
09-19 00:11:00.600 1982-1982/? D/dlopen: 75fe86b000-75fe998000 r--p 00000000 103:1d 309                           /apex/com.android.runtime/lib64/libart.so
09-19 00:11:00.600 1982-1982/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart.so loaded in Android at 0x75fe86b000
09-19 00:11:00.600 1989-1993/? E/audio_hw_acdb: acdb_init_v2: dlsym error undefined symbol: acdb_loader_init_v4 for acdb_loader_init_v4
09-19 00:11:00.600 1989-1993/? D/ACDB-LOADER: ACDB -> already initialized, exit
09-19 00:11:00.600 1989-1993/? D/audio_hw_acdb: acdb_init_v2: ACDB Instance ID support after ACDB init:0
09-19 00:11:00.600 1989-1993/? D/msm8974_platform: ACDB initialized
    hw_util_open Opening device /dev/snd/hwC0D1000
09-19 00:11:00.601 1989-1993/? D/msm8974_platform: hw_util_open success
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:11:00.601 1989-1993/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:11:00.601 1989-1993/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:11:00.601 1989-1993/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:11:00.601 1989-1993/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:11:00.601 1989-1993/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:11:00.601 1989-1993/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:11:00.601 1982-1982/? I/nougat_dlfcn: _ZN3art3jit3Jit20jit_compiler_handle_E found at 0x75fee2e960
09-19 00:11:00.601 1989-1993/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:11:00.601 1989-1993/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:11:00.601 1989-1993/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:11:00.601 1989-1993/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:11:00.601 1989-1993/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:11:00.601 1989-1993/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:11:00.601 1989-1993/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:11:00.601 1989-1993/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:11:00.601 1989-1993/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:11:00.601 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:11:00.601 1989-1993/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
09-19 00:11:00.602 1989-1993/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:11:00.602 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
09-19 00:11:00.602 1989-1993/? E/ACDB-LOADER: Error: ACDB ANC returned = -19
09-19 00:11:00.602 1989-1993/? D/ACDB-LOADER: ACDB -> ACDB_CMD_GET_ANC_SETTING
    send_wcd9xxx_anc_cal: anc_version = 1
09-19 00:11:00.602 1989-1993/? D/anc_map: Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    Setwcd9xxxANC_IIRCoeffs:enter
    Setwcd9xxxANC_IIRCoeffs:leave
    convert_anc_acdb_to_reg:leave
09-19 00:11:00.602 1989-1993/? D/msm8974_platform: send_codec_cal: anc_cal cal sent successfully
09-19 00:11:00.602 1989-1993/? D/ACDB-LOADER: send mbhc data
    ACDB -> MBHC ACDB_PID_GENERAL_CONFIG
    ACDB -> MBHC ACDB_PID_PLUG_REMOVAL_DETECTION
    ACDB -> MBHC ACDB_PID_PLUG_TYPE_DETECTION
    ACDB -> MBHC ACDB_PID_BUTTON_PRESS_DETECTION
    ACDB -> MBHC ACDB_PID_IMPEDANCE_DETECTION
09-19 00:11:00.602 1989-1993/? D/msm8974_platform: send_codec_cal: mbhc_cal cal sent successfully
09-19 00:11:00.602 1989-1993/? D/ACDB-LOADER: send vbat data
    ACDB -> VBAT ACDB_PID_ADC_CAL
    ACDB -> VBAT ACDB_PID_GAIN_PROC
    send vbat data, calling convert_vbat_data
    copied vbat cal size =72
09-19 00:11:00.602 1989-1993/? D/msm8974_platform: send_codec_cal: vbat_cal cal sent successfully
09-19 00:11:00.602 1982-1982/? D/dlopen: 75f4a94000-75f4b56000 r--p 00000000 103:1d 306                           /apex/com.android.runtime/lib64/libart-compiler.so
09-19 00:11:00.602 1982-1982/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart-compiler.so loaded in Android at 0x75f4a94000
09-19 00:11:00.603 1982-1982/? I/nougat_dlfcn: jit_compile_method found at 0x75f4cce3dc
09-19 00:11:00.603 1989-1993/? W/msm8974_platform: init_be_dai_name_table: sound device  has no hw interface set
09-19 00:11:00.603 1989-1993/? D/msm8974_platform: init_be_dai_name_table: sound device speaker-and-headphones does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-and-headphones-hifi-filter does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-safe-and-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-and-line does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-safe-and-line does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-and-headphones-ext-1 does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-and-headphones-ext-2 does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-and-hdmi does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-HDMI
    init_be_dai_name_table: sound device speaker-and-display-port does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-DISPLAY_PORT
    init_be_dai_name_table: sound device speaker-and-bt-a2dp does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_7_RX
    init_be_dai_name_table: sound device speaker-safe-and-bt-a2dp does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_7_RX
    init_be_dai_name_table: sound device speaker-and-bt-sco does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_7_RX
    init_be_dai_name_table: sound device speaker-safe-and-bt-sco does not have a valid hw interface set (disregard for combo devices) QUAT_TDM_RX_0-and-SLIMBUS_7_RX
    init_be_dai_name_table: sound device speaker-and-bt-sco-wb does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_7_RX
    init_be_dai_name_table: sound device speaker-safe-and-bt-sco-wb does not have a valid hw interface set (disregard for combo devices) QUAT_TDM_RX_0-and-SLIMBUS_7_RX
    init_be_dai_name_table: sound device speaker-and-bt-sco-swb does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SEC_AUX_PCM_RX
    init_be_dai_name_table: sound device speaker-safe-and-bt-sco-swb does not have a valid hw interface set (disregard for combo devices) QUAT_TDM_RX_0-and-SLIMBUS_7_RX
09-19 00:11:00.603 1989-1993/? W/msm8974_platform: init_be_dai_name_table: sound device wsa-speaker-and-bt-sco has no hw interface set
    init_be_dai_name_table: sound device wsa-speaker-and-bt-sco-wb has no hw interface set
    init_be_dai_name_table: sound device wsa-speaker-and-bt-sco-wb has no hw interface set
09-19 00:11:00.603 1989-1993/? D/msm8974_platform: init_be_dai_name_table: sound device speaker-and-usb-headphones does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-USB_AUDIO_RX
    init_be_dai_name_table: sound device speaker-safe-and-usb-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-USB_AUDIO_RX
    init_be_dai_name_table: sound device speaker-and-anc-headphones does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device speaker-and-anc-fb-headphones does not have a valid hw interface set (disregard for combo devices) QUAT_MI2S_RX-and-SLIMBUS_6_RX
09-19 00:11:00.603 1989-1993/? W/msm8974_platform: init_be_dai_name_table: sound device speaker-protected has no hw interface set
    init_be_dai_name_table: sound device speaker-protected-vbat has no hw interface set
09-19 00:11:00.603 1989-1993/? D/msm8974_platform: init_be_dai_name_table: sound device voice-speaker-and-voice-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device voice-speaker-and-voice-anc-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device voice-speaker-and-voice-anc-fb-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device voice-speaker-stereo-and-voice-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device voice-speaker-stereo-and-voice-anc-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device voice-speaker-stereo-and-voice-anc-fb-headphones does not have a valid hw interface set (disregard for combo devices) SLIMBUS_0_RX-and-SLIMBUS_6_RX
    init_be_dai_name_table: sound device hearing-aid does not have a valid hw interface set (disregard for combo devices) BT_RX
    init_be_dai_name_table: sound device spdif-in does not have a valid hw interface set (disregard for combo devices) PRI_SPDIF_TX
    init_be_dai_name_table: sound device hdmi-arc-in does not have a valid hw interface set (disregard for combo devices) SEC_SPDIF_TX
09-19 00:11:00.603 1989-1993/? W/msm8974_platform: init_be_dai_name_table: sound device usb-headset-mic has no hw interface set
09-19 00:11:00.603 1989-1993/? I/chatty: uid=1041(audioserver) HwBinder:1989_2 identical 1 line
09-19 00:11:00.603 1989-1993/? W/msm8974_platform: init_be_dai_name_table: sound device usb-headset-mic has no hw interface set
    init_be_dai_name_table: sound device handset-6mic has no hw interface set
    init_be_dai_name_table: sound device handset-8mic has no hw interface set
    init_be_dai_name_table: sound device (null) has no hw interface set
    init_be_dai_name_table: sound device (null) has no hw interface set
    init_be_dai_name_table: sound device incall-rec-rx-tx has no hw interface set
    init_be_dai_name_table: sound device ec-ref-loopback has no hw interface set
    init_be_dai_name_table: sound device handset-dmic-and-ec-ref-loopback has no hw interface set
    init_be_dai_name_table: sound device handset-qmic-and-ec-ref-loopback has no hw interface set
    init_be_dai_name_table: sound device handset-6mic-and-ec-ref-loopback has no hw interface set
    init_be_dai_name_table: sound device handset-8mic-and-ec-ref-loopback has no hw interface set
09-19 00:11:00.603 1989-1993/? D/audio_hw_extn: audio_extn_can_use_ras: ras.enabled property is set to 0
09-19 00:11:00.603 1989-1993/? D/msm8974_platform: platform_init: Fluence_Type(1) max_mic_count(4) mic_type(0xf) fluence_in_voice_call(1) fluence_in_voice_rec(0) fluence_in_spkr_mode(1) fluence_in_hfp_call(0)fluence_sb_enabled(0)
    platform_get_snd_device_backend_interface: hw_interface set for device SEC_MI2S_TX
09-19 00:11:00.604 1982-1982/? D/dlopen: 75f4a94000-75f4b56000 r--p 00000000 103:1d 306                           /apex/com.android.runtime/lib64/libart-compiler.so
09-19 00:11:00.604 1982-1982/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart-compiler.so loaded in Android at 0x75f4a94000
    jit_load found at 0x75f4cce298
09-19 00:11:00.606 1982-1982/? D/dlopen: 75fe86b000-75fe998000 r--p 00000000 103:1d 309                           /apex/com.android.runtime/lib64/libart.so
09-19 00:11:00.606 1982-1982/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart.so loaded in Android at 0x75fe86b000
09-19 00:11:00.607 1982-1982/? I/nougat_dlfcn: _ZN3art3Dbg9SuspendVMEv found at 0x75fea263f4
09-19 00:11:00.608 1982-1982/? D/dlopen: 75fe86b000-75fe998000 r--p 00000000 103:1d 309                           /apex/com.android.runtime/lib64/libart.so
09-19 00:11:00.608 1982-1982/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart.so loaded in Android at 0x75fe86b000
09-19 00:11:00.609 1982-1982/? I/nougat_dlfcn: _ZN3art3Dbg8ResumeVMEv found at 0x75fea26478
09-19 00:11:00.610 1982-1982/? D/dlopen: 75fe86b000-75fe998000 r--p 00000000 103:1d 309                           /apex/com.android.runtime/lib64/libart.so
09-19 00:11:00.610 1982-1982/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart.so loaded in Android at 0x75fe86b000
09-19 00:11:00.611 1982-1982/? I/nougat_dlfcn: _ZN3art9JavaVMExt16AddWeakGlobalRefEPNS_6ThreadENS_6ObjPtrINS_6mirror6ObjectEEE found at 0x75febdf380
09-19 00:11:00.612 1982-1982/? D/dlopen: 75fe86b000-75fe998000 r--p 00000000 103:1d 309                           /apex/com.android.runtime/lib64/libart.so
09-19 00:11:00.612 1982-1982/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart.so loaded in Android at 0x75fe86b000
09-19 00:11:00.615 1982-1982/? D/dlopen: 75fe86b000-75fe998000 r--p 00000000 103:1d 309                           /apex/com.android.runtime/lib64/libart.so
09-19 00:11:00.615 1982-1982/? I/nougat_dlfcn: /apex/com.android.runtime/lib64/libart.so loaded in Android at 0x75fe86b000
    _ZN3art12ProfileSaver20ForceProcessProfilesEv found at 0x75febb3084
09-19 00:11:00.619 1989-1993/? D/msm8974_platform: platform_get_mixer_control: mixer ctl not obtained
09-19 00:11:00.619 1989-1993/? I/chatty: uid=1041(audioserver) HwBinder:1989_2 identical 1 line
09-19 00:11:00.619 1989-1993/? D/msm8974_platform: platform_get_mixer_control: mixer ctl not obtained
09-19 00:11:00.620 1982-1982/? E/nougat_dlfcn: /system/lib64/libsandhook-native.so not found in my userspace
09-19 00:11:00.621 1989-1993/? D/msm8974_platform: platform_get_mixer_control: mixer ctl not obtained
09-19 00:11:00.621 1989-1993/? I/chatty: uid=1041(audioserver) HwBinder:1989_2 identical 1 line
09-19 00:11:00.621 1989-1993/? D/msm8974_platform: platform_get_mixer_control: mixer ctl not obtained
09-19 00:11:00.621 1989-1993/? E/audio_hw_utils: audio_extn_utils_get_codec_variant: ERROR. cannot open /proc/asound/card0/codecs/wcd937x/variant
09-19 00:11:00.621 1989-1993/? D/audio_hw_utils: audio_extn_utils_get_codec_version: codec version WCD9335_2_0
09-19 00:11:00.623 1989-1993/? E/audio_hw_primary: Amplifier initialization failed
09-19 00:11:00.623 1989-1993/? D/ultrasound: us_init: enter
09-19 00:11:00.624 1989-1993/? D/ultrasound: us_init: exit, status(0)
09-19 00:11:00.624 1989-1993/? D/audio_hw_utils: audio_extn_utils_update_streams_cfg_lists: failed to open io config file(/vendor/etc/audio_io_policy.conf), trying older config file
09-19 00:11:00.624 1989-1993/? I/audio_hw_utils: load_cfg_list: could not load input, node is NULL
09-19 00:11:00.624 1989-1993/? I/qc_adm: ADM buffering size (6) ms requested, defaulting to 3 ms
09-19 00:11:00.625 1982-1982/? E/nougat_dlfcn: /odm/lib64/libsandhook-native.so not found in my userspace
09-19 00:11:00.625 1989-1993/? E/audio_hw_extn: audio_extn_perf_lock_init: Perf lock handles Success 
09-19 00:11:00.625 1989-1993/? I/soundtrigger: audio_extn_sound_trigger_init: Enter
09-19 00:11:00.626 1989-1993/? I/soundtrigger: audio_extn_sound_trigger_init: DLOPEN successful for /vendor/lib/hw/sound_trigger.primary.msm8998.so
09-19 00:11:00.626 1989-1993/? D/soundtrigger: audio_extn_sound_trigger_init: sthal is using proprietary API version 0x0100
09-19 00:11:00.627 1989-1989/? W/DeviceHAL: Error from HAL Device in function get_master_volume: Function not implemented
    Error from HAL Device in function get_master_mute: Function not implemented
    Error from HAL Device in function set_master_volume: Function not implemented
    Error from HAL Device in function set_master_mute: Function not implemented
09-19 00:11:00.627 1984-1984/? I/AudioFlinger: loadHwModule() Loaded primary audio interface, handle 10
    openOutput() this 0x72a9c29600, module 10 Device 0x2, SamplingRate 48000, Format 0x000001, Channels 0x3, flags 0x6
09-19 00:11:00.627 1989-1989/? D/audio_hw_primary: adev_open_output_stream: enter: format(0x1) sample_rate(48000) channel_mask(0x3) devices(0x2) flags(0x6)        stream_handle(0xf03a0000) address()
09-19 00:11:00.627 1989-1989/? I/audio_hw_primary: adev_open_output_stream: dynamic qos voting not enabled for platform
09-19 00:11:00.627 1989-1989/? I/audio_hw_utils: audio_extn_utils_update_stream_output_app_type_cfg Allowing 24 and above bits playback on speaker ONLY at default sampling rate
09-19 00:11:00.627 1989-1989/? D/audio_hw_primary: adev_open_output_stream: Stream (0xf03a0000) picks up usecase (low-latency-playback)
09-19 00:11:00.628 1984-1984/? I/AudioFlinger: HAL output buffer size 192 frames, normal sink buffer size 960 frames
09-19 00:11:00.630 1982-1982/? E/nougat_dlfcn: /vendor/lib64/libsandhook-native.so not found in my userspace
09-19 00:11:00.635 1982-1982/? E/nougat_dlfcn: libsandhook-native.so not found in my userspace
09-19 00:11:00.636 1982-1982/? D/SandHook: method <public static android.app.ActivityThread android.app.ActivityThread.systemMain()> hook <replacement> success!
09-19 00:11:00.637 1989-1989/? D/volume_listener: init_once Called 
    init_once: using custome volume table
09-19 00:11:00.637 1989-1989/? I/EffectDiracSound: DiracSoundLib_GetDescriptor() start
09-19 00:11:00.637 1984-1984/? I/BufferProvider: found effect "Multichannel Downmix To Stereo" from The Android Open Source Project
09-19 00:11:00.639 1984-2129/? I/AudioFlinger: AudioFlinger's thread 0x72a9d11bc0 tid=2129 ready to run
09-19 00:11:00.639 1984-2129/? W/AudioFlinger: no wake lock to update, system not ready yet
09-19 00:11:00.639 1984-1984/? I/AudioFlinger: Using module 10 as the primary audio interface
09-19 00:11:00.637 1982-1982/? W/main: type=1400 audit(0.0:106): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:00.639 1989-1993/? D/audio_hw_primary: out_standby: enter: stream (0xf03a0000) usecase(1: low-latency-playback)
    out_standby: exit
09-19 00:11:00.640 1984-2129/? W/AudioFlinger: no wake lock to update, system not ready yet
09-19 00:11:00.643 1984-1984/? W/AudioFlinger: moveEffects() bad srcOutput 0
09-19 00:11:00.644 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:00.645 1982-1982/? D/SandHook: method <private void android.app.ActivityThread.handleBindApplication(android.app.ActivityThread$AppBindData)> hook <replacement> success!
09-19 00:11:00.643 1982-1982/? W/main: type=1400 audit(0.0:108): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:00.654 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:00.655 1982-1982/? D/SandHook: method <public android.app.LoadedApk(android.app.ActivityThread,android.content.pm.ApplicationInfo,android.content.res.CompatibilityInfo,java.lang.ClassLoader,boolean,boolean,boolean)> hook <replacement> success!
09-19 00:11:00.657 1982-1982/? W/main: type=1400 audit(0.0:110): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:00.665 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:00.666 1982-1982/? D/SandHook: method <public android.content.res.Resources android.app.ApplicationPackageManager.getResourcesForApplication(android.content.pm.ApplicationInfo) throws android.content.pm.PackageManager$NameNotFoundException> hook <replacement> success!
09-19 00:11:00.668 1989-1993/? D/audio_hw_primary: out_set_parameters: enter: usecase(1: low-latency-playback) kvpairs: routing=2
09-19 00:11:00.663 1982-1982/? W/main: type=1400 audit(0.0:112): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:00.668 1989-1993/? D/audio_hw_extn: audio_extn_fm_set_parameters: Enter
09-19 00:11:00.668 1989-1993/? D/audio_hw_hfp: hfp_set_parameters: enter
09-19 00:11:00.663 1982-1982/? W/main: type=1400 audit(0.0:113): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:00.671 1984-1984/? I/AudioFlinger: openOutput() this 0x72a9c29600, module 10 Device 0x2, SamplingRate 48000, Format 0x000001, Channels 0x3, flags 0x4
09-19 00:11:00.671 1989-1993/? D/audio_hw_primary: adev_open_output_stream: enter: format(0x1) sample_rate(48000) channel_mask(0x3) devices(0x2) flags(0x4)        stream_handle(0xf03d9000) address()
09-19 00:11:00.671 1989-1993/? I/audio_hw_primary: adev_open_output_stream: dynamic qos voting not enabled for platform
09-19 00:11:00.671 1989-1993/? I/audio_hw_utils: audio_extn_utils_update_stream_output_app_type_cfg Allowing 24 and above bits playback on speaker ONLY at default sampling rate
09-19 00:11:00.671 1989-1993/? E/audio_hw_primary: adev_open_output_stream: Primary output is already opened
09-19 00:11:00.671 1989-1993/? D/audio_hw_primary: adev_open_output_stream: exit: ret -17
09-19 00:11:00.671 1989-1993/? W/DeviceHAL: Error from HAL Device in function open_output_stream: File exists
09-19 00:11:00.671 1984-1984/? I/AudioHwDevice: openOutputStream(), HAL returned sampleRate 48000, Format 0x1, channelMask 0x3, status -61
09-19 00:11:00.671 1984-1984/? W/APM_AudioPolicyManager: Cannot open output stream for devices type:0x2,@: on hw module primary
09-19 00:11:00.671 1984-1984/? I/AudioFlinger: openOutput() this 0x72a9c29600, module 10 Device 0x2, SamplingRate 48000, Format 0x000001, Channels 0x3, flags 0x8
09-19 00:11:00.672 1989-1993/? D/audio_hw_primary: adev_open_output_stream: enter: format(0x1) sample_rate(48000) channel_mask(0x3) devices(0x2) flags(0x8)        stream_handle(0xf03d9000) address()
09-19 00:11:00.672 1989-1993/? I/audio_hw_utils: audio_extn_utils_update_stream_output_app_type_cfg Allowing 24 and above bits playback on speaker ONLY at default sampling rate
09-19 00:11:00.672 1989-1993/? D/audio_hw_primary: adev_open_output_stream: Stream (0xf03d9000) picks up usecase (deep-buffer-playback)
09-19 00:11:00.672 1984-1984/? I/AudioFlinger: HAL output buffer size 1920 frames, normal sink buffer size 1920 frames
09-19 00:11:00.673 1984-2132/? I/AudioFlinger: AudioFlinger's thread 0x721c9a0580 tid=2132 ready to run
09-19 00:11:00.673 1984-2132/? W/AudioFlinger: no wake lock to update, system not ready yet
09-19 00:11:00.673 1989-1993/? D/audio_hw_primary: out_standby: enter: stream (0xf03d9000) usecase(0: deep-buffer-playback)
    out_standby: exit
09-19 00:11:00.673 1984-2132/? W/AudioFlinger: no wake lock to update, system not ready yet
09-19 00:11:00.674 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:00.675 1982-1982/? D/SandHook: method <private android.content.res.Resources android.app.ResourcesManager.getOrCreateResources(android.os.IBinder,android.content.res.ResourcesKey,java.lang.ClassLoader)> hook <replacement> success!
09-19 00:11:00.676 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:00.673 1982-1982/? W/main: type=1400 audit(0.0:114): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:00.683 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:00.683 1982-1982/? D/SandHook: method <static android.content.res.TypedArray android.content.res.TypedArray.obtain(android.content.res.Resources,int)> hook <replacement> success!
09-19 00:11:00.683 1982-1982/? W/main: type=1400 audit(0.0:116): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:00.690 1982-1982/? I/chatty: uid=0(root) main identical 2 lines
09-19 00:11:00.690 1982-1982/? W/main: type=1400 audit(0.0:119): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:00.691 1982-1982/? W/zygote64: Unsupported class loader
09-19 00:11:00.692 1982-1982/? W/zygote64: Could not establish class loader context
09-19 00:11:00.692 1982-1982/? D/SandHook: method <public android.view.View android.view.LayoutInflater.inflate(org.xmlpull.v1.XmlPullParser,android.view.ViewGroup,boolean)> hook <replacement> success!
09-19 00:11:00.700 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:00.700 1982-1982/? D/SandHook: method <private void android.view.LayoutInflater.parseInclude(org.xmlpull.v1.XmlPullParser,android.content.Context,android.view.View,android.util.AttributeSet) throws org.xmlpull.v1.XmlPullParserException,java.io.IOException> hook <replacement> success!
09-19 00:11:00.701 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/com.bigsing.fakemap-N6PbN7a22Ns4jlp2fADtxg==/base.apk
09-19 00:11:00.701 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:00.718 1989-1989/? D/audio_hw_primary: out_set_parameters: enter: usecase(0: deep-buffer-playback) kvpairs: routing=2
09-19 00:11:00.721 1984-1984/? W/APM_AudioPolicyManager: Output profile contains no device on module primary
09-19 00:11:00.721 1984-1984/? I/AudioFlinger: openOutput() this 0x72a9c29600, module 10 Device 0x10000, SamplingRate 48000, Format 0x000001, Channels 0x3, flags 0
09-19 00:11:00.721 1989-1989/? D/audio_hw_primary: adev_open_output_stream: enter: format(0x1) sample_rate(48000) channel_mask(0x3) devices(0x10000) flags(0)        stream_handle(0xf03a2800) address()
    adev_open_output_stream: Stream (0xf03a2800) picks up usecase (afe-proxy-playback)
09-19 00:11:00.722 1984-1984/? I/AudioFlinger: HAL output buffer size 768 frames, normal sink buffer size 1152 frames
09-19 00:11:00.723 1984-2136/? I/AudioFlinger: AudioFlinger's thread 0x721ca01800 tid=2136 ready to run
09-19 00:11:00.723 1984-2136/? W/AudioFlinger: no wake lock to update, system not ready yet
09-19 00:11:00.723 1989-1989/? D/audio_hw_primary: out_standby: enter: stream (0xf03a2800) usecase(51: afe-proxy-playback)
    out_standby: exit
09-19 00:11:00.724 1984-2136/? W/AudioFlinger: no wake lock to update, system not ready yet
09-19 00:11:00.778 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:00.782 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:739] qti_file_open():Could not open device file. Errno 2 error msg=No such file or directory
09-19 00:11:00.783 1989-1989/? D/audio_hw_primary: out_set_parameters: enter: usecase(51: afe-proxy-playback) kvpairs: routing=65536
09-19 00:11:00.785 1989-1989/? D/audio_hw_primary: adev_open_input_stream: enter: sample_rate(48000) channel_mask(0xc) devices(0x80000004)        stream_handle(0xf2db4800) io_handle(14) source(1) format 1
09-19 00:11:00.785 1989-1989/? W/audio_hw_utils: audio_extn_utils_update_stream_input_app_type_cfg: App type could not be selected. Falling back to default
09-19 00:11:00.790 1984-2140/? I/AudioFlinger: AudioFlinger's thread 0x721cad3240 tid=2140 ready to run
09-19 00:11:00.790 1989-1989/? D/audio_hw_primary: adev_open_input_stream: enter: sample_rate(192000) channel_mask(0x8000000f) devices(0x80000004)        stream_handle(0xf2db4a80) io_handle(22) source(1) format 5
    adev_open_input_stream: enter: sample_rate(48000) channel_mask(0x8000000f) devices(0x80000004)        stream_handle(0xf2db4a80) io_handle(22) source(1) format 1
09-19 00:11:00.790 1989-1989/? W/audio_hw_utils: audio_extn_utils_update_stream_input_app_type_cfg: App type could not be selected. Falling back to default
09-19 00:11:00.791 1989-1989/? D/audio_hw_primary: adev_close_input_stream: enter:stream_handle(0xf2db4800)
09-19 00:11:00.792 1989-1989/? D/soundtrigger: audio_extn_sound_trigger_check_ec_ref_enable: EC Reference is disabled
09-19 00:11:00.792 1989-1989/? W/sound_trigger_hw: sound_trigger_hw_call_back: Unknown event 16
09-19 00:11:00.792 1989-1989/? D/soundtrigger: audio_extn_sound_trigger_update_ec_ref_status: update audio echo ref status false
09-19 00:11:00.792 1989-1989/? D/audio_hw_primary: in_standby: enter: stream (0xf2db4800) usecase(20: audio-record)
09-19 00:11:00.794 1984-2142/? I/AudioFlinger: AudioFlinger's thread 0x721cb4d3c0 tid=2142 ready to run
09-19 00:11:00.794 1989-1989/? D/audio_hw_primary: adev_open_input_stream: enter: sample_rate(48000) channel_mask(0xc) devices(0x80000040)        stream_handle(0xf2db4800) io_handle(30) source(1) format 1
09-19 00:11:00.794 1989-1993/? D/audio_hw_primary: adev_close_input_stream: enter:stream_handle(0xf2db4a80)
09-19 00:11:00.794 1989-1993/? D/soundtrigger: audio_extn_sound_trigger_check_ec_ref_enable: EC Reference is disabled
09-19 00:11:00.794 1989-1993/? W/sound_trigger_hw: sound_trigger_hw_call_back: Unknown event 16
09-19 00:11:00.794 1989-1993/? D/soundtrigger: audio_extn_sound_trigger_update_ec_ref_status: update audio echo ref status false
09-19 00:11:00.794 1989-1993/? D/audio_hw_primary: in_standby: enter: stream (0xf2db4a80) usecase(20: audio-record)
09-19 00:11:00.794 1989-1989/? W/audio_hw_utils: audio_extn_utils_update_stream_input_app_type_cfg: App type could not be selected. Falling back to default
09-19 00:11:00.799 1984-2146/? I/AudioFlinger: AudioFlinger's thread 0x721cad3e80 tid=2146 ready to run
09-19 00:11:00.799 1989-1989/? D/audio_hw_primary: adev_open_input_stream: enter: sample_rate(48000) channel_mask(0x80000007) devices(0x80000004)        stream_handle(0xf2db4d00) io_handle(38) source(1) format 1
09-19 00:11:00.799 1989-1989/? W/audio_hw_utils: audio_extn_utils_update_stream_input_app_type_cfg: App type could not be selected. Falling back to default
09-19 00:11:00.799 1989-2145/? D/audio_hw_primary: adev_close_input_stream: enter:stream_handle(0xf2db4800)
09-19 00:11:00.799 1989-2145/? D/soundtrigger: audio_extn_sound_trigger_check_ec_ref_enable: EC Reference is disabled
09-19 00:11:00.799 1989-2145/? W/sound_trigger_hw: sound_trigger_hw_call_back: Unknown event 16
09-19 00:11:00.799 1989-2145/? D/soundtrigger: audio_extn_sound_trigger_update_ec_ref_status: update audio echo ref status false
09-19 00:11:00.799 1989-2145/? D/audio_hw_primary: in_standby: enter: stream (0xf2db4800) usecase(52: afe-proxy-record)
09-19 00:11:00.802 1984-2149/? I/AudioFlinger: AudioFlinger's thread 0x721cb47400 tid=2149 ready to run
09-19 00:11:00.802 1984-1984/? E/APM_AudioPolicyManager: initialize: Input device list is empty!
09-19 00:11:00.807 1984-1984/? I/bt_a2dp_hw: adev_open:  adev_open in A2dp_hw module
09-19 00:11:00.807 1984-1984/? I/AudioFlinger: loadHwModule() Loaded a2dp audio interface, handle 18
09-19 00:11:00.807 1984-1984/? E/APM_AudioPolicyManager: initialize: Input device list is empty!
09-19 00:11:00.808 1989-1992/? D/vndksupport: Loading /vendor/lib/hw/audio.usb.default.so from current namespace instead of sphal namespace.
09-19 00:11:00.808 1989-2148/? D/audio_hw_primary: adev_close_input_stream: enter:stream_handle(0xf2db4d00)
09-19 00:11:00.808 1989-2148/? D/soundtrigger: audio_extn_sound_trigger_check_ec_ref_enable: EC Reference is disabled
09-19 00:11:00.808 1989-2148/? W/sound_trigger_hw: sound_trigger_hw_call_back: Unknown event 16
09-19 00:11:00.808 1989-2148/? D/soundtrigger: audio_extn_sound_trigger_update_ec_ref_status: update audio echo ref status false
09-19 00:11:00.808 1989-2148/? D/audio_hw_primary: in_standby: enter: stream (0xf2db4d00) usecase(20: audio-record)
09-19 00:11:00.809 1989-1992/? W/DeviceHAL: Error from HAL Device in function set_master_volume: Function not implemented
09-19 00:11:00.810 1984-1984/? I/AudioFlinger: loadHwModule() Loaded usb audio interface, handle 26
09-19 00:11:00.810 1989-1992/? D/vndksupport: Loading /vendor/lib/hw/audio.r_submix.default.so from current namespace instead of sphal namespace.
09-19 00:11:00.811 1989-1992/? I/r_submix: adev_open(name=audio_hw_if)
09-19 00:11:00.812 1989-1992/? I/r_submix: adev_init_check()
09-19 00:11:00.812 1989-1992/? W/DeviceHAL: Error from HAL Device in function set_master_volume: Function not implemented
    Error from HAL Device in function set_master_mute: Function not implemented
09-19 00:11:00.812 1984-1984/? I/AudioFlinger: loadHwModule() Loaded r_submix audio interface, handle 34
09-19 00:11:00.813 1989-1992/? D/r_submix: adev_open_input_stream(addr=0)
    submix_audio_device_create_pipe_l(addr=0, idx=9)
      now using address 0 for route 9
09-19 00:11:00.815 1984-2151/? I/AudioFlinger: AudioFlinger's thread 0x721cad3500 tid=2151 ready to run
09-19 00:11:00.816 1984-1984/? D/AudioPolicyManagerCustom: USE_XML_AUDIO_POLICY_CONF is TRUE
09-19 00:11:00.817 1989-1992/? D/r_submix: adev_close_input_stream()
09-19 00:11:00.818 1989-1992/? D/r_submix: submix_audio_device_release_pipe_l(idx=9) addr=0
    submix_audio_device_destroy_pipe_l(): pipe destroyed
09-19 00:11:00.878 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:00.966 925-1074/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 44000 mC, weight[0] 2
    vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:11:00.978 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:01.011 1982-1982/? I/EdXposed-Bridge:   Loading class com.bigsing.fakemap.MainHook
09-19 00:11:01.012 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/com.lanyus.blocksecureflag-QkgSXuv3JtDkgn3BXLv7VA==/base.apk
09-19 00:11:01.012 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:01.044 1081-1081/? I/Atfwd_Daemon: qmi_client_init_instance status retry : 2
     qmi_client_init_instance....
    qmi_client_init_instance status: 0, num_retries: 3, retryCnt: 2
    qmi_client_register_error_cb status: 0
    result : 0 	 ,Init step :1 	 ,qmiErrorCode: 0
     Back to main.
     tryinit complete with connectresult: 0
     TrtyInit: retryCnt: 1
    Invalid type 2
     tryinit complete with connectresult: 0
    Trying to register 8 commands:
    cmd0: +CKPD
    sending QMI_AT_REG_AT_CMD_FWD_REQ_V01 message
09-19 00:11:01.046 1081-1081/? I/Atfwd_Daemon: cmd1: +CTSA
    sending QMI_AT_REG_AT_CMD_FWD_REQ_V01 message
09-19 00:11:01.048 1081-1081/? I/Atfwd_Daemon: cmd2: +CFUN
    sending QMI_AT_REG_AT_CMD_FWD_REQ_V01 message
09-19 00:11:01.049 1081-1081/? I/Atfwd_Daemon: cmd3: +CMAR
    sending QMI_AT_REG_AT_CMD_FWD_REQ_V01 message
    cmd4: +CDIS
    sending QMI_AT_REG_AT_CMD_FWD_REQ_V01 message
    cmd5: +CRSL
    sending QMI_AT_REG_AT_CMD_FWD_REQ_V01 message
09-19 00:11:01.050 1081-1081/? I/Atfwd_Daemon: cmd6: +CSS
    sending QMI_AT_REG_AT_CMD_FWD_REQ_V01 message
    cmd7: $QCPWRDN
    sending QMI_AT_REG_AT_CMD_FWD_REQ_V01 message
    Registered AT Commands event handler
    Waiting for ctrCond
09-19 00:11:01.079 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:01.080 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:01.082 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:11:01.083 1982-1982/? I/EdXposed-Bridge:   Loading class com.lanyus.blocksecureflag.XposedMain
09-19 00:11:01.084 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/com.df.callblocker-LNcAKCNcPT-cSh6jxYZPSQ==/base.apk
09-19 00:11:01.084 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:01.088 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:01.088 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:11:01.088 1982-1982/? I/EdXposed-Bridge:   Loading class com.droidmate.xposed.PermissionMod
09-19 00:11:01.092 1982-1982/? E/EdXposed-Bridge: de.robv.android.xposed.XposedHelpers$ClassNotFoundError: java.lang.ClassNotFoundException: com.android.server.pm.PackageManagerService
        at de.robv.android.xposed.XposedHelpers.findClass(XposedHelpers.java:71)
        at com.droidmate.xposed.PermissionMod.alterPermissions(Unknown Source:8)
        at com.droidmate.xposed.PermissionMod.initZygote(Unknown Source:43)
        at de.robv.android.xposed.XposedInit.loadModule(XposedInit.java:479)
        at de.robv.android.xposed.XposedInit.loadModules(XposedInit.java:345)
        at com.elderdrivers.riru.edxp.proxy.BaseRouter.loadModulesSafely(BaseRouter.java:78)
        at com.elderdrivers.riru.edxp.proxy.NormalProxy.forkSystemServerPre(NormalProxy.java:50)
        at com.elderdrivers.riru.edxp.core.Main.forkSystemServerPre(Main.java:108)
        at com.android.internal.os.Zygote.nativeForkSystemServer(Native Method)
        at com.android.internal.os.Zygote.forkSystemServer(Zygote.java:355)
        at com.android.internal.os.ZygoteInit.forkSystemServer(ZygoteInit.java:780)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:913)
     Caused by: java.lang.ClassNotFoundException: com.android.server.pm.PackageManagerService
        at java.lang.Class.classForName(Native Method)
        at java.lang.Class.forName(Class.java:454)
        at external.org.apache.commons.lang3.ClassUtils.getClass(ClassUtils.java:823)
        at de.robv.android.xposed.XposedHelpers.findClass(XposedHelpers.java:69)
        at com.droidmate.xposed.PermissionMod.alterPermissions(Unknown Source:8) 
        at com.droidmate.xposed.PermissionMod.initZygote(Unknown Source:43) 
        at de.robv.android.xposed.XposedInit.loadModule(XposedInit.java:479) 
        at de.robv.android.xposed.XposedInit.loadModules(XposedInit.java:345) 
        at com.elderdrivers.riru.edxp.proxy.BaseRouter.loadModulesSafely(BaseRouter.java:78) 
        at com.elderdrivers.riru.edxp.proxy.NormalProxy.forkSystemServerPre(NormalProxy.java:50) 
        at com.elderdrivers.riru.edxp.core.Main.forkSystemServerPre(Main.java:108) 
        at com.android.internal.os.Zygote.nativeForkSystemServer(Native Method) 
        at com.android.internal.os.Zygote.forkSystemServer(Zygote.java:355) 
        at com.android.internal.os.ZygoteInit.forkSystemServer(ZygoteInit.java:780) 
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:913) 
     Caused by: java.lang.ClassNotFoundException: Didn't find class "com.android.server.pm.PackageManagerService" on path: DexPathList[[zip file "/data/app/com.df.callblocker-LNcAKCNcPT-cSh6jxYZPSQ==/base.apk"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at java.lang.Class.classForName(Native Method) 
        at java.lang.Class.forName(Class.java:454) 
        at external.org.apache.commons.lang3.ClassUtils.getClass(ClassUtils.java:823) 
        at de.robv.android.xposed.XposedHelpers.findClass(XposedHelpers.java:69) 
        at com.droidmate.xposed.PermissionMod.alterPermissions(Unknown Source:8) 
        at com.droidmate.xposed.PermissionMod.initZygote(Unknown Source:43) 
        at de.robv.android.xposed.XposedInit.loadModule(XposedInit.java:479) 
        at de.robv.android.xposed.XposedInit.loadModules(XposedInit.java:345) 
        at com.elderdrivers.riru.edxp.proxy.BaseRouter.loadModulesSafely(BaseRouter.java:78) 
        at com.elderdrivers.riru.edxp.proxy.NormalProxy.forkSystemServerPre(NormalProxy.java:50) 
        at com.elderdrivers.riru.edxp.core.Main.forkSystemServerPre(Main.java:108) 
        at com.android.internal.os.Zygote.nativeForkSystemServer(Native Method) 
        at com.android.internal.os.Zygote.forkSystemServer(Zygote.java:355) 
        at com.android.internal.os.ZygoteInit.forkSystemServer(ZygoteInit.java:780) 
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:913) 
09-19 00:11:01.090 1982-1982/? W/main: type=1400 audit(0.0:120): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:01.100 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:01.101 1982-1982/? D/SandHook: method <public int android.app.AppOpsManager.checkOp(int,int,java.lang.String)> hook <replacement> success!
09-19 00:11:01.100 1982-1982/? W/main: type=1400 audit(0.0:122): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:01.109 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:01.110 1982-1982/? D/SandHook: method <public int android.app.AppOpsManager.checkOpNoThrow(int,int,java.lang.String)> hook <replacement> success!
09-19 00:11:01.110 1982-1982/? W/main: type=1400 audit(0.0:124): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:01.118 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:01.119 1982-1982/? D/SandHook: method <public int android.app.AppOpsManager.noteOp(int,int,java.lang.String)> hook <replacement> success!
09-19 00:11:01.117 1982-1982/? W/main: type=1400 audit(0.0:126): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:01.127 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:01.128 1982-1982/? D/SandHook: method <public int android.app.AppOpsManager.noteOpNoThrow(int,int,java.lang.String)> hook <replacement> success!
09-19 00:11:01.127 1982-1982/? W/main: type=1400 audit(0.0:128): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:01.136 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:01.137 1982-1982/? D/SandHook: method <public int android.app.AppOpsManager.startOp(int,int,java.lang.String)> hook <replacement> success!
09-19 00:11:01.137 1982-1982/? W/main: type=1400 audit(0.0:130): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:01.145 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:01.146 1982-1982/? D/SandHook: method <public int android.app.AppOpsManager.startOpNoThrow(int,int,java.lang.String)> hook <replacement> success!
09-19 00:11:01.146 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/com.devin.islowramdevice-ey8WMdZp-IUDY3h4qPbIYA==/base.apk
09-19 00:11:01.146 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:01.170 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:01.171 1982-1982/? I/EdXposed-Bridge:   Loading class com.devin.islowramdevice.XIsLowRamDevice
09-19 00:11:01.172 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/ma.wanam.wanamkit-mDFL8N9RpaVfGiQy4SjMXA==/base.apk
09-19 00:11:01.172 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:01.179 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:01.280 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:01.281 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:01.282 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:11:01.283 1982-1982/? I/EdXposed-Bridge:   Loading class ma.wanam.wanamkit.Xposed
09-19 00:11:01.284 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/org.meowcat.edxposed.manager-vV43FdjgRSKoaRvjzrhayQ==/base.apk
09-19 00:11:01.284 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:01.364 882-979/? I/QC-NETMGR-LIB: NetmgrNetdClientSetIpForwardEnable(): Looking for Netd service
    NetmgrNetdClientSetIpForwardEnable(): starting command
    setIpForwardEnable(): Attempting setIpForwardEnable
09-19 00:11:01.364 1987-2014/? D/TetherController: Setting IP forward enable = 1
09-19 00:11:01.365 882-979/? I/QC-NETMGR-LIB: NetmgrNetdClientSetIpForwardEnable(): completed command
    NetmgrNetdClientAddInterfaceToOemNetwork(): Looking for Netd service
    NetmgrNetdClientAddInterfaceToOemNetwork(): starting command
    addInterfaceToOemNetwork(): Attempting addInterfaceToOemNetwork
09-19 00:11:01.368 882-979/? I/QC-NETMGR-LIB: NetmgrNetdClientAddInterfaceToOemNetwork(): completed command
09-19 00:11:01.380 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:01.462 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
    Found duplicate classes, falling back to extracting from APK : /data/app/org.meowcat.edxposed.manager-vV43FdjgRSKoaRvjzrhayQ==/base.apk
    NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /data/app/org.meowcat.edxposed.manager-vV43FdjgRSKoaRvjzrhayQ==/base.apk and /system/framework/edxp.jar
09-19 00:11:01.481 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:01.484 1632-1632/? I/imsrcsd: getAndroidPropValue : vendor.ims.modem.multisub.cap[1]
    Uce Service HAL  detected modemVersion[1]
    getAndroidPropValue : vendor.ims.rcs_version[1]
    getAndroidPropValue : vendor.ims.rcs_version[1]
    Uce Service HAL  loading lib-uceservice
09-19 00:11:01.555 1632-1632/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    DPL : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0 gIsDebugDataPathDisabled = 0
09-19 00:11:01.556 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.557 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.558 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.559 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.559 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.559 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.559 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.559 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.559 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.559 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.559 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.559 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.559 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.559 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.559 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.559 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.559 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.559 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.559 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.559 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.559 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.559 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.559 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.559 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.559 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.559 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.559 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.559 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.559 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.559 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.559 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.560 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.560 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.560 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.560 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.560 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.560 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.560 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.560 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.560 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.560 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.560 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.560 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.560 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.561 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.561 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.561 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.561 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.561 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.561 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.561 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.561 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.561 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.561 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.561 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.561 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.561 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.561 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.561 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.561 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.561 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.561 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.561 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.561 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.562 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.561 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.562 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.562 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.562 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.562 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.562 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.562 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.562 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.562 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.562 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.562 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.562 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.562 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.562 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.563 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.563 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.563 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.563 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.563 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.563 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.563 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.563 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.563 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.563 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.563 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.563 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.563 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.563 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.563 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.563 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.563 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.563 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.564 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.564 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.564 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.564 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.564 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.564 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.565 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.566 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.567 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.568 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.569 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.570 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.571 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.572 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.573 927-2184/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.574 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.575 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.576 927-2184/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.577 927-2184/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.578 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.579 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.580 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.581 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.581 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:01.581 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.582 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.583 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.584 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.585 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.586 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.587 1132-1132/? E/Diag_Lib: DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.591 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.634 1982-1982/? I/EdXposed-Bridge:   Loading class org.meowcat.edxposed.manager.xposed.Enhancement
09-19 00:11:01.635 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-8y2xge8uLmrhBt8pzNcgVA==/base.apk
09-19 00:11:01.635 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:01.682 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:01.691 1132-1132/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.692 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.693 1132-1132/? E/Diag_Lib: qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    DATAD : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.709 1632-2183/? E/Diag_Lib: [IMS_FATAL]| 2183 |qpCheckSockEventsOnNetConnProfiles : pNetConnProfileArray NULL
09-19 00:11:01.714 1632-2183/? I/chatty: uid=1001(radio) /vendor/bin/imsrcsd identical 10 lines
09-19 00:11:01.715 1632-2183/? E/Diag_Lib: [IMS_FATAL]| 2183 |qpCheckSockEventsOnNetConnProfiles : pNetConnProfileArray NULL
09-19 00:11:01.716 1632-2183/? E/Diag_Lib: DPL : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0 gIsDebugDataPathDisabled = 0
09-19 00:11:01.718 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.719 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.720 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.721 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.722 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.723 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.724 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.725 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.726 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.727 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.728 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.729 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.729 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.729 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.729 927-2185/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.729 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.729 927-2185/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.729 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.729 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.730 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.732 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.732 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.732 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.732 927-2185/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.732 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.732 927-2185/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.732 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.732 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.732 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.733 927-2185/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.733 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.733 927-2185/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.733 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.733 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.734 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.735 927-2185/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.735 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.735 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.736 927-2185/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.736 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.736 927-2185/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.736 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.737 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.737 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.737 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.737 927-2185/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.737 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.737 927-2185/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.737 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.737 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.737 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.737 927-2185/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.738 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.738 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.738 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.738 927-2185/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.738 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.738 927-2185/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.738 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.738 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.739 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.739 927-2185/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.739 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.739 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.739 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.739 927-2185/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.739 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.739 927-2185/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.739 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.739 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.739 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.740 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.739 927-2185/? E/Diag_Lib: qpLogDiagInit <== result : 0
09-19 00:11:01.740 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.740 927-2185/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.740 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.740 927-2185/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.740 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.741 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.741 927-2185/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.741 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.742 927-927/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.743 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.744 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.745 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.746 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.747 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.748 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
09-19 00:11:01.749 927-927/? E/Diag_Lib: qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.750 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.751 927-927/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.751 1632-2183/? I/com.qualcomm.qti.uceservice@1.0-service: Successful Initialization
    Starting Service for First Time
09-19 00:11:01.751 1632-2183/? I/ServiceManagement: Registered com.qualcomm.qti.uceservice@2.0::IUceService/com.qualcomm.qti.uceservice (start delay of 5300ms)
09-19 00:11:01.752 927-2186/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.753 927-2187/? E/Diag_Lib:  Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
09-19 00:11:01.753 1632-2183/? I/ServiceManagement: Registered com.qualcomm.qti.imscmservice@2.0::IImsCmService/qti.ims.connectionmanagerservice (start delay of 5301ms)
09-19 00:11:01.753 927-2187/? E/Diag_Lib: QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
     Diag_LSM_Init: Failed to open handle to diag driver, error = 13
    qpLogDiagInit <== result : 0
    QMID : gIsQXDMDisabled 0, gIsADBDisabled 1, gIsDebugDisabled 0, gIsIMSLogsDisabled 0
09-19 00:11:01.782 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:01.782 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:739] qti_file_open():Could not open device file. Errno 2 error msg=No such file or directory
09-19 00:11:01.883 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:01.969 925-1074/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 45000 mC, weight[0] 2
09-19 00:11:01.970 925-1074/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:11:01.983 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:01.987 925-1080/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 45000 mC, weight[0] 2
09-19 00:11:01.988 925-1080/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:11:02.017 1982-1982/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
09-19 00:11:02.018 1982-1982/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
      Loading class ai.lazero.lazero.HookTest_v0
09-19 00:11:02.019 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/com.oranav.ditheredholobackground-WGw3w1Oj7KB1upluOt6Kqw==/base.apk
09-19 00:11:02.019 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.033 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:02.034 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:11:02.034 1982-1982/? I/EdXposed-Bridge:   Loading class com.oranav.ditheredholobackground.DitheredHoloBackground
09-19 00:11:02.037 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/com.jy.xposed.web-0cFiSLP-t5GVpgMJ1Zv9lw==/base.apk
09-19 00:11:02.037 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.053 1982-1982/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:02.054 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Hierarchies don't match'
09-19 00:11:02.054 1982-1982/? I/EdXposed-Bridge:   Loading class com.jy.xposed.web.core.Main
09-19 00:11:02.056 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/z.houbin.skip-ALbC9SZ8n0lVdbMmAc5fQQ==/base.apk
09-19 00:11:02.056 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.084 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:02.106 1982-1982/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
    Found duplicate classes, falling back to extracting from APK : /data/app/z.houbin.skip-ALbC9SZ8n0lVdbMmAc5fQQ==/base.apk
    NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /data/app/z.houbin.skip-ALbC9SZ8n0lVdbMmAc5fQQ==/base.apk and /system/framework/edxp.jar
09-19 00:11:02.152 1982-1982/? I/EdXposed-Bridge:   Loading class z.houbin.skip.MainHook
09-19 00:11:02.153 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/xyz.joas.forcedarkmodeoreo-PGC5RmNRt7E7ivwzrfliMQ==/base.apk
09-19 00:11:02.153 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.185 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:02.210 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:02.211 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:11:02.211 1982-1982/? I/EdXposed-Bridge:   Loading class xyz.joas.forcedarkmodeoreo.ForceDarkMode
09-19 00:11:02.212 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/ml.pyshivam.imeimasker-kBZTMKUVVbE3p0YdbIrmSw==/base.apk
09-19 00:11:02.212 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.291 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:02.293 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
    Found duplicate classes, falling back to extracting from APK : /data/app/ml.pyshivam.imeimasker-kBZTMKUVVbE3p0YdbIrmSw==/base.apk
    NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /data/app/ml.pyshivam.imeimasker-kBZTMKUVVbE3p0YdbIrmSw==/base.apk and /system/framework/edxp.jar
09-19 00:11:02.370 1982-1982/? I/EdXposed-Bridge:   Loading class ml.pyshivam.imeimasker.IMEIMasker
09-19 00:11:02.371 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/com.xloger.exlink.app-k4miYHCp7k_RBO4_2BxjHg==/base.apk
09-19 00:11:02.371 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.392 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:02.394 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:02.395 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:11:02.395 1982-1982/? I/EdXposed-Bridge:   Loading class com.xloger.exlink.app.HookMain
09-19 00:11:02.397 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/louis.baseapk-Nb3bv9DiXpVlLtzRL5xIdQ==/base.apk
09-19 00:11:02.397 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.453 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:02.454 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:11:02.455 1982-1982/? I/EdXposed-Bridge:   Loading class louis.ʹ
    Loading modules from /data/app/io.alcatraz.noapplet-eIitfHwR5bBcjeYqx3rDpA==/base.apk
09-19 00:11:02.455 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.493 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:02.537 1982-1982/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
    Found duplicate classes, falling back to extracting from APK : /data/app/io.alcatraz.noapplet-eIitfHwR5bBcjeYqx3rDpA==/base.apk
09-19 00:11:02.538 1982-1982/? W/zygote64: NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /data/app/io.alcatraz.noapplet-eIitfHwR5bBcjeYqx3rDpA==/base.apk and /system/framework/edxp.jar
09-19 00:11:02.594 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:02.615 1982-1982/? I/EdXposed-Bridge:   Loading class io.alcatraz.noapplet.ModuleMain
09-19 00:11:02.616 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/li.lingfeng.ltweaks-wp3kMW3n45fUnDO4mVLXAg==/base.apk
09-19 00:11:02.616 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.695 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:02.765 1982-1982/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:02.768 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Hierarchies don't match'
09-19 00:11:02.769 1982-1982/? I/EdXposed-Bridge:   Loading class li.lingfeng.ltweaks.xposed.XposedLoader
09-19 00:11:02.778 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/ru.bluecat.android.xposed.mods.appsettings-VYHj687WS3roYgko83SRXg==/base.apk
09-19 00:11:02.778 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.783 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:739] qti_file_open():Could not open device file. Errno 2 error msg=No such file or directory
09-19 00:11:02.787 1982-1982/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
    Found duplicate classes, falling back to extracting from APK : /data/app/ru.bluecat.android.xposed.mods.appsettings-VYHj687WS3roYgko83SRXg==/base.apk
    NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /data/app/ru.bluecat.android.xposed.mods.appsettings-VYHj687WS3roYgko83SRXg==/base.apk and /system/framework/edxp.jar
09-19 00:11:02.792 1982-1982/? I/EdXposed-Bridge:   Loading class ru.bluecat.android.xposed.mods.appsettings.hooks.XposedMod
09-19 00:11:02.796 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:02.797 1982-1982/? W/main: type=1400 audit(0.0:132): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:02.805 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:02.806 1982-1982/? D/SandHook: method <private void android.view.Display.updateDisplayInfoLocked()> hook <replacement> success!
09-19 00:11:02.807 1982-1982/? W/main: type=1400 audit(0.0:134): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:02.816 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:02.817 1982-1982/? D/SandHook: method <protected android.view.ViewGroup com.android.internal.policy.PhoneWindow.generateLayout(com.android.internal.policy.DecorView)> hook <replacement> success!
09-19 00:11:02.817 1982-1982/? W/main: type=1400 audit(0.0:136): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:02.825 1982-1982/? W/zygote64: Unsupported class loader
09-19 00:11:02.826 1982-1982/? W/zygote64: Could not establish class loader context
09-19 00:11:02.826 1982-1982/? D/SandHook: method <public void android.view.Window.setFlags(int,int)> hook <replacement> success!
09-19 00:11:02.827 1982-1982/? W/main: type=1400 audit(0.0:138): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:02.835 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:02.836 1982-1982/? D/SandHook: method <public void android.view.ViewRootImpl.dispatchSystemUiVisibilityChanged(int,int,int,int)> hook <replacement> success!
09-19 00:11:02.837 1982-1982/? W/main: type=1400 audit(0.0:140): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:02.844 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:02.844 1982-1982/? D/SandHook: method <public void android.app.Activity.setRequestedOrientation(int)> hook <replacement> success!
09-19 00:11:02.843 1982-1982/? W/main: type=1400 audit(0.0:142): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:02.852 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:02.853 1982-1982/? D/SandHook: method <void android.inputmethodservice.InputMethodService.doStartInput(android.view.inputmethod.InputConnection,android.view.inputmethod.EditorInfo,boolean)> hook <replacement> success!
09-19 00:11:02.853 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/top.imlk.confesstalk-nX7zXQm5XMtH6SjG9zammA==/base.apk
09-19 00:11:02.853 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.869 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:02.870 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:11:02.870 1982-1982/? I/EdXposed-Bridge:   Loading class top.imlk.confesstalk.hooker.Injecter
09-19 00:11:02.871 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/hdfg159.qqsendpoke-oK-fuqejo1vRTTkNDpO7iw==/base.apk
09-19 00:11:02.871 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.877 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:02.877 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:11:02.878 1982-1982/? I/EdXposed-Bridge:   Loading class hdfg159.qqsendpoke.hook.PokeMsgHook
    Loading modules from /data/app/com.arjerine.textxposed-wwEDo2OIEu6Gyza_qvGUUA==/base.apk
09-19 00:11:02.878 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:02.896 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:02.973 925-1074/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 45000 mC, weight[0] 2
09-19 00:11:02.974 925-1074/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:11:02.997 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:02.997 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:03.000 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:11:03.001 1982-1982/? I/EdXposed-Bridge:   Loading class com.arjerine.textxposed.xposed.Xposed
09-19 00:11:03.011 1982-1982/? I/EdXposed-Bridge:   Loading class com.arjerine.textxposed.xposed.XposedDetect
      Loading class com.arjerine.textxposed.macro.Xposed
09-19 00:11:03.015 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:11:03.015 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:03.038 1982-1982/? W/zygote64: Method La/b/m/a/b;.b is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:11:03.039 1982-1982/? W/zygote64: Method La/i/f/j;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/f/j;.b is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/l/u$c;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/l/u$c;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/l/d/n;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.b is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.e is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.g is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.h is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:11:03.040 1982-1982/? W/zygote64: Method Lb/c/a/a/f0/d;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.g is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.h is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.i is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.j is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.m is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.o is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.p is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.s is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:11:03.041 1982-1982/? W/zygote64: Method La/i/f/k/c;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/f/k/c;.setTintList is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:11:03.058 1982-1982/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
    Found duplicate classes, falling back to extracting from APK : /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk and /system/framework/edxp.jar
09-19 00:11:03.078 1982-1982/? W/zygote64: Method La/b/m/a/b;.b is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/f/j;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/f/j;.b is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/l/u$c;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/l/u$c;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/l/d/n;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.b is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.e is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.g is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/s/b0;.h is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:11:03.079 1982-1982/? W/zygote64: Method Lb/c/a/a/f0/d;.a is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.g is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.h is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.i is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.j is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.m is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.o is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.p is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method Lb/c/a/a/z/e;.s is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:11:03.080 1982-1982/? W/zygote64: Method La/i/f/k/c;.c is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
    Method La/i/f/k/c;.setTintList is abstract, but the declaring class is neither abstract nor an interface in dex file /data/app/com.modosa.unblockdarkmode-Tt2JE85O1WGyg0l925JhKw==/base.apk
09-19 00:11:03.093 1982-1982/? I/EdXposed-Bridge:   Loading class com.modosa.unblockdarkmode.util.XModule
09-19 00:11:03.095 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/tk.navideju.darkthemefixer-n5QMTRQLRxmyDjunCSs9-Q==/base.apk
09-19 00:11:03.095 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:03.099 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:03.184 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:03.185 1982-1982/? I/EdXposed-Bridge:   Loading class tk.navideju.darkthemefixer.Main
09-19 00:11:03.199 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:03.208 1982-1982/? I/EdXposed-Bridge: [DarkThemeFixer] From zygote: true can read?: false
09-19 00:11:03.209 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/ru.uMcSebxc.QziYqbJtk-gLoMearDmswr_Yiwmy4c9g==/base.apk
09-19 00:11:03.209 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:03.300 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:03.322 1982-1982/? W/zygote64: ClassLoaderContext parent mismatch.  (PCL[] | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
    Found duplicate classes, falling back to extracting from APK : /data/app/ru.uMcSebxc.QziYqbJtk-gLoMearDmswr_Yiwmy4c9g==/base.apk
    NOTE: This wastes RAM and hurts startup performance.
    Found duplicated class when checking oat files: 'Landroidx/annotation/Keep;' in /data/app/ru.uMcSebxc.QziYqbJtk-gLoMearDmswr_Yiwmy4c9g==/base.apk and /system/framework/edxp.jar
09-19 00:11:03.359 817-817/? I/MSM-irqbalance: Discovered a new IRQ: 76
    Discovered a new IRQ: 77
    Discovered a new IRQ: 78
    Discovered a new IRQ: 79
    Discovered a new IRQ: 80
    Discovered a new IRQ: 81
    Discovered a new IRQ: 82
    Discovered a new IRQ: 84
    Discovered a new IRQ: 85
    Discovered a new IRQ: 86
    Discovered a new IRQ: 87
09-19 00:11:03.361 817-817/? E/MSM-irqbalance: WARNING: Cannot find matching virq for hwirq(22).
09-19 00:11:03.401 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:03.427 1982-1982/? I/EdXposed-Bridge:   Loading class com.xposed.XSupport
09-19 00:11:03.430 1982-1982/? W/main: type=1400 audit(0.0:144): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:03.438 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:03.439 1982-1982/? D/SandHook: method <protected boolean com.android.org.conscrypt.OpenSSLSignature.engineVerify(byte[]) throws java.security.SignatureException> hook <replacement> success!
09-19 00:11:03.437 1982-1982/? W/main: type=1400 audit(0.0:146): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:03.447 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:03.448 1982-1982/? D/SandHook: method <public static boolean java.security.MessageDigest.isEqual(byte[],byte[])> hook <replacement> success!
09-19 00:11:03.447 1982-1982/? W/main: type=1400 audit(0.0:148): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:03.456 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:03.456 1982-1982/? D/SandHook: method <public final boolean java.security.Signature.verify(byte[]) throws java.security.SignatureException> hook <replacement> success!
09-19 00:11:03.457 1982-1982/? W/main: type=1400 audit(0.0:150): avc: denied { write } for name="0" dev="sda17" ino=3932163 scontext=u:r:zygote:s0 tcontext=u:object_r:system_data_file:s0 tclass=dir permissive=0
09-19 00:11:03.465 1982-1982/? W/zygote64: Unsupported class loader
    Could not establish class loader context
09-19 00:11:03.466 1982-1982/? D/SandHook: method <public final boolean java.security.Signature.verify(byte[],int,int) throws java.security.SignatureException> hook <replacement> success!
09-19 00:11:03.466 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/fi.veetipaananen.android.disableflagsecure-vph3x2wEvvnXRoJcUJAdmQ==/base.apk
09-19 00:11:03.466 1982-1982/? W/zygote64: Opening an oat file without a class loader. Are you using the deprecated DexFile APIs?
09-19 00:11:03.472 1982-1982/? W/zygote64: ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[/system/framework/org.apache.http.legacy.jar*2680228128]} | PCL[];PCL[/system/framework/edxp.jar*1350745069:/system/framework/eddalvikdx.jar*249839725:/system/framework/eddexmaker.jar*2240721425];IMC[<unknown>*3538116118];PCL[])
09-19 00:11:03.473 1982-1982/? I/zygote64: Failed to add image file Rejecting application image due to class loader mismatch: 'Mismatch in shared libraries'
09-19 00:11:03.473 1982-1982/? I/EdXposed-Bridge:   Loading class fi.veetipaananen.android.disableflagsecure.DisableFlagSecureModule
09-19 00:11:03.479 1982-1982/? D/Zygote: Forked child process 2193
09-19 00:11:03.479 1982-1982/? I/Zygote: System server process 2193 has been created
09-19 00:11:03.481 1982-1982/? I/Zygote: Accepting command socket connections
09-19 00:11:03.502 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:03.519 2193-2193/? I/system_server: The ClassLoaderContext is a special shared library.
09-19 00:11:03.529 2193-2193/? I/chatty: uid=1000 system_server identical 3 lines
09-19 00:11:03.531 2193-2193/? I/system_server: The ClassLoaderContext is a special shared library.
09-19 00:11:03.551 2193-2193/? V/Riru: edxp: forkSystemServerPost
09-19 00:11:03.594 2193-2193/? I/SystemServer: InitBeforeStartServices
09-19 00:11:03.596 2193-2193/? I/SystemServer: Entered the Android system server!
09-19 00:11:03.602 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:03.687 2193-2193/system_process E/UsbAlsaJackDetectorJNI: Can't register UsbAlsaJackDetector native methods
09-19 00:11:03.689 2193-2193/system_process V/Riru: jniRegisterNativeMethods com/android/server/storage/AppFuseBridge
09-19 00:11:03.696 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.697 2193-2193/system_process D/SandHook: method <private void com.android.server.SystemServer.startBootstrapServices()> hook <replacement> success!
09-19 00:11:03.702 2193-2193/system_process D/SystemServerTiming: InitBeforeStartServices took to complete: 108ms
09-19 00:11:03.702 2193-2193/system_process I/SystemServer: StartServices
09-19 00:11:03.703 2193-2193/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "android.content.pm.PackageParser.Package" on path: DexPathList[[zip file "/system/framework/org.lineageos.platform.jar", zip file "/system/framework/services.jar", zip file "/system/framework/ethernet-service.jar", zip file "/system/framework/wifi-service.jar", zip file "/system/framework/com.android.location.provider.jar"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at ai.lazero.lazero.HookTest_v0.handleLoadPackage(HookTest_v0.java:35)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-19 00:11:03.704 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:03.712 2193-2193/system_process E/EdXposed-Bridge: de.robv.android.xposed.XposedHelpers$ClassNotFoundError: java.lang.ClassNotFoundException: com.android.internal.policy.impl.GlobalActions
        at de.robv.android.xposed.XposedHelpers.findClass(XposedHelpers.java:71)
        at ma.wanam.wanamkit.XGlobalActions.doHook(XGlobalActions.java:108)
        at ma.wanam.wanamkit.Xposed.handleLoadPackage(Xposed.java:58)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
     Caused by: java.lang.ClassNotFoundException: com.android.internal.policy.impl.GlobalActions
        at java.lang.Class.classForName(Native Method)
        at java.lang.Class.forName(Class.java:454)
        at external.org.apache.commons.lang3.ClassUtils.getClass(ClassUtils.java:823)
        at de.robv.android.xposed.XposedHelpers.findClass(XposedHelpers.java:69)
        at ma.wanam.wanamkit.XGlobalActions.doHook(XGlobalActions.java:108) 
        at ma.wanam.wanamkit.Xposed.handleLoadPackage(Xposed.java:58) 
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37) 
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61) 
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117) 
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36) 
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51) 
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357) 
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46) 
        at com.android.server.SystemServer.run(SystemServer.java:527) 
        at com.android.server.SystemServer.main(SystemServer.java:356) 
        at java.lang.reflect.Method.invoke(Native Method) 
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491) 
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918) 
     Caused by: java.lang.ClassNotFoundException: Didn't find class "com.android.internal.policy.impl.GlobalActions" on path: DexPathList[[zip file "/system/framework/org.lineageos.platform.jar", zip file "/system/framework/services.jar", zip file "/system/framework/ethernet-service.jar", zip file "/system/framework/wifi-service.jar", zip file "/system/framework/com.android.location.provider.jar"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at java.lang.Class.classForName(Native Method) 
        at java.lang.Class.forName(Class.java:454) 
        at external.org.apache.commons.lang3.ClassUtils.getClass(ClassUtils.java:823) 
        at de.robv.android.xposed.XposedHelpers.findClass(XposedHelpers.java:69) 
        at ma.wanam.wanamkit.XGlobalActions.doHook(XGlobalActions.java:108) 
        at ma.wanam.wanamkit.Xposed.handleLoadPackage(Xposed.java:58) 
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37) 
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61) 
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117) 
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36) 
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51) 
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357) 
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46) 
        at com.android.server.SystemServer.run(SystemServer.java:527) 
        at com.android.server.SystemServer.main(SystemServer.java:356) 
        at java.lang.reflect.Method.invoke(Native Method) 
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491) 
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918) 
09-19 00:11:03.713 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.714 2193-2193/system_process D/SandHook: method <com.android.server.pm.SharedUserSetting com.android.server.pm.Settings.addSharedUserLPw(java.lang.String,int,int,int)> hook <replacement> success!
09-19 00:11:03.716 2193-2193/system_process E/EdXposed-Bridge: java.lang.NullPointerException: Attempt to read from field 'int android.content.pm.ApplicationInfo.flags' on a null object reference
        at com.jy.xposed.web.core.Main.handleLoadPackage(Unknown Source:2)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
    java.lang.NoSuchMethodError: android.app.WallpaperManager$Globals#getWallpaperColors(int,int)#exact
        at de.robv.android.xposed.XposedHelpers.findMethodExact(XposedHelpers.java:344)
        at de.robv.android.xposed.XposedHelpers.findAndHookMethod(XposedHelpers.java:185)
        at de.robv.android.xposed.XposedHelpers.findAndHookMethod(XposedHelpers.java:260)
        at xyz.joas.forcedarkmodeoreo.ForceDarkMode.handleLoadPackage(ForceDarkMode.java:102)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-19 00:11:03.721 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.723 2193-2193/system_process D/SandHook: method <public android.content.pm.ApplicationInfo com.android.server.pm.PackageManagerService.getApplicationInfo(java.lang.String,int,int)> hook <replacement> success!
09-19 00:11:03.725 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.726 2193-2193/system_process D/SandHook: method <public android.content.pm.PackageInfo com.android.server.pm.PackageManagerService.getPackageInfo(java.lang.String,int,int)> hook <replacement> success!
09-19 00:11:03.730 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.731 2193-2193/system_process D/SandHook: method <int com.android.server.am.ActivityManagerService.appRestrictedInBackgroundLocked(int,java.lang.String,int)> hook <replacement> success!
09-19 00:11:03.733 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.734 2193-2193/system_process D/SandHook: method <int com.android.server.am.ActivityManagerService.appServicesRestrictedInBackgroundLocked(int,java.lang.String,int)> hook <replacement> success!
09-19 00:11:03.735 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.736 2193-2193/system_process D/SandHook: method <int com.android.server.am.ActivityManagerService.getAppStartModeLocked(int,java.lang.String,int,int,boolean,boolean,boolean)> hook <replacement> success!
09-19 00:11:03.737 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.738 2193-2193/system_process D/SandHook: method <public void android.view.SurfaceView.setSecure(boolean)> hook <replacement> success!
09-19 00:11:03.739 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.741 2193-2193/system_process D/SandHook: method <com.android.server.am.ProcessRecord(com.android.server.am.ActivityManagerService,android.content.pm.ApplicationInfo,java.lang.String,int)> hook <replacement> success!
09-19 00:11:03.741 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.742 2193-2193/system_process D/SandHook: method <boolean com.android.server.wm.ActivityStackSupervisor.realStartActivityLocked(com.android.server.wm.ActivityRecord,com.android.server.wm.WindowProcessController,boolean,boolean) throws android.os.RemoteException> hook <replacement> success!
09-19 00:11:03.743 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.745 2193-2193/system_process D/SandHook: method <com.android.server.wm.ActivityRecord(com.android.server.wm.ActivityTaskManagerService,com.android.server.wm.WindowProcessController,int,int,java.lang.String,android.content.Intent,java.lang.String,android.content.pm.ActivityInfo,android.content.res.Configuration,com.android.server.wm.ActivityRecord,java.lang.String,int,boolean,boolean,com.android.server.wm.ActivityStackSupervisor,android.app.ActivityOptions,com.android.server.wm.ActivityRecord)> hook <replacement> success!
09-19 00:11:03.746 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.747 2193-2193/system_process D/SandHook: method <boolean com.android.server.wm.ActivityTaskManagerService.isGetTasksAllowed(java.lang.String,int,int)> hook <replacement> success!
09-19 00:11:03.748 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.749 2193-2193/system_process D/SandHook: method <public void com.android.server.pm.PackageManagerService.systemReady()> hook <replacement> success!
09-19 00:11:03.750 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.750 2193-2193/system_process D/SandHook: method <com.android.server.pm.permission.PermissionManagerService(android.content.Context,java.lang.Object)> hook <replacement> success!
09-19 00:11:03.751 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.752 2193-2193/system_process D/SandHook: method <private void com.android.server.pm.permission.PermissionManagerService.restorePermissionState(android.content.pm.PackageParser$Package,boolean,java.lang.String,com.android.server.pm.permission.PermissionManagerServiceInternal$PermissionCallback)> hook <replacement> success!
09-19 00:11:03.753 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.754 2193-2193/system_process D/SandHook: method <void com.android.server.notification.NotificationManagerService.enqueueNotificationInternal(java.lang.String,java.lang.String,int,int,java.lang.String,int,android.app.Notification,int)> hook <replacement> success!
09-19 00:11:03.755 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.756 2193-2193/system_process D/SandHook: method <public android.widget.TextView(android.content.Context)> hook <replacement> success!
09-19 00:11:03.756 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.757 2193-2193/system_process D/SandHook: method <public android.widget.TextView(android.content.Context,android.util.AttributeSet)> hook <replacement> success!
09-19 00:11:03.757 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.758 2193-2193/system_process D/SandHook: method <public android.widget.TextView(android.content.Context,android.util.AttributeSet,int)> hook <replacement> success!
09-19 00:11:03.758 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.759 2193-2193/system_process D/SandHook: method <public android.widget.TextView(android.content.Context,android.util.AttributeSet,int,int)> hook <replacement> success!
09-19 00:11:03.760 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.761 2193-2193/system_process D/SandHook: method <protected void android.widget.TextView.onFocusChanged(boolean,int,android.graphics.Rect)> hook <replacement> success!
09-19 00:11:03.762 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.763 2193-2193/system_process D/SandHook: method <public boolean android.widget.Editor$TextActionModeCallback.onCreateActionMode(android.view.ActionMode,android.view.Menu)> hook <replacement> success!
09-19 00:11:03.763 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.764 2193-2193/system_process D/SandHook: method <public boolean android.widget.Editor$TextActionModeCallback.onActionItemClicked(android.view.ActionMode,android.view.MenuItem)> hook <replacement> success!
09-19 00:11:03.765 2193-2193/system_process E/EdXposed-Bridge: java.lang.AbstractMethodError: abstract method "void de.robv.android.xposed.IXposedHookLoadPackage.handleLoadPackage(de.robv.android.xposed.callbacks.XC_LoadPackage$LoadPackageParam)"
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-19 00:11:03.772 2193-2193/system_process E/EdXposed-Bridge: java.io.FileNotFoundException: /data/data/com.xloger.exlink.app/files/AppData: open failed: ENOENT (No such file or directory)
        at libcore.io.IoBridge.open(IoBridge.java:496)
        at java.io.FileInputStream.<init>(FileInputStream.java:159)
        at java.io.FileInputStream.<init>(FileInputStream.java:115)
        at com.xloger.exlink.app.c.c.b(Unknown Source:20)
        at com.xloger.exlink.app.c.b.a(Unknown Source:8)
        at com.xloger.exlink.app.HookMain.handleLoadPackage(Unknown Source:13)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
     Caused by: android.system.ErrnoException: open failed: ENOENT (No such file or directory)
        at libcore.io.Linux.open(Native Method)
        at libcore.io.ForwardingOs.open(ForwardingOs.java:167)
        at libcore.io.BlockGuardOs.open(BlockGuardOs.java:252)
        at libcore.io.IoBridge.open(IoBridge.java:482)
        at java.io.FileInputStream.<init>(FileInputStream.java:159) 
        at java.io.FileInputStream.<init>(FileInputStream.java:115) 
        at com.xloger.exlink.app.c.c.b(Unknown Source:20) 
        at com.xloger.exlink.app.c.b.a(Unknown Source:8) 
        at com.xloger.exlink.app.HookMain.handleLoadPackage(Unknown Source:13) 
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37) 
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61) 
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117) 
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36) 
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51) 
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357) 
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46) 
        at com.android.server.SystemServer.run(SystemServer.java:527) 
        at com.android.server.SystemServer.main(SystemServer.java:356) 
        at java.lang.reflect.Method.invoke(Native Method) 
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491) 
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918) 
09-19 00:11:03.772 2193-2193/system_process W/System.err: java.io.FileNotFoundException: /data/data/com.xloger.exlink.app/files/AppData: open failed: ENOENT (No such file or directory)
        at libcore.io.IoBridge.open(IoBridge.java:496)
        at java.io.FileInputStream.<init>(FileInputStream.java:159)
        at java.io.FileInputStream.<init>(FileInputStream.java:115)
        at com.xloger.exlink.app.c.c.b(Unknown Source:20)
        at com.xloger.exlink.app.c.b.a(Unknown Source:8)
        at com.xloger.exlink.app.HookMain.handleLoadPackage(Unknown Source:13)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.StartBootstrapServices.beforeHookedMethod(StartBootstrapServices.java:36)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
    Caused by: android.system.ErrnoException: open failed: ENOENT (No such file or directory)
        at libcore.io.Linux.open(Native Method)
        at libcore.io.ForwardingOs.open(ForwardingOs.java:167)
        at libcore.io.BlockGuardOs.open(BlockGuardOs.java:252)
        at libcore.io.IoBridge.open(IoBridge.java:482)
    	... 17 more
09-19 00:11:03.773 2193-2193/system_process I/Xposed: Load li.lingfeng.ltweaks.xposed.system.XposedSetInactive for android, with prefs []
09-19 00:11:03.776 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.777 2193-2193/system_process D/SandHook: method <final void com.android.server.am.ActivityManagerService.finishBooting()> hook <replacement> success!
09-19 00:11:03.777 2193-2193/system_process I/Xposed: Load li.lingfeng.ltweaks.xposed.system.XposedPreventForegroundService for android, with prefs []
    Load li.lingfeng.ltweaks.xposed.system.XposedPreventReceiver for android, with prefs []
09-19 00:11:03.778 2193-2193/system_process I/Xposed: Load li.lingfeng.ltweaks.xposed.system.XposedPreventWakeLock for android, with prefs []
    Load li.lingfeng.ltweaks.xposed.system.XposedShareFilter for android, with prefs []
09-19 00:11:03.780 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.781 2193-2193/system_process D/SandHook: method <private java.util.List com.android.server.pm.PackageManagerService.queryIntentActivitiesInternal(android.content.Intent,java.lang.String,int,int)> hook <replacement> success!
09-19 00:11:03.781 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.782 2193-2193/system_process D/SandHook: method <private java.util.List com.android.server.pm.PackageManagerService.queryIntentActivitiesInternal(android.content.Intent,java.lang.String,int,int,int,boolean,boolean)> hook <replacement> success!
09-19 00:11:03.783 2193-2193/system_process I/Xposed: Load li.lingfeng.ltweaks.xposed.system.XposedTrustAgentWifi for android, with prefs []
09-19 00:11:03.783 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:756] qti_file_open():Could not open device file. Abort. Errno 2 error msg=No such file or directory
    [qti_rmnet_peripheral.c:841] qti_rmnet_ph_init():Failed to open MHI peripheral device file. Abort. Error 2
09-19 00:11:03.784 917-917/? I/QTI_SDM_INFO: [qti_rmnet_dpm.c:237] qti_dpm_init():qti_dpm_init()
09-19 00:11:03.784 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.785 917-917/? E/QMI_FW: QMUXD: WARNING qmi_qmux_if_pwr_up_init failed! rc=-6
09-19 00:11:03.785 917-917/? I/QTI_SDM_INFO: [qti_rmnet_dpm.c:630] dpm_service_available_cb():dpm_service_available_cb 
    [qti_rmnet_dpm.c:266] qti_dpm_init():Successful DPM service registration
    [qti_rmnet_peripheral.c:1428] qti_dpl_ph_init():Open DPL file to receive QMI messages
09-19 00:11:03.786 2193-2193/system_process D/SandHook: method <public int com.android.server.pm.PackageManagerService.checkPermission(java.lang.String,java.lang.String,int)> hook <replacement> success!
09-19 00:11:03.786 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:739] qti_file_open():Could not open device file. Errno 2 error msg=No such file or directory
09-19 00:11:03.786 2193-2193/system_process I/Xposed: Load li.lingfeng.ltweaks.xposed.system.XposedTextActions for all packages (exclude 1), with prefs []
    Load li.lingfeng.ltweaks.xposed.system.XposedPreventExactAlarm for android, with prefs []
09-19 00:11:03.788 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.789 2193-2193/system_process D/SandHook: method <public boolean android.content.ContextWrapper.bindService(android.content.Intent,int,java.util.concurrent.Executor,android.content.ServiceConnection)> hook <replacement> success!
09-19 00:11:03.789 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.790 917-2215/? I/QTI_SDM_INFO: [qti_rmnet_dpm.c:133] dpm_client_init(): DPM client inited 2
    [qti_rmnet_peripheral.c:1221] qti_rmnet_ph_set_modem_state():Received set modem state to 1
09-19 00:11:03.790 917-2215/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:1233] qti_rmnet_ph_set_modem_state():Couldn't set ph_iface_fd
    [qti_rmnet_modem.c:1813] qti_rmnet_modem_in_service():Failed to set modem state on peripheral driver file
    [qti_rmnet_modem.c:1826] qti_rmnet_modem_in_service():Failed to set ph_iface_fd
09-19 00:11:03.790 917-2215/? I/QTI_SDM_INFO: [qti_rmnet_peripheral.c:1298] qti_dpl_process_ph_reset():Processing DPL peripheral reset
    [qti_rmnet_peripheral.c:1306] qti_dpl_process_ph_reset():Couldn't get FRMNET LINE STATE from driver
09-19 00:11:03.790 2193-2193/system_process D/SandHook: method <public boolean android.content.ContextWrapper.bindService(android.content.Intent,android.content.ServiceConnection,int)> hook <replacement> success!
09-19 00:11:03.790 917-2215/? E/QTI_SDM_INFO: [qti_rmnet_dpm.c:194] dpm_client_init():DPL DPM Init check failed
09-19 00:11:03.790 917-2215/? I/QTI_SDM_INFO: [qti_cmdq.c:113] qti_cmdq_cmd_free():qcmap_cmdq: free one commmand data
09-19 00:11:03.794 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.795 2193-2193/system_process D/SandHook: method <public android.content.Intent android.content.Intent.setPackage(java.lang.String)> hook <replacement> success!
09-19 00:11:03.796 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.797 2193-2193/system_process D/SandHook: method <public com.android.server.pm.PackageManagerService(android.content.Context,com.android.server.pm.Installer,boolean,boolean)> hook <replacement> success!
09-19 00:11:03.799 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.801 2193-2193/system_process D/SandHook: method <private android.content.pm.PackageParser$Package com.android.server.pm.PackageManagerService.scanPackageLI(java.io.File,int,int,long,android.os.UserHandle) throws com.android.server.pm.PackageManagerException> hook <replacement> success!
09-19 00:11:03.803 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.804 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:03.805 2193-2193/system_process D/SandHook: method <public boolean android.content.pm.PackageParser$SigningDetails.checkCapability(android.content.pm.PackageParser$SigningDetails,int)> hook <replacement> success!
09-19 00:11:03.805 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.806 2193-2193/system_process D/SandHook: method <public boolean android.content.pm.PackageParser$SigningDetails.checkCapability(java.lang.String,int)> hook <replacement> success!
09-19 00:11:03.807 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.808 2193-2193/system_process D/SandHook: method <public static int com.android.server.pm.PackageManagerServiceUtils.compareSignatures(android.content.pm.Signature[],android.content.pm.Signature[])> hook <replacement> success!
09-19 00:11:03.811 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.813 2193-2193/system_process D/SandHook: method <void com.android.server.pm.PackageManagerService.installStage(com.android.server.pm.PackageManagerService$ActiveInstallSession)> hook <replacement> success!
09-19 00:11:03.813 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.814 2193-2193/system_process D/SandHook: method <void com.android.server.pm.PackageManagerService.installStage(java.util.List) throws com.android.server.pm.PackageManagerException> hook <replacement> success!
09-19 00:11:03.815 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.817 2193-2193/system_process D/SandHook: method <private static void com.android.server.pm.PackageManagerService.checkDowngrade(android.content.pm.PackageParser$Package,android.content.pm.PackageInfoLite) throws com.android.server.pm.PackageManagerException> hook <replacement> success!
09-19 00:11:03.821 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.823 2193-2193/system_process D/SandHook: method <private android.content.pm.PackageInfo com.android.server.pm.PackageManagerService.generatePackageInfo(com.android.server.pm.PackageSetting,int,int)> hook <replacement> success!
09-19 00:11:03.825 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.826 2193-2193/system_process D/SandHook: method <public android.content.pm.ParceledListSlice com.android.server.pm.PackageManagerService.getInstalledApplications(int,int)> hook <replacement> success!
09-19 00:11:03.827 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.829 2193-2193/system_process D/SandHook: method <public android.content.pm.ParceledListSlice com.android.server.pm.PackageManagerService.getInstalledPackages(int,int)> hook <replacement> success!
09-19 00:11:03.831 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.832 2193-2193/system_process D/SandHook: method <protected android.app.ApplicationPackageManager(android.app.ContextImpl,android.content.pm.IPackageManager)> hook <replacement> success!
09-19 00:11:03.833 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.834 2193-2193/system_process D/SandHook: method <public android.content.pm.PackageInfo android.app.ApplicationPackageManager.getPackageInfo(android.content.pm.VersionedPackage,int) throws android.content.pm.PackageManager$NameNotFoundException> hook <replacement> success!
09-19 00:11:03.834 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.835 2193-2193/system_process D/SandHook: method <public android.content.pm.PackageInfo android.app.ApplicationPackageManager.getPackageInfo(java.lang.String,int) throws android.content.pm.PackageManager$NameNotFoundException> hook <replacement> success!
09-19 00:11:03.836 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.837 2193-2193/system_process D/SandHook: method <public android.content.pm.ApplicationInfo android.app.ApplicationPackageManager.getApplicationInfo(java.lang.String,int) throws android.content.pm.PackageManager$NameNotFoundException> hook <replacement> success!
09-19 00:11:03.837 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.838 2193-2193/system_process D/SandHook: method <public java.util.List android.app.ApplicationPackageManager.getInstalledApplications(int)> hook <replacement> success!
09-19 00:11:03.839 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.840 2193-2193/system_process D/SandHook: method <public java.util.List android.app.ApplicationPackageManager.getInstalledPackages(int)> hook <replacement> success!
09-19 00:11:03.840 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.841 2193-2193/system_process D/SandHook: method <public java.util.List android.app.ApplicationPackageManager.getPreferredPackages(int)> hook <replacement> success!
09-19 00:11:03.846 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.847 2193-2193/system_process D/SandHook: method <public java.lang.String android.telephony.TelephonyManager.getImei()> hook <replacement> success!
09-19 00:11:03.847 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.848 2193-2193/system_process D/SandHook: method <public java.lang.String android.telephony.TelephonyManager.getDeviceId()> hook <replacement> success!
09-19 00:11:03.848 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.849 2193-2193/system_process D/SandHook: method <public java.lang.String android.telephony.TelephonyManager.getImei(int)> hook <replacement> success!
09-19 00:11:03.850 2193-2193/system_process W/system_server: Unsupported class loader
09-19 00:11:03.850 2193-2193/system_process D/SandHook: method <public java.lang.String android.telephony.TelephonyManager.getDeviceId(int)> hook <replacement> success!
09-19 00:11:03.852 2193-2193/system_process I/SystemServer: StartWatchdog
09-19 00:11:03.862 2193-2193/system_process D/SystemServerTiming: StartWatchdog took to complete: 10ms
09-19 00:11:03.862 2193-2193/system_process I/SystemServer: Reading configuration...
    ReadingSystemConfig
09-19 00:11:03.863 2193-2193/system_process D/SystemServerTiming: ReadingSystemConfig took to complete: 0ms
09-19 00:11:03.863 2193-2193/system_process I/SystemServer: StartInstaller
09-19 00:11:03.863 2193-2193/system_process I/SystemServiceManager: Starting com.android.server.pm.Installer
09-19 00:11:03.864 2193-2226/system_process D/SystemServerInitThreadPool: Started executing ReadingSystemConfig
09-19 00:11:03.865 956-1022/? D/installd: Found quota mount /dev/block/bootdevice/by-name/userdata at /data
09-19 00:11:03.902 2193-2193/system_process D/SystemServerTiming: StartInstaller took to complete: 39ms
09-19 00:11:03.902 2193-2193/system_process I/SystemServer: DeviceIdentifiersPolicyService
09-19 00:11:03.902 2193-2193/system_process I/SystemServiceManager: Starting com.android.server.os.DeviceIdentifiersPolicyService
09-19 00:11:03.904 2193-2193/system_process D/SystemServerTiming: DeviceIdentifiersPolicyService took to complete: 2ms
09-19 00:11:03.904 2193-2193/system_process I/SystemServer: UriGrantsManagerService
09-19 00:11:03.904 2193-2193/system_process I/SystemServiceManager: Starting com.android.server.uri.UriGrantsManagerService$Lifecycle
09-19 00:11:03.905 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:03.907 2193-2193/system_process D/SystemServerTiming: UriGrantsManagerService took to complete: 3ms
09-19 00:11:03.907 2193-2193/system_process I/SystemServer: StartActivityManager
09-19 00:11:03.907 2193-2193/system_process I/SystemServiceManager: Starting com.android.server.wm.ActivityTaskManagerService$Lifecycle
09-19 00:11:03.916 2193-2226/system_process W/SystemConfig: No directory /product_services/etc/sysconfig, skipping
    No directory /product_services/etc/permissions, skipping
09-19 00:11:03.916 2193-2226/system_process D/SystemServerInitThreadPool: Finished executing ReadingSystemConfig
09-19 00:11:03.928 2193-2193/system_process I/SystemServiceManager: Starting com.android.server.am.ActivityManagerService$Lifecycle
09-19 00:11:03.932 2193-2193/system_process I/ActivityManager: Memory class: 192
09-19 00:11:03.935 2193-2193/system_process E/libpsi: No kernel psi monitor support (errno=2)
09-19 00:11:03.935 2193-2193/system_process E/LowMemDetector: Failed to register psi trigger
09-19 00:11:03.939 2193-2193/system_process D/BatteryStatsImpl: Reading daily items from /data/system/batterystats-daily.xml
09-19 00:11:03.958 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.power.stats@1.0::IPowerStats/default in either framework or device manifest.
09-19 00:11:03.960 2193-2232/system_process I/BatteryStatsService: Using power HAL
09-19 00:11:03.960 2193-2232/system_process E/BatteryStatsService: Unable to load Power.Stats.HAL. Setting rail availability to false
09-19 00:11:03.960 2193-2232/system_process E/BluetoothAdapter: Bluetooth binder is null
09-19 00:11:03.961 2193-2232/system_process E/BatteryExternalStatsWorker: no controller energy info supplied for telephony
09-19 00:11:03.966 2193-2232/system_process I/KernelCpuUidFreqTimeReader: mPerClusterTimesAvailable=true
09-19 00:11:03.976 925-1074/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 45000 mC, weight[0] 2
09-19 00:11:03.977 925-1074/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:11:03.984 2193-2232/system_process I/PowerManagerService-JNI: Loaded power HAL 1.0 service
    Loaded power HAL 1.1 service
09-19 00:11:03.990 925-1080/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 45000 mC, weight[0] 2
09-19 00:11:03.991 925-1080/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:11:04.005 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:04.012 2193-2193/system_process I/IntentFirewall: Read new rules (A:0 B:0 S:0)
09-19 00:11:04.017 2193-2193/system_process E/libprocessgroup: Failed to open /dev/memcg/apps: Permission denied
09-19 00:11:04.018 2193-2193/system_process D/AppOps: AppOpsService published
09-19 00:11:04.018 2193-2193/system_process D/SystemServerTiming: StartActivityManager took to complete: 110ms
09-19 00:11:04.018 2193-2193/system_process I/SystemServer: StartPowerManager
09-19 00:11:04.018 2193-2193/system_process I/SystemServiceManager: Starting com.android.server.power.PowerManagerService
09-19 00:11:04.026 791-791/? E/QTI PowerHAL: Failed to acquire lock for hint_id: 1041.
09-19 00:11:04.026 2193-2193/system_process D/SystemServerTiming: StartPowerManager took to complete: 7ms
09-19 00:11:04.026 2193-2193/system_process I/SystemServer: StartThermalManager
09-19 00:11:04.026 2193-2193/system_process I/SystemServiceManager: Starting com.android.server.power.ThermalManagerService
09-19 00:11:04.027 2193-2193/system_process D/SystemServerTiming: StartThermalManager took to complete: 0ms
09-19 00:11:04.027 2193-2193/system_process I/SystemServer: InitPowerManagement
09-19 00:11:04.027 2193-2193/system_process D/SystemServerTiming: InitPowerManagement took to complete: 0ms
09-19 00:11:04.027 2193-2193/system_process I/SystemServer: StartRecoverySystemService
09-19 00:11:04.027 2193-2193/system_process I/SystemServiceManager: Starting com.android.server.RecoverySystemService
09-19 00:11:04.027 2193-2193/system_process D/SystemServerTiming: StartRecoverySystemService took to complete: 1ms
09-19 00:11:04.028 2193-2193/system_process V/RescueParty: Disabled because of active USB connection
09-19 00:11:04.028 2193-2193/system_process I/SystemServer: StartLightsService
09-19 00:11:04.028 2193-2193/system_process I/SystemServiceManager: Starting com.android.server.lights.LightsService
09-19 00:11:04.030 2193-2193/system_process D/SystemServerTiming: StartLightsService took to complete: 2ms
09-19 00:11:04.030 2193-2193/system_process I/SystemServer: StartSidekickService
09-19 00:11:04.030 2193-2193/system_process D/SystemServerTiming: StartSidekickService took to complete: 0ms
09-19 00:11:04.030 2193-2193/system_process I/SystemServer: StartDisplayManager
09-19 00:11:04.030 2193-2193/system_process I/SystemServiceManager: Starting com.android.server.display.DisplayManagerService
09-19 00:11:04.033 2193-2193/system_process D/SystemServerTiming: StartDisplayManager took to complete: 3ms
09-19 00:11:04.033 2193-2193/system_process I/SystemServer: WaitForDisplay
09-19 00:11:04.033 2193-2193/system_process I/SystemServiceManager: Starting phase 100
09-19 00:11:04.036 784-784/? I/SDM: HWCDisplay::GetColorModeCount: Supported color mode count = 0
09-19 00:11:04.038 2193-2222/system_process I/DisplayManagerService: Display device added: DisplayDeviceInfo{"Built-in Screen": uniqueId="local:0", 1080 x 2160, modeId 1, defaultModeId 1, supportedModes [{id=1, width=1080, height=2160, fps=60.000004}], colorMode 0, supportedColorModes [0], HdrCapabilities android.view.Display$HdrCapabilities@40f16308, density 400, 403.411 x 403.411 dpi, appVsyncOff 2000000, presDeadline 11666666, touch INTERNAL, rotation 0, type BUILT_IN, address {port=0}, state UNKNOWN, FLAG_DEFAULT_DISPLAY, FLAG_ROTATES_WITH_CONTENT, FLAG_SECURE, FLAG_SUPPORTS_PROTECTED_BUFFERS}
09-19 00:11:04.039 832-832/? D/SurfaceFlinger: Setting power mode 2 on display 0
09-19 00:11:04.041 2193-2222/system_process I/DisplayManagerService: Display device changed state: "Built-in Screen", ON
09-19 00:11:04.042 2193-2193/system_process D/SystemServerTiming: WaitForDisplay took to complete: 9ms
09-19 00:11:04.042 2193-2193/system_process I/SystemServer: StartPackageManagerService
09-19 00:11:04.042 2193-2193/system_process I/Watchdog: Pausing HandlerChecker: main thread for reason: packagemanagermain. Pause count: 1
09-19 00:11:04.047 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.system
09-19 00:11:04.048 2193-2193/system_process I/EdXposed-Bridge: PM has Hooked!
09-19 00:11:04.049 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
    Permission UID method has Hooked! android.uid.phone
    Permission UID method has Hooked! android.uid.log
    Permission UID method has Hooked! android.uid.nfc
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! android.uid.shell
    Permission UID method has Hooked! android.uid.se
09-19 00:11:04.050 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.networkstack
09-19 00:11:04.053 2193-2193/system_process D/SELinuxMMAC: Using policy file /system/etc/selinux/plat_mac_permissions.xml
09-19 00:11:04.054 2193-2193/system_process D/SELinuxMMAC: Using policy file /vendor/etc/selinux/vendor_mac_permissions.xml
09-19 00:11:04.056 2193-2193/system_process D/FallbackCategoryProvider: Found 1 fallback categories
09-19 00:11:04.105 971-1125/? I/ServiceManager: Waiting for service 'package_native' on '/dev/binder'...
09-19 00:11:04.142 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.media
09-19 00:11:04.143 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.networkstack
    Permission UID method has Hooked! android.uid.systemui
09-19 00:11:04.145 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.nfc
09-19 00:11:04.146 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.se
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! ai.lazero.lazero
09-19 00:11:04.146 2193-2193/system_process E/PackageManager: Adding duplicate shared user, keeping first: ai.lazero.lazero
09-19 00:11:04.147 2193-2193/system_process E/PackageManager: Occurred while parsing settings at START_TAG <shared-user name='ai.lazero.lazero' userId='10171'>@7454:57 in java.io.InputStreamReader@b8016cb
09-19 00:11:04.148 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.shared
    Permission UID method has Hooked! android.uid.system
    PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-19 00:11:04.149 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.phone
09-19 00:11:04.150 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.shell
09-19 00:11:04.151 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.calendar
09-19 00:11:04.152 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! com.termux
    Permission UID method has Hooked! com.android.emergency.uid
09-19 00:11:04.156 2193-2193/system_process E/PackageManager: Bad package setting: package ai.lazero.lazero has shared uid 10171 that is not defined
09-19 00:11:04.157 2193-2193/system_process W/PackageManager: No package known for stopped package ai.lazero.lazero
09-19 00:11:04.180 2193-2193/system_process D/PackageManager: Keeping known cache e923b92d3c96d64a19be89d4f4846aad93752eb7
09-19 00:11:04.206 971-1125/? W/ServiceManager: Service package_native didn't start. Returning NULL
09-19 00:11:04.206 971-1125/? E/storaged: getService package_native failed
09-19 00:11:04.279 2193-2193/system_process I/System.out: Update settings xposed
09-19 00:11:04.280 2193-2193/system_process W/System.err: java.io.FileNotFoundException: /data/local/tmp/xposed: open failed: EACCES (Permission denied)
        at libcore.io.IoBridge.open(IoBridge.java:496)
        at java.io.RandomAccessFile.<init>(RandomAccessFile.java:289)
        at com.chelpus.ˆ.ˆ(Utils.java:7086)
        at com.chelpus.ˆ.ᐧ(Utils.java:10063)
        at com.xposed.XSupport.ʻ(XSupport.java:1249)
        at com.xposed.XSupport$9.beforeHookedMethod(XSupport.java:466)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_2nkqvsp0pjs3mavtk6arhdmkc0.hook(Unknown Source:55)
        at com.android.server.pm.PackageManagerService.applyPolicy(PackageManagerService.java:11795)
        at com.android.server.pm.PackageManagerService.scanPackageNewLI(PackageManagerService.java:11071)
        at com.android.server.pm.PackageManagerService.addForInitLI(PackageManagerService.java:9609)
        at com.android.server.pm.PackageManagerService.scanPackageChildLI(PackageManagerService.java:9331)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9154)
        at com.android.server.pm.PackageManagerService.scanDirTracedLI(PackageManagerService.java:9108)
        at com.android.server.pm.PackageManagerService.<init>(PackageManagerService.java:2671)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_2ptsr6rbsnc7sqphenvn7nghm3.hook(Unknown Source:70)
        at com.android.server.pm.PackageManagerService.main(PackageManagerService.java:2318)
        at com.android.server.SystemServer.startBootstrapServices(SystemServer.java:753)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
09-19 00:11:04.277 2193-2193/system_process W/system_server: type=1400 audit(0.0:152): avc: denied { open } for path="/data/local/tmp/xposed" dev="sda17" ino=7077893 scontext=u:r:system_server:s0 tcontext=u:object_r:shell_data_file:s0 tclass=file permissive=0
09-19 00:11:04.280 2193-2193/system_process W/System.err:     at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-19 00:11:04.281 2193-2193/system_process W/System.err: Caused by: android.system.ErrnoException: open failed: EACCES (Permission denied)
        at libcore.io.Linux.open(Native Method)
        at libcore.io.ForwardingOs.open(ForwardingOs.java:167)
        at libcore.io.BlockGuardOs.open(BlockGuardOs.java:252)
        at libcore.io.IoBridge.open(IoBridge.java:482)
    	... 30 more
    org.json.JSONException: Value ���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� of type java.lang.String cannot be converted to JSONObject
        at org.json.JSON.typeMismatch(JSON.java:112)
        at org.json.JSONObject.<init>(JSONObject.java:168)
        at org.json.JSONObject.<init>(JSONObject.java:181)
        at com.chelpus.ˆ.ᐧ(Utils.java:10063)
        at com.xposed.XSupport.ʻ(XSupport.java:1249)
        at com.xposed.XSupport$9.beforeHookedMethod(XSupport.java:466)
        at de.robv.android.xposed.XC_MethodHook.callBeforeHookedMethod(XC_MethodHook.java:51)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:357)
        at SandHookerNew_2nkqvsp0pjs3mavtk6arhdmkc0.hook(Unknown Source:55)
        at com.android.server.pm.PackageManagerService.applyPolicy(PackageManagerService.java:11795)
        at com.android.server.pm.PackageManagerService.scanPackageNewLI(PackageManagerService.java:11071)
        at com.android.server.pm.PackageManagerService.addForInitLI(PackageManagerService.java:9609)
        at com.android.server.pm.PackageManagerService.scanPackageChildLI(PackageManagerService.java:9331)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9154)
        at com.android.server.pm.PackageManagerService.scanDirTracedLI(PackageManagerService.java:9108)
        at com.android.server.pm.PackageManagerService.<init>(PackageManagerService.java:2671)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_2ptsr6rbsnc7sqphenvn7nghm3.hook(Unknown Source:70)
        at com.android.server.pm.PackageManagerService.main(PackageManagerService.java:2318)
        at com.android.server.SystemServer.startBootstrapServices(SystemServer.java:753)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
09-19 00:11:04.282 2193-2193/system_process W/System.err:     at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-19 00:11:04.314 2193-2193/system_process D/PackageManager: No files in app dir /product_services/overlay
    No files in app dir /odm/overlay
    No files in app dir /oem/overlay
09-19 00:11:04.317 2193-2193/system_process W/PackageManager: Failed to parse /system/framework/arm64: Missing base APK in /system/framework/arm64
    Failed to parse /system/framework/arm: Missing base APK in /system/framework/arm
09-19 00:11:04.318 2193-2193/system_process W/PackageManager: Failed to parse /system/framework/oat: Missing base APK in /system/framework/oat
09-19 00:11:04.351 2193-2193/system_process W/PackageManager: Package ai.lazero.lazero shared user changed from <nothing> to ai.lazero.lazero; replacing with new
09-19 00:11:04.353 2193-2193/system_process I/System.out: SetPmContext
09-19 00:11:04.353 2193-2193/system_process I/Watchdog: Resuming HandlerChecker: main thread for reason: packagemanagermain. Pause count: 0
09-19 00:11:04.353 2193-2193/system_process E/System: ******************************************
09-19 00:11:04.354 2193-2193/system_process E/System: ************ Failure starting system services
    java.lang.NullPointerException: Attempt to read from field 'long com.android.server.pm.PackageSettingBase.versionCode' on a null object reference
        at com.android.server.pm.PackageManagerService.addForInitLI(PackageManagerService.java:9538)
        at com.android.server.pm.PackageManagerService.scanPackageChildLI(PackageManagerService.java:9331)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9154)
        at com.android.server.pm.PackageManagerService.scanDirTracedLI(PackageManagerService.java:9108)
        at com.android.server.pm.PackageManagerService.<init>(PackageManagerService.java:2725)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_2ptsr6rbsnc7sqphenvn7nghm3.hook(Unknown Source:70)
        at com.android.server.pm.PackageManagerService.main(PackageManagerService.java:2318)
        at com.android.server.SystemServer.startBootstrapServices(SystemServer.java:753)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
    	Suppressed: java.lang.IllegalStateException: Not all tasks finished before calling close: [java.util.concurrent.FutureTask@952ad88, java.util.concurrent.FutureTask@8438321, java.util.concurrent.FutureTask@3391346, java.util.concurrent.FutureTask@150b907, java.util.concurrent.FutureTask@a291a34, java.util.concurrent.FutureTask@1b4305d, java.util.concurrent.FutureTask@5631dd2, java.util.concurrent.FutureTask@b5dea3, java.util.concurrent.FutureTask@c57a5a0, java.util.concurrent.FutureTask@f887559, java.util.concurrent.FutureTask@cb1451e, java.util.concurrent.FutureTask@dbdc1ff, java.util.concurrent.FutureTask@5217bcc]
        at com.android.server.pm.ParallelPackageParser.close(ParallelPackageParser.java:145)
        at com.android.server.pm.PackageManagerService.$closeResource(PackageManagerService.java:3561)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9178)
        		... 17 more
09-19 00:11:04.354 2193-2193/system_process D/SystemServerTiming: StartPackageManagerService took to complete: 312ms
09-19 00:11:04.354 2193-2193/system_process E/Zygote: System zygote died with exception
    java.lang.NullPointerException: Attempt to read from field 'long com.android.server.pm.PackageSettingBase.versionCode' on a null object reference
        at com.android.server.pm.PackageManagerService.addForInitLI(PackageManagerService.java:9538)
        at com.android.server.pm.PackageManagerService.scanPackageChildLI(PackageManagerService.java:9331)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9154)
        at com.android.server.pm.PackageManagerService.scanDirTracedLI(PackageManagerService.java:9108)
        at com.android.server.pm.PackageManagerService.<init>(PackageManagerService.java:2725)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_2ptsr6rbsnc7sqphenvn7nghm3.hook(Unknown Source:70)
        at com.android.server.pm.PackageManagerService.main(PackageManagerService.java:2318)
        at com.android.server.SystemServer.startBootstrapServices(SystemServer.java:753)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
    	Suppressed: java.lang.IllegalStateException: Not all tasks finished before calling close: [java.util.concurrent.FutureTask@952ad88, java.util.concurrent.FutureTask@8438321, java.util.concurrent.FutureTask@3391346, java.util.concurrent.FutureTask@150b907, java.util.concurrent.FutureTask@a291a34, java.util.concurrent.FutureTask@1b4305d, java.util.concurrent.FutureTask@5631dd2, java.util.concurrent.FutureTask@b5dea3, java.util.concurrent.FutureTask@c57a5a0, java.util.concurrent.FutureTask@f887559, java.util.concurrent.FutureTask@cb1451e, java.util.concurrent.FutureTask@dbdc1ff, java.util.concurrent.FutureTask@5217bcc]
        at com.android.server.pm.ParallelPackageParser.close(ParallelPackageParser.java:145)
        at com.android.server.pm.PackageManagerService.$closeResource(PackageManagerService.java:3561)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9178)
        		... 17 more
09-19 00:11:04.354 2193-2193/system_process D/AndroidRuntime: Shutting down VM
09-19 00:11:04.354 2193-2193/system_process E/AndroidRuntime: *** FATAL EXCEPTION IN SYSTEM PROCESS: main
    java.lang.NullPointerException: Attempt to read from field 'long com.android.server.pm.PackageSettingBase.versionCode' on a null object reference
        at com.android.server.pm.PackageManagerService.addForInitLI(PackageManagerService.java:9538)
        at com.android.server.pm.PackageManagerService.scanPackageChildLI(PackageManagerService.java:9331)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9154)
        at com.android.server.pm.PackageManagerService.scanDirTracedLI(PackageManagerService.java:9108)
        at com.android.server.pm.PackageManagerService.<init>(PackageManagerService.java:2725)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_2ptsr6rbsnc7sqphenvn7nghm3.hook(Unknown Source:70)
        at com.android.server.pm.PackageManagerService.main(PackageManagerService.java:2318)
        at com.android.server.SystemServer.startBootstrapServices(SystemServer.java:753)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_76sqduusglom4enahqif5d7ntb.hook(Unknown Source:46)
        at com.android.server.SystemServer.run(SystemServer.java:527)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
    	Suppressed: java.lang.IllegalStateException: Not all tasks finished before calling close: [java.util.concurrent.FutureTask@952ad88, java.util.concurrent.FutureTask@8438321, java.util.concurrent.FutureTask@3391346, java.util.concurrent.FutureTask@150b907, java.util.concurrent.FutureTask@a291a34, java.util.concurrent.FutureTask@1b4305d, java.util.concurrent.FutureTask@5631dd2, java.util.concurrent.FutureTask@b5dea3, java.util.concurrent.FutureTask@c57a5a0, java.util.concurrent.FutureTask@f887559, java.util.concurrent.FutureTask@cb1451e, java.util.concurrent.FutureTask@dbdc1ff, java.util.concurrent.FutureTask@5217bcc]
        at com.android.server.pm.ParallelPackageParser.close(ParallelPackageParser.java:145)
        at com.android.server.pm.PackageManagerService.$closeResource(PackageManagerService.java:3561)
        at com.android.server.pm.PackageManagerService.scanDirLI(PackageManagerService.java:9178)
        		... 17 more
09-19 00:11:04.355 2193-2193/system_process E/AndroidRuntime: Error reporting crash
    java.lang.NullPointerException: Attempt to invoke interface method 'void android.app.IActivityManager.handleApplicationCrash(android.os.IBinder, android.app.ApplicationErrorReport$ParcelableCrashInfo)' on a null object reference
        at com.android.internal.os.RuntimeInit$KillApplicationHandler.uncaughtException(RuntimeInit.java:147)
        at java.lang.ThreadGroup.uncaughtException(ThreadGroup.java:1073)
        at java.lang.ThreadGroup.uncaughtException(ThreadGroup.java:1068)
        at java.lang.Thread.dispatchUncaughtException(Thread.java:2187)
09-19 00:11:04.355 2193-2193/system_process I/Process: Sending signal. PID: 2193 SIG: 9
09-19 00:11:04.384 584-584/? I/ServiceManager: service 'device_identifiers' died
    service 'uri_grants' died
    service 'activity_task' died
    service 'batterystats' died
    service 'appops' died
    service 'power' died
    service 'thermalservice' died
    service 'recovery' died
    service 'display' died
09-19 00:11:04.387 1982-1982/? I/Zygote: Process 2193 exited due to signal 9 (Killed)
09-19 00:11:04.387 1982-1982/? E/Zygote: Exit zygote because system server (pid 2193) has terminated
09-19 00:11:04.423 584-584/? I/ServiceManager: service 'media.audio_flinger' died
09-19 00:11:04.424 1989-2148/? I/r_submix: adev_close()
09-19 00:11:04.424 1989-2145/? D/audio_hw_primary: adev_close_output_stream: enter:stream_handle(low-latency-playback)
    out_standby: enter: stream (0xf03a0000) usecase(1: low-latency-playback)
    out_standby: exit
    adev_close_output_stream: enter:stream_handle(deep-buffer-playback)
    out_standby: enter: stream (0xf03d9000) usecase(0: deep-buffer-playback)
    out_standby: exit
    adev_close_output_stream: enter:stream_handle(afe-proxy-playback)
    out_standby: enter: stream (0xf03a2800) usecase(51: afe-proxy-playback)
    out_standby: exit
09-19 00:11:04.424 1989-2145/? I/soundtrigger: audio_extn_sound_trigger_deinit: Enter
09-19 00:11:04.433 1989-2145/? D/ACDB-LOADER: ACDB -> deallocate_ADIE
09-19 00:11:04.433 1989-2145/? D/ACDB-LOADER: ACDB -> deallocate_ACDB
    [ACPH]->acph_deinit->is called
    g_pCmdTbl is not NULL, g_pCmdTbl->pNodeHead is not NULL
    Node1 is not empty, address[0xf07eb6d0]
    Node2 is not empty, address[0xf07eb820]
    g_pCmdTbl->pNodeTail is not NULL, address[0xf07eb820]
    Free first node, pNodeHead[0xf07eb820],pCur[0xf07eb6d0],pNext[0xf07eb820]
    [ACPH]->Online service Unregistered with ACPH
09-19 00:11:04.442 1989-2145/? D/ACDB-LOADER: ACDB -> deallocate_ACDB done!
09-19 00:11:04.442 1989-2145/? D/ultrasound: us_deinit: enter
    us_deinit: exit
09-19 00:11:04.443 584-584/? I/ServiceManager: service 'media.player' died
    service 'media.resource_manager' died
09-19 00:11:04.451 584-584/? I/ServiceManager: service 'dnsresolver' died
    service 'netd' died
09-19 00:11:04.451 882-1736/? E/QC-NETMGR-LIB: serviceDied(): Netd service died
09-19 00:11:04.457 584-584/? I/ServiceManager: service 'wificond' died
09-19 00:11:04.786 917-917/? E/QTI_SDM_INFO: [qti_rmnet_peripheral.c:739] qti_file_open():Could not open device file. Errno 2 error msg=No such file or directory
09-19 00:11:04.803 2260-2260/? I/wificond: wificond is starting up...
09-19 00:11:04.817 2259-2259/? I/netdClient: Skipping libnetd_client init since *we* are netd
09-19 00:11:04.820 2259-2259/? I/netd: netd 1.0 starting
09-19 00:11:04.823 2259-2259/? I/Netd: Loaded resolver library from /apex/com.android.resolv/lib64/libnetd_resolv.so
09-19 00:11:04.823 2259-2259/? D/TetherController: Setting IP forward enable = 0
09-19 00:11:04.825 2259-2259/? D/FirewallController: Could not read /proc/self/uid_map, max uid defaulting to 4294967294
09-19 00:11:04.830 2261-2261/? D/vndksupport: Loading /vendor/lib/hw/android.hardware.audio@5.0-impl.so from current namespace instead of sphal namespace.
09-19 00:11:04.835 2261-2261/? I/ServiceManagement: Registered android.hardware.audio@5.0::IDevicesFactory/default (start delay of 64ms)
09-19 00:11:04.836 2261-2261/? I/ServiceManagement: Removing namespace from process name android.hardware.audio@2.0-service to audio@2.0-service.
09-19 00:11:04.836 2261-2261/? I/audiohalservice: Registration complete for android.hardware.audio@5.0::IDevicesFactory/default.
09-19 00:11:04.836 2261-2261/? D/vndksupport: Loading /vendor/lib/hw/android.hardware.audio.effect@5.0-impl.so from current namespace instead of sphal namespace.
09-19 00:11:04.845 2261-2261/? I/ServiceManagement: Registered android.hardware.audio.effect@5.0::IEffectsFactory/default (start delay of 74ms)
09-19 00:11:04.846 2261-2261/? I/audiohalservice: Registration complete for android.hardware.audio.effect@5.0::IEffectsFactory/default.
09-19 00:11:04.846 2261-2261/? D/vndksupport: Loading /vendor/lib/hw/android.hardware.soundtrigger@2.2-impl.so from current namespace instead of sphal namespace.
09-19 00:11:04.848 2261-2261/? D/vndksupport: Loading /vendor/lib/hw/sound_trigger.primary.msm8998.so from current namespace instead of sphal namespace.
09-19 00:11:04.852 2261-2261/? D/sound_trigger_hw: stdev_open: Enter
09-19 00:11:04.854 2259-2259/? I/netd: Creating child chains: 19.4ms
09-19 00:11:04.855 2259-2259/? I/netd: Setting up OEM hooks: 0.2ms
09-19 00:11:04.857 2261-2261/? D/sound_trigger_hw: load_audio_hal: ahal is using proprietary API version 0x0101
09-19 00:11:04.857 2261-2261/? I/sound_trigger_platform: platform_stdev_init: Enter
09-19 00:11:04.859 2261-2261/? W/sound_trigger_platform: load_smlib: generate_sound_trigger_phrase_recognition_event_v3 not found. undefined symbol: generate_sound_trigger_phrase_recognition_event_v3
09-19 00:11:04.862 2261-2261/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: snd_card_name: msm8998-tasha-snd-card
09-19 00:11:04.862 2261-2261/? W/hardware_info: update_hardware_info_msm8998: Not a msm8998 device
09-19 00:11:04.862 2261-2261/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: Opened sound card:0
09-19 00:11:04.866 2259-2259/? I/netd: Setting up FirewallController hooks: 11.5ms
09-19 00:11:04.869 2258-2258/? I/mediaserver: ServiceManager: 0xe81232a0
09-19 00:11:04.869 2258-2258/? W/BatteryNotifier: batterystats service unavailable!
    batterystats service unavailable!
09-19 00:11:04.870 2259-2259/? I/netd: Setting up TetherController hooks: 3.7ms
09-19 00:11:04.873 2259-2259/? I/netd: Setting up BandwidthController hooks: 3.1ms
    Setting up IdletimerController hooks: 0.1ms
09-19 00:11:04.876 2259-2259/? I/netd: Setting up StrictController hooks: 3.0ms
09-19 00:11:04.876 2259-2259/? I/ClatdController: Pre-4.9 kernel or pre-P api shipping level - disabling clat ebpf.
09-19 00:11:04.876 2259-2259/? I/netd: Initializing ClatdController: 0.0ms
    Initializing traffic control: 0.0ms
09-19 00:11:04.882 2259-2259/? I/netd: Enabling bandwidth control: 6.1ms
09-19 00:11:04.883 2259-2259/? E/Netd: Error adding route 0.0.0.0/0 -> (null) dummy0 to table 1003: File exists
09-19 00:11:04.884 2259-2259/? I/netd: Initializing RouteController: 1.4ms
09-19 00:11:04.884 2259-2259/? D/XfrmController: XfrmController::ipSecAddXfrmInterface, line=1379
    XfrmController::ipSecRemoveTunnelInterface, line=1592
    deviceName=ipsec_test
    Sending Netlink XFRM Message: XFRM_MSG_FLUSHSA
    Sending Netlink XFRM Message: XFRM_MSG_FLUSHPOLICY
09-19 00:11:04.884 2259-2259/? I/netd: Initializing XfrmController: 0.5ms
09-19 00:11:04.884 2259-2259/? E/Netd: Unable to create netlink socket for family 5: Protocol not supported
09-19 00:11:04.884 2259-2259/? W/Netd: Unable to open qlog quota socket, check if xt_quota2 can send via UeventHandler
09-19 00:11:04.885 2259-2259/? I/libnetd_resolv: resolv_init: Initializing resolver
09-19 00:11:04.886 2259-2259/? D/MDnsDS: MDnsSdListener::Hander starting up
09-19 00:11:04.887 2259-2276/? D/MDnsDS: MDnsSdListener starting to monitor
    Going to poll with pollCount 1
09-19 00:11:04.887 2259-2259/? I/netd: Registering NetdNativeService: 0.2ms
09-19 00:11:04.889 882-1736/? I/QC-NETMGR-LIB: onRegistration(): Starting Netd getService thread
09-19 00:11:04.889 2259-2259/? I/ServiceManagement: Registered android.system.net.netd@1.1::INetd/default (start delay of 127ms)
09-19 00:11:04.889 2259-2259/? I/netd: Registering NetdHwService: 2.1ms
    Netd started in 69ms
09-19 00:11:04.891 2254-2254/? I/Riru: Riru v21.3 (36) in zygote64
    config dir is /data/misc/riru
    system version 10 (api 29, preview_sdk 0)
09-19 00:11:04.891 2255-2255/? I/Riru: Riru v21.3 (36) in zygote
    config dir is /data/misc/riru
    system version 10 (api 29, preview_sdk 0)
09-19 00:11:04.892 882-2280/? I/QC-NETMGR-LIB: getServiceImpl(): INetd discovered
    registerLinkToDeath(): Success registerLinkToDeath!
09-19 00:11:04.892 882-1736/? D/QC-NETMGR-LIB: onRegistration(): netd restart detected
09-19 00:11:04.892 882-979/? I/QC-NETMGR-LIB: NetmgrNetdClientRegisterNetwork(): Looking for Netd service
    NetmgrNetdClientRegisterNetwork(): register to create new OEM network
    registerNetwork(): Attempting createOemNetwork
09-19 00:11:04.892 2259-2279/? D/TcpSocketMonitor: suspending tcpinfo polling
09-19 00:11:04.893 2254-2254/? I/Riru: hook installed
09-19 00:11:04.894 882-979/? I/QC-NETMGR-LIB: registerNetwork(): command completed!
    registerNetwork(): createOemNetwork succeeded [packet mark : 0xf0001] [net id : 1] [network handle : 0x1cafed00d]
    NetmgrNetdClientRegisterNetwork(): [packet mark : 0xf0001] [network handle : 0x1cafed00d]
09-19 00:11:04.894 2255-2255/? I/Riru: hook installed
09-19 00:11:04.895 2254-2254/? I/Riru: module loaded: edxp (api 4)
09-19 00:11:04.895 2254-2254/? V/Riru: edxp: onModuleLoaded
09-19 00:11:04.895 2254-2254/? I/EdXposed: onModuleLoaded: welcome to EdXposed!
    Start to install inline hooks
    Using api level 29
    Start to install Riru hook
09-19 00:11:04.896 2255-2255/? I/Riru: module loaded: edxp (api 4)
09-19 00:11:04.897 2255-2255/? V/Riru: edxp: onModuleLoaded
09-19 00:11:04.897 2255-2255/? I/EdXposed: onModuleLoaded: welcome to EdXposed!
    Start to install inline hooks
    Using api level 29
    Start to install Riru hook
09-19 00:11:04.906 2254-2254/? I/EdXposed: Riru hooks installed
09-19 00:11:04.912 2255-2255/? I/EdXposed: Riru hooks installed
09-19 00:11:04.913 2254-2254/? D/AndroidRuntime: >>>>>> START com.android.internal.os.ZygoteInit uid 0 <<<<<<
09-19 00:11:04.917 2254-2254/? I/EdXposed: ART hooks installed
09-19 00:11:04.917 2254-2254/? I/AndroidRuntime: Using default boot image
    Leaving lock profiling enabled
09-19 00:11:04.917 2254-2254/? I/EdXposed: system_property_get: dalvik.vm.dex2oat-filter -> quicken
    system_property_get: dalvik.vm.dex2oat-flags -> --inline-max-code-units=0
09-19 00:11:04.918 2255-2255/? D/AndroidRuntime: >>>>>> START com.android.internal.os.ZygoteInit uid 0 <<<<<<
09-19 00:11:04.918 2254-2254/? I/zygote64: option[0]=-Xzygote
09-19 00:11:04.919 2254-2254/? I/zygote64: option[1]=exit
    option[2]=vfprintf
    option[3]=sensitiveThread
    option[4]=-verbose:gc
    option[5]=-Xms8m
    option[6]=-Xmx512m
    option[7]=-XX:HeapGrowthLimit=192m
    option[8]=-XX:HeapMinFree=8m
    option[9]=-XX:HeapMaxFree=16m
    option[10]=-XX:HeapTargetUtilization=0.6
    option[11]=-Xusejit:true
    option[12]=-Xjitsaveprofilinginfo
    option[13]=-XjdwpOptions:suspend=n,server=y
    option[14]=-XjdwpProvider:default
    option[15]=-Xlockprofthreshold:500
    option[16]=-Ximage-compiler-option
    option[17]=--runtime-arg
    option[18]=-Ximage-compiler-option
    option[19]=-Xms64m
    option[20]=-Ximage-compiler-option
    option[21]=--runtime-arg
    option[22]=-Ximage-compiler-option
    option[23]=-Xmx64m
    option[24]=-Ximage-compiler-option
    option[25]=--profile-file=/system/etc/boot-image.prof
    option[26]=-Ximage-compiler-option
    option[27]=--compiler-filter=speed-profile
    option[28]=-Xcompiler-option
    option[29]=--runtime-arg
    option[30]=-Xcompiler-option
    option[31]=-Xms64m
    option[32]=-Xcompiler-option
    option[33]=--runtime-arg
    option[34]=-Xcompiler-option
    option[35]=-Xmx512m
    option[36]=-Xcompiler-option
    option[37]=--compiler-filter=quicken
    option[38]=-Ximage-compiler-option
    option[39]=--instruction-set-variant=cortex-a73
    option[40]=-Xcompiler-option
    option[41]=--instruction-set-variant=cortex-a73
    option[42]=-Ximage-compiler-option
    option[43]=--instruction-set-features=default
    option[44]=-Xcompiler-option
    option[45]=--instruction-set-features=default
    option[46]=-Xcompiler-option
    option[47]=--inline-max-code-units=0
    option[48]=-Duser.locale=en-US
    option[49]=--cpu-abilist=arm64-v8a
    option[50]=-Xcompiler-option
    option[51]=--generate-mini-debug-info
    option[52]=-Xcore-platform-api-policy:just-warn
    option[53]=-Xfingerprint:Xiaomi/chiron/chiron:8.0.0/OPR1.170623.027/V9.5.4.0.ODEMIFA:user/release-keys
09-19 00:11:04.921 2254-2254/? I/zygote64: Core platform API reporting enabled, enforcing=false
09-19 00:11:04.922 2255-2255/? I/EdXposed: ART hooks installed
09-19 00:11:04.922 2255-2255/? I/AndroidRuntime: Using default boot image
    Leaving lock profiling enabled
09-19 00:11:04.922 2255-2255/? I/EdXposed: system_property_get: dalvik.vm.dex2oat-filter -> quicken
    system_property_get: dalvik.vm.dex2oat-flags -> --inline-max-code-units=0
09-19 00:11:04.924 2255-2255/? I/zygote: option[0]=-Xzygote
    option[1]=exit
    option[2]=vfprintf
    option[3]=sensitiveThread
    option[4]=-verbose:gc
    option[5]=-Xms8m
    option[6]=-Xmx512m
    option[7]=-XX:HeapGrowthLimit=192m
    option[8]=-XX:HeapMinFree=8m
    option[9]=-XX:HeapMaxFree=16m
    option[10]=-XX:HeapTargetUtilization=0.6
    option[11]=-Xusejit:true
    option[12]=-Xjitsaveprofilinginfo
    option[13]=-XjdwpOptions:suspend=n,server=y
    option[14]=-XjdwpProvider:default
    option[15]=-Xlockprofthreshold:500
    option[16]=-Ximage-compiler-option
    option[17]=--runtime-arg
    option[18]=-Ximage-compiler-option
    option[19]=-Xms64m
    option[20]=-Ximage-compiler-option
    option[21]=--runtime-arg
    option[22]=-Ximage-compiler-option
    option[23]=-Xmx64m
    option[24]=-Ximage-compiler-option
    option[25]=--profile-file=/system/etc/boot-image.prof
    option[26]=-Ximage-compiler-option
    option[27]=--compiler-filter=speed-profile
    option[28]=-Xcompiler-option
    option[29]=--runtime-arg
    option[30]=-Xcompiler-option
    option[31]=-Xms64m
    option[32]=-Xcompiler-option
    option[33]=--runtime-arg
    option[34]=-Xcompiler-option
    option[35]=-Xmx512m
09-19 00:11:04.925 2255-2255/? I/zygote: option[36]=-Xcompiler-option
    option[37]=--compiler-filter=quicken
    option[38]=-Ximage-compiler-option
    option[39]=--instruction-set-variant=cortex-a73
    option[40]=-Xcompiler-option
    option[41]=--instruction-set-variant=cortex-a73
    option[42]=-Ximage-compiler-option
    option[43]=--instruction-set-features=default
    option[44]=-Xcompiler-option
    option[45]=--instruction-set-features=default
    option[46]=-Xcompiler-option
    option[47]=--inline-max-code-units=0
    option[48]=-Duser.locale=en-US
    option[49]=--cpu-abilist=armeabi-v7a,armeabi
    option[50]=-Xcompiler-option
    option[51]=--generate-mini-debug-info
    option[52]=-Xcore-platform-api-policy:just-warn
    option[53]=-Xfingerprint:Xiaomi/chiron/chiron:8.0.0/OPR1.170623.027/V9.5.4.0.ODEMIFA:user/release-keys
09-19 00:11:04.927 2255-2255/? I/zygote: Core platform API reporting enabled, enforcing=false
09-19 00:11:04.935 2256-2256/? I/FastMixerState: sMaxFastTracks = 8
09-19 00:11:04.938 2256-2256/? V/MediaUtils: physMem: 6004461568
    requested limit: 536870912
09-19 00:11:04.938 2256-2256/? I/libc: malloc_limit: Allocation limit enabled, max size 536870912 bytes
09-19 00:11:04.939 2256-2256/? I/audioserver: ServiceManager: 0x7254906dc0
09-19 00:11:04.939 2256-2256/? W/BatteryNotifier: batterystats service unavailable!
09-19 00:11:04.942 585-585/? I/hwservicemanager: getTransport: Cannot find entry android.hardware.audio@5.0::IDevicesFactory/msd in either framework or device manifest.
09-19 00:11:04.944 2256-2256/? I/AudioFlinger: Using default 3000 mSec as standby time.
09-19 00:11:04.947 2256-2256/? E/APM::Serializer: deserialize: Could not parse /odm/etc/audio_policy_configuration.xml document.
    deserialize: Could not parse /vendor/etc/audio/audio_policy_configuration.xml document.
09-19 00:11:04.953 2256-2256/? E/APM::AudioPolicyEngine/Config: parse: Could not parse document /vendor/etc/audio_policy_engine_configuration.xml
09-19 00:11:04.954 2256-2256/? W/APM::AudioPolicyEngine/Base: loadAudioPolicyEngineConfig: No configuration found, using default matching phone experience.
09-19 00:11:04.954 2256-2256/? E/APM::AudioPolicyEngine/Config: parseLegacyVolumeFile: Could not parse document /odm/etc/audio_policy_configuration.xml
09-19 00:11:04.959 2261-2268/? D/vndksupport: Loading /vendor/lib/hw/audio.primary.msm8998.so from current namespace instead of sphal namespace.
09-19 00:11:04.959 2261-2268/? D/audio_hw_primary: adev_open: enter
09-19 00:11:04.960 2261-2268/? W/audio_hw_utils: vndk_fwk_init: failed to dlopen VNDK_FWK_LIB No such file or directory
    audio_extn_utils_get_vendor_enhanced_info: default to vendor_enhanced_info 0x0
09-19 00:11:04.960 2261-2268/? D/audio_hw_extn: snd_mon_feature_init: Called with feature NOT Enabled
09-19 00:11:04.960 2261-2268/? W/audio_hw_extn: :: snd_mon_feature_init: ---- Feature SND_MONITOR is disabled ----
    :: compr_cap_feature_init: ---- Feature COMPRESS_CAPTURE is disabled ----
09-19 00:11:04.960 2261-2268/? D/audio_hw_extn: dsm_feedback_feature_init: Called with feature NOT Enabled
09-19 00:11:04.960 2261-2268/? W/audio_hw_extn: :: dsm_feedback_feature_init: ---- Feature DSM_FEEDBACK is disabled ----
    :: ssrec_feature_init: ---- Feature SSREC is disabled ----
09-19 00:11:04.960 2261-2268/? D/audio_hw_extn: src_trkn_feature_init:: ---- Feature SOURCE_TRACKING is Enabled ----
    hdmi_edid_feature_init: HDMI_EDID feature NOT Enabled
09-19 00:11:04.960 2261-2268/? W/audio_hw_extn: :: hdmi_edid_feature_init: ---- Feature HDMI_EDID is disabled ----
09-19 00:11:04.960 2261-2268/? D/audio_hw_extn: :: keep_alive_feature_init: ---- Feature KEEP_ALIVE is  NOT ENABLED ----
    :: hifi_audio_feature_init: ---- Feature HIFI_AUDIO is  NOT ENABLED ----
    :: ras_feature_init: ---- Feature RAS_FEATURE is ENABLED ----
    :: kpi_optimize_feature_init: ---- Feature KPI_OPTIMIZE is ENABLED ----
    usb_offload_feature_init: Called with feature Enabled
    usb_offload_burst_mode_feature_init: Called with feature NOT Enabled
    usb_offload_sidetone_volume_feature_init: Called with feature NOT Enabled
    a2dp_offload_feature_init: Called with feature NOT Enabled
09-19 00:11:04.960 2261-2268/? W/audio_hw_extn: :: a2dp_offload_feature_init: ---- Feature A2DP_OFFLOAD is disabled ----
09-19 00:11:04.960 2261-2268/? D/audio_hw_extn: :: vbat_feature_init: ---- Feature VBAT is ENABLED ----
    :: display_port_feature_init: ---- Feature DISPLAY_PORT is ENABLED ----
    :: fluence_feature_init: ---- Feature FLUENCE is ENABLED ----
    :: custom_stereo_feature_init: ---- Feature CUSTOM_STEREO is ENABLED ----
    :: anc_headset_feature_init: ---- Feature ANC_HEADSET is ENABLED----
    spkr_prot_feature_init: Called with feature NOT Enabled, vendor_enhanced_info 0x0
09-19 00:11:04.960 2261-2268/? W/audio_hw_extn: :: spkr_prot_feature_init: ---- Feature SPKR_PROT is disabled ----
09-19 00:11:04.960 2261-2268/? D/audio_hw_extn: fm_feature_init: ---- Feature FM_POWER_OPT is ENABLED----
    external_qdsp_feature_init: Called with feature NOT Enabled
09-19 00:11:04.960 2261-2268/? W/audio_hw_extn: :: external_qdsp_feature_init: ---- Feature EXTERNAL_QDSP is disabled ----
09-19 00:11:04.960 2261-2268/? D/audio_hw_extn: external_speaker_feature_init: Called with feature NOT Enabled
09-19 00:11:04.960 2261-2268/? W/audio_hw_extn: :: external_speaker_feature_init: ---- Feature EXTERNAL_SPKR is disabled ----
09-19 00:11:04.960 2261-2268/? D/audio_hw_extn: external_speaker_tfa_feature_init: Called with feature NOT Enabled
09-19 00:11:04.960 2261-2268/? W/audio_hw_extn: :: external_speaker_tfa_feature_init: ---- Feature EXTERNAL_SPKR_TFA is disabled ----
09-19 00:11:04.960 2261-2268/? D/audio_hw_extn: hwdep_cal_feature_init: Called with feature NOT Enabled
09-19 00:11:04.960 2261-2268/? W/audio_hw_extn: :: hwdep_cal_feature_init: ---- Feature HWDEP_CAL is disabled ----
09-19 00:11:04.960 2261-2268/? D/audio_hw_extn: hfp_feature_init: Called with feature Enabled
09-19 00:11:04.963 2261-2268/? D/audio_hw_extn: hfp_feature_init:: ---- Feature HFP is Enabled ----
    ext_hw_plugin_feature_init: Called with feature NOT Enabled
09-19 00:11:04.963 2261-2268/? W/audio_hw_extn: :: ext_hw_plugin_feature_init: ---- Feature EXT_HW_PLUGIN is disabled ----
09-19 00:11:04.963 2261-2268/? D/audio_hw_extn: record_play_concurency_feature_init: ---- Feature RECORD_PLAY_CONCURRENCY is NOT ENABLED----
    hdmi_passthrough_feature_init: Called with feature NOT Enabled
09-19 00:11:04.963 2261-2268/? W/audio_hw_extn: :: hdmi_passthrough_feature_init: ---- Feature HDMI_PASSTHROUGH is disabled ----
09-19 00:11:04.963 2261-2268/? D/audio_hw_extn: concurrent_capture_feature_init: ---- Feature CONCURRENT_CAPTURE is NOT ENABLED----
    compress_in_feature_init: ---- Feature COMPRESS_IN is NOT ENABLED----
09-19 00:11:04.963 2261-2268/? W/audio_hw_extn: :: battery_listener_feature_init: ---- Feature BATTERY_LISTENER is disabled ----
09-19 00:11:04.963 2261-2268/? D/audio_hw_extn: maxx_audio_feature_init: Called with feature NOT Enabled
09-19 00:11:04.963 2261-2268/? W/audio_hw_extn: :: maxx_audio_feature_init: ---- Feature MAXX_AUDIO is disabled ----
09-19 00:11:04.963 2261-2268/? D/audio_hw_extn: audiozoom_feature_init: Called with feature NOT Enabled
09-19 00:11:04.963 2261-2268/? W/audio_hw_extn: :: audiozoom_feature_init: ---- Feature AUDIOZOOM is disabled ----
09-19 00:11:04.963 2261-2268/? D/voice_extn: :: dynamic_ecns_feature_init: ---- Feature DYNAMIC_ECNS is NOT ENABLED ----
09-19 00:11:04.965 2257-2257/? I/cameraserver: ServiceManager: 0xedd231a0
09-19 00:11:04.966 2257-2257/? I/CameraService: CameraService started (pid=2257)
    CameraService process starting
09-19 00:11:04.966 2257-2257/? W/BatteryNotifier: batterystats service unavailable!
    batterystats service unavailable!
09-19 00:11:04.966 2261-2268/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: snd_card_name: msm8998-tasha-snd-card
09-19 00:11:04.966 2261-2268/? W/hardware_info: update_hardware_info_msm8998: Not a msm8998 device
09-19 00:11:04.966 2261-2268/? D/audio_hw_utils: audio_extn_utils_open_snd_mixer: Opened sound card:0
09-19 00:11:04.966 2261-2268/? D/msm8974_platform: platform_init: Opened sound card:0
09-19 00:11:04.966 2261-2268/? I/audio_hw_extn: audio_extn_set_snd_card_split: snd_card_name(msm8998-tasha-snd-card) device(msm8998) snd_card(tasha) form_factor(snd)
09-19 00:11:04.966 2261-2268/? W/hardware_info: update_hardware_info_msm8998: Not a msm8998 device
09-19 00:11:04.966 2261-2268/? D/msm8974_platform: platform_init: Loading mixer file: /vendor/etc/mixer_paths_tasha.xml
09-19 00:11:04.968 2257-2257/? I/CameraProviderManager: Connecting to new camera provider: legacy/0, isRemote? 1
09-19 00:11:04.970 2257-2257/? I/CameraProviderManager: Enumerating new camera device: device@1.0/legacy/0
09-19 00:11:04.971 774-1435/? I/CamDev@1.0-impl: Opening camera 0
09-19 00:11:04.971 774-1435/? I/QCamera: <HAL><INFO> openLegacy: 503: openLegacy halVersion: 256 cameraId = 0
09-19 00:11:04.972 774-1435/? D/vndksupport: Loading /vendor/lib/hw/power.default.so from current namespace instead of sphal namespace.
09-19 00:11:04.978 2254-2254/? I/EdXposed: using installer org.meowcat.edxposed.manager
    data path prefix: /data/user_de/0/
      application list mode: false
        using whitelist: false
09-19 00:11:04.978 774-1435/? E/Watermark: getFontData Font file does not exist!
09-19 00:11:04.979 2254-2254/? I/EdXposed:   dynamic modules mode: false
      resources hook: true
      deopt boot image: false
      no module log: false
09-19 00:11:04.979 774-1435/? E/Watermark: getFontData Get file status failed
    getFontData Font file does not exist!
    getFontData Get file status failed
09-19 00:11:04.979 774-1435/? I/QCamera: <HAL><INFO> openCamera: 1923: [KPI Perf]: E PROFILE_OPEN_CAMERA camera id 0
09-19 00:11:04.979 925-1074/? I/ThermalEngine: vs_get_temperature: read[0] xo_therm 45000 mC, weight[0] 2
09-19 00:11:04.980 2255-2255/? I/EdXposed: using installer org.meowcat.edxposed.manager
    data path prefix: /data/user_de/0/
      application list mode: false
        using whitelist: false
      dynamic modules mode: false
      resources hook: true
      deopt boot image: false
      no module log: false
09-19 00:11:04.980 925-1074/? I/ThermalEngine: vs_get_temperature: read[1] quiet_therm 36000 mC, weight[1] 1
09-19 00:11:04.982 774-1435/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:11:04.982 2257-2257/? W/CameraProviderManager: Camera provider legacy/0 says an unknown camera device@1.0/legacy/0 now has torch status 0. Curious.
    Camera provider legacy/0 says an unknown camera device@3.3/legacy/0 now has torch status 0. Curious.
09-19 00:11:04.982 774-1435/? D/QCamera: Debug log file is not enabled
09-19 00:11:05.010 774-2301/? E/mm-camera: <SENSOR><ERROR> chiron_imx386_semco_autofocus_calibration: 571: adjusted code_per_step: 165, qvalue: 128
09-19 00:11:05.015 774-1435/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:11:05.015 774-1435/? I/chatty: uid=1047(cameraserver) HwBinder:774_1 identical 3 lines
09-19 00:11:05.015 774-1435/? E/mm-camera: <STATS ><ERROR> 2989: stats_port_check_caps_reserve: Invalid Port capability type!
09-19 00:11:05.019 2254-2254/? D/ICU: Time zone APEX file found: /apex/com.android.tzdata/etc/icu/icu_tzdata.dat
09-19 00:11:05.022 774-2294/? E/QCamera: <HAL><ERROR> calcThermalLevel: 10178: level: 0, preview minfps 7000.000000, preview maxfpS 30000.000000, video minfps 7000.000000, video maxfps 30000.000000
    <HAL><ERROR> calcThermalLevel: 10183: level change to -> 0
    <HAL><ERROR> calcThermalLevel: 10262: Adjusted preview minfps 7.000000, preview maxfpS 30.000000, video minfps 7.000000, video maxfps 30.000000
09-19 00:11:05.022 2255-2255/? D/ICU: Time zone APEX file found: /apex/com.android.tzdata/etc/icu/icu_tzdata.dat
09-19 00:11:05.023 774-2294/? E/QCameraParameters: setOISValue9690 OISEnabled=1 
    res_idx = 0 chromatix_lib_name[1] = chiron_imx386_semco_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_imx386_semco_common
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[9] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[10] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[11] = chiron_imx386_semco_cpp_video
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_imx386_semco_zsl_preview
    res_idx = 0 chromatix_lib_name[1] = chiron_imx386_semco_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_imx386_semco_common
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[9] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[10] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[11] = chiron_imx386_semco_cpp_video
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_imx386_semco_zsl_preview
    res_idx = 0 chromatix_lib_name[1] = chiron_imx386_semco_snapshot
    res_idx = 0 chromatix_lib_name[2] = chiron_imx386_semco_common
    res_idx = 0 chromatix_lib_name[3] = chiron_imx386_semco_cpp_preview
    res_idx = 0 chromatix_lib_name[4] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[5] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[6] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[7] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[8] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[9] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[10] = chiron_imx386_semco_cpp_snapshot
    res_idx = 0 chromatix_lib_name[11] = chiron_imx386_semco_cpp_video
    res_idx = 0 chromatix_lib_name[12] = chiron_imx386_semco_postproc
    res_idx = 0 chromatix_lib_name[13] = chiron_imx386_semco_zsl_preview
09-19 00:11:05.026 774-1435/? I/Thermal-Lib: Thermal-Lib-Client: Registration successful for camera with handle:1
09-19 00:11:05.026 774-1435/? I/QCamera: <HAL><INFO> openCamera: 1938: [KPI Perf]: X PROFILE_OPEN_CAMERA camera id 0, rc: 0
09-19 00:11:05.027 774-1435/? I/CamDev@1.0-impl: could not cast ICameraDeviceCallback to IQCameraDeviceCallback
09-19 00:11:05.030 774-774/? I/CamDev@1.0-impl: Closing camera 0
09-19 00:11:05.030 774-774/? I/QCamera: <HAL><INFO> close_camera_device: 1571: [KPI Perf]: E camera id 0
09-19 00:11:05.033 2254-2254/? V/Riru: jniRegisterNativeMethods com/android/internal/os/RuntimeInit
    jniRegisterNativeMethods com/android/internal/os/ZygoteInit
    jniRegisterNativeMethods android/os/SystemClock
09-19 00:11:05.033 774-774/? E/QCamera: <HAL><ERROR> acquirePerfLock: 542: Failed to acquire the perf lock
09-19 00:11:05.033 2254-2254/? V/Riru: jniRegisterNativeMethods android/util/EventLog
    jniRegisterNativeMethods android/util/Log
    jniRegisterNativeMethods android/util/MemoryIntArray
    jniRegisterNativeMethods android/util/PathParser
    jniRegisterNativeMethods android/util/StatsLog
    jniRegisterNativeMethods android/util/StatsLogInternal
09-19 00:11:05.034 774-774/? I/QCamera: <HAL><INFO> closeCamera: 2351: E
    <HAL><INFO> closeCamera: 2356: [KPI Perf]: E PROFILE_CLOSE_CAMERA camera id 0
09-19 00:11:05.034 774-2296/? E/mm-camera: <SENSOR><ERROR> 711: sensor_pick_resolution: res_idx: 1
09-19 00:11:05.034 774-1310/? E/mm-camera: <IMGLIB><ERROR> 297: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Invalid dimensions 0x0
    <IMGLIB><ERROR> 197: int img_algo_preload(img_base_ops_t *, void *): Preload: Failed to allocate buffer, rc -4
    <IMGLIB><ERROR> 119: module_imgbase_client_preload_exec: IMG_CORE_PRELOAD failed -4
09-19 00:11:05.034 2254-2254/? V/Riru: jniRegisterNativeMethods android/app/admin/SecurityLog
09-19 00:11:05.035 2254-2254/? V/Riru: jniRegisterNativeMethods android/content/res/AssetManager
    jniRegisterNativeMethods android/content/res/StringBlock
    jniRegisterNativeMethods android/content/res/XmlBlock
    jniRegisterNativeMethods android/content/res/ApkAssets
    jniRegisterNativeMethods android/text/AndroidCharacter
    jniRegisterNativeMethods android/text/Hyphenator
    jniRegisterNativeMethods android/view/KeyCharacterMap
    jniRegisterNativeMethods android/os/Process
    jniRegisterNativeMethods android/os/SystemProperties
09-19 00:11:05.035 2254-2254/? I/Riru: replaced android.os.SystemProperties#native_set
09-19 00:11:05.035 2255-2255/? V/Riru: jniRegisterNativeMethods com/android/internal/os/RuntimeInit
09-19 00:11:05.035 2254-2254/? V/Riru: jniRegisterNativeMethods android/os/Binder
09-19 00:11:05.035 2255-2255/? V/Riru: jniRegisterNativeMethods com/android/internal/os/ZygoteInit
    jniRegisterNativeMethods android/os/SystemClock
09-19 00:11:05.035 2254-2254/? V/Riru: jniRegisterNativeMethods com/android/internal/os/BinderInternal
09-19 00:11:05.035 2255-2255/? V/Riru: jniRegisterNativeMethods android/util/EventLog
09-19 00:11:05.035 2254-2254/? V/Riru: jniRegisterNativeMethods android/os/BinderProxy
09-19 00:11:05.035 2255-2255/? V/Riru: jniRegisterNativeMethods android/util/Log
    jniRegisterNativeMethods android/util/MemoryIntArray
    jniRegisterNativeMethods android/util/PathParser
09-19 00:11:05.036 2255-2255/? V/Riru: jniRegisterNativeMethods android/util/StatsLog
    jniRegisterNativeMethods android/util/StatsLogInternal
09-19 00:11:05.036 774-774/? E/Thermal-Lib: pipe write error:9
09-19 00:11:05.036 2254-2254/? V/Riru: jniRegisterNativeMethods android/os/Parcel
09-19 00:11:05.036 774-774/? I/Thermal-Lib: Thermal-Lib-Client: Unregisteration is successfull for handle:1
09-19 00:11:05.036 2254-2254/? V/Riru: jniRegisterNativeMethods android/os/HidlSupport
    jniRegisterNativeMethods android/os/HwBinder
    jniRegisterNativeMethods android/os/HwBlob
    jniRegisterNativeMethods android/os/HwParcel
    jniRegisterNativeMethods android/os/HwRemoteBinder
    jniRegisterNativeMethods android/os/VintfObject
    jniRegisterNativeMethods android/os/VintfRuntimeInfo
    jniRegisterNativeMethods android/graphics/Canvas
    jniRegisterNativeMethods android/graphics/BaseCanvas
    jniRegisterNativeMethods android/graphics/BaseRecordingCanvas
    jniRegisterNativeMethods android/graphics/ColorSpace$Rgb
09-19 00:11:05.036 2255-2255/? V/Riru: jniRegisterNativeMethods android/app/admin/SecurityLog
09-19 00:11:05.037 2255-2255/? V/Riru: jniRegisterNativeMethods android/content/res/AssetManager
    jniRegisterNativeMethods android/content/res/StringBlock
    jniRegisterNativeMethods android/content/res/XmlBlock
    jniRegisterNativeMethods android/content/res/ApkAssets
    jniRegisterNativeMethods android/text/AndroidCharacter
    jniRegisterNativeMethods android/text/Hyphenator
    jniRegisterNativeMethods android/view/KeyCharacterMap
    jniRegisterNativeMethods android/os/Process
    jniRegisterNativeMethods android/os/SystemProperties
09-19 00:11:05.037 2255-2255/? I/Riru: replaced android.os.SystemProperties#native_set
09-19 00:11:05.037 2254-2254/? V/Riru: jniRegisterNativeMethods android/view/DisplayEventReceiver
09-19 00:11:05.037 2255-2255/? V/Riru: jniRegisterNativeMethods android/os/Binder
09-19 00:11:05.037 2254-2254/? V/Riru: jniRegisterNativeMethods android/graphics/RenderNode
09-19 00:11:05.037 2255-2255/? V/Riru: jniRegisterNativeMethods com/android/internal/os/BinderInternal
09-19 00:11:05.037 2254-2254/? V/Riru: jniRegisterNativeMethods android/view/RenderNodeAnimator
    jniRegisterNativeMethods android/graphics/RecordingCanvas
    jniRegisterNativeMethods android/view/InputApplicationHandle
09-19 00:11:05.037 2255-2255/? V/Riru: jniRegisterNativeMethods android/os/BinderProxy
09-19 00:11:05.037 2254-2254/? V/Riru: jniRegisterNativeMethods android/view/InputWindowHandle
09-19 00:11:05.038 2254-2254/? V/Riru: jniRegisterNativeMethods android/view/TextureLayer
    jniRegisterNativeMethods android/graphics/HardwareRenderer
    jniRegisterNativeMethods android/view/Surface
09-19 00:11:05.038 2255-2255/? V/Riru: jniRegisterNativeMethods android/os/Parcel
09-19 00:11:05.038 2254-2254/? V/Riru: jniRegisterNativeMethods android/view/SurfaceControl
09-19 00:11:05.038 2255-2255/? V/Riru: jniRegisterNativeMethods android/os/HidlSupport
    jniRegisterNativeMethods android/os/HwBinder
    jniRegisterNativeMethods android/os/HwBlob
    jniRegisterNativeMethods android/os/HwParcel
    jniRegisterNativeMethods android/os/HwRemoteBinder
09-19 00:11:05.038 2254-2254/? V/Riru: jniRegisterNativeMethods android/view/SurfaceSession
    jniRegisterNativeMethods android/view/CompositionSamplingListener
09-19 00:11:05.038 2255-2255/? V/Riru: jniRegisterNativeMethods android/os/VintfObject
09-19 00:11:05.038 2254-2254/? V/Riru: jniRegisterNativeMethods android/view/TextureView
09-19 00:11:05.038 2255-2255/? V/Riru: jniRegisterNativeMethods android/os/VintfRuntimeInfo
09-19 00:11:05.038 2254-2254/? V/Riru: jniRegisterNativeMethods com/android/internal/view/animation/NativeInterpolatorFactoryHelper
09-19 00:11:05.038 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/Canvas
09-19 00:11:05.038 2254-2254/? V/Riru: jniRegisterNativeMethods com/google/android/gles_jni/EGLImpl
09-19 00:11:05.038 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/BaseCanvas
09-19 00:11:05.038 2254-2254/? V/Riru: jniRegisterNativeMethods com/google/android/gles_jni/GLImpl
09-19 00:11:05.038 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/BaseRecordingCanvas
    jniRegisterNativeMethods android/graphics/ColorSpace$Rgb
09-19 00:11:05.039 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/EGL14
09-19 00:11:05.039 2255-2255/? V/Riru: jniRegisterNativeMethods android/view/DisplayEventReceiver
09-19 00:11:05.039 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/EGL15
    jniRegisterNativeMethods android/opengl/EGLExt
09-19 00:11:05.039 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/RenderNode
09-19 00:11:05.039 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/GLES10
09-19 00:11:05.039 2255-2255/? V/Riru: jniRegisterNativeMethods android/view/RenderNodeAnimator
    jniRegisterNativeMethods android/graphics/RecordingCanvas
    jniRegisterNativeMethods android/view/InputApplicationHandle
09-19 00:11:05.039 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/GLES10Ext
09-19 00:11:05.039 2255-2255/? V/Riru: jniRegisterNativeMethods android/view/InputWindowHandle
09-19 00:11:05.039 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/GLES11
09-19 00:11:05.040 2255-2255/? V/Riru: jniRegisterNativeMethods android/view/TextureLayer
09-19 00:11:05.040 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/GLES11Ext
09-19 00:11:05.040 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/HardwareRenderer
    jniRegisterNativeMethods android/view/Surface
    jniRegisterNativeMethods android/view/SurfaceControl
09-19 00:11:05.040 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/GLES20
09-19 00:11:05.040 2255-2255/? V/Riru: jniRegisterNativeMethods android/view/SurfaceSession
    jniRegisterNativeMethods android/view/CompositionSamplingListener
    jniRegisterNativeMethods android/view/TextureView
    jniRegisterNativeMethods com/android/internal/view/animation/NativeInterpolatorFactoryHelper
    jniRegisterNativeMethods com/google/android/gles_jni/EGLImpl
    jniRegisterNativeMethods com/google/android/gles_jni/GLImpl
09-19 00:11:05.040 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/GLES30
09-19 00:11:05.041 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/GLES31
    jniRegisterNativeMethods android/opengl/GLES31Ext
    jniRegisterNativeMethods android/opengl/GLES32
    jniRegisterNativeMethods android/graphics/Bitmap
09-19 00:11:05.041 2255-2255/? V/Riru: jniRegisterNativeMethods android/opengl/EGL14
09-19 00:11:05.041 2254-2254/? V/Riru: jniRegisterNativeMethods android/graphics/BitmapFactory
    jniRegisterNativeMethods android/graphics/BitmapRegionDecoder
09-19 00:11:05.041 2255-2255/? V/Riru: jniRegisterNativeMethods android/opengl/EGL15
    jniRegisterNativeMethods android/opengl/EGLExt
09-19 00:11:05.041 2254-2254/? V/Riru: jniRegisterNativeMethods android/graphics/Camera
09-19 00:11:05.041 2255-2255/? V/Riru: jniRegisterNativeMethods android/opengl/GLES10
09-19 00:11:05.041 2254-2254/? V/Riru: jniRegisterNativeMethods android/graphics/CanvasProperty
    jniRegisterNativeMethods android/graphics/ColorFilter
    jniRegisterNativeMethods android/graphics/PorterDuffColorFilter
    jniRegisterNativeMethods android/graphics/BlendModeColorFilter
09-19 00:11:05.042 2254-2254/? V/Riru: jniRegisterNativeMethods android/graphics/LightingColorFilter
    jniRegisterNativeMethods android/graphics/ColorMatrixColorFilter
    jniRegisterNativeMethods android/graphics/DrawFilter
    jniRegisterNativeMethods android/graphics/PaintFlagsDrawFilter
    jniRegisterNativeMethods android/graphics/FontFamily
09-19 00:11:05.042 2255-2255/? V/Riru: jniRegisterNativeMethods android/opengl/GLES10Ext
    jniRegisterNativeMethods android/opengl/GLES11
    jniRegisterNativeMethods android/opengl/GLES11Ext
    jniRegisterNativeMethods android/opengl/GLES20
09-19 00:11:05.043 2255-2255/? V/Riru: jniRegisterNativeMethods android/opengl/GLES30
    jniRegisterNativeMethods android/opengl/GLES31
09-19 00:11:05.044 2255-2255/? V/Riru: jniRegisterNativeMethods android/opengl/GLES31Ext
    jniRegisterNativeMethods android/opengl/GLES32
    jniRegisterNativeMethods android/graphics/Bitmap
    jniRegisterNativeMethods android/graphics/BitmapFactory
    jniRegisterNativeMethods android/graphics/BitmapRegionDecoder
    jniRegisterNativeMethods android/graphics/Camera
    jniRegisterNativeMethods android/graphics/CanvasProperty
    jniRegisterNativeMethods android/graphics/ColorFilter
    jniRegisterNativeMethods android/graphics/PorterDuffColorFilter
    jniRegisterNativeMethods android/graphics/BlendModeColorFilter
    jniRegisterNativeMethods android/graphics/LightingColorFilter
    jniRegisterNativeMethods android/graphics/ColorMatrixColorFilter
    jniRegisterNativeMethods android/graphics/DrawFilter
    jniRegisterNativeMethods android/graphics/PaintFlagsDrawFilter
    jniRegisterNativeMethods android/graphics/FontFamily
09-19 00:11:05.044 2254-2254/? V/Riru: jniRegisterNativeMethods android/graphics/GraphicBuffer
    jniRegisterNativeMethods android/graphics/ImageDecoder
    jniRegisterNativeMethods android/graphics/drawable/AnimatedImageDrawable
    jniRegisterNativeMethods android/graphics/Interpolator
09-19 00:11:05.045 2254-2254/? V/Riru: jniRegisterNativeMethods android/graphics/MaskFilter
    jniRegisterNativeMethods android/graphics/BlurMaskFilter
    jniRegisterNativeMethods android/graphics/EmbossMaskFilter
    jniRegisterNativeMethods android/graphics/TableMaskFilter
    jniRegisterNativeMethods android/graphics/Matrix
    jniRegisterNativeMethods android/graphics/Movie
    jniRegisterNativeMethods android/graphics/NinePatch
    jniRegisterNativeMethods android/graphics/Paint
    jniRegisterNativeMethods android/graphics/Path
    jniRegisterNativeMethods android/graphics/PathMeasure
    jniRegisterNativeMethods android/graphics/PathEffect
    jniRegisterNativeMethods android/graphics/ComposePathEffect
    jniRegisterNativeMethods android/graphics/SumPathEffect
    jniRegisterNativeMethods android/graphics/DashPathEffect
    jniRegisterNativeMethods android/graphics/PathDashPathEffect
    jniRegisterNativeMethods android/graphics/CornerPathEffect
    jniRegisterNativeMethods android/graphics/DiscretePathEffect
    jniRegisterNativeMethods android/graphics/Picture
    jniRegisterNativeMethods android/graphics/Region
    jniRegisterNativeMethods android/graphics/RegionIterator
    jniRegisterNativeMethods android/graphics/Color
    jniRegisterNativeMethods android/graphics/Shader
    jniRegisterNativeMethods android/graphics/BitmapShader
    jniRegisterNativeMethods android/graphics/LinearGradient
    jniRegisterNativeMethods android/graphics/RadialGradient
    jniRegisterNativeMethods android/graphics/SweepGradient
    jniRegisterNativeMethods android/graphics/ComposeShader
    jniRegisterNativeMethods android/graphics/SurfaceTexture
    jniRegisterNativeMethods android/graphics/Typeface
    jniRegisterNativeMethods android/graphics/YuvImage
    jniRegisterNativeMethods android/graphics/drawable/AnimatedVectorDrawable
    jniRegisterNativeMethods android/graphics/drawable/VectorDrawable
09-19 00:11:05.046 2254-2254/? V/Riru: jniRegisterNativeMethods android/graphics/fonts/Font$Builder
    jniRegisterNativeMethods android/graphics/fonts/FontFamily$Builder
    jniRegisterNativeMethods android/graphics/pdf/PdfDocument
    jniRegisterNativeMethods android/graphics/pdf/PdfEditor
    jniRegisterNativeMethods android/graphics/pdf/PdfRenderer
    jniRegisterNativeMethods android/graphics/text/MeasuredText
    jniRegisterNativeMethods android/graphics/text/MeasuredText$Builder
    jniRegisterNativeMethods android/graphics/text/LineBreaker
    jniRegisterNativeMethods android/database/CursorWindow
    jniRegisterNativeMethods android/database/sqlite/SQLiteConnection
    jniRegisterNativeMethods android/database/sqlite/SQLiteGlobal
    jniRegisterNativeMethods android/database/sqlite/SQLiteDebug
    jniRegisterNativeMethods android/os/Debug
    jniRegisterNativeMethods android/os/FileObserver$ObserverThread
    jniRegisterNativeMethods android/os/GraphicsEnvironment
    jniRegisterNativeMethods android/os/MessageQueue
    jniRegisterNativeMethods android/os/SELinux
    jniRegisterNativeMethods android/os/Trace
    jniRegisterNativeMethods android/os/UEventObserver
    jniRegisterNativeMethods android/net/LocalSocketImpl
    jniRegisterNativeMethods android/net/NetworkUtils
    jniRegisterNativeMethods android/os/MemoryFile
    jniRegisterNativeMethods android/os/SharedMemory
    jniRegisterNativeMethods com/android/internal/os/ClassLoaderFactory
    jniRegisterNativeMethods com/android/internal/os/Zygote
09-19 00:11:05.046 2254-2254/? I/Riru: replaced com.android.internal.os.Zygote#nativeForkAndSpecialize
    replaced com.android.internal.os.Zygote#nativeForkSystemServer
    replaced com.android.internal.os.Zygote#nativeSpecializeAppProcess
09-19 00:11:05.047 2254-2254/? V/Riru: jniRegisterNativeMethods com/android/internal/os/ZygoteInit
    jniRegisterNativeMethods com/android/internal/util/VirtualRefBasePtr
    jniRegisterNativeMethods android/hardware/Camera
    jniRegisterNativeMethods android/hardware/camera2/impl/CameraMetadataNative
    jniRegisterNativeMethods android/hardware/camera2/legacy/LegacyCameraDevice
    jniRegisterNativeMethods android/hardware/camera2/legacy/PerfMeasurement
    jniRegisterNativeMethods android/hardware/camera2/DngCreator
    jniRegisterNativeMethods android/hardware/HardwareBuffer
    jniRegisterNativeMethods android/hardware/SystemSensorManager
    jniRegisterNativeMethods android/hardware/SystemSensorManager$BaseEventQueue
    jniRegisterNativeMethods android/hardware/SerialPort
09-19 00:11:05.047 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/GraphicBuffer
    jniRegisterNativeMethods android/graphics/ImageDecoder
    jniRegisterNativeMethods android/graphics/drawable/AnimatedImageDrawable
09-19 00:11:05.047 2254-2254/? V/Riru: jniRegisterNativeMethods android/hardware/soundtrigger/SoundTrigger
    jniRegisterNativeMethods android/hardware/soundtrigger/SoundTriggerModule
09-19 00:11:05.047 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/Interpolator
09-19 00:11:05.047 2254-2254/? V/Riru: jniRegisterNativeMethods android/hardware/usb/UsbDevice
09-19 00:11:05.047 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/MaskFilter
    jniRegisterNativeMethods android/graphics/BlurMaskFilter
09-19 00:11:05.047 2254-2254/? V/Riru: jniRegisterNativeMethods android/hardware/usb/UsbDeviceConnection
09-19 00:11:05.047 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/EmbossMaskFilter
09-19 00:11:05.047 2254-2254/? V/Riru: jniRegisterNativeMethods android/hardware/usb/UsbRequest
09-19 00:11:05.047 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/TableMaskFilter
09-19 00:11:05.047 2254-2254/? V/Riru: jniRegisterNativeMethods android/hardware/location/ActivityRecognitionHardware
09-19 00:11:05.047 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/Matrix
09-19 00:11:05.047 2254-2254/? V/Riru: jniRegisterNativeMethods android/media/AudioSystem
09-19 00:11:05.047 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/Movie
    jniRegisterNativeMethods android/graphics/NinePatch
    jniRegisterNativeMethods android/graphics/Paint
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/Path
    jniRegisterNativeMethods android/graphics/PathMeasure
    jniRegisterNativeMethods android/graphics/PathEffect
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/media/AudioSystem
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/ComposePathEffect
    jniRegisterNativeMethods android/graphics/SumPathEffect
    jniRegisterNativeMethods android/graphics/DashPathEffect
    jniRegisterNativeMethods android/graphics/PathDashPathEffect
    jniRegisterNativeMethods android/graphics/CornerPathEffect
    jniRegisterNativeMethods android/graphics/DiscretePathEffect
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/media/AudioPortEventHandler
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/Picture
    jniRegisterNativeMethods android/graphics/Region
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/media/AudioRecord
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/RegionIterator
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/media/AudioTrack
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/Color
    jniRegisterNativeMethods android/graphics/Shader
    jniRegisterNativeMethods android/graphics/BitmapShader
    jniRegisterNativeMethods android/graphics/LinearGradient
    jniRegisterNativeMethods android/graphics/RadialGradient
    jniRegisterNativeMethods android/graphics/SweepGradient
    jniRegisterNativeMethods android/graphics/ComposeShader
    jniRegisterNativeMethods android/graphics/SurfaceTexture
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/media/AudioAttributes
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/Typeface
09-19 00:11:05.048 2254-2254/? W/zygote64: JNI RegisterNativeMethods: attempt to register 0 native methods for android.media.AudioAttributes
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/YuvImage
    jniRegisterNativeMethods android/graphics/drawable/AnimatedVectorDrawable
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/media/audiopolicy/AudioProductStrategy
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/drawable/VectorDrawable
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/media/audiopolicy/AudioVolumeGroup
    jniRegisterNativeMethods android/media/audiopolicy/AudioVolumeGroupChangeHandler
    jniRegisterNativeMethods android/media/JetPlayer
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/fonts/Font$Builder
    jniRegisterNativeMethods android/graphics/fonts/FontFamily$Builder
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/media/RemoteDisplay
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/pdf/PdfDocument
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/media/ToneGenerator
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/pdf/PdfEditor
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/Matrix
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/pdf/PdfRenderer
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/Visibility
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/text/MeasuredText
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/GLUtils
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/text/MeasuredText$Builder
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/opengl/ETC1
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/graphics/text/LineBreaker
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods com/android/server/NetworkManagementSocketTagger
09-19 00:11:05.048 2255-2255/? V/Riru: jniRegisterNativeMethods android/database/CursorWindow
09-19 00:11:05.048 2254-2254/? V/Riru: jniRegisterNativeMethods android/ddm/DdmHandleNativeHeap
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/app/backup/BackupDataInput
    jniRegisterNativeMethods android/app/backup/BackupDataOutput
09-19 00:11:05.049 2255-2255/? V/Riru: jniRegisterNativeMethods android/database/sqlite/SQLiteConnection
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/app/backup/FileBackupHelperBase
    jniRegisterNativeMethods android/app/backup/BackupHelperDispatcher
    jniRegisterNativeMethods android/app/backup/FullBackup
    jniRegisterNativeMethods android/app/Activity
09-19 00:11:05.049 2255-2255/? V/Riru: jniRegisterNativeMethods android/database/sqlite/SQLiteGlobal
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/app/ActivityThread
09-19 00:11:05.049 2255-2255/? V/Riru: jniRegisterNativeMethods android/database/sqlite/SQLiteDebug
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/app/NativeActivity
09-19 00:11:05.049 2255-2255/? V/Riru: jniRegisterNativeMethods android/os/Debug
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/util/jar/StrictJarFile
    jniRegisterNativeMethods android/view/InputChannel
09-19 00:11:05.049 2255-2255/? V/Riru: jniRegisterNativeMethods android/os/FileObserver$ObserverThread
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/view/InputEventReceiver
09-19 00:11:05.049 2255-2255/? V/Riru: jniRegisterNativeMethods android/os/GraphicsEnvironment
    jniRegisterNativeMethods android/os/MessageQueue
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/view/InputEventSender
09-19 00:11:05.049 2255-2255/? V/Riru: jniRegisterNativeMethods android/os/SELinux
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/view/InputQueue
09-19 00:11:05.049 2255-2255/? V/Riru: jniRegisterNativeMethods android/os/Trace
    jniRegisterNativeMethods android/os/UEventObserver
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/view/KeyEvent
    jniRegisterNativeMethods android/view/MotionEvent
09-19 00:11:05.049 2255-2255/? V/Riru: jniRegisterNativeMethods android/net/LocalSocketImpl
    jniRegisterNativeMethods android/net/NetworkUtils
    jniRegisterNativeMethods android/os/MemoryFile
    jniRegisterNativeMethods android/os/SharedMemory
    jniRegisterNativeMethods com/android/internal/os/ClassLoaderFactory
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/view/VelocityTracker
09-19 00:11:05.049 2255-2255/? V/Riru: jniRegisterNativeMethods com/android/internal/os/Zygote
09-19 00:11:05.049 2255-2255/? I/Riru: replaced com.android.internal.os.Zygote#nativeForkAndSpecialize
    replaced com.android.internal.os.Zygote#nativeForkSystemServer
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/content/res/ObbScanner
09-19 00:11:05.049 2255-2255/? I/Riru: replaced com.android.internal.os.Zygote#nativeSpecializeAppProcess
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/animation/PropertyValuesHolder
09-19 00:11:05.049 2255-2255/? V/Riru: jniRegisterNativeMethods com/android/internal/os/ZygoteInit
    jniRegisterNativeMethods com/android/internal/util/VirtualRefBasePtr
09-19 00:11:05.049 2254-2254/? V/Riru: jniRegisterNativeMethods android/security/Scrypt
    jniRegisterNativeMethods com/android/internal/content/NativeLibraryHelper
    jniRegisterNativeMethods com/android/internal/os/AtomicDirectory
09-19 00:11:05.049 2255-2255/? V/Riru: jniRegisterNativeMethods android/hardware/Camera
09-19 00:11:05.050 2254-2254/? V/Riru: jniRegisterNativeMethods com/android/internal/os/FuseAppLoop
09-19 00:11:05.050 2255-2255/? V/Riru: jniRegisterNativeMethods android/hardware/camera2/impl/CameraMetadataNative
    jniRegisterNativeMethods android/hardware/camera2/legacy/LegacyCameraDevice
    jniRegisterNativeMethods android/hardware/camera2/legacy/PerfMeasurement
    jniRegisterNativeMethods android/hardware/camera2/DngCreator
    jniRegisterNativeMethods android/hardware/HardwareBuffer
    jniRegisterNativeMethods android/hardware/SystemSensorManager
    jniRegisterNativeMethods android/hardware/SystemSensorManager$BaseEventQueue
    jniRegisterNativeMethods android/hardware/SerialPort
    jniRegisterNativeMethods android/hardware/soundtrigger/SoundTrigger
    jniRegisterNativeMethods android/hardware/soundtrigger/SoundTriggerModule
    jniRegisterNativeMethods android/hardware/usb/UsbDevice
    jniRegisterNativeMethods android/hardware/usb/UsbDeviceConnection
    jniRegisterNativeMethods android/hardware/usb/UsbRequest
    jniRegisterNativeMethods android/hardware/location/ActivityRecognitionHardware
    jniRegisterNativeMethods android/media/AudioSystem
09-19 00:11:05.051 2255-2255/? V/Riru: jniRegisterNativeMethods android/media/AudioSystem
    jniRegisterNativeMethods android/media/AudioPortEventHandler
    jniRegisterNativeMethods android/media/AudioRecord
    jniRegisterNativeMethods android/media/AudioTrack
    jniRegisterNativeMethods android/media/AudioAttributes
09-19 00:11:05.051 2255-2255/? W/zygote: JNI RegisterNativeMethods: attempt to register 0 native methods for android.media.AudioAttributes
09-19 00:11:05.051 2254-2254/? D/Zygote: begin preload
09-19 00:11:05.051 2254-2254/? I/Zygote: Calling ZygoteHooks.beginPreload()
09-19 00:11:05.051 2255-2255/? V/Riru: jniRegisterNativeMethods android/media/audiopolicy/AudioProductStrategy
    jniRegisterNativeMethods android/media/audiopolicy/AudioVolumeGroup
    jniRegisterNativeMethods android/media/audiopolicy/AudioVolumeGroupChangeHandler
    jniRegisterNativeMethods android/media/JetPlayer
    jniRegisterNativeMethods android/media/RemoteDisplay
    jniRegisterNativeMethods android/media/ToneGenerator
    jniRegisterNativeMethods android/opengl/Matrix
    jniRegisterNativeMethods android/opengl/Visibility
    jniRegisterNativeMethods android/opengl/GLUtils
    jniRegisterNativeMethods android/opengl/ETC1
    jniRegisterNativeMethods com/android/server/NetworkManagementSocketTagger
09-19 00:11:05.052 2255-2255/? V/Riru: jniRegisterNativeMethods android/ddm/DdmHandleNativeHeap
    jniRegisterNativeMethods android/app/backup/BackupDataInput
    jniRegisterNativeMethods android/app/backup/BackupDataOutput
    jniRegisterNativeMethods android/app/backup/FileBackupHelperBase
    jniRegisterNativeMethods android/app/backup/BackupHelperDispatcher
    jniRegisterNativeMethods android/app/backup/FullBackup
    jniRegisterNativeMethods android/app/Activity
    jniRegisterNativeMethods android/app/ActivityThread
    jniRegisterNativeMethods android/app/NativeActivity
    jniRegisterNativeMethods android/util/jar/StrictJarFile
    jniRegisterNativeMethods android/view/InputChannel
    jniRegisterNativeMethods android/view/InputEventReceiver
    jniRegisterNativeMethods android/view/InputEventSender
    jniRegisterNativeMethods android/view/InputQueue
    jniRegisterNativeMethods android/view/KeyEvent
    jniRegisterNativeMethods android/view/MotionEvent
    jniRegisterNativeMethods android/view/VelocityTracker
    jniRegisterNativeMethods android/content/res/ObbScanner
    jniRegisterNativeMethods android/animation/PropertyValuesHolder
    jniRegisterNativeMethods android/security/Scrypt
    jniRegisterNativeMethods com/android/internal/content/NativeLibraryHelper
    jniRegisterNativeMethods com/android/internal/os/AtomicDirectory
09-19 00:11:05.053 2255-2255/? V/Riru: jniRegisterNativeMethods com/android/internal/os/FuseAppLoop
09-19 00:11:05.056 2254-2254/? D/Zygote64Timing: BeginPreload took to complete: 5ms
09-19 00:11:05.056 2254-2254/? I/Zygote: Preloading classes...
09-19 00:11:05.057 2254-2254/? W/Zygote: Class not found for preloading: android.app.-$$Lambda$ActivityThread$ZXDWm3IBeFmLnFVblhB-IOZCr9o
09-19 00:11:05.057 2255-2255/? I/zygote: Explicit concurrent copying GC freed 303(39KB) AllocSpace objects, 0(0B) LOS objects, 99% free, 24KB/24MB, paused 60us total 2.587ms
09-19 00:11:05.060 2255-2255/? I/zygote: Explicit concurrent copying GC freed 5(32KB) AllocSpace objects, 0(0B) LOS objects, 99% free, 24KB/24MB, paused 14us total 2.495ms
09-19 00:11:05.060 2255-2255/? D/Zygote32Timing: PostZygoteInitGC took to complete: 6ms
    ZygoteInit took to complete: 6ms
09-19 00:11:05.093 2255-2255/? I/Zygote: Accepting command socket connections
09-19 00:11:05.094 774-2341/? E/mm-camera: <IMGLIB><ERROR> 328: static int32_t QCameraPAAF::AllocateBuffers(img_base_ops_t *, bool): Nothing allocated or already freed!
09-19 00:11:05.097 2254-2254/? W/Zygote: Class not found for preloading: android.bluetooth.BluetoothA2dp$2
09-19 00:11:05.099 2254-2254/? I/PackageBackwardCompatibility: Could not find android.content.pm.AndroidTestBaseUpdater, ignoring
09-19 00:11:05.194 2254-2254/? E/ActivityRecognitionHardware: activity_recognition HAL is deprecated. class_init is effectively a no-op
