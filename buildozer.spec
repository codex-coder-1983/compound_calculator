[app]
# App details
title = My Kivy App
package.name = mykivyapp
package.domain = org.example

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
android.ndk = 23b
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
