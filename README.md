# csg5-chatacademico-python

## 🛠 Getting Started

To run this project you need to install the prerequisites:

[Python](https://python.org/) `v3.8`
[Poetry](https://python-poetry.org/docs/)

## ⚙️ Installation

##### Clone the repository

```bash
git clone  git@github.com:PUCRSteam/csg5-chatacademico-python.git
cd csg5-chatacademico-python
```

##### Install dependencies

```bash
poetry install
```

##### Create a file called `.env` in the root directory

```bash
touch .env
```

##### Set up environment variables as shown below

```
FLASK_DEBUG=1
DB_ENGINE=
DB_HOST=
DB_USERNAME=
DB_PASSWORD=
DB_PORT=
DB_NAME=
```

## Setup postgres database

```bash
docker pull postgress
docker run -p 5432:5432 -v /tmp/database:/var/lib/postgresql/data -e POSTGRES_PASSWORD=1234 -d postgres
```

## 🚀 Run

After installing process you just need to run in develop mode

```bash
poetry shell # Access poetry's terminal
gunicorn --worker-class eventlet -w 1 "app:create_app()"
```

# ☕