Если вы компилируете проект из исходника используя pyinstaller, команда для компиляции должна выглядеть так:
pyinstaller main.py --icon=icon.ico --hidden-import=plyer --hidden-import=plyer.platforms --hidden-import=plyer.platforms.win --hidden-import=plyer.platforms.win.notification

После чего в папку с готовым exe файлом нужно поместить файл icon.ico

Так-же что-бы скомпилированная вами программа работала, в соответсвующие места вставьте ваш Client-ID (12 строка), ID стримера (16 строка) и логин стримера (25, 26 и 32 строки).

Получить Client-ID можно тут: https://dev.twitch.tv/console/extensions/create

А ID стримера можно получить, выполнив curl запрос:


curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: ВАШ CLIENT-ID' \
-X GET https://api.twitch.tv/kraken/users?login=ЛОГИН_СТРИМЕРА


Этот код можно выполнить на сайте https://onlinecurl.com/, а полученный JSON можно привести в читабельный вид с помощью http://chris.photobooks.com/json/default.htm
