from infrastructure.db.microservice_schema import Microservice
import logging

logger = logging.getLogger(__name__)
logger.debug("HOLA")
class MicroserviceRepositoryPostgres:
    def add_microservice(self, db, microservice):
        db.add(microservice)
        db.commit()
        logger.info("Added new microservice")
        logger.debug("Name of the new microservice: %s", microservice.name)

    def get_microservice(self, db, microservice_id):
        logger.debug("Getting microservice %s", microservice_id)
        microservice = db.query(Microservice).filter(Microservice.id == microservice_id).first()
        return microservice

    def get_microservice_by_name(self, db, name):
        logger.debug("Getting microservice %s", name)
        microservice = db.query(Microservice).filter(Microservice.name == name).first()
        return microservice

    def get_microservices_by_name_list(self, db, name_list):
        logger.debug("Getting microservices by list: %s", str(name_list))
        microservices = db.query(Microservice).filter(Microservice.name.in_(name_list)).all()
        return microservices

    def get_all_microservices(self, db, state):
        logger.debug("Getting all microservices")
        query = db.query(Microservice)
        if state is not None:
            logger.debug("Using state filter: %s", state)
            query = query.filter(Microservice.state == state)
        microservices = query.all()
        return microservices

    def delete_microservice(self, db, microservice):
        db.delete(microservice)
        db.commit()
        logger.debug("Delete microservice %s", microservice.name)

    def update_microservice(self, db):
        db.commit()
