from apistar import test

from app import app, original_iris_data


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


def test_get_iris():
    response = client.get('/88/')
    assert response.status_code == 200

    expected = {
        'sepal_length': 6.3,
        'sepal_width': 2.3,
        'petal_length': 4.4,
        'petal_width': 1.3,
        'class_': 'Iris-versicolor',
    }
    assert response.json() == expected


def test_create_iris():
    data = {
        'sepal_length': 9,
        'sepal_width': 9,
        'petal_length': 9,
        'petal_width': 9,
        'class_': 'Iris-virginica',
    }

    response = client.post('/', data=data)
    assert response.status_code == 201
    assert len(original_iris_data) == 151

    response = client.get('/151/')
    expected = {
        'sepal_length': 9,
        'sepal_width': 9,
        'petal_length': 9,
        'petal_width': 9,
        'class_': 'Iris-virginica',
    }
    assert response.json() == expected
