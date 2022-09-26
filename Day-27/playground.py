def add(*args):
    total = 0
    for n in args:
        total += n
    return total


def calculate(n, **kwargs):
    # print(type(kwargs))
    # # Looping through keyword arguments:
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # # Getting hold of the value of a particular keyword argument:
    # print(kwargs["add"])
    n += kwargs["add"]  # Adding n with keyword argument value in add
    n *= kwargs["multiply"]  # Multiplying n with keyword argument value in add
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __int__(self, **kwargs):
        self.make = kwargs.get("make")


my_car = Car(make="Nissan")
print(my_car.make)
