# FastAPI ML Template
## Run Web API
### Local

```sh
$ sh run.sh
#   poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 9000
```

### Docker
```sh
$ docker build -f Dockerfile -t fastapi-ml .
$ docker run -p 9000:9000 --rm --name fastapi-ml -t -i fastapi-ml
```

### Docker Compose

```sh
$ docker compose up --build
```

## Request Commands

```sh 
$ curl --request POST --url http://127.0.0.1:8000/api/v1/predict --header 'Content-Type: application/json' --data '{"input_text": "test"}'
```

```sh
$ http POST http://127.0.0.1:8000/api/v1/predict input_text=テスト
```

## Development
### Run Tests and Linter

```
$ poetry run tox
```