#!/bin/bash

ssh $1 "/System/Library/Frameworks/ScreenSaver.framework/Resources/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine" & 2>&1 >/dev/null
