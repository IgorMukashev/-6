# class Cars:
#     def __init__(self, speed, color, name, is_police):
#         self.speed= speed
#         self.color= color
#         self.name= name
#         self.is_polyce= is_police
#
#     def go(self):
#             print(f" машина {self.color} цвета, марки {self.name} поехала со скоростью {self.speed}")
#
#
#     def stop(self):
#         print(f" машина {self.color} цвета, марки {self.name} осановилась {self.speed}")
#
#     def turn(self, direction):
#         print(f" машина {self.color} цвета, марки {self.name} повернула на {direction}")
#
#     def show_speed(self):
#         print(f"Текущая скорость машины {self.speed}")
#
# class TownCar(Cars):
#
#     def show_speed(self):
#         if self.speed > 60:
#             print("Превышение скорости! Сбавьте скорость")
#         else:
#             cars.show_speed(self)
#
# class SportCar(Cars):
#
#     def __init__(self, speed, color, name):
#         suoer().__init__(soeed, color, name, is_polyce=False)
#
#
# class WorkCar(Cars):
#
#     def show_speed(self):
#         if speed > 40:
#             print("Превышение скорости! Сбавьте скорость")
#
# class PoliceCar(Cars):
#     def __int__(self, speed, color, name):
#         Cars.__init__(self, speed, color, name, is_police=True)
#
# my_police_car = police_car(90,"White", "Lada Granta")
# my_police_car.go()
# my_police_car.turn("лево")
# my_police_car.stop
# my_police_car.show_speed()
#
# work_car = work_car(75,"black", "work_car", False)
# work_car.go()
# work_car.turn("лево")
# work_car.stop
# work_car.show_speed()
#
# sport_car = work_car(175,"red", "sport_car", False)
# sport_car.go()
# sport_car.turn("лево")
# sport_car.stop
# sport_car.show_speed()