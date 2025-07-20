from tasks import app


def test_get_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    if data:
        assert "id" in data[0]
        assert "title" in data[0]


def test_add_task_success():
    client = app.test_client()
    new_task_data = {"title": "Deploy to production"}
    response = client.post("/tasks", json=new_task_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == new_task_data["title"]
    assert data["completed"] is False


def test_add_task_failure():
    client = app.test_client()
    response = client.post("/tasks", json={})
    assert response.status_code == 400
