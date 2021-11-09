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
        self.team = None

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
        if self.is_alive() and opponent.is_alive():
            attack_moves = self.abilities or self.weapons
            for attack_move in attack_moves:
                attack_damage = attack_move.attack()
                print(f'-{self.name} attacked {opponent.name} for {attack_damage}!-')

                opponent.defended(attack_move, attack_damage)
                if opponent.is_alive():
                    print(f'{YELLOW + opponent.name} is still alive with {opponent.current_health}{ENDC}\n')
                else:
                    print(f'{RED + opponent.name} died!{ENDC}\n')
                    self.add_kill(1)
                    opponent.add_death(1)
                    return

    def defended(self, ability, attack_damage):
        while attack_damage > 0:  # consider creating new armor variable
            for armor in self.armors:
                armor_health = armor.block()

                if armor_health - attack_damage > 0:
                    print("BLOCKED!")
                    return  # unbroken armor, regenerates for next fight
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
