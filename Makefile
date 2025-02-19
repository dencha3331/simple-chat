DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = simple_chat
ENV = --env-file .env

.PHONY: app
app:
	${DC} ${ENV} -f ${APP_FILE} up --build -d

.PHONY: app-down
app-down:
	${DC} ${ENV} -f ${APP_FILE} down

.PHONY: app-shell
app-shell:
	${EXEC} ${APP_CONTAINER} bash

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: test
test:
	${EXEC} ${APP_CONTAINER} pytest -v -s