09-18 15:30:56.987 14896-14896/system_process I/PackageManager: Un-granting permission android.permission.SYSTEM_ALERT_WINDOW from package io.animal.monkey (protectionLevel=1250 flags=0x30c8be46)
    Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
09-18 15:30:56.988 14896-14896/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
    Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
    Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
09-18 15:30:56.989 14896-14896/system_process I/PackageManager: Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
    Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
    Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
09-18 15:30:56.989 14896-14896/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-18 15:30:56.989 14896-14896/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf47)
09-18 15:30:56.989 14896-14896/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-18 15:30:56.990 14896-14896/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf47)
    Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
09-18 15:30:57.033 14896-14896/system_process E/System: ******************************************
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
09-18 15:30:57.033 14896-14896/system_process E/Zygote: System zygote died with exception
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
09-18 15:30:57.033 14896-14896/system_process E/AndroidRuntime: *** FATAL EXCEPTION IN SYSTEM PROCESS: main
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
09-18 15:30:59.865 15127-15127/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-GPFZ_Mc01IseRfNOtSvzmQ==/base.apk
09-18 15:31:03.344 15328-15328/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
    Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
09-18 15:31:03.345 15328-15328/system_process I/PackageManager: Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
    Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
    Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
    Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
09-18 15:31:03.346 15328-15328/system_process I/PackageManager: Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
09-18 15:31:03.346 15328-15328/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-18 15:31:03.346 15328-15328/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x3048bf47)
09-18 15:31:03.346 15328-15328/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-18 15:31:03.346 15328-15328/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x3048bf47)
    Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
09-18 15:31:05.387 15328-15328/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
    Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
09-18 15:31:05.388 15328-15328/system_process I/PackageManager: Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
    Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
    Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
09-18 15:31:05.389 15328-15328/system_process I/PackageManager: Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
    Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
09-18 15:31:05.389 15328-15328/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-18 15:31:05.389 15328-15328/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf47)
09-18 15:31:05.389 15328-15328/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-18 15:31:05.389 15328-15328/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf47)
    Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
09-18 15:31:05.433 15328-15328/system_process E/System: ******************************************
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
09-18 15:31:05.434 15328-15328/system_process E/Zygote: System zygote died with exception
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
09-18 15:31:05.434 15328-15328/system_process E/AndroidRuntime: *** FATAL EXCEPTION IN SYSTEM PROCESS: main
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
09-18 15:31:08.161 15559-15559/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-GPFZ_Mc01IseRfNOtSvzmQ==/base.apk
09-18 15:31:11.413 15760-15760/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
    Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
09-18 15:31:11.414 15760-15760/system_process I/PackageManager: Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
    Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
    Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
    Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
09-18 15:31:11.415 15760-15760/system_process I/PackageManager: Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
09-18 15:31:11.415 15760-15760/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-18 15:31:11.415 15760-15760/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x3048bf47)
09-18 15:31:11.415 15760-15760/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-18 15:31:11.415 15760-15760/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x3048bf47)
    Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x3048bf47)
09-18 15:31:13.600 15760-15760/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_SECURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
    Un-granting permission android.permission.CAPTURE_VIDEO_OUTPUT from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
09-18 15:31:13.601 15760-15760/system_process I/PackageManager: Un-granting permission android.permission.INTERNAL_SYSTEM_WINDOW from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
    Un-granting permission android.permission.BIND_DEVICE_ADMIN from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
    Un-granting permission android.permission.BIND_ACCESSIBILITY_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
09-18 15:31:13.602 15760-15760/system_process I/PackageManager: Un-granting permission android.permission.DEVICE_POWER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
    Un-granting permission android.permission.READ_FRAME_BUFFER from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
09-18 15:31:13.602 15760-15760/system_process W/PackageManager: Privileged permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS for package ai.lazero.lazero - not in privapp-permissions whitelist
09-18 15:31:13.602 15760-15760/system_process I/PackageManager: Un-granting permission android.permission.MOUNT_UNMOUNT_FILESYSTEMS from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf47)
09-18 15:31:13.602 15760-15760/system_process W/PackageManager: Privileged permission android.permission.CAPTURE_AUDIO_OUTPUT for package ai.lazero.lazero - not in privapp-permissions whitelist
09-18 15:31:13.602 15760-15760/system_process I/PackageManager: Un-granting permission android.permission.CAPTURE_AUDIO_OUTPUT from package ai.lazero.lazero (protectionLevel=18 flags=0x30c8bf47)
    Un-granting permission android.permission.BIND_JOB_SERVICE from package ai.lazero.lazero (protectionLevel=2 flags=0x30c8bf47)
09-18 15:31:13.644 15760-15760/system_process E/System: ******************************************
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
09-18 15:31:13.644 15760-15760/system_process E/Zygote: System zygote died with exception
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
09-18 15:31:13.644 15760-15760/system_process E/AndroidRuntime: *** FATAL EXCEPTION IN SYSTEM PROCESS: main
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
09-18 15:31:16.453 15990-15990/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-GPFZ_Mc01IseRfNOtSvzmQ==/base.apk