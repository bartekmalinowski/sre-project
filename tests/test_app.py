import sys
import os
from app import app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World! Welcome to the SRE Project App." in response.data


def test_status_page():
    client = app.test_client()
    response = client.get("/status")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "OK"


def test_error_page():
    client = app.test_client()
    response = client.get("/error")
    assert response.status_code == 500
