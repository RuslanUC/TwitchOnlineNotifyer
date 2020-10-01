default: build

build:
	pyinstaller main.py --icon=icon.ico --hidden-import=plyer --hidden-import=plyer.platforms --hidden-import=plyer.platforms.win --hidden-import=plyer.platforms.win.notification -F --noconsole
config:
	python config.py