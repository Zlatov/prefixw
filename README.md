# Prefixw

Заменяет стандартные заголовки окон Sublime text 3 "filePath fileName (projectName)" на имя проекта.

Это временное решение для Sublime text 3, пока разработчики не сделают подобный функционал нормальными методами.

При активации какой либо из вкладок в окне запускается выполнение скрипта на bash, меняющего заголовки окон с помощью утилиты xdotool.

## Требования

  - Linux
  - xdotool

## Установка

```
mkdir ~/.config/sublime-text-3/Packages/Prefixw
git clone https://github.com/Zlatov/prefixw.git ~/.config/sublime-text-3/Packages/Prefixw
```
