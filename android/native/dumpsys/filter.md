09-17 21:43:59.727 4045-4045/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:43:59.728 4045-4045/system_process I/PackageManager: Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package ai.lazero.lazero (protectionLevel=1250 flags=0x30c8bf46)
    Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:43:59.729 4045-4045/system_process I/PackageManager: Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:43:59.730 4045-4045/system_process I/PackageManager: Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:43:59.730 4045-4045/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:43:59.730 4045-4045/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf46)
09-17 21:43:59.730 4045-4045/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:43:59.730 4045-4045/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf46)
09-17 21:43:59.731 4045-4045/system_process I/PackageManager: Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.REQUEST_INSTALL_PACKAGES from package org.lineageos.jelly (protectionLevel=66 flags=0x30c8be45)
09-17 21:43:59.768 4045-4045/system_process E/System: ******************************************
    ************ Failure starting system services
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:43:59.768 4045-4045/system_process E/Zygote: System zygote died with exception
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:43:59.769 4045-4045/system_process E/AndroidRuntime: *** FATAL EXCEPTION IN SYSTEM PROCESS: main
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:02.086 4274-4274/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-9n_TgXMS9gGpzVLxGZG3nw==/base.apk
09-17 21:44:02.504 4274-4274/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
09-17 21:44:02.505 4274-4274/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
    Loading modules from /data/app/com.oranav.ditheredholobackground-WGw3w1Oj7KB1upluOt6Kqw==/base.apk
09-17 21:44:04.647 4475-4475/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
    Permission UID method has Hooked! android.uid.phone
09-17 21:44:04.756 4475-4475/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! ai.lazero.lazero
    Permission UID method has Hooked! android.uid.shared
09-17 21:44:04.757 4475-4475/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.system
    PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-17 21:44:05.292 4475-4475/system_process I/PackageManager: Un-granting permission android.permission.REQUEST_INSTALL_PACKAGES from package com.tencent.mobileqq (protectionLevel=66 flags=0x38083e44)
    Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package io.animal.monkey (protectionLevel=1250 flags=0x3048be46)
    Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:05.293 4475-4475/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package ai.lazero.lazero (protectionLevel=1250 flags=0x3048bf46)
    Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:05.294 4475-4475/system_process I/PackageManager: Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:05.294 4475-4475/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:05.294 4475-4475/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x3048bf46)
09-17 21:44:05.294 4475-4475/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:05.294 4475-4475/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x3048bf46)
09-17 21:44:05.295 4475-4475/system_process I/PackageManager: Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.REQUEST_INSTALL_PACKAGES from package org.lineageos.jelly (protectionLevel=66 flags=0x3048be45)
09-17 21:44:05.958 4475-4475/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "com.android.server.pm.Settings" on path: DexPathList[[zip file "/system/priv-app/SettingsProvider/SettingsProvider.apk"],nativeLibraryDirectories=[/system/priv-app/SettingsProvider/lib/arm64, /system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at ai.lazero.lazero.HookTest_v3.handleLoadPackage(HookTest_v3.java:25)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.LoadedApkGetCL.afterHookedMethod(LoadedApkGetCL.java:61)
        at de.robv.android.xposed.XC_MethodHook.callAfterHookedMethod(XC_MethodHook.java:68)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:388)
        at SandHookerNew_35f4vrpdo2vmlbkhbqk0r22p8o.hook(Unknown Source:46)
        at android.app.ContextImpl.getClassLoader(ContextImpl.java:371)
        at android.app.ActivityThread.installProvider(ActivityThread.java:6965)
        at android.app.ActivityThread.installContentProviders(ActivityThread.java:6528)
        at android.app.ActivityThread.installSystemProviders(ActivityThread.java:7169)
        at com.android.server.am.ActivityManagerService.installSystemProviders(ActivityManagerService.java:7545)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:1002)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:05.997 4475-4475/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "com.android.server.pm.Settings" on path: DexPathList[[zip file "/system/priv-app/LineageSettingsProvider/LineageSettingsProvider.apk"],nativeLibraryDirectories=[/system/priv-app/LineageSettingsProvider/lib/arm64, /system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at ai.lazero.lazero.HookTest_v3.handleLoadPackage(HookTest_v3.java:25)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.LoadedApkGetCL.afterHookedMethod(LoadedApkGetCL.java:61)
        at de.robv.android.xposed.XC_MethodHook.callAfterHookedMethod(XC_MethodHook.java:68)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:388)
        at SandHookerNew_35f4vrpdo2vmlbkhbqk0r22p8o.hook(Unknown Source:46)
        at android.app.ContextImpl.getClassLoader(ContextImpl.java:371)
        at android.app.ActivityThread.installProvider(ActivityThread.java:6965)
        at android.app.ActivityThread.installContentProviders(ActivityThread.java:6528)
        at android.app.ActivityThread.installSystemProviders(ActivityThread.java:7169)
        at com.android.server.am.ActivityManagerService.installSystemProviders(ActivityManagerService.java:7545)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:1002)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:07.382 4475-4475/system_process I/PackageManager: Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package io.animal.monkey (protectionLevel=1250 flags=0x30c8be46)
    Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:07.383 4475-4475/system_process I/PackageManager: Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package ai.lazero.lazero (protectionLevel=1250 flags=0x30c8bf46)
    Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:07.384 4475-4475/system_process I/PackageManager: Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:07.384 4475-4475/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:07.384 4475-4475/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf46)
