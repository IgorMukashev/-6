# from itertools import cycle
# from time import sleep
#
# class TrafficLight:
#     colors_queue = ("желтый", "желтый", "зеленный" )
#     time_queue = (7, 2, 6)
#     message = ("Красный свет- проезда нет!", "Желтый спет- будб готов", "А зеленый свет- кати")
#
#     def __init__(self, color):
#         self.__color = color
#
#         def running(self):
#             my_cycle = cycle(self.colors_queue)
#             for traffic_color in my_cycle:
#                 if self.__color == traffic_color:
#                     print(self.message[self.colors_queues.index(self.__color)])
#                     sleep(self.time_queue[self.colors_queue.index(self.__color)])
#                     self.__color = next(my_cycle)
#
#                     my_traffic = TrafficLight("зеленный")
#                     my_traffic.running()