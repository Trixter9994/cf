09-19 00:10:56.486 765-765/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-8y2xge8uLmrhBt8pzNcgVA==/base.apk
09-19 00:10:56.871 765-765/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
      Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
09-19 00:10:56.872 765-765/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v0
    Loading modules from /data/app/com.oranav.ditheredholobackground-WGw3w1Oj7KB1upluOt6Kqw==/base.apk
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
09-19 00:10:59.277 1841-1841/system_process E/PackageManager: Bad package setting: package ai.lazero.lazero has shared uid 10171 that is not defined
09-19 00:10:59.279 1841-1841/system_process W/PackageManager: No package known for stopped package ai.lazero.lazero
09-19 00:10:59.559 1841-1841/system_process W/PackageManager: Package ai.lazero.lazero shared user changed from <nothing> to ai.lazero.lazero; replacing with new
09-19 00:11:01.635 1982-1982/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-8y2xge8uLmrhBt8pzNcgVA==/base.apk
09-19 00:11:02.017 1982-1982/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
09-19 00:11:02.018 1982-1982/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
      Loading class ai.lazero.lazero.HookTest_v0
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
09-19 00:11:04.049 2193-2193/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
    Permission UID method has Hooked! android.uid.phone
    Permission UID method has Hooked! android.uid.log
    Permission UID method has Hooked! android.uid.nfc
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! android.uid.shell
    Permission UID method has Hooked! android.uid.se
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
09-19 00:11:04.156 2193-2193/system_process E/PackageManager: Bad package setting: package ai.lazero.lazero has shared uid 10171 that is not defined
09-19 00:11:04.157 2193-2193/system_process W/PackageManager: No package known for stopped package ai.lazero.lazero
09-19 00:11:04.351 2193-2193/system_process W/PackageManager: Package ai.lazero.lazero shared user changed from <nothing> to ai.lazero.lazero; replacing with new
09-19 00:11:06.775 2254-2254/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-8y2xge8uLmrhBt8pzNcgVA==/base.apk
09-19 00:11:07.193 2254-2254/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
09-19 00:11:07.194 2254-2254/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
      Loading class ai.lazero.lazero.HookTest_v0
