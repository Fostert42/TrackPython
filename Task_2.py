# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    result = []
    with open(INPUT_FILENAME, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        for row in reader:
            result.append(row)  # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, indent=4, ensure_ascii=False)  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
