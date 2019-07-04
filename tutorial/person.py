# python tutorial/person.py
class DummyClass:
    wow = 3


dummy = DummyClass()
print(dummy.wow)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def boom(nein):
        return nein + 42


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
del p1.age  # Printing p1.age at this stage is breaking awfully...
p1.age = 310
print(p1.age)
print(Person.boom(3))
print(p1.boom(3))  # Static methods are available on instances....

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x.capitalize())

thislist = ["apple", "banana", "cherry"]

mappedListed = list(map(lambda a: a.capitalize(), thislist))
print(mappedListed)

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

try:
    print(somethingWhichDoesNotExist)
except:
    print("An exception occurred")

import datetime

x = datetime.datetime.now()
print(x)

a = 1
a = 2
print(a)  # mutating stuff

import lol

print(lol.lolol(32))


def tata(x):
    if x > 42:
        result = "no way"
    else:
        result = "ok all good"
    return result


print(tata(3))
print(tata(43))


def toto(x):
    return "no way" if (x > 42) else "ok all good"


print(toto(3))
print(toto(43))

print("-".join(["fesfaew", "fewawe"]))

app = 'apples'
lem = 'lemons'
stuff = "In the basket are %s and %s" % (app, lem)
print(stuff)
