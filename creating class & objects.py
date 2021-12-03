class Dog:
    attr1= "Mammal"
    def __init__(self, name) -> None:
        pass
        self.name=name
Rodger= Dog(" Rodger")
Tomy = Dog("Tomy")
print("Rodger is a {} ".format(Rodger.__class__.attr1))
print("Tomy is a {} ".format(Tomy.__class__.attr1))

print(' My name is {} '.format(Rodger.name))
print(' My name is {} '.format(Tomy.name))