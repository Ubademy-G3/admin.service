from fastapi.testclient import TestClient
from main import app
from unittest import TestCase, mock
from persistence.repositories.microservice_repository_postgres import MicroserviceRepositoryPostgres
from infrastructure.db.microservice_schema import Microservice, MicroserviceStateEnum
import json
import os
from datetime import datetime


apikey = os.getenv("API_KEY")

mrp = MicroserviceRepositoryPostgres()


client = TestClient(app)


# Post
post_header = {"apikey": apikey}

post_body = {
    "name": "courses",
    "apikey": "hola",
    "description": "hola",
}

# Get
get_header = {"apikey": apikey, "microservice_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

return_from_get = Microservice(
    id="5122b737-f815-4e15-a56d-abbff2fee900",
    name="courses",
    apikey="hola",
    state=MicroserviceStateEnum.active,
    description="hola",
    timestamp=datetime.fromisoformat('2011-11-04T00:05:23.283333')
)

# Get by name
get_by_name_header = {"apikey": apikey, "name": "courses"}

return_from_get_by_name = Microservice(
    id="5122b737-f815-4e15-a56d-abbff2fee900",
    name="courses",
    apikey="hola",
    state=MicroserviceStateEnum.active,
    description="hola",
    timestamp=datetime.fromisoformat('2011-11-04T00:05:23.283333')
)

# Get by name list
get_by_name_list_header = {"apikey": apikey}

get_by_name_list_body = {
    "name_list": ["courses"]
}

return_from_get_by_name_list = [
    Microservice(
        id="5122b737-f815-4e15-a56d-abbff2fee900",
        name="courses",
        apikey="hola",
        state=MicroserviceStateEnum.active,
        description="hola",
        timestamp=datetime.fromisoformat('2011-11-04T00:05:23.283333')
    )
]

# Get all
get_all_header = {"apikey": apikey}

return_from_get_all = [
    Microservice(
        id="5122b737-f815-4e15-a56d-abbff2fee900",
        name="courses",
        apikey="hola",
        state=MicroserviceStateEnum.active,
        description="hola",
        timestamp=datetime.fromisoformat('2011-11-04T00:05:23.283333')
    )
]

# Delete
delete_header = {"apikey": apikey, "microservice_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

return_from_delete = None

# Update
update_header = {"apikey": apikey, "microservice_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

update_body = {
    "state": "blocked",
}


class MicroserviceMock(TestCase):

    @mock.patch.object(MicroserviceRepositoryPostgres, "add_microservice")
    @mock.patch.object(MicroserviceRepositoryPostgres, "get_microservice_by_name")
    def test_create_microservice(self, mock_get_by_name, mock_post):
        mock_get_by_name.return_value = None
        mock_post.return_value = None

        response = client.post(
            "/microservices/",
            data=json.dumps(post_body),
            headers=post_header
        )
        assert response.status_code == 201, response.text
        data = response.json()
        assert data["name"] == "courses"
        assert data["apikey"] == "hola"
        assert data["state"] == "active"
        assert data["description"] == "hola"

    @mock.patch.object(MicroserviceRepositoryPostgres, "get_microservice")
    def test_get_microservice(self, mock_get):
        mock_get.return_value = return_from_get

        microservice_id = "5122b737-f815-4e15-a56d-abbff2fee900"

        response = client.get(
            f"/microservices/{microservice_id}",
            headers=get_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["id"] == microservice_id
        assert data["name"] == "courses"
        assert data["apikey"] == "hola"
        assert data["state"] == "active"
        assert data["description"] == "hola"
        assert data["timestamp"] == "2011-11-04T00:05:23.283333"

    @mock.patch.object(MicroserviceRepositoryPostgres, "get_microservice_by_name")
    def test_get_microservice_by_name(self, mock_get_by_name):
        mock_get_by_name.return_value = return_from_get_by_name

        name = "courses"

        response = client.get(
            f"/microservices/name/{name}",
            headers=get_by_name_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["name"] == "courses"
        assert data["apikey"] == "hola"
        assert data["state"] == "active"
        assert data["description"] == "hola"
        assert data["timestamp"] == "2011-11-04T00:05:23.283333"

    @mock.patch.object(MicroserviceRepositoryPostgres, "get_microservices_by_name_list")
    def test_get_microservices_by_name_list(self, mock_get_by_name_list):
        mock_get_by_name_list.return_value = return_from_get_by_name_list

        response = client.get(
            "/microservices/name/",
            data=json.dumps(get_by_name_list_body),
            headers=get_by_name_list_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["amount"] == 1
        assert data["microservices"][0]["id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["microservices"][0]["name"] == "courses"
        assert data["microservices"][0]["apikey"] == "hola"
        assert data["microservices"][0]["state"] == "active"
        assert data["microservices"][0]["description"] == "hola"
        assert data["microservices"][0]["timestamp"] == "2011-11-04T00:05:23.283333"

    @mock.patch.object(MicroserviceRepositoryPostgres, "get_all_microservices")
    def test_get_all_microservices(self, mock_get_all):
        mock_get_all.return_value = return_from_get_all

        response = client.get(
            "/microservices/",
            headers=get_all_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["amount"] == 1
        assert data["microservices"][0]["id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["microservices"][0]["name"] == "courses"
        assert data["microservices"][0]["apikey"] == "hola"
        assert data["microservices"][0]["state"] == "active"
        assert data["microservices"][0]["description"] == "hola"
        assert data["microservices"][0]["timestamp"] == "2011-11-04T00:05:23.283333"

    @mock.patch.object(MicroserviceRepositoryPostgres, "delete_microservice")
    @mock.patch.object(MicroserviceRepositoryPostgres, "get_microservice")
    def test_delete_microservice(self, mock_get, mock_delete):
        mock_get.return_value = return_from_get
        mock_delete.return_value = return_from_delete

        microservice_id = "5122b737-f815-4e15-a56d-abbff2fee900"

        response = client.delete(
            f"/microservices/{microservice_id}",
            headers=delete_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["message"] == f"The microservice {microservice_id} was deleted successfully"

    @mock.patch.object(MicroserviceRepositoryPostgres, "update_microservice")
    @mock.patch.object(MicroserviceRepositoryPostgres, "get_microservice_by_name")
    @mock.patch.object(MicroserviceRepositoryPostgres, "get_microservice")
    def test_update_microservice(self, mock_get, mock_get_by_name, mock_update):
        mock_get.return_value = return_from_get
        mock_get_by_name.return_value = return_from_get_by_name
        mock_update.return_value = None

        microservice_id = "5122b737-f815-4e15-a56d-abbff2fee900"

        response = client.patch(
            f"/microservices/{microservice_id}",
            data=json.dumps(update_body),
            headers=update_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["id"] == microservice_id
        assert data["name"] == "courses"
        assert data["apikey"] == "hola"
        assert data["state"] == "blocked"
        assert data["description"] == "hola"
        assert data["timestamp"] == "2011-11-04T00:05:23.283333"
