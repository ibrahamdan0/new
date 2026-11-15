[app]
title = IbrahemRemote
package.name = ibrahemremote
package.domain = org.control
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# تم حذف socket لأنها مكتبة مدمجة في بايثون
requirements = python3,kivy

android.permissions = INTERNET, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 34
android.minapi = 21
android.archs = arm64-v8a
