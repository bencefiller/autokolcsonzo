from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def info(self):
        pass

class Szemelyauto(Auto):
    def info(self):
        return f"Személyautó - {self.rendszam}, {self.tipus}, {self.berleti_dij} Ft/nap"

class Teherauto(Auto):
    def info(self):
        return f"Teherautó - {self.rendszam}, {self.tipus}, {self.berleti_dij} Ft/nap"
