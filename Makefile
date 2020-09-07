REGISTRY ?= docker.io/bluesquanium
CORPLIST_NAME ?= corplist
CORPLIST_UPDATE_CORPCODE_NAME ?= corplist-update-corpcode
FINANCIAL_STATEMENT_NAME ?= financial-statement
VERSION ?= latest

init:
	pip install -r requirements.txt

image-corplist:
	docker build --tag $(REGISTRY)/$(CORPLIST_NAME):$(VERSION) .

image-corplist-update-corpcode:
	docker build --tag $(REGISTRY)/$(CORPLIST_UPDATE_CORPCODE_NAME):$(VERSION) .

image-financial-statement:
	docker build --tag $(REGISTRY)/$(FINANCIAL_STATEMENT_NAME):$(VERSION) .
