import abc


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(abc.ABC):
    def __init__(self, code, name):
        self.code = code
        self.name = name

    @abc.abstractmethod
    def get_hours(self):
        return 8


class Manager(Employee):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.__department = Department('manager', 1)

    def get_department(self):
        return self.__department

    def set_department(self, dep):
        self.__department = dep


class Seller(Employee):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.__department = Department('seller', 2)
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, sal):
        self.__sales += sal
