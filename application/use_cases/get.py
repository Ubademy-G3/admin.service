from persistence.repositories.microservice_repository_postgres import MicroserviceRepositoryPostgres
from exceptions.http_exception import NotFoundException
from application.serializers.microservice_serializer import MicroserviceSerializer

mrp = MicroserviceRepositoryPostgres()


def get_microservice(db, microservice_id):
    microservice = mrp.get_microservice(db, microservice_id)
    if microservice is None:
        raise NotFoundException("Microservice {}".format(microservice_id))
    return MicroserviceSerializer.serialize(microservice)


def get_microservice_by_name(db, name):
    microservice = mrp.get_microservice_by_name(db, name)
    if microservice is None:
        raise NotFoundException("Microservice {}".format(name))
    return MicroserviceSerializer.serialize(microservice)


def get_microservices_by_name_list(db, name_list):
    microservices = mrp.get_microservices_by_name_list(db, name_list)
    if microservices is None:
        raise NotFoundException("Microservice {}".format(name_list))

    microservice_list = []
    for microservice in microservices:
        microservice_list.append(MicroserviceSerializer.serialize(microservice))
    microservice_list = sorted(microservice_list, key=lambda x: x['name'])
    return {
        "amount": len(microservice_list),
        "microservices": microservice_list,
    }


def get_all_microservices(db, state):
    microservices = mrp.get_all_microservices(db, state)

    microservice_list = []
    for microservice in microservices:
        microservice_list.append(MicroserviceSerializer.serialize(microservice))
    return {
        "amount": len(microservice_list),
        "microservices": microservice_list,
    }
