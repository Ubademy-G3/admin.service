from infrastructure.db.microservice_schema import Microservice


class MicroserviceRepositoryPostgres:
    def add_microservice(self, db, microservice):
        db.add(microservice)
        db.commit()

    def get_microservice(self, db, microservice_id):
        microservice = db.query(Microservice).filter(Microservice.id == microservice_id).first()
        return microservice

    def get_microservice_by_name(self, db, name):
        microservice = db.query(Microservice).filter(Microservice.name == name).first()
        return microservice

    def get_all_microservices(self, db, state):
        query = db.query(Microservice)
        if state is not None:
            query = query.filter(Microservice.state == state)
        microservices = query.all()
        return microservices

    def delete_microservice(self, db, microservice):
        db.delete(microservice)
        db.commit()

    def update_microservice(self, db):
        db.commit()
