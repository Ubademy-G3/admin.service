from application.use_cases import create, get, delete, update


class MicroserviceController:
    @classmethod
    def create_microservice(self, db, args):
        return create.add_microservice(db, args)

    @classmethod
    def get_microservice(self, db, microservice_id):
        return get.get_microservice(db, microservice_id)

    @classmethod
    def get_microservice_by_name(self, db, name):
        return get.get_microservice_by_name(db, name)

    @classmethod
    def get_all_microservices(self, db, state):
        return get.get_all_microservices(db, state)

    @classmethod
    def delete_microservice(self, db, microservice_id):
        return delete.delete_microservice(db, microservice_id)

    @classmethod
    def update_microservice(self, db, microservice_id, payload):
        return update.update_microservice(db, microservice_id, payload)
