from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List
import enum
from datetime import datetime


class MicroserviceStateEnum(enum.Enum):
    active = 1
    blocked = 2
    taken_down = 3


class MicroservicePostBody(BaseModel):
    name: str
    apikey: str
    state: Optional[str]
    description: Optional[str]


class MicroserviceDB(BaseModel):
    id: UUID
    name: str
    apikey: str
    state: Optional[str]
    description: str
    timestamp: datetime


class MicroserviceList(BaseModel):
    amount: int
    microservices: Optional[List[MicroserviceDB]]


class MicroservicePatch(BaseModel):
    name: Optional[str]
    apikey: Optional[str]
    state: Optional[str]
    description: Optional[str]
