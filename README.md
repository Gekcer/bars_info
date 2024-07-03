# bars_info
Приложение Flask для просмотра информации о барах. Проект предназначен, чтобы обучиться 
основам docker-compose

## Docker-compose

```yaml
version: '3'
services:
  db:
    image: postgres:12
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: krasnodarbars
    volumes:
      - db_data:/var/lib/postgresql/data

  web:
    build: .
    command: python app.py
    ports:
      - "5000:5000"
    environment:
      DATABASE_URL: postgresql://postgres:postgres@db:5432/krasnodarbars
    depends_on:
      - db

volumes:
  db_data:
```

### 1. Сохранение dump базы данных

```commandline
pg_dump -U postgres -d {db_name} -f {file_name}.sql -h localhost -p 5432
```
### 2. Загрузка дампа в docker контейнер
Запуск контейнера
```commandline
docker-compose up -d
```

```commandline
docker cp {dump_name}.sql {container_id}:/{dump_name}.sql
```

### 3. Применение дампа к бд
```commandline
docker exec -it {container_id} bash
```
```commandline
psql -U postgres -d krasnodarbars -f /krasnodarbars.sql
```

В результате удалось запустить приложение на другом компьютере в друго сети только с помощью docker-compose. 
В дальнейшем можно поиска, возможно ли передавать состояние базы данных Postgres каким-то другим способом.