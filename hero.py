from ability import Ability
from armor import Armor

YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = [Ability("Debugging Ability", 20)]
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def __str__(self):
        return f'HERO: {self.name}\ncurrent health: {self.current_health}'

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def fight(self, opponent):
        if opponent.current_health > 0:
            for ability in self.abilities:
                attack_damage = ability.attack()
                print(f'{self.name} attacked {opponent.name} for {attack_damage}!')

                if opponent.defended(ability, attack_damage):
                    self.abilities.remove(ability)

                if opponent.is_alive():
                    print(f'{YELLOW + opponent.name} is still alive with {opponent.current_health}{ENDC}')
                else:
                    print(f'{RED + opponent.name} died!{ENDC}')

    def defended(self, ability, attack_damage):
        while self.armors and attack_damage > 0:  # consider creating new armor variable
            for armor in self.armors:
                armor_health = armor.block()
                # armor_health_left = armor_health - attack_damage

                if armor_health - attack_damage > 0:
                    # armor_health -= attack_damage
                    return True  # unbroken armor, regenerates for next fight
                else:
                    attack_damage -= armor_health
                    self.armors.remove(armor)
                    print(f'{YELLOW + self.name}\'s {armor.name} broke!!{ENDC}')

        # opponent has no shields left
        if attack_damage > 0:
            print(f'{RED + self.name} took a direct hit of {attack_damage}!{ENDC}')
            self.current_health -= attack_damage
            return

    def is_alive(self):
        return self.current_health > 0


if __name__ == '__main__':
    hero1 = Hero('Grace Hopper', 10)
    shield1 = Armor("Knight Armor", 5)
    shield2 = Armor("Wither Armor", 5)
    hero1.add_armor(shield1)
    hero1.add_armor(shield2)

    hero2 = Hero('Elon Musk', 10)
    attack2 = Ability("Debugging Ability", 20)
    hero2.add_ability(attack2)

    hero2.fight(hero1)
