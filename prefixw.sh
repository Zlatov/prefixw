#!/bin/bash
pids=$(xdotool search --class --onlyvisible "subl")
status=$?
if [[ status -eq 0 ]]
    then
        for pid in $pids; do
            name=$(xdotool getwindowname $pid)
            if [[ $name == *" Sublime Text"* ]]; then
                start=`expr index "$name" '\('`
                finish=`expr index "$name" '\)'`
                let "len=finish-start-1"
                newTitle=${name:start:len}
                size=${#newTitle}
                if [[ $size -gt 0 ]]; then
                    xdotool set_window --name "$newTitle" "$pid"
                fi
            fi
        done
        echo "done"
    else
        echo "It may need a xdotool, use apt-get install xdotool"
fi
