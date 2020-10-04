default: build

build:
ifeq ($(OS), Windows_NT)
	compile.bat
else
	chmod +x compile.sh
	./compile.sh
endif
config:
ifeq ($(OS), Windows_NT)
	echo win32 >> .config
	python config.py
else
	echo linux >> .config
	python3 config.py
endif