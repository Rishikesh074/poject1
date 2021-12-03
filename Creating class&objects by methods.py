class Dog:
    attr1=" Mammal"
    def __init__(self,name) -> None:
        pass
        self.name=name
    def speak(self):
        print(" My name is {} ".format(self.name))
Rodger= Dog(" Rodger")
Tomy = Dog("Tomy")

Rodger.speak()
Tomy.speak()