09-17 21:44:07.384 4475-4475/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:07.384 4475-4475/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf46)
    Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:07.419 4475-4475/system_process E/System: ******************************************
    ************ Failure starting system services
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:07.419 4475-4475/system_process E/Zygote: System zygote died with exception
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:07.419 4475-4475/system_process E/AndroidRuntime: *** FATAL EXCEPTION IN SYSTEM PROCESS: main
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:09.732 4705-4705/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-9n_TgXMS9gGpzVLxGZG3nw==/base.apk
09-17 21:44:10.150 4705-4705/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
09-17 21:44:10.151 4705-4705/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
09-17 21:44:12.337 4904-4904/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
    Permission UID method has Hooked! android.uid.phone
    Permission UID method has Hooked! android.uid.log
    Permission UID method has Hooked! android.uid.nfc
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! android.uid.shell
    Permission UID method has Hooked! android.uid.se
    Permission UID method has Hooked! android.uid.networkstack
09-17 21:44:12.440 4904-4904/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Permission UID method has Hooked! android.uid.shared
09-17 21:44:12.441 4904-4904/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.system
    PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-17 21:44:13.061 4904-4904/system_process I/PackageManager: Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package io.animal.monkey (protectionLevel=1250 flags=0x3048be46)
    Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:13.062 4904-4904/system_process I/PackageManager: Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package ai.lazero.lazero (protectionLevel=1250 flags=0x3048bf46)
    Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:13.063 4904-4904/system_process I/PackageManager: Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:13.063 4904-4904/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:13.063 4904-4904/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x3048bf46)
09-17 21:44:13.063 4904-4904/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:13.063 4904-4904/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x3048bf46)
    Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:13.797 4904-4904/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "com.android.server.pm.Settings" on path: DexPathList[[zip file "/system/priv-app/SettingsProvider/SettingsProvider.apk"],nativeLibraryDirectories=[/system/priv-app/SettingsProvider/lib/arm64, /system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at ai.lazero.lazero.HookTest_v3.handleLoadPackage(HookTest_v3.java:25)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.LoadedApkGetCL.afterHookedMethod(LoadedApkGetCL.java:61)
        at de.robv.android.xposed.XC_MethodHook.callAfterHookedMethod(XC_MethodHook.java:68)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:388)
        at SandHookerNew_35f4vrpdo2vmlbkhbqk0r22p8o.hook(Unknown Source:46)
        at android.app.ContextImpl.getClassLoader(ContextImpl.java:371)
        at android.app.ActivityThread.installProvider(ActivityThread.java:6965)
        at android.app.ActivityThread.installContentProviders(ActivityThread.java:6528)
        at android.app.ActivityThread.installSystemProviders(ActivityThread.java:7169)
        at com.android.server.am.ActivityManagerService.installSystemProviders(ActivityManagerService.java:7545)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:1002)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:13.827 4904-4904/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "com.android.server.pm.Settings" on path: DexPathList[[zip file "/system/priv-app/LineageSettingsProvider/LineageSettingsProvider.apk"],nativeLibraryDirectories=[/system/priv-app/LineageSettingsProvider/lib/arm64, /system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at ai.lazero.lazero.HookTest_v3.handleLoadPackage(HookTest_v3.java:25)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.LoadedApkGetCL.afterHookedMethod(LoadedApkGetCL.java:61)
        at de.robv.android.xposed.XC_MethodHook.callAfterHookedMethod(XC_MethodHook.java:68)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:388)
        at SandHookerNew_35f4vrpdo2vmlbkhbqk0r22p8o.hook(Unknown Source:46)
        at android.app.ContextImpl.getClassLoader(ContextImpl.java:371)
        at android.app.ActivityThread.installProvider(ActivityThread.java:6965)
        at android.app.ActivityThread.installContentProviders(ActivityThread.java:6528)
        at android.app.ActivityThread.installSystemProviders(ActivityThread.java:7169)
        at com.android.server.am.ActivityManagerService.installSystemProviders(ActivityManagerService.java:7545)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:1002)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:15.162 4904-4904/system_process I/PackageManager: Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package io.animal.monkey (protectionLevel=1250 flags=0x30c8be46)
    Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:15.163 4904-4904/system_process I/PackageManager: Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package ai.lazero.lazero (protectionLevel=1250 flags=0x30c8bf46)
    Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:15.164 4904-4904/system_process I/PackageManager: Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:15.164 4904-4904/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:15.164 4904-4904/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf46)
