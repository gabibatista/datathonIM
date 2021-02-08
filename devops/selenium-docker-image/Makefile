# REPO_NAME = $(shell basename `git rev-parse --show-toplevel`)
REPO_NAME = prod/dextra-dna
VERSION = $(shell basename `git describe --abbrev=0`)
AWS_DEFAULT_REGION = us-east-1
AWS_ACCOUNT = 152797794397
IMAGE = $(AWS_ACCOUNT).dkr.ecr.$(AWS_DEFAULT_REGION).amazonaws.com/$(REPO_NAME):$(VERSION)
# Homolog image
REPO_NAME_HOMOLOG = homolog/dextra-dna
IMAGE_HOMOLOG = $(AWS_ACCOUNT).dkr.ecr.$(AWS_DEFAULT_REGION).amazonaws.com/$(REPO_NAME_HOMOLOG):homolog

create_repo:
	docker run --rm -it -v ~/.aws:/root/.aws -v $(pwd):/aws amazon/aws-cli:2.0.23 \
		ecr create-repository --repository-name $(REPO_NAME) >/dev/null 2>&1

check_repo:
	docker run --rm -it -v ~/.aws:/root/.aws -v $(pwd):/aws amazon/aws-cli:2.0.23 \
		ecr describe-repositories --repository-names $(REPO_NAME) >/dev/null 2>&1 || $(MAKE) create_repo >/dev/null 2>&1

ecrlogin:
	docker run --rm -it -v ~/.aws:/root/.aws -v $(pwd):/aws amazon/aws-cli:2.0.23 \
	ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $(AWS_ACCOUNT).dkr.ecr.us-east-1.amazonaws.com

build:
	docker build -t $(IMAGE) .

push: ecrlogin check_repo
	docker push $(IMAGE)

build-homolog: ecrlogin
	docker build -t $(IMAGE_HOMOLOG) .

push-homolog: ecrlogin check_repo
	docker push $(IMAGE_HOMOLOG)
