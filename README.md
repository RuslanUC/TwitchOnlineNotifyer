#Перед компиляцией и установкой
Необходимо скачать и установить python (3.5-3.7)
#Компиляция:
```
git clone https://github.com/RuslanUC/TwitchOnlineNotifyer
cd TwitchOnlineNotifyer
pip install requests plyer
make config
make
```
После компиляции готовая программа будет в папке dist, и что-бы она работала в одной папке с ней должен быть файл icon.ico
#Получение данных для конфигурации
Получить Client-ID можно тут: https://dev.twitch.tv/console/extensions/create
А ID стримера можно получить, выполнив curl запрос:
```
curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: ВАШ CLIENT-ID' \
-X GET https://api.twitch.tv/kraken/users?login=ЛОГИН СТРИМЕРА
```
Этот запрос можно выполнить на сайте https://reqbin.com/curl
#Инструкция в картинках
![Cloning the repo](/images/01_clone.png)
![CD](/images/02_cd.png)
![Configuring](/images/03_config.png)
![Building](/images/04_build.png)
![Done](/images/05_done.png)
![Copying icon](/images/06_copy.png)