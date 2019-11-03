import sys
import json
import time
import ctypes
import requests
import platform
from plyer import notification
if sys.platform != "win32":
	exit("Данная программа работает только на Windows!")
headers = {
	'Accept': 'application/vnd.twitchtv.v5+json',
	'Client-ID': 'ВАШ CLIENT-ID',
}
winver = platform.win32_ver()[0]
while True:
	response = requests.get('https://api.twitch.tv/kraken/streams/ID СТРИМЕРА', headers=headers)
	js = json.loads(response.text)
	status = js['stream']
	if status == None:
		print("Stream offline")
	else:
		print("Stream online")
		if winver == "10":
			notification.notify(
				title='*Streamer* онлайн!',
				message='*Streamer* запустим стрим!',
				app_name='TwitchOnline',
				app_icon='icon.ico'
			)
		else:
			print("Windows notifications not available")
			ctypes.windll.user32.MessageBoxW(0, "*Streamer* запустил стрим!", "TwitchOnline", 1)
		break
	time.sleep(1)
sys.exit()