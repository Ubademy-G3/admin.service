# Admin Microservice

[![CI](https://github.com/Ubademy-G3/admin.service/actions/workflows/default.yml/badge.svg)](https://github.com/Ubademy-G3/admin.service/actions/workflows/default.yml)
[![codecov](https://codecov.io/gh/Ubademy-G3/admin.service/branch/main/graph/badge.svg?token=N90QGLTQ0J)](https://codecov.io/gh/Ubademy-G3/admin.service)

# File Structure:
```tree
├── main.py
├── src
│   ├── infrastructure
│   │   ├── db
│   │   │   ├──  microservice_schema.py 
│   │   │   └──  database.py 
│   │   ├── routes
│   │   │   └──  microservice.py
│   ├── persistence
│   │   └── repositories
│   │       └── microservice_repository_postgres.py
│   ├── application
│   │   ├── controllers
│   │   │   └── 
│   │   ├──serializers
│   │   │   └── 
│   │   └── useCases
│   │       └── 
│   └── domain
│       ├── microservice_model.py
│       └── microservice_repository.py
├── monitoring
├── deploy
└── tests
```

# Local Environment 

## Requirements 

* Docker
* Docker-compose

## Build and Deploy Services

```docker-compose up -d --build```

This command deploys the service:

* `adminservice_web`: Web Service
* `adminservice_db`: Data base
* `pgadmin`: Data base admin

## Stop services

```docker-compose stop```
