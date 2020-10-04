default: build

build:
ifeq ($(OS), Windows_NT)
	compile.bat
else
	./compile.sh
endif
config:
ifeq ($(OS), Windows_NT)
	echo win32 >> .config
else
	echo linux >> .config
endif
	python config.py