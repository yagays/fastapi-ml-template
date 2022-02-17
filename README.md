# FastAPI ML Template

I wrote a blog post about this repository in Japanese.

[機械学習の推論WebAPIの実装をテンプレート化して使い回せるようした](https://zenn.dev/yag_ays/articles/eef1a8c8e1ee39)

## Run Web API
### Local

```sh
$ sh run.sh
```

```sh
$ poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 9000
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
$ curl --request POST --url http://127.0.0.1:9000/api/v1/predict --header 'Content-Type: application/json' --data '{"input_text": "test"}'
```

```sh
$ http POST http://127.0.0.1:9000/api/v1/predict input_text=テスト
```

## Development
### Run Tests and Linter

```
$ poetry run tox
```

## Reference

- [tiangolo/full\-stack\-fastapi\-postgresql: Full stack, modern web application generator\. Using FastAPI, PostgreSQL as database, Docker, automatic HTTPS and more\.](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [eightBEC/fastapi\-ml\-skeleton: FastAPI Skeleton App to serve machine learning models production\-ready\.](https://github.com/eightBEC/fastapi-ml-skeleton)