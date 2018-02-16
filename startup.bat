@echo off
cls
echo BOT WATCHDOG
echo Protecting Bot from crashes...
echo If you want to close Bot and this script, close the python window and type Y depending on your language followed by Enter.
title BOT WATCHDOG
:LOOP
echo (%time%) Bot started.
start /wait python callie-bot.py
echo (%time%) WARNING: Bot closed or crashed, restarting.
goto LOOP