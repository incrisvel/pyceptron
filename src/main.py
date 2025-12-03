from csv import DictReader
from pyceptron import Pyceptron

def start():
    read_from_csv()

def read_from_csv():
    with open('data/water_clean.csv', newline = '') as data:
        water_data = DictReader(data)

        pyceptron = Pyceptron(water_data.fieldnames[:-1])

        dataset = []
        answers = []

        rows = list(water_data)
        split_index = int(len(rows) * 0.8)
        train_rows = rows[:split_index]
        test_rows = rows[split_index:]

        for row in train_rows:
            data, answer = row_to_dict(row)
            dataset.append(data)
            answers.append(answer)

        pyceptron.train(dataset, answers)

        correct_guesses = 0
        total_guesses = 0

        for row in test_rows:
            test_data, test_label = row_to_dict(row)
            prediction = pyceptron.guess(test_data)

            if prediction == test_label:
                correct_guesses += 1
            total_guesses += 1

        print(f"Acertos: {correct_guesses}/{total_guesses} = {correct_guesses/total_guesses:.2%}")


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
