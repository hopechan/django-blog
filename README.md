# Django Polls

_Django Basic Tutorial_

### Pre-requirements 📋

```
Docker 19.03.1, docker-compose 1.24.1 and postgresql 9.5
```

or use a virtual environment

```
virtualenv environment_name -p python3
```

Activate virtual environment

```
source environment_name/bin/activate
```


## Test ⚙️

```
python manage.py test polls
```

##Database 

Open postgres shell
```
psql -h localhost -U postgres -d postgres
```

Create a database
```
CREATE DATABASE pollsdb;
```

Create a new superuser

```
CREATE USER admin WITH PASSWORD '1234';
```

```
ALTER ROLE admin SET client_encoding TO 'utf8';
```

```
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
```

```
ALTER ROLE admin SET timezone TO 'UTC';
```

Give access rights to the database

```
GRANT ALL PRIVILEGES ON DATABASE pollsdb TO admin;
```

Exit postgres shell

```
exit
```

## Deployment 📦

_If you are using docker_

```
docker-compose up --build
```

_If you are using a virtual environment_

```
python manage.py runserver
```

## Migrations 📦

```
python manage.py migrate
```

```
python manage.py makemigrations polls
```

```
python manage.py sqlmigrate polls 0001
```

```
python manage.py migrate
```

