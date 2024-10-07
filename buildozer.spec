[app]

# (str) Title of your application
title = WiFi Hacker App

# (str) Package name
package.name = wifi_hacker

# (str) Package domain (needed for android/ios packaging)
package.domain = org.wifi_hacker

# (str) Source directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of directory to exclude (separate by comma)
source.exclude_dirs = .direnv,.git,__pycache__,env,venv,build,dist

# (str) Application versioning (method 1)
version = 0.1

# (str) Name of the application to use when talking to the user
#osx.app_name = My Application

# (str) Application versioning (method 2)
#version.regex = __version__ = ['"](.*)['"]
#version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sphinx,git,buildozer
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.10.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE,ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 27

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 20

# (str) Android NDK version to use
android.ndk = 19b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (Google Play) or --dir public storage (default)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
# android.accept_sdk_license = False

# (str) Android entry point
#android.entrypoint = main.py

# (str) Android status bar color (black, black, white, or any other supported color)
#android.statusbar.color = black

# (list) Application requirements
#android.requires =

# (str) Icon of the application
#android.icon = @drawable/icon

# (str) Path to a custom whitelist
#android.whitelist =

# (str) Path to a custom blacklist
#android.blacklist =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AIDL
#android.add_aidl =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files =

# (list) Android AIDL
#android.add_aidl_files
