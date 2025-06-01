from datetime import datetime

class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        try:
            self.datum = datetime.strptime(datum, "%Y-%m-%d").date()
            if self.datum < datetime.now().date():
                raise ValueError("A dátum nem lehet múltbeli.")
        except ValueError as e:
            raise ValueError(f"Érvénytelen dátum: {e}")

    def ar(self):
        return self.auto.berleti_dij
