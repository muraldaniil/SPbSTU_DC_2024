import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]  # Преобразование в список словарей

    with open(OUTPUT_FILENAME, mode='w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
