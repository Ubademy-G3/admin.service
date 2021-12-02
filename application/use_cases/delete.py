from persistence.repositories.microservice_repository_postgres import MicroserviceRepositoryPostgres
from exceptions.http_exception import NotFoundException

mrp = MicroserviceRepositoryPostgres()


def delete_microservice(db, microservice_id):
    microservice = mrp.get_microservice(db, microservice_id)
    if not microservice:
        raise NotFoundException("Microservice {}".format(microservice_id))
    return mrp.delete_microservice(db, microservice)
