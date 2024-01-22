from bmi import BodyMassIndex as Bmi
from bmr import Bmr

p1 = Bmi("Taylor", 74.1, 185.5)
p2 = Bmr(p1, "male", 18)
# Reference to parent function:
# print(super(Bmr, p2).info())
# print(Bmi.info(p2))
# Reference to child function:
# print(p2.info())
# print(p1.info())
