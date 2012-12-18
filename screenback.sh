#!/bin/bash
ssh $1 "killall ScreenSaverEngine" & 2>&1 >/dev/null
