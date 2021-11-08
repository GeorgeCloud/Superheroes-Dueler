from ability import Ability
from weapon import Weapon
from armor import Armor
from team import Team

YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.weapons = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def __str__(self):
        return f'HERO: {self.name}\ncurrent health: {self.current_health}'

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def fight(self, opponent):
        if opponent.is_alive():
            for ability in self.abilities:
                attack_damage = ability.attack()
                print(f'{self.name} attacked {opponent.name} for {attack_damage}!')

                if opponent.defended(ability, attack_damage):
                    self.abilities.remove(ability)
                if opponent.is_alive():
                    print(f'{YELLOW + opponent.name} is still alive with {opponent.current_health}{ENDC}')
                else:
                    print(f'{RED + opponent.name} died!{ENDC}')
                    return

    def defended(self, ability, attack_damage):
        while attack_damage > 0:  # consider creating new armor variable
            for armor in self.armors:
                armor_health = armor.block()

                if armor_health - attack_damage > 0:
                    return True  # unbroken armor, regenerates for next fight
                else:
                    attack_damage -= armor_health
                    self.armors.remove(armor)
                    print(f'{YELLOW + self.name}\'s {armor.name} broke!! -{armor_health}{ENDC}')
            break

        # opponent has no shields left
        if attack_damage > 0:
            print(f'{RED + self.name} took a direct hit of {attack_damage}!{ENDC}')
            self.current_health -= attack_damage

        return

    def is_alive(self):
        return self.current_health > 0


if __name__ == '__main__':
    # Team 1 attack moves
    bite = Ability('Bite', 10)
    sword = Weapon('Sword', 10)

    # Team 2 attack moves
    ray_gun = Weapon('Space Gun', 10)
    fireball = Ability('Fire Ball', 10)

    # Armor
    wither_armor  = Armor("Wither Armor", 15)
    diamond_armor = Armor("Diamond Armor", 10)
    iron_armor    = Armor("Iron Armor", 5)
    blanket_armor = Armor("Blanket Armor", 1)

    # Team 1
    team_candy = Team('Candy Kingdom')
    hero1 = Hero('Finn The Human', 10)
    hero1.add_weapon(sword)
    hero1.add_armor(blanket_armor)

    hero2 = Hero('Marceline the vampire', 10)
    hero2.add_ability(bite)
    hero2.add_armor(wither_armor)

    # Team 2
    team_fire  = Team('Fire Kingdom')
    hero3 = Hero('Princess BubbleGum', 10)
    hero3.add_weapon(sword)
    hero3.add_armor(diamond_armor)

    hero4 = Hero('Flame Princess', 10)
    hero4.add_ability(fireball)
    hero4.add_armor(iron_armor)

    team_candy.add_heroes([hero1, hero2])

    team_fire.add_heroes([hero3, hero4])

    # hero2.fight(hero1)

