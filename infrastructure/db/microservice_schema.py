from infrastructure.db.database import Base
from sqlalchemy import Column, String, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from domain.microservice_model import MicroserviceStateEnum


class Microservice(Base):

    __tablename__ = "microservices"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String(50), nullable=False)
    apikey = Column(String(50), nullable=False)
    state = Column(Enum(MicroserviceStateEnum))
    description = Column(String(255), nullable=False)
    timestamp = Column(DateTime, nullable=False)

    def __init__(self, id, name, apikey, state, description, timestamp):
        self.id = id
        self.name = name
        self.apikey = apikey
        self.state = state
        self.description = description
        self.timestamp = timestamp
