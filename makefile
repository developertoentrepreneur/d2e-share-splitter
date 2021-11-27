COVERAGE = 0
DOCKER_LOCAL = -f local.yml
CONTAINER_BACKEND = django

ifeq (${COVERAGE}, 1)
COVERAGE_CONFIG = --cov --cov-config=.coveragerc
endif

bash:
	docker exec -it $(CONTAINER_BACKEND) sh

db-migrate:
	docker exec -it $(CONTAINER_BACKEND) bash -c "python manage.py makemigrations && python manage.py migrate"

local:
	# start develop environment
	docker-compose $(DOCKER_LOCAL) up ${ARGS}

local-build:
	# build docker images of the develop environment
	# add environment COMPOSE_DOCKER_CLI_BUILD and DOCKER_BUILDKIT to use the new docker build image engine
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose $(DOCKER_LOCAL) build ${ARGS}

test-all:
	docker exec -it $(CONTAINER_BACKEND) bash -c "pytest ${APP} -svv --reuse-db ${COVERAGE_CONFIG} --ds=config.settings.test"