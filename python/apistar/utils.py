def convert_to_json(data):
    results = []
    for each in data:
        result = {
            'sepal-length': each[0],
            'sepal-width': each[1],
            'petal-length': each[2],
            'petal-width': each[3],
            'class': each[4],
        }
        results.append(result)

    return results