09-17 21:44:15.164 4904-4904/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:15.165 4904-4904/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf46)
    Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.REQUEST_INSTALL_PACKAGES from package org.lineageos.jelly (protectionLevel=66 flags=0x30c8be45)
09-17 21:44:15.207 4904-4904/system_process E/System: ******************************************
    ************ Failure starting system services
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:15.207 4904-4904/system_process E/Zygote: System zygote died with exception
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:15.208 4904-4904/system_process E/AndroidRuntime: *** FATAL EXCEPTION IN SYSTEM PROCESS: main
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:17.544 5135-5135/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-9n_TgXMS9gGpzVLxGZG3nw==/base.apk
09-17 21:44:17.963 5135-5135/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
      Loading class ai.lazero.lazero.HookTest_v2
09-17 21:44:17.964 5135-5135/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v3
    Loading modules from /data/app/com.oranav.ditheredholobackground-WGw3w1Oj7KB1upluOt6Kqw==/base.apk
09-17 21:44:20.102 5335-5335/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
    Permission UID method has Hooked! android.uid.phone
    Permission UID method has Hooked! android.uid.log
    Permission UID method has Hooked! android.uid.nfc
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! android.uid.shell
    Permission UID method has Hooked! android.uid.se
    Permission UID method has Hooked! android.uid.networkstack
09-17 21:44:20.231 5335-5335/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! ai.lazero.lazero
09-17 21:44:20.232 5335-5335/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.shared
    Permission UID method has Hooked! android.uid.system
    PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-17 21:44:20.848 5335-5335/system_process I/PackageManager: Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package io.animal.monkey (protectionLevel=1250 flags=0x3048be46)
    Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:20.849 5335-5335/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package ai.lazero.lazero (protectionLevel=1250 flags=0x3048bf46)
    Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:20.850 5335-5335/system_process I/PackageManager: Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:20.850 5335-5335/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:20.850 5335-5335/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x3048bf46)
