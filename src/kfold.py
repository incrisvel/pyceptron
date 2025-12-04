from models.set import FoldSets, PyceptronSet
from models.water import Train


class KFold:
    def __init__(self, dataset: list[Train], k_folds: int = 5) -> None:
        self.dataset = dataset
        self.total = len(dataset)
        self.k_folds = k_folds
        self.fold_size = self.total // k_folds

    def get_sets_for_fold(self, fold_index: int):
        start_index = fold_index * self.fold_size
        end_index = start_index + self.fold_size if fold_index < self.k_folds - 1 else self.total

        test_dataset = self.dataset[start_index:end_index]
        train_dataset = self.dataset[:start_index] + self.dataset[end_index:]

        test = self.generate_pyceptron_set(test_dataset)
        train = self.generate_pyceptron_set(train_dataset)
        
        return FoldSets(test=test, train=train)

    def generate_pyceptron_set(self, dataset: list[Train]) -> PyceptronSet:
        features = [obj.get_features() for obj in dataset]
        labels = [obj.get_label() for obj in dataset]
        return PyceptronSet(features, labels)
