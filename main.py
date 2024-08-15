class Warrior():
    def __init__(self, name, power, energy, hair_color):
        self.name = name
        self.power = power
        self.energy = energy
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} спит..")
        self.energy += 2

    def eat(self):
        print(f"{self.name} кушает..")

    def hit(self):
        print(f"{self.name} бьет кого-то..")
        self.energy -= 6

    def walk(self):
        print(f"{self.name} гуляет..")

    def info(self):
        print(f"Имя воина - {self.name}")
        print(f"Цвет волос воина - {self.hair_color}")
        print(f"Сила воина - {self.power}")
        print(f"Энергия воина - {self.energy}")

war1 = Warrior("Степа", 76, 54,"коричневый")
print(war1.name)

print(war1.energy)
war1.sleep()
print(war1.energy)
war1.eat()
print(war1.energy)
war1.walk()
print(war1.energy)
war1.hit()
print(war1.energy)
war1.info()