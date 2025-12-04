class PyceptronSet:
    def __init__(self, features: list[dict], labels: list[str]):
        self.features = features
        self.labels = labels
        
class FoldSets:
    def __init__(self, test: PyceptronSet, train: PyceptronSet):
        self.test = test
        self.train = train 