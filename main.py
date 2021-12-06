from fastapi import FastAPI
import logging
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from infrastructure.routes import microservice_router
from infrastructure.db.database import Base, engine, DATABASE_URL
from sqlalchemy.exc import SQLAlchemyError
from exceptions.ubademy_exception import UbademyException
from exceptions.auth_exception import AuthorizationException

if DATABASE_URL is not None:
    Base.metadata.create_all(engine)

app = FastAPI(title="ubademy-adminservice", description="Admin service API")

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    message = {"message": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content=message)


@app.exception_handler(UbademyException)
async def ubademy_exception_hanlder(request, exc):
    message = {"message": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content=message)


@app.exception_handler(AuthorizationException)
async def auth_exception_handler(request, exc):
    message = {"message": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content=message)


@app.exception_handler(SQLAlchemyError)
async def sql_exception_handler(request, exc):
    message = {"message": str(exc.__dict__)}
    logging.error(f"status_code: 500 message: {str(exc.__dict__)}")
    return JSONResponse(status_code=500, content=message)


@app.exception_handler(Exception)
async def unknown_exception_handler(request, exc):
    message = {"message": str(exc.__dict__)}
    logging.error(f"status_code: 500 message: {str(exc.__dict__)}")
    return JSONResponse(status_code=500, content=message)


app.include_router(
    microservice_router.router,
    prefix="/microservices",
    tags=["microservices"]
)
