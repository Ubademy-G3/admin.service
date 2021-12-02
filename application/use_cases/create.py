from persistence.repositories.microservice_repository_postgres import MicroserviceRepositoryPostgres
from application.serializers.microservice_serializer import MicroserviceSerializer
from infrastructure.db.microservice_schema import Microservice, MicroserviceStateEnum
from uuid import uuid4
from exceptions.ubademy_exception import InvalidMicroserviceStateException


mrp = MicroserviceRepositoryPostgres()


def add_microservice(db, args):

    if (args.state is not None and args.state not in ["active", "blocked", "taken_down"]):
        raise InvalidMicroserviceStateException(args.state)

    new_microservice = Microservice(
        id=uuid4(),
        name=args.name,
        apikey=args.apikey,
        state=MicroserviceStateEnum.active,
    )

    if(args.apikey == "blocked"):
        new_microservice.apikey = MicroserviceStateEnum.blocked

    if(args.apikey == "taken_down"):
        new_microservice.apikey = MicroserviceStateEnum.taken_down

    mrp.add_microservice(db, new_microservice)
    return MicroserviceSerializer.serialize(new_microservice)
