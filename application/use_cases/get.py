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
        raise NotFoundException("Microservice {}".format(microservice_id))
    return MicroserviceSerializer.serialize(microservice)


def get_all_microservices(db, state):
    microservices = mrp.get_all_microservices(db, state)

    print(type(microservices))
    microservice_list = []
    for microservice in microservices:
        print(type(microservice))
        microservice_list.append(MicroserviceSerializer.serialize(microservice))
    return {
        "amount": len(microservice_list),
        "microservices": microservice_list,
    }
