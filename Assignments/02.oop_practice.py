class Employee:

  def __init__(self, id:str, name:str):
    self.id = id
    self.name = name

  def get_id(self):
    return self.id
  def get_name(self):
    return self.name
  def calculate_salary(self):
    pass
  def get_info(self):
    return f"id : {self.id} \nname : {self.name}\n"

class FullTimeEmployee(Employee):

  def __init__(self, id: str, name: str, base_salary:float, bonus:float):
    super().__init__(id, name)
    self.base_salary = base_salary
    self.bonus = bonus

  def calculate_salary(self):
    return self.base_salary + self.bonus
  def get_info(self):
    return super().get_info() + f"salary : {self.calculate_salary()}\n"

class PartTimeEmployee(Employee):

  def __init__(self, id: str, name: str, hourly_rate:float, hours_worked:int):
    super().__init__(id, name)
    self.hourly_rate = hourly_rate
    self.hours_worked = hours_worked

  def calculate_salary(self):
    return self.hourly_rate * self.hours_worked
  def get_info(self):
    return super().get_info() + f"salary : {self.calculate_salary()}\n"

class Contractor(Employee):

  def __init__(self, id: str, name: str, daily_rate:float, days_worked:int):
    super().__init__(id, name)
    self.daily_rate = daily_rate
    self.days_worked = days_worked

  def calculate_salary(self):
    return self.daily_rate * self.days_worked
  def get_info(self):
    return super().get_info() + f"salary : {self.calculate_salary()}\n"




emp1 = FullTimeEmployee(id="FT-101", name="Ali Khan", base_salary=75000.0, bonus=15000.0)
emp2 = PartTimeEmployee(id="PT-201", name="Ayesha Ahmed", hourly_rate=500.0, hours_worked=80)
emp3 = Contractor(id="CON-301", name="Bilal Shaheen", daily_rate=3500.0, days_worked=22)

payroll_list = [emp1, emp2, emp3]

print("--- 💼 Startup Payroll Dashboard 💼 ---\n")

for worker in payroll_list:
    print(worker.get_info())
    print("-" * 30)
