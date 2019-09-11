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

_If you are using a virtual environment_

```
python manage.py runserver
```