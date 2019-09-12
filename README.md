# Django Polls

_Django Basic Tutorial_

### Pre-requirements 📋

```
Docker 19.03.1 and docker-compose 1.24.1
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

## Deployment 📦

_If you are using docker_

```
docker-compose up --build
```

_Create superuser_
```
docker-compose run web python manage.py createsuperuser
```

_Migrations_

```
docker-compose run web python3 manage.py migrate
```

```
docker-compose run web python3 manage.py makemigrations polls
```

```
docker-compose run web python3 manage.py sqlmigrate polls 0001
```

_Run one more time_

```
docker-compose run web python3 manage.py migrate
```

_If you are using a virtual environment_

```
python manage.py runserver
```

_Migrations_

```
python3 manage.py migrate
```

```
python3 manage.py makemigrations polls
```

```
python3 manage.py sqlmigrate polls 0001
```

_Run one more time_

```
python3 manage.py migrate
```

