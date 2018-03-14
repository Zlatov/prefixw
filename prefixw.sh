#!/bin/bash
pids=$(xdotool search --class --onlyvisible "subl")
status=$?
if [[ status -eq 0 ]]
    then
        for pid in $pids; do
            name=$(xdotool getwindowname $pid)
            if [[ $name == *" Sublime Text"* ]]; then
                # Определяем индекс первого вхождения символов „(“ и „)“.
                start=`expr index "$name" '\('`
                finish=`expr index "$name" '\)'`
                # Длинна имени проекта
                let "len=finish-start-1"
                # Фиксим начало вырезания если в имени таба есть символ • (не сохранён)
                IS_FILE_NOT_SAVED=`if [[ "$name" = *"•"* ]]; then echo true; else echo false; fi;`
                if [[ "$IS_FILE_NOT_SAVED" = true ]]; then
                    let "start = $start - 2"
                fi
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
