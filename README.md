# Django Polls

_Tutorial basico de Django_

### Pre-requisitos 📋

```
Docker 19.03.1 y docker-compose 1.24.1
```

ó utilizar un entorno virtual

```
virtualenv nombre_de_tu_entorno -p python3
```

Activar entorno virtual

```
source nombre_entorno_virtual/bin/activate
```


## Pruebas  ⚙️

```
python manage.py test polls
```

## Deployment 📦

_Si se esta utilizando docker_

```
docker-compose up --build
```

_Si se esta utilizando un entorno virtual_

```
python manage.py runserver
```