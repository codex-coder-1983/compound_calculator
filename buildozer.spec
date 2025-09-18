[app]
title = Compounding Calculator
package.name = calculator
package.domain = org.example
version = 0.1

# Use GitHub runner’s installed Android SDK/NDK
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/android-ndk-r25b
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
verbose = 1

# Tell buildozer to look in cmdline-tools (not tools/bin which doesn’t exist anymore)
bin_path = /home/runner/android-sdk/cmdline-tools/latest/bin:/home/runner/android-sdk/platform-tools
