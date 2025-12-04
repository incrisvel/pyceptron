from kfold import KFold
from models.set import PyceptronSet
from pyceptron import Pyceptron
from reader import Reader 


K_VALUE = 5

def start():
    normalized_dataset = Reader.read_from_csv("data/water_potability.csv")
    Reader.shuffle_dataset(normalized_dataset)

    kfold = KFold(normalized_dataset, k_folds=K_VALUE)
    
    feature_names = list(normalized_dataset[0].get_features().keys())
    all_accuracies = []
    
    for index in range(K_VALUE):
        print(f"\nFOLD {index + 1}/{K_VALUE}")
        
        sets = kfold.get_sets_for_fold(index)
        train_set = sets.train
        test_set = sets.test

        pyceptron = Pyceptron(feature_names=feature_names) 
        pyceptron.train(train_set.features, train_set.labels)

        accuracy = test_fold(index, pyceptron, test_set)
        all_accuracies.append(accuracy)

    avg_accuracy = sum(all_accuracies) / len(all_accuracies)
    print("\nRESULTADOS FINAIS")
    print(f"Acurácias por Fold: {[f'{acc:.2%}' for acc in all_accuracies]}")
    print(f"Acurácia Média ({K_VALUE}-fold): {avg_accuracy:.2%}")


def test_fold(fold: int, pyceptron: Pyceptron, test: PyceptronSet) -> float:
    correct_guesses = 0
    total_guesses = 0

    for test_data, test_label in zip(test.features, test.labels):
        prediction = pyceptron.guess(test_data)

        if prediction == test_label:
            correct_guesses += 1
        total_guesses += 1

    accuracy = calculate_accuracy(correct_guesses, total_guesses)
    print(f"Acertos no Fold {fold + 1}: {correct_guesses}/{total_guesses} = {accuracy:.2%}")
    return accuracy

def calculate_accuracy(correct: int, total: int):
    return correct / total

if __name__ == "__main__":
    start()