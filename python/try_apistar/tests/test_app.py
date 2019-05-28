from apistar import test

from app import app


client = test.TestClient(app)


def test_list_iris():
    response = client.get('/')
    assert response.status_code == 200

    json_resp = response.json()
    assert len(json_resp) == 150

    expected = {
        'sepal_length': 5.1,
        'sepal_width': 3.5,
        'petal_length': 1.4,
        'petal_width': 0.2,
        'class_': 'Iris-setosa',
    }
    assert json_resp[0] == expected
