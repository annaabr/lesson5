class Warrior():
    def __init__(self, name, power, energy, hair_color):
        self.name = name
        self.power = power
        self.energy = energy
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} is sleeping..")
        self.energy += 2

    def eat(self):
        print(f"{self.name} sat down to eat..")

    def hit(self):
        print(f"{self.name} shits someone..")
        self.energy -= 6

    def walk(self):
        print(f"{self.name} is walking..")

    def info(self):
        print(f"Имя воина -{self.name}}")
        print(f"Цвет волос воина -{self.hair_color}}")
        print(f"Сила воина -{self.power}}")
        print(f"Энергия воина -{self.energy}}")


