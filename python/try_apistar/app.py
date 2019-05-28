import csv

from apistar import App, Route, types, validators
from apistar.http import JSONResponse

from utils import convert_to_json


def _load_iris_data():
    with open('iris.csv') as f:
        data = []
        reader = csv.reader(f)
        for each in reader:
            data.append(each)

    return data


original_iris_data = convert_to_json(_load_iris_data())


class Iris(types.Type):
    sepal_length = validators.Number()
    sepal_width = validators.Number()
    petal_length = validators.Number()
    petal_width = validators.Number()
    class_ = validators.String()


def list_iris() -> JSONResponse:
    iris_data = [Iris(each) for each in original_iris_data]
    return JSONResponse(iris_data)


def get_iris(iris_id: int) -> JSONResponse:
    iris = original_iris_data[iris_id - 1]
    return JSONResponse(Iris(iris), status_code=200)


routes = [
    Route('/', method='GET', handler=list_iris),
    Route('/{iris_id}/', method='GET', handler=get_iris),
]

app = App(routes=routes)

if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
