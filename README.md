# Simple Chat

## Описание

Simple Chat - простое приложение для демонстрации работы с вебсокетами. И настройки проекта.

## Требования

- Python 3.12+

- Docker (необязательно)
- Docker Compose (необязательно)


## Установка и запуск.

---

Клонировать репозиторий: 
``` bash
git clone https://github.com/username/simple-chat.git
cd simple-chat
```

### Конфигурация


Все необходимые переменные окружения для запуска уже есть в .env.example, для старта ничего настраивать не нужно, 
но вы можете их переопределить.


---

+ ### Pip:

 ### Установить зависимостей: 

#### 1. Создать виртуальное окружение:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 2. Установить зависимости:


``` bash
pip install -r requirements.txt
```

#### 3. Запуск приложения: 

```bash
cd app/
python3 main.py
```
#### или

```bash
PYTHONPATH=app python3 app/main.py
```
___

+ ### Docker Compose + Docker:



#### 1. C makefile:


Запустить приложение:

```bash
make app
```

#### Закрытие контейнера:

```bash
make app-down  
```

#### Запустить логи:

```bash
make app-logs 
```

#### Запустить командную строку:

```bash
make app-shell 
```

#### Запуск тестов:

```bash
make tests 
```

#### 2. Docker Compose:

```bash
# запустить контейнер с приложением
docker compose --env-file .env -f docker_compose/app.yaml up --build -d
```



#
