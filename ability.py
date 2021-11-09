import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = int(max_damage)

    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value
