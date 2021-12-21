# Admin Microservice

[![CI](https://github.com/Ubademy-G3/admin.service/actions/workflows/default.yml/badge.svg)](https://github.com/Ubademy-G3/admin.service/actions/workflows/default.yml)
[![codecov](https://codecov.io/gh/Ubademy-G3/admin.service/branch/main/graph/badge.svg?token=N90QGLTQ0J)](https://codecov.io/gh/Ubademy-G3/admin.service)

Microservice for manage other microservices.

This microservice provides:

* Register a microservice
* Block a microservice
* Update a microservice

# File Structure:
```tree
├── application
│   ├── controllers
│   │   ├── __init__.py
│   │   └── microservice_controller.py
│   ├── __init__.py
│   ├── serializers
│   │   ├── __init__.py
│   │   └── microservice_serializer.py
│   ├── services
│   │   ├── auth.py
│   │   └── __init__.py
│   └── use_cases
│       ├── create.py
│       ├── delete.py
│       ├── get.py
│       ├── __init__.py
│       └── update.py
├── deploy
│   └── heroku-entrypoint.sh
├── docker-compose.yml
├── Dockerfile
├── domain
│   ├── __init__.py
│   └── microservice_model.py
├── exceptions
│   ├── auth_exception.py
│   ├── http_exception.py
│   ├── __init__.py
│   └── ubademy_exception.py
├── heroku.yml
├── infrastructure
│   ├── db
│   │   ├── database.py
│   │   ├── __init__.py
│   │   └── microservice_schema.py
│   ├── __init__.py
│   └── routes
│       ├── __init__.py
│       └── microservice_router.py
├── LICENSE
├── logging.ini
├── main.py
├── monitoring
│   └── datadog.yml
├── persistence
│   ├── __init__.py
│   └── repositories
│       ├── __init__.py
│       └── microservice_repository_postgres.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_microservices.py
```

# Local Environment 

## Requirements 

* Docker
* Docker-compose

## Environment variables

To run this application you need to define the following environment variable:

```
API_KEY = YOUR_ADMIN_SERVICE_APIKEY
```

## Build and Deploy Services

```docker-compose up -d --build```

This command deploys the service:

* `adminservice_web`: Web Service
* `adminservice_db`: Data base
* `pgadmin`: Data base admin

## Stop services

```docker-compose stop```

## Down services and remove containers, networks, volumes and images created by 'up'

```docker-compose down```

## To run tests

```docker-compose exec web pytest .```


You can try it out at <https://staging-admin-service-app-v2.herokuapp.com/docs>
