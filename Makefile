REGISTRY ?= docker.io/bluesquanium
CORPLIST_NAME ?= corplist
VERSION ?= latest

init:
	pip install -r requirements.txt

image-corplist:
	docker build --tag $(REGISTRY)/$(CORPLIST_NAME):$(VERSION) .
