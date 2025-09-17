[app]
# App details
title = Compounding Calculator
package.name = calculator
package.domain = org.example
version = 0.1

# Force Buildozer to use the modern SDK/NDK path
android.sdk_path = $HOME/android-sdk
android.ndk_path = $HOME/.buildozer/android/platform/android-ndk-r25b
android.ndk_api = 21

# The main .py file
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# App requirements
requirements = python3,kivy

# (str) Supported orientation (one of: landscape, portrait, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# Android specific
android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
