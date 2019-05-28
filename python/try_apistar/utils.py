def convert_to_json(data):
    results = []
    for each in data:
        result = {
            'sepal_length': float(each[0]),
            'sepal_width': float(each[1]),
            'petal_length': float(each[2]),
            'petal_width': float(each[3]),
            'class_': each[4],
        }
        results.append(result)

    return results
