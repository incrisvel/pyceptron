from abc import ABC, abstractmethod


class Train(ABC):
    @abstractmethod
    def get_features(self) -> dict:
        pass

    @abstractmethod
    def get_label(self) -> int:
        pass


class Water(Train):
    def __init__(self, row: dict):
        def to_float(value):
            return float(value) if value not in ("", None) else 0.0

        self.ph = to_float(row.get("ph"))
        self.hardness = to_float(row.get("Hardness"))
        self.solids = to_float(row.get("Solids"))
        self.chloramines = to_float(row.get("Chloramines"))
        self.sulfate = to_float(row.get("Sulfate"))
        self.conductivity = to_float(row.get("Conductivity"))
        self.organic_carbon = to_float(row.get("Organic Carbon"))
        self.trihalomethanes = to_float(row.get("Trihalomethanes"))
        self.turbidity = to_float(row.get("Turbidity"))
        self.potability = int(row.get("Potability", 0))
        

    def get_features(self) -> dict:
        return {
            "ph": self.ph,
            "hardness": self.hardness,
            "solids": self.solids,
            "chloramines": self.chloramines,
            "sulfate": self.sulfate,
            "conductivity": self.conductivity,
            "organic_carbon": self.organic_carbon,
            "trihalomethanes": self.trihalomethanes,
            "turbidity": self.turbidity,
        }

    def get_label(self) -> int:
        return self.potability