09-19 00:11:09.113 2463-2463/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "android.content.pm.PackageParser.Package" on path: DexPathList[[zip file "/system/framework/org.lineageos.platform.jar", zip file "/system/framework/services.jar", zip file "/system/framework/ethernet-service.jar", zip file "/system/framework/wifi-service.jar", zip file "/system/framework/com.android.location.provider.jar"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
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
09-19 00:11:09.349 2463-2463/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
    Permission UID method has Hooked! android.uid.phone
    Permission UID method has Hooked! android.uid.log
    Permission UID method has Hooked! android.uid.nfc
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! android.uid.shell
    Permission UID method has Hooked! android.uid.se
    Permission UID method has Hooked! android.uid.networkstack
09-19 00:11:09.451 2463-2463/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
09-19 00:11:09.451 2463-2463/system_process E/PackageManager: Adding duplicate shared user, keeping first: ai.lazero.lazero
09-19 00:11:09.452 2463-2463/system_process E/PackageManager: Occurred while parsing settings at START_TAG <shared-user name='ai.lazero.lazero' userId='10171'>@7454:57 in java.io.InputStreamReader@f453a06
09-19 00:11:09.453 2463-2463/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.system
    PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-19 00:11:09.461 2463-2463/system_process E/PackageManager: Bad package setting: package ai.lazero.lazero has shared uid 10171 that is not defined
09-19 00:11:09.462 2463-2463/system_process W/PackageManager: No package known for stopped package ai.lazero.lazero
09-19 00:11:09.757 2463-2463/system_process W/PackageManager: Package ai.lazero.lazero shared user changed from <nothing> to ai.lazero.lazero; replacing with new
09-19 00:11:12.035 2522-2522/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-8y2xge8uLmrhBt8pzNcgVA==/base.apk
09-19 00:11:12.453 2522-2522/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
      Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
09-19 00:11:12.454 2522-2522/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v0
    Loading modules from /data/app/com.oranav.ditheredholobackground-WGw3w1Oj7KB1upluOt6Kqw==/base.apk
09-19 00:11:14.323 2723-2723/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "android.content.pm.PackageParser.Package" on path: DexPathList[[zip file "/system/framework/org.lineageos.platform.jar", zip file "/system/framework/services.jar", zip file "/system/framework/ethernet-service.jar", zip file "/system/framework/wifi-service.jar", zip file "/system/framework/com.android.location.provider.jar"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
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
    java.lang.NullPointerException: Attempt to read from field 'int android.content.pm.ApplicationInfo.flags' on a null object reference
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
09-19 00:11:14.640 2723-2723/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
    Permission UID method has Hooked! android.uid.phone
    Permission UID method has Hooked! android.uid.log
    Permission UID method has Hooked! android.uid.nfc
    Permission UID method has Hooked! android.uid.bluetooth
09-19 00:11:14.747 2723-2723/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! ai.lazero.lazero
09-19 00:11:14.747 2723-2723/system_process E/PackageManager: Adding duplicate shared user, keeping first: ai.lazero.lazero
09-19 00:11:14.748 2723-2723/system_process E/PackageManager: Occurred while parsing settings at START_TAG <shared-user name='ai.lazero.lazero' userId='10171'>@7454:57 in java.io.InputStreamReader@d0032fd
09-19 00:11:14.749 2723-2723/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.system
    PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-19 00:11:14.757 2723-2723/system_process E/PackageManager: Bad package setting: package ai.lazero.lazero has shared uid 10171 that is not defined
09-19 00:11:14.758 2723-2723/system_process W/PackageManager: No package known for stopped package ai.lazero.lazero
09-19 00:11:14.953 2723-2723/system_process W/PackageManager: Package ai.lazero.lazero shared user changed from <nothing> to ai.lazero.lazero; replacing with new
09-19 00:11:17.230 2781-2781/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-8y2xge8uLmrhBt8pzNcgVA==/base.apk
09-19 00:11:17.647 2781-2781/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
09-19 00:11:17.648 2781-2781/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
      Loading class ai.lazero.lazero.HookTest_v0
09-19 00:11:19.447 2984-2984/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "android.content.pm.PackageParser.Package" on path: DexPathList[[zip file "/system/framework/org.lineageos.platform.jar", zip file "/system/framework/services.jar", zip file "/system/framework/ethernet-service.jar", zip file "/system/framework/wifi-service.jar", zip file "/system/framework/com.android.location.provider.jar"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
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
09-19 00:11:19.784 2984-2984/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-19 00:11:19.886 2984-2984/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! ai.lazero.lazero
09-19 00:11:19.886 2984-2984/system_process E/PackageManager: Adding duplicate shared user, keeping first: ai.lazero.lazero
09-19 00:11:19.887 2984-2984/system_process E/PackageManager: Occurred while parsing settings at START_TAG <shared-user name='ai.lazero.lazero' userId='10171'>@7454:57 in java.io.InputStreamReader@9c1641b
09-19 00:11:19.888 2984-2984/system_process I/EdXposed-Bridge: PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-19 00:11:19.895 2984-2984/system_process E/PackageManager: Bad package setting: package ai.lazero.lazero has shared uid 10171 that is not defined
09-19 00:11:19.897 2984-2984/system_process W/PackageManager: No package known for stopped package ai.lazero.lazero
09-19 00:11:20.169 2984-2984/system_process W/PackageManager: Package ai.lazero.lazero shared user changed from <nothing> to ai.lazero.lazero; replacing with new
09-19 00:11:22.480 3043-3043/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-8y2xge8uLmrhBt8pzNcgVA==/base.apk
09-19 00:11:22.899 3043-3043/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
09-19 00:11:22.900 3043-3043/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
      Loading class ai.lazero.lazero.HookTest_v0
    Loading modules from /data/app/com.oranav.ditheredholobackground-WGw3w1Oj7KB1upluOt6Kqw==/base.apk
09-19 00:11:24.833 3243-3243/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "android.content.pm.PackageParser.Package" on path: DexPathList[[zip file "/system/framework/org.lineageos.platform.jar", zip file "/system/framework/services.jar", zip file "/system/framework/ethernet-service.jar", zip file "/system/framework/wifi-service.jar", zip file "/system/framework/com.android.location.provider.jar"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
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
09-19 00:11:25.052 3243-3243/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
    Permission UID method has Hooked! android.uid.phone
    Permission UID method has Hooked! android.uid.log
    Permission UID method has Hooked! android.uid.nfc
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! android.uid.shell
    Permission UID method has Hooked! android.uid.se
    Permission UID method has Hooked! android.uid.networkstack
09-19 00:11:25.155 3243-3243/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.se
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! ai.lazero.lazero
09-19 00:11:25.155 3243-3243/system_process E/PackageManager: Adding duplicate shared user, keeping first: ai.lazero.lazero
09-19 00:11:25.156 3243-3243/system_process E/PackageManager: Occurred while parsing settings at START_TAG <shared-user name='ai.lazero.lazero' userId='10171'>@7454:57 in java.io.InputStreamReader@1bce12d
09-19 00:11:25.157 3243-3243/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.shared
    Permission UID method has Hooked! android.uid.system
    PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-19 00:11:25.165 3243-3243/system_process E/PackageManager: Bad package setting: package ai.lazero.lazero has shared uid 10171 that is not defined
09-19 00:11:25.166 3243-3243/system_process W/PackageManager: No package known for stopped package ai.lazero.lazero
09-19 00:11:25.398 3243-3243/system_process W/PackageManager: Package ai.lazero.lazero shared user changed from <nothing> to ai.lazero.lazero; replacing with new
09-19 00:11:27.691 3301-3301/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-8y2xge8uLmrhBt8pzNcgVA==/base.apk
09-19 00:11:28.109 3301-3301/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
      Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
09-19 00:11:28.110 3301-3301/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v0
    Loading modules from /data/app/com.oranav.ditheredholobackground-WGw3w1Oj7KB1upluOt6Kqw==/base.apk
09-19 00:11:30.037 3501-3501/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "android.content.pm.PackageParser.Package" on path: DexPathList[[zip file "/system/framework/org.lineageos.platform.jar", zip file "/system/framework/services.jar", zip file "/system/framework/ethernet-service.jar", zip file "/system/framework/wifi-service.jar", zip file "/system/framework/com.android.location.provider.jar"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
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
09-19 00:11:30.279 3501-3501/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
    Permission UID method has Hooked! android.uid.phone
    Permission UID method has Hooked! android.uid.log
    Permission UID method has Hooked! android.uid.nfc
    Permission UID method has Hooked! android.uid.bluetooth
09-19 00:11:30.384 3501-3501/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! ai.lazero.lazero
09-19 00:11:30.384 3501-3501/system_process E/PackageManager: Adding duplicate shared user, keeping first: ai.lazero.lazero
09-19 00:11:30.385 3501-3501/system_process E/PackageManager: Occurred while parsing settings at START_TAG <shared-user name='ai.lazero.lazero' userId='10171'>@7454:57 in java.io.InputStreamReader@62f2933
09-19 00:11:30.386 3501-3501/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.system
    PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-19 00:11:30.394 3501-3501/system_process E/PackageManager: Bad package setting: package ai.lazero.lazero has shared uid 10171 that is not defined
09-19 00:11:30.396 3501-3501/system_process W/PackageManager: No package known for stopped package ai.lazero.lazero
09-19 00:11:30.726 3501-3501/system_process W/PackageManager: Package ai.lazero.lazero shared user changed from <nothing> to ai.lazero.lazero; replacing with new
09-19 00:11:33.035 3559-3559/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-8y2xge8uLmrhBt8pzNcgVA==/base.apk
09-19 00:11:33.452 3559-3559/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
09-19 00:11:33.453 3559-3559/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
      Loading class ai.lazero.lazero.HookTest_v0
    Loading modules from /data/app/com.oranav.ditheredholobackground-WGw3w1Oj7KB1upluOt6Kqw==/base.apk
09-19 00:11:35.263 3761-3761/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "android.content.pm.PackageParser.Package" on path: DexPathList[[zip file "/system/framework/org.lineageos.platform.jar", zip file "/system/framework/services.jar", zip file "/system/framework/ethernet-service.jar", zip file "/system/framework/wifi-service.jar", zip file "/system/framework/com.android.location.provider.jar"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
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
09-19 00:11:35.607 3761-3761/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
09-19 00:11:35.718 3761-3761/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
09-19 00:11:35.718 3761-3761/system_process E/PackageManager: Adding duplicate shared user, keeping first: ai.lazero.lazero
    Occurred while parsing settings at START_TAG <shared-user name='ai.lazero.lazero' userId='10171'>@7454:57 in java.io.InputStreamReader@718f947
09-19 00:11:35.719 3761-3761/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.shared
    Permission UID method has Hooked! android.uid.system
    PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-19 00:11:35.727 3761-3761/system_process E/PackageManager: Bad package setting: package ai.lazero.lazero has shared uid 10171 that is not defined
09-19 00:11:35.729 3761-3761/system_process W/PackageManager: No package known for stopped package ai.lazero.lazero
09-19 00:11:36.014 3761-3761/system_process W/PackageManager: Package ai.lazero.lazero shared user changed from <nothing> to ai.lazero.lazero; replacing with new
09-19 00:11:38.348 3818-3818/? I/EdXposed-Bridge: Loading modules from /data/app/ai.lazero.lazero-8y2xge8uLmrhBt8pzNcgVA==/base.apk
09-19 00:11:38.765 3818-3818/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest
09-19 00:11:38.766 3818-3818/? I/EdXposed-Bridge:   Loading class ai.lazero.lazero.HookTest_v2
      Loading class ai.lazero.lazero.HookTest_v3
      Loading class ai.lazero.lazero.HookTest_v0
09-19 00:11:40.718 4019-4019/system_process E/EdXposed-Bridge: java.lang.ClassNotFoundException: Didn't find class "android.content.pm.PackageParser.Package" on path: DexPathList[[zip file "/system/framework/org.lineageos.platform.jar", zip file "/system/framework/services.jar", zip file "/system/framework/ethernet-service.jar", zip file "/system/framework/wifi-service.jar", zip file "/system/framework/com.android.location.provider.jar"],nativeLibraryDirectories=[/system/lib64, /system/product/lib64, /vendor/lib64, /system/lib64, /system/product/lib64, /vendor/lib64]]
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
09-19 00:11:40.927 4019-4019/system_process I/EdXposed-Bridge: Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
    Permission UID method has Hooked! android.uid.phone
    Permission UID method has Hooked! android.uid.log
    Permission UID method has Hooked! android.uid.nfc
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! android.uid.shell
    Permission UID method has Hooked! android.uid.se
09-19 00:11:41.034 4019-4019/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.se
    Permission UID method has Hooked! android.uid.bluetooth
    Permission UID method has Hooked! ai.lazero.lazero
09-19 00:11:41.034 4019-4019/system_process E/PackageManager: Adding duplicate shared user, keeping first: ai.lazero.lazero
09-19 00:11:41.035 4019-4019/system_process E/PackageManager: Occurred while parsing settings at START_TAG <shared-user name='ai.lazero.lazero' userId='10171'>@7454:57 in java.io.InputStreamReader@7514f39
09-19 00:11:41.036 4019-4019/system_process I/EdXposed-Bridge: Permission UID method has Hooked! android.uid.shared
    Permission UID method has Hooked! android.uid.system
    PM has Hooked!
    Permission UID method has Hooked! ai.lazero.lazero
    Somehow Executed.
    Try Block Executed.
09-19 00:11:41.044 4019-4019/system_process E/PackageManager: Bad package setting: package ai.lazero.lazero has shared uid 10171 that is not defined
09-19 00:11:41.046 4019-4019/system_process W/PackageManager: No package known for stopped package ai.lazero.lazero
09-19 00:11:41.272 4019-4019/system_process W/PackageManager: Package ai.lazero.lazero shared user changed from <nothing> to ai.lazero.lazero; replacing with new
