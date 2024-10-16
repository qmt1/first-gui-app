
PYTHON = python3
APP = main.py 

all: run

run:
	$(PYTHON) $(APP)

clean:
	rm -rf __pycache__