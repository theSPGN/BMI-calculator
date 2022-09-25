from bmi import BodyMassIndex


class Bmr(BodyMassIndex):
    def __init__(self, obj_bmi: BodyMassIndex, gender: str, age: int):
        # super(Bmr, self).__init__(obj_bmi.name, obj_bmi.weight, obj_bmi.height)
        # super().__init__(obj_bmi.name, obj_bmi.weight, obj_bmi.height)
        BodyMassIndex.__init__(self, obj_bmi.name, obj_bmi.weight, obj_bmi.height)
        self.gender = gender
        self.age = age
        self.bmr = float

    def calculate_bmr(self) -> float:
        if self.gender == 'male' or self.gender == 'Male':
            self.bmr = 66.5 + (13.75 * self.weight) + (5.003 * self.height) - (6.75 * self.age)
        else:
            self.bmr = 655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age)
        return float("%.2f" % self.bmr)

    def exercises(self, frequency=0) -> float:
        match frequency:
            case 0:
                frequency = 1.2
            case 1:
                frequency = 1.375
            case 2:
                frequency = 1.55
            case 3:
                frequency = 1.725
            case 4:
                frequency = 1.9
            case _:
                frequency = 1.2
        bmr_with_exercises = self.calculate_bmr() * frequency
        return float("%.2f" % bmr_with_exercises)

    def prepare_to_save(self) -> str:
        return BodyMassIndex.prepare_to_save(self) + str(self.exercises()) + ' kcal' + '\n'
        # return super(Bmr, self).prepare_to_save() + str(self.exercises()) + ' kcal' + '\n'
        # return super().prepare_to_save() + str(self.exercises()) + ' kcal' + '\n'

    def info(self) -> list:
        return BodyMassIndex.info(self) + [self.gender, self.age, self.exercises()]
        # return super().info() + [self.gender, self.age, self.exercises()]
        # return super(Bmr, self).info() + [self.gender, self.age, self.exercises()]
