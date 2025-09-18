[app]
title = Compounding Calculator
package.name = calculator
package.domain = org.example
version = 0.1

# Use GitHub runner’s preinstalled SDK/NDK
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724
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