09-17 21:44:20.850 5335-5335/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:20.850 5335-5335/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x3048bf46)
    Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:21.543 5335-5335/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "com.android.server.pm.Settings" on path: DexPathList[[zip file "/system/priv-app/SettingsProvider/SettingsProvider.apk"],nativeLibraryDirectories=[/system/priv-app/SettingsProvider/lib/arm64, /system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at ai.lazero.lazero.HookTest_v3.handleLoadPackage(HookTest_v3.java:25)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.LoadedApkGetCL.afterHookedMethod(LoadedApkGetCL.java:61)
        at de.robv.android.xposed.XC_MethodHook.callAfterHookedMethod(XC_MethodHook.java:68)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:388)
        at SandHookerNew_35f4vrpdo2vmlbkhbqk0r22p8o.hook(Unknown Source:46)
        at android.app.ContextImpl.getClassLoader(ContextImpl.java:371)
        at android.app.ActivityThread.installProvider(ActivityThread.java:6965)
        at android.app.ActivityThread.installContentProviders(ActivityThread.java:6528)
        at android.app.ActivityThread.installSystemProviders(ActivityThread.java:7169)
        at com.android.server.am.ActivityManagerService.installSystemProviders(ActivityManagerService.java:7545)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:1002)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:21.589 5335-5335/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "com.android.server.pm.Settings" on path: DexPathList[[zip file "/system/priv-app/LineageSettingsProvider/LineageSettingsProvider.apk"],nativeLibraryDirectories=[/system/priv-app/LineageSettingsProvider/lib/arm64, /system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at ai.lazero.lazero.HookTest_v3.handleLoadPackage(HookTest_v3.java:25)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.LoadedApkGetCL.afterHookedMethod(LoadedApkGetCL.java:61)
        at de.robv.android.xposed.XC_MethodHook.callAfterHookedMethod(XC_MethodHook.java:68)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:388)
        at SandHookerNew_35f4vrpdo2vmlbkhbqk0r22p8o.hook(Unknown Source:46)
        at android.app.ContextImpl.getClassLoader(ContextImpl.java:371)
        at android.app.ActivityThread.installProvider(ActivityThread.java:6965)
        at android.app.ActivityThread.installContentProviders(ActivityThread.java:6528)
        at android.app.ActivityThread.installSystemProviders(ActivityThread.java:7169)
        at com.android.server.am.ActivityManagerService.installSystemProviders(ActivityManagerService.java:7545)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:1002)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:22.666 5335-5335/system_process I/PackageManager: Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package io.animal.monkey (protectionLevel=1250 flags=0x30c8be46)
    Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:22.667 5335-5335/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package ai.lazero.lazero (protectionLevel=1250 flags=0x30c8bf46)
    Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:22.668 5335-5335/system_process I/PackageManager: Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:22.668 5335-5335/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:22.668 5335-5335/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf46)
09-17 21:44:22.668 5335-5335/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:22.668 5335-5335/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf46)
09-17 21:44:22.669 5335-5335/system_process I/PackageManager: Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.REQUEST_INSTALL_PACKAGES from package org.lineageos.jelly (protectionLevel=66 flags=0x30c8be45)
09-17 21:44:22.710 5335-5335/system_process E/System: ******************************************
    ************ Failure starting system services
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:22.710 5335-5335/system_process E/Zygote: System zygote died with exception
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:22.711 5335-5335/system_process E/AndroidRuntime: *** FATAL EXCEPTION IN SYSTEM PROCESS: main
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:25.036 5564-5564/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-9n_TgXMS9gGpzVLxGZG3nw==/base.apk
09-17 21:44:25.456 5564-5564/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
      Loading class ai.lazero.lazero.HookTest_v2
09-17 21:44:25.457 5564-5564/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v3
    Loading modules from /data/app/com.oranav.ditheredholobackground-WGw3w1Oj7KB1upluOt6Kqw==/base.apk
09-17 21:44:27.710 5764-5764/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
    Permission UID method has Hooked! android.uid.phone
    Permission UID method has Hooked! android.uid.log
    Permission UID method has Hooked! android.uid.nfc
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! android.uid.shell
09-17 21:44:27.814 5764-5764/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Permission UID method has Hooked! android.uid.shared
    Permission UID method has Hooked! android.uid.system
    PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-17 21:44:28.471 5764-5764/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package ai.lazero.lazero (protectionLevel=1250 flags=0x3048bf46)
09-17 21:44:28.472 5764-5764/system_process I/PackageManager: Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
    Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:28.473 5764-5764/system_process I/PackageManager: Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:28.473 5764-5764/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:28.473 5764-5764/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x3048bf46)
09-17 21:44:28.473 5764-5764/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:28.473 5764-5764/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x3048bf46)
    Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf46)
