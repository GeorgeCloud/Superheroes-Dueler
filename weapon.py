from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        random_value = random.randint(self.max_damage//2, self.max_damage)
        return random_value
