���� �� ������������ ������ �� ��������� ��������� pyinstaller, ������� ��� ���������� ������ ��������� ���:

pyinstaller main.py --icon=icon.ico --hidden-import=plyer --hidden-import=plyer.platforms --hidden-import=plyer.platforms.win --hidden-import=plyer.platforms.win.notification

����� ���� � ����� � ������� exe ������ ����� ��������� ���� icon.ico

���-�� ���-�� ���������������� ���� ��������� ��������, � �������������� ����� �������� ��� Client-ID (12 ������), ID �������� (16 ������) � ����� �������� (25, 26 � 32 ������).
�������� Client-ID ����� ���: https://dev.twitch.tv/console/extensions/create
� ID �������� ����� ��������, �������� curl ������:

curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: ��� CLIENT-ID' \
-X GET https://api.twitch.tv/kraken/users?login=����� ��������

���� ��� ����� ��������� �� ����� https://onlinecurl.com/, � ���������� JSON ����� �������� � ����������� ��� � ������� http://chris.photobooks.com/json/default.htm
