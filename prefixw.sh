#!/bin/bash
pids=$(xdotool search --class --onlyvisible "subl")
for pid in $pids; do
    name=$(xdotool getwindowname $pid)
    if [[ $name == *" Sublime Text"* ]]; then
        start=`expr index "$name" '\('`
        finish=`expr index "$name" '\)'`
        let "len=finish-start-1"
        newTitle=${name:start:len}
        xdotool set_window --name "$newTitle" "$pid"
    fi
done
