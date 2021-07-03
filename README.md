# FastAPI and Neo4j Microservices Template

An opinionated yet customizable RESTful CRUD APIs for generic business domain services, rename/copy-paste the folders to suit your needs.

### Run a Microservice on local (without docker compose)

1. Create A PostgreSQL Instance, using docker and expose ports 5432

    ```bash
    docker-compose up -d neo4j # docker daemon should be running
    ``` 

1. Run a particular microservice (eg domain)

    ```
    cd services/domain
    pipenv install # for first time setup
    pipenv run python main.py # or
    pipenv run uvicorn main:app --reload # for hot reload
    ```

1. Endpoint available at

    `http://0.0.0.0:8000/api/v1/domain`

### Run a Microservices using Docker compose

```
docker-compose up
```

Endpoints available at

`http://0.0.0.0:7000/api/v1/domain`

`http://0.0.0.0:8000/api/v1/patient`

Maintainer -
- [Nikhil Akki](http://nikhilakki.in)