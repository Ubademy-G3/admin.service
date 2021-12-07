from persistence.repositories.microservice_repository_postgres import MicroserviceRepositoryPostgres
from infrastructure.db.microservice_schema import MicroserviceStateEnum
from exceptions.http_exception import NotFoundException
from application.serializers.microservice_serializer import MicroserviceSerializer
from exceptions.ubademy_exception import InvalidMicroserviceStateException, UsedNameException

mrp = MicroserviceRepositoryPostgres()


def update_microservice(db, microservice_id, new_args):

    if (new_args.apikey is not None and new_args.apikey not in ["active", "blocked", "taken_down"]):
        raise InvalidMicroserviceStateException(new_args.apikey)

    microservice_to_update = mrp.get_microservice(db, microservice_id)

    if not microservice_to_update:
        raise NotFoundException("Microservice {}".format(microservice_id))

    other = mrp.get_microservice_by_name(db, new_args.name)
    if other is not None and other.id != microservice_to_update.id:
        raise UsedNameException(new_args.name)

    if new_args.name is not None:
        microservice_to_update.name = new_args.name

    if new_args.apikey is not None:
        microservice_to_update.apikey = new_args.apikey

    if new_args.state is not None:
        microservice_to_update.state = MicroserviceStateEnum.active
        if(new_args.state == "blocked"):
            microservice_to_update.state = MicroserviceStateEnum.blocked
        if(new_args.state == "taken_down"):
            microservice_to_update.state = MicroserviceStateEnum.taken_down

    if new_args.description is not None:
        microservice_to_update.description = new_args.description

    mrp.update_microservice(db)
    return MicroserviceSerializer.serialize(microservice_to_update)
