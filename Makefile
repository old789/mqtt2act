Targa := mqtt2act
Src_files := $(Targa).head.py $(wildcard _*.py) $(Targa).main.py

all: $(Src_files)
	cat $^ > $(Targa).py
	chmod 755 $(Targa).py
	python3 -m py_compile $(Targa).py

install:
	scp $(Targa).py 192.168.1.101:

clean:
	@rm -f $(Targa).py
	@rm -fr __pycache__
