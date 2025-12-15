#GET
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    r = requests.get(f"{BASE_URL}/posts")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

#POST 
def test_create_post():
    payload = {
        "title": "QA Test",
        "body": "Post de prueba",
        "userId": 1
    }

    r = requests.post(f"{BASE_URL}/posts", json=payload)

    assert r.status_code == 201
    body = r.json()
    assert body["title"] == "QA Test"

#DELETE 
def test_delete_post():
    r = requests.delete(f"{BASE_URL}/posts/1")
    assert r.status_code == 200

def test_create_and_delete_post_flow():
    payload = {
        "title": "Flow Test",
        "body": "Encadenado",
        "userId": 1
    }

    create = requests.post(f"{BASE_URL}/posts", json=payload)
    assert create.status_code == 201

    post_id = create.json()["id"]

    delete = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert delete.status_code == 200


