# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name= name
#         self.surname= surname
#         self.position= position
#         self._income = {'wage': wage, 'bonus': bonus}
#
#         class Position(Worker):
#
#             @property
#             def get_full_name(self):
#                 return f"{self.name} {self.surname}"
#
#             @property
#             def get_full_salary(self):
#                 return self._income['wage']+ self._income['bonus']
#
# my_position = Position('Ivan', 'Petrov', 'programmer', 110000, 30000)
# print(f'Total salary of {my_position.full_name} is {my_position,full_salary}')