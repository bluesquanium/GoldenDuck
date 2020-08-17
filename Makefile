CORPLIST_NAME ?= corplist
VERSION ?= latest

init:
	pip install -r requirements.txt

images-corplist:
	docker build --tag $(CORPLIST_NAME):$(VERSION) ./dockerfiles/corplist/
