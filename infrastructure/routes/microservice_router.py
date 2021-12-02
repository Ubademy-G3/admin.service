from fastapi import APIRouter, Header, Depends, Query
from infrastructure.db.database import Session, get_db
from typing import Optional
from application.controllers.microservice_controller import MicroserviceController
from application.services.auth import auth_service
from domain.microservice_model import (MicroservicePostBody, MicroserviceDB, MicroserviceList,
                                       MicroservicePatch)

router = APIRouter()


@router.post("/", response_model=MicroserviceDB, status_code=201)
async def create_microservice(
    microservice: MicroservicePostBody,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return MicroserviceController.create_microservice(db, microservice)


@router.get("/{microservice_id}", response_model=MicroserviceDB, status_code=200)
async def get_microservice(
    microservice_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return MicroserviceController.get_microservice(db, microservice_id)


@router.get("/name/{name}", response_model=MicroserviceDB, status_code=200)
async def get_microservice_by_name(
    name: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return MicroserviceController.get_microservice_by_name(db, name)


@router.get("/", response_model=MicroserviceList, status_code=200)
async def get_all_microservices(
    state: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return MicroserviceController.get_all_microservices(db, state)


@router.delete("/{microservice_id}", response_model=dict, status_code=200)
async def delete_microservice(
    microservice_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    MicroserviceController.delete_microservice(db, microservice_id)
    return {"message": "The microservice {} was deleted successfully".format(microservice_id)}


@router.patch("/{microservice_id}", response_model=MicroserviceDB, status_code=200)
async def update_microservice(
    microservice_id: str,
    microservice: MicroservicePatch,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):

    auth_service.check_api_key(apikey)
    return MicroserviceController.update_microservice(db, microservice_id, microservice)
