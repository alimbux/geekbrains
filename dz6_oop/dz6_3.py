class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus};

    def square(self):
        return self.param_1 * self.param_2


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


python_developer = Position("John", "Smith", "Python developer", 5000, 500)
print(f"{python_developer.get_full_name()} - {python_developer.position}")
print(f"Total income: {python_developer.get_total_income()}")
