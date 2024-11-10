# TODO решите задачу
import json

FILENAME = 'input.json'


def task() -> float:
    with open(FILENAME) as f:
        data = json.load(f)

    sum_of_values = sum(item['score'] * item['weight'] for item in data)
    return round(sum_of_values, 3)


print(task())
