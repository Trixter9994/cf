#!/bin/bash
mkdir /dev/shm/xvfb
xvfb-run -f ~/.Xauthority -n 1 -s "-pixdepths 3 27 -fbdir /dev/shm/xvfb" xterm
#xvfb-run -f ~/.Xauthority -n 1 -s "-pixdepths 3 27 -fbdir /dev/shm/xvfb -listen tcp " xterm
