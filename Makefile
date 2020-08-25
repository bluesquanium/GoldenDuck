CORPLIST_NAME ?= corplist
VERSION ?= latest

init:
	pip install -r requirements.txt

image-corplist:
	docker build --tag $(CORPLIST_NAME):$(VERSION) .
