from persistence.repositories.microservice_repository_postgres import MicroserviceRepositoryPostgres
from exceptions.http_exception import NotFoundException
import logging

logger = logging.getLogger(__name__)

mrp = MicroserviceRepositoryPostgres()


def delete_microservice(db, microservice_id):
    microservice = mrp.get_microservice(db, microservice_id)
    if not microservice:
        logger.warn("Microservice %s not found", microservice_id)
        raise NotFoundException("Microservice {}".format(microservice_id))
    return mrp.delete_microservice(db, microservice)
