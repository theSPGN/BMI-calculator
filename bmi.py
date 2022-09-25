import datetime


class BodyMassIndex:
    def __init__(self, name='name', weight=71.3, height=180.5):
        self.name = name
        self.weight = weight
        self.height = height
        self.bmi = float

    def calculuate_bmi(self) -> float:
        height_in_m = self.height / 100
        self.bmi = self.weight / (height_in_m * height_in_m)
        return float("%.2f" % self.bmi)

    def is_right(self):
        if self.calculuate_bmi() <= 16.0:
            return "Too low weight (Dangerous)"
        elif self.calculuate_bmi() <= 17.0:
            return "Too low weight"
        elif self.calculuate_bmi() <= 18.5:
            return "A little too low weight"
        elif self.calculuate_bmi() <= 25.0:
            return "Good weight-height proportion"
        elif self.calculuate_bmi() <= 30.0:
            return "A little too high"
        elif self.calculuate_bmi() <= 35.0:
            return "Too high weight"
        elif self.calculuate_bmi() <= 40.0:
            return "Too high weight (Dangerous)"
        else:
            return "Too high weight (Really danger)"

    def prepare_to_save(self) -> str:
        return str(self.weight) + 'kg ' + str(self.height) + 'cm ' + str(self.calculuate_bmi()) + ' ' + str(
            datetime.date.today()) + '  '

    def save(self):
        file = open(self.name + '.txt', 'a')
        p = self.prepare_to_save()
        file.write(p)
        file.close()

    def info(self) -> list:
        return [self.name, self.weight, self.height, self.calculuate_bmi()]
