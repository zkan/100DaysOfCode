from utils import convert_to_json


def test_data_list_to_json():
    data = [
        [5.1, 3.5, 1.4, 0.2, 'Iris-setosa'],
        [4.9, 3.0, 1.4, 0.2, 'Iris-setosa'],
    ]
    results = convert_to_json(data)

    expected = [
        {
            'sepal_length': 5.1,
            'sepal_width': 3.5,
            'petal_length': 1.4,
            'petal_width': 0.2,
            'class_': 'Iris-setosa',
        },
        {
            'sepal_length': 4.9,
            'sepal_width': 3.0,
            'petal_length': 1.4,
            'petal_width': 0.2,
            'class_': 'Iris-setosa',
        },
    ]

    assert results == expected


def test_data_list_including_string_to_json():
    data = [
        ['5.1', '3.5', '1.4', '0.2', 'Iris-setosa'],
        ['4.9', '3.0', '1.4', '0.2', 'Iris-setosa'],
    ]
    results = convert_to_json(data)

    expected = [
        {
            'sepal_length': 5.1,
            'sepal_width': 3.5,
            'petal_length': 1.4,
            'petal_width': 0.2,
            'class_': 'Iris-setosa',
        },
        {
            'sepal_length': 4.9,
            'sepal_width': 3.0,
            'petal_length': 1.4,
            'petal_width': 0.2,
            'class_': 'Iris-setosa',
        },
    ]

    assert results == expected
