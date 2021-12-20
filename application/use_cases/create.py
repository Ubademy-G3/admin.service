from persistence.repositories.microservice_repository_postgres import MicroserviceRepositoryPostgres
from application.serializers.microservice_serializer import MicroserviceSerializer
from infrastructure.db.microservice_schema import Microservice, MicroserviceStateEnum
from uuid import uuid4
from exceptions.ubademy_exception import InvalidMicroserviceStateException, UsedNameException
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

mrp = MicroserviceRepositoryPostgres()


def add_microservice(db, args):

    logger.info("Add new microservice")

    if (args.state is not None and args.state not in ["active", "blocked", "taken_down"]):
        logger.error("Trying to create microservice "+args.name+" without or invalid state")
        raise InvalidMicroserviceStateException(args.state)

    other = mrp.get_microservice_by_name(db, args.name)
    if other is not None:
        logger.error("Microservice "+args.name+" already exists")
        raise UsedNameException(args.name)

    if args.description is None:
        args.description = "Non descriptive text"

    new_microservice = Microservice(
        id=uuid4(),
        name=args.name,
        apikey=args.apikey,
        state=MicroserviceStateEnum.active,
        description=args.description,
        timestamp=datetime.now(),
    )

    if(args.apikey == "blocked"):
        new_microservice.apikey = MicroserviceStateEnum.blocked

    if(args.apikey == "taken_down"):
        new_microservice.apikey = MicroserviceStateEnum.taken_down

    mrp.add_microservice(db, new_microservice)
    return MicroserviceSerializer.serialize(new_microservice)
