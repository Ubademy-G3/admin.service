from fastapi.testclient import TestClient
from main import app
from unittest import TestCase, mock
from persistence.repositories.microservice_repository_postgres import MicroserviceRepositoryPostgres
from infrastructure.db.microservice_schema import Microservice, MicroserviceStateEnum
import json
import os


apikey = os.getenv("API_KEY")

mrp = MicroserviceRepositoryPostgres()


client = TestClient(app)


# Post
post_header = {"apikey": apikey}

post_body = {
    "name": "Courses"
    "apikey": "hola"
}

# Get
get_header = {"apikey": apikey, "microservice_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

return_from_get = Microservice(
    id="5122b737-f815-4e15-a56d-abbff2fee900",
    name="Courses",
    name="hola",
    state=MicroserviceStateEnum.draft,
)

# Get all
get_all_header = {"apikey": apikey}

return_from_get_all = [
    Microservice(
        id="5122b737-f815-4e15-a56d-abbff2fee900",
        name="Courses",
        name="hola",
        state=MicroserviceStateEnum.draft,
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
    def test_create_microservice(self, mock_post):
        mock_post.return_value = None

        response = client.post(
            "/microservices/",
            data=json.dumps(post_body),
            headers=post_header
        )
        assert response.status_code == 201, response.text
        data = response.json()
        assert data["name"] == "Courses"
        assert data["apikey"] == "hola"
        assert data["state"] == "active"

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
        assert data["name"] == "Courses"
        assert data["apikey"] == "hola"
        assert data["state"] == "active"

    @mock.patch.object(MicroserviceRepositoryPostgres, "get_all_microservices")
    def test_get_all_microservices(self, mock_get_all):
        mock_get_all.return_value = return_from_get_all

        response = client.get(
            f"/microservices/",
            headers=get_all_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["amount"] == 1
        assert data["microservices"][0]["id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["microservices"][0]["name"] == "Courses"
        assert data["microservices"][0]["name"] == "hola"
        assert data["microservices"][0]["state"] == "draft"

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
    @mock.patch.object(MicroserviceRepositoryPostgres, "get_microservice")
    def test_update_microservice(self, mock_get, mock_update):
        mock_get.return_value = return_from_get
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
        assert data["name"] == "Courses"
        assert data["apikey"] == "hola"
        assert data["state"] == "blocked"
