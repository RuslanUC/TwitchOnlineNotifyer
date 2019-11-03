Set pathBat=%~dp0TwitchOnlineNotifyer.exe
Reg Add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "TwitchOnlineNotifyer" /t REG_SZ /d "%pathBat%" /f
del AutoStart.bat