#����� ����������� � ����������
���������� ������� � ���������� python (3.5-3.7)
#����������:
```
git clone https://github.com/RuslanUC/TwitchOnlineNotifyer
cd TwitchOnlineNotifyer
pip install requests plyer
make config
make
```
����� ���������� ������� ��������� ����� � ����� dist, � ���-�� ��� �������� � ����� ����� � ��� ������ ���� ���� icon.ico
#��������� ������ ��� ������������
�������� Client-ID ����� ���: https://dev.twitch.tv/console/extensions/create
� ID �������� ����� ��������, �������� curl ������:
```
curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: ��� CLIENT-ID' \
-X GET https://api.twitch.tv/kraken/users?login=����� ��������
```
���� ������ ����� ��������� �� ����� https://reqbin.com/curl
#���������� � ���������
![Cloning the repo](/images/01_clone.png)
![CD](/images/02_cd.png)
![Configuring](/images/03_config.png)
![Building](/images/04_build.png)
![Done](/images/05_done.png)
![Copying icon](/images/06_copy.png)