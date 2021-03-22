#!/usr/bin/env bash

theme="style"

dir="$HOME/.config/rofi/launchers/text"
styles=($(ls -p --hide="colors.rasi" $dir/styles))
color="${styles[$(( $RANDOM % 10 ))]}"


rofi -no-lazy-grab -show drun \
-modi run,drun,window \
-theme $dir/"$theme" \
-columns 2 -width 100

