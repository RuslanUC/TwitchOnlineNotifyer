import sys
import argparse

if sys.platform != "win32":
	exit("Данная программа работает только на Windows!")

cid = input("Client ID: ")
sid = input("Streamer ID: ")
sn = input("Streamer Nickname: ")
try:
	winver = int(input("Windows version: "))
except:
	winver = 7

f = open("main.py", "w", encoding="utf-8")
f.write("import sys\n")
f.write("import json\n")
f.write("import time\n")
f.write("import ctypes\n")
f.write("import requests\n")
f.write("import platform\n")
f.write("from plyer import notification\n")
f.write("\n")
f.write("client_id = '"+cid+"'\n")
f.write("streamer_id = '"+sid+"'\n")
f.write("streamer_nickname = '"+sn+"'\n")
f.write("\n")
f.write("headers = {\n")
f.write("	'Accept': 'application/vnd.twitchtv.v5+json',\n")
f.write("	'Client-ID': client_id,\n")
f.write("}\n")
f.write("while True:\n")
f.write("	response = requests.get('https://api.twitch.tv/kraken/streams/' + streamer_id, headers=headers)\n")
f.write("	js = json.loads(response.text)\n")
f.write("	status = js['stream']\n")
f.write("	if status != None:\n")
if winver == 10:
	f.write("		notification.notify(\n")
	f.write("			title=streamer_nickname + ' онлайн!',\n")
	f.write("			message=streamer_nickname + ' запустил стрим!',\n")
	f.write("			app_name='TwitchOnline',\n")
	f.write("			app_icon='icon.ico'\n")
	f.write("		)\n")
else:
	f.write("		ctypes.windll.user32.MessageBoxW(0, streamer_nickname + ' запустил стрим!', 'TwitchOnline', 1)\n")
f.write("		break\n")
f.write("	time.sleep(3)\n")
f.write("time.sleep(30)\n")
f.write("sys.exit()\n")
f.close()