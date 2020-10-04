# Оглавление
0. [Перед компиляцией и установкой](#Перед-компиляцией-и-установкой)
1. [Получение Client-ID и Streamer-ID](#Получение-Client-ID-и-Streamer-ID)
2. [Компиляция](#Компиляция)
3. [Инструкция в картинках для Windows](#Инструкция-в-картинках-для-Windows)
4. [Инструкция в картинках для Linux](#Инструкция-в-картинках-для-Linux)
____
# Перед компиляцией и установкой
Необходимо скачать и установить python (3.5-3.7)
____
# Получение Client-ID и Streamer-ID
Получить Client-ID можно тут: https://dev.twitch.tv/console/extensions/create
А ID стримера можно получить, выполнив curl запрос:
```
curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: ВАШ CLIENT-ID' \
-X GET https://api.twitch.tv/kraken/users?login=ЛОГИН СТРИМЕРА
```
Этот запрос можно выполнить на сайте https://reqbin.com/curl
____
# Компиляция:
```
git clone https://github.com/RuslanUC/TwitchOnlineNotifyer
cd TwitchOnlineNotifyer
pip install -r requirements.txt
make config
make
```
После компиляции готовая программа будет в папке dist, и что-бы она работала в одной папке с ней должен быть файл icon.ico (только для windows)
____
# Инструкция в картинках для Windows
![Cloning the repo](/images/win/01_clone.png)
![CD](/images/win/02_cd.png)
![Configuring](/images/win/03_config.png)
![Building](/images/win/04_build.png)
![Done](/images/win/05_done.png)
![Copying icon](/images/win/06_copy.png)
____
# Инструкция в картинках для Linux
![Cloning the repo](/images/linux/01_clone.png)
![CD](/images/linux/02_cd.png)
![Configuring](/images/linux/03_config.png)
![Building](/images/linux/04_build.png)
![Done](/images/linux/05_done.png)