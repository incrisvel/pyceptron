import random
from csv import DictReader

from models.water import Water


class Reader:
    @staticmethod
    def read_from_csv(path: str) -> list:
        """Lê o CSV, cria e retorna uma lista de objetos Water."""
        dataset = []
        with open(path, newline="") as data:
            water_data = DictReader(data)
            for row in water_data:
                dataset.append(Water(row))
        return dataset

    @staticmethod
    def shuffle_dataset(dataset: list):
        """Embaralha o dataset."""
        print("Embaralhando o dataset...")
        random.shuffle(dataset)