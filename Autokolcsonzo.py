from Berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def listaz_berleseket(self):
        return [
            f"{berles.auto.rendszam} ({berles.datum}) - {berles.auto.tipus} - {berles.ar()} Ft"
            for berles in self.berlesek
        ]

    def auto_hozzaad(self, auto):
        self.autok.append(auto)

    def listaz_elerheto_autok(self):
        foglalt_rendszamok = {berles.auto.rendszam for berles in self.berlesek}
        return [auto for auto in self.autok if auto.rendszam not in foglalt_rendszamok]

    def berel(self, rendszam, datum):
        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            return None

        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and str(berles.datum) == datum:
                return None

        try:
            uj_berles = Berles(auto, datum)
            self.berlesek.append(uj_berles)
            return uj_berles.ar()
        except ValueError:
            return "mult"

    def lemond(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and str(berles.datum) == datum:
                self.berlesek.remove(berles)
                return True
        return False

    def foglalhato_autok(self, datum):
        return [
            auto for auto in self.autok
            if not any(berles.auto.rendszam == auto.rendszam and str(berles.datum) == datum
                       for berles in self.berlesek)
        ]

