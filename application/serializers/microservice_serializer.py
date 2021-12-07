from infrastructure.db.microservice_schema import Microservice
from domain.microservice_model import MicroserviceStateEnum


class MicroserviceSerializer:
    @classmethod
    def serialize(self, microservice: Microservice):

        state = "active"
        if microservice.state == MicroserviceStateEnum.blocked:
            state = "blocked"
        if microservice.state == MicroserviceStateEnum.taken_down:
            state = "taken_down"
        return {
            "id": microservice.id,
            "name": microservice.name,
            "apikey": microservice.apikey,
            "state": state,
            "description": microservice.description,
            "timestamp": microservice.timestamp,
        }