09-17 21:44:29.240 5764-5764/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "com.android.server.pm.Settings" on path: DexPathList[[zip file "/system/priv-app/SettingsProvider/SettingsProvider.apk"],nativeLibraryDirectories=[/system/priv-app/SettingsProvider/lib/arm64, /system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at ai.lazero.lazero.HookTest_v3.handleLoadPackage(HookTest_v3.java:25)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.LoadedApkGetCL.afterHookedMethod(LoadedApkGetCL.java:61)
        at de.robv.android.xposed.XC_MethodHook.callAfterHookedMethod(XC_MethodHook.java:68)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:388)
        at SandHookerNew_35f4vrpdo2vmlbkhbqk0r22p8o.hook(Unknown Source:46)
        at android.app.ContextImpl.getClassLoader(ContextImpl.java:371)
        at android.app.ActivityThread.installProvider(ActivityThread.java:6965)
        at android.app.ActivityThread.installContentProviders(ActivityThread.java:6528)
        at android.app.ActivityThread.installSystemProviders(ActivityThread.java:7169)
        at com.android.server.am.ActivityManagerService.installSystemProviders(ActivityManagerService.java:7545)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:1002)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:29.283 5764-5764/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "com.android.server.pm.Settings" on path: DexPathList[[zip file "/system/priv-app/LineageSettingsProvider/LineageSettingsProvider.apk"],nativeLibraryDirectories=[/system/priv-app/LineageSettingsProvider/lib/arm64, /system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
        at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:196)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:379)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:312)
        at ai.lazero.lazero.HookTest_v3.handleLoadPackage(HookTest_v3.java:25)
        at de.robv.android.xposed.IXposedHookLoadPackage$Wrapper.handleLoadPackage(IXposedHookLoadPackage.java:37)
        at de.robv.android.xposed.callbacks.XC_LoadPackage.call(XC_LoadPackage.java:61)
        at de.robv.android.xposed.callbacks.XCallback.callAll(XCallback.java:117)
        at com.elderdrivers.riru.edxp._hooker.impl.LoadedApkGetCL.afterHookedMethod(LoadedApkGetCL.java:61)
        at de.robv.android.xposed.XC_MethodHook.callAfterHookedMethod(XC_MethodHook.java:68)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:388)
        at SandHookerNew_35f4vrpdo2vmlbkhbqk0r22p8o.hook(Unknown Source:46)
        at android.app.ContextImpl.getClassLoader(ContextImpl.java:371)
        at android.app.ActivityThread.installProvider(ActivityThread.java:6965)
        at android.app.ActivityThread.installContentProviders(ActivityThread.java:6528)
        at android.app.ActivityThread.installSystemProviders(ActivityThread.java:7169)
        at com.android.server.am.ActivityManagerService.installSystemProviders(ActivityManagerService.java:7545)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:1002)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:30.582 5764-5764/system_process I/PackageManager: Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package io.animal.monkey (protectionLevel=1250 flags=0x30c8be46)
    Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:30.583 5764-5764/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package ai.lazero.lazero (protectionLevel=1250 flags=0x30c8bf46)
    Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:30.584 5764-5764/system_process I/PackageManager: Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
    Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:30.584 5764-5764/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:30.584 5764-5764/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf46)
09-17 21:44:30.584 5764-5764/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-17 21:44:30.584 5764-5764/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf46)
    Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf46)
09-17 21:44:30.620 5764-5764/system_process E/System: ************ Failure starting system services
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:30.620 5764-5764/system_process E/Zygote: System zygote died with exception
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:30.620 5764-5764/system_process E/AndroidRuntime: *** FATAL EXCEPTION IN SYSTEM PROCESS: main
    java.lang.IllegalStateException: Signature|privileged permissions not in privapp-permissions whitelist: {ai.lazero.lazero: android.permission.MOUNT_UNMOUNT_FILESYSTEMS, ai.lazero.lazero: android.permission.CAPTURE_AUDIO_OUTPUT}
        at com.android.server.pm.permission.PermissionManagerService.systemReady(PermissionManagerService.java:2970)
        at com.android.server.pm.permission.PermissionManagerService.access$100(PermissionManagerService.java:122)
        at com.android.server.pm.permission.PermissionManagerService$PermissionManagerServiceInternalImpl.systemReady(PermissionManagerService.java:3031)
        at com.android.server.pm.PackageManagerService.systemReady(PackageManagerService.java:21883)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.swift.sandhook.SandHook.callOriginMethod(SandHook.java:185)
        at com.swift.sandhook.xposedcompat.hookstub.HookStubManager.hookBridge(HookStubManager.java:375)
        at SandHookerNew_3md2db65g9mutmlhpuddt42asb.hook(Unknown Source:46)
        at com.android.server.SystemServer.startOtherServices(SystemServer.java:2037)
        at com.android.server.SystemServer.run(SystemServer.java:529)
        at com.android.server.SystemServer.main(SystemServer.java:356)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:491)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:918)
09-17 21:44:33.000 5994-5994/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-9n_TgXMS9gGpzVLxGZG3nw==/base.apk
09-17 21:44:33.418 5994-5994/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
09-17 21:44:33.419 5994-5994/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
    Loading modules from /data/app/com.oranav.ditheredholobackground-WGw3w1Oj7KB1upluOt6Kqw==/base.apk
