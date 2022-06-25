class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age


class PersonSlots:
    __slots__ = ("name", "address", "age")

    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age
