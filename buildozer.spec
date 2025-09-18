[app]
title = Compounding Calculator
package.name = calculator
package.domain = org.example
version = 0.1

# Force Buildozer to use manually installed SDK/NDK
android.sdk_path = $HOME/android-sdk
android.ndk_path = $HOME/android-sdk/android-ndk-r25b
android.ndk_api = 21

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
