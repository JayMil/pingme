.PHONY: run
run:
	python3 ./pingme.py "pingme test message"

.PHONY: init
init:
	make -p /var/log/pingme/
	sudo chown ${USER} /var/log/pingme
	pip3 install -r requirements.txt

	
