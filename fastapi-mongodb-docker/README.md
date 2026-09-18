# FastAPI + MongoDB + Docker

## Run the application

```bash
docker compose up --build
```

Open Swagger UI:

http://localhost:8000/docs

Stop containers:

```bash
docker compose down
```

The MongoDB data is stored in the `mongo_data` Docker volume.
