from ..utils import convert_to_json


def test_data_list_to_json():
    data = [
        [5.1, 3.5, 1.4, 0.2, 'Iris-setosa'],
        [4.9, 3.0, 1.4, 0.2, 'Iris-setosa'],
    ]
    results = convert_to_json(data)

    expected = [
        {
            'sepal-length': 5.1,
            'sepal-width': 3.5,
            'petal-length': 1.4,
            'petal-width': 0.2,
            'class': 'Iris-setosa',
        },
        {
            'sepal-length': 4.9,
            'sepal-width': 3.0,
            'petal-length': 1.4,
            'petal-width': 0.2,
            'class': 'Iris-setosa',
        },
    ]

    assert results == expected
