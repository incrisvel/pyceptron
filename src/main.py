from csv import DictReader
from pyceptron import Pyceptron

def start():
    read_from_csv()

def read_from_csv():
    with open('data/water_potability.csv', newline = '') as data:
        water_data = DictReader(data)

        rows = []
        for i, row in enumerate(water_data):
            if i >= 6:
                break
            rows.append(row)

        pyceptron = Pyceptron(water_data.fieldnames[:-1])

        dataset = []
        answers = []

        # for row in water_data:
        #     data, answer = row_to_dict(row)
        #     dataset.append(data)
        #     answers.append(answer)

        for row in rows[:5]:
            data, label = row_to_dict(row)
            dataset.append(data)
            answers.append(label)

        pyceptron.train(dataset, answers)

        test_data, test_label = row_to_dict(rows[5])
        prediction = pyceptron.guess(test_data)

        print("Entrada:", test_data)
        print("Resposta certa:", test_label)
        print("Resposta Pyceptron:", prediction)

def row_to_dict(row):
    data = {}

    for key, value in row.items():
        if key == "Potability": # ignorar coluna de resposta
            continue

        data[key] = float(value) if value != "" else 0.0

    correct_answer = int(row["Potability"])

    return data, correct_answer # deixar cada linha no formato ({dados}, resposta)

if __name__ == '__main__':
    start()
