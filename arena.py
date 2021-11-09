from ability import Ability
from weapon import Weapon
from armor import Armor
from team import Team
from hero import Hero

class Arena:
    def __init__(self, team_one_name, team_two_name):
        self.team_one = Team(team_one_name)
        self.team_two = Team(team_two_name)
        self.heroes = []

    def create_ability(self):
        """ Returns Ability instance with values from user Input"""
        name = input('What is the ability name: ')
        max_damage = input('What is the max damage of the ability: ')

        return Ability(name, max_damage)

    def create_weapon(self):
        """ Returns Weapon instance with values from user input. """
        name = input('What is the weapon name:  ')
        max_damage = input('What is the max damage of the weapon: ')

        return Weapon(name, max_damage)

    def create_armor(self):
        """ Returns Armor instance with values from user input. """
        name = input('What is the armors name: ')
        max_health = input('What is the max health of the armor: ')

        return Armor(name, max_health)

    # build_team_one is provided to you
    def build_team_one(self):
        """ Prompt the user to build team_one. """
        num_of_team_members = int(input('How many members would you like on Team One: '))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
            self.heroes.append(hero)

    def create_hero(self):
        """ Returns Hero instance with values from user input. """
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != '4':
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == '1':
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == '2':
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == '3':
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_two(self):
        """ Prompt the user to build team_two. """
        num_of_team_members = int(input('How many members would you like on Team Two: '))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
            self.heroes.append(hero)

    def team_battle(self):
        """ Battle team_one and team_two together. """
        self.team_one.attack(self.team_two)

    def show_stats(self):
        """ Prints team statistics to terminal. """
        print("\n")
        print(f'{self.team_one.name}  statistics: ')
        self.team_one.stats()
        print("\n")
        print(f'{self.team_two.name}  statistics: ')
        self.team_two.stats()
        print("\n")

        # Calculate the average K/D for each team
        if self.team_one.deaths == 0:
            self.team_one.deaths = 1

        if self.team_two.deaths == 0:
            self.team_two.deaths = 1

        print(self.team_one.name + " average K/D was: " + str(self.team_one.kills / self.team_one.deaths))
        print(self.team_two.name + " average K/D was: " + str(self.team_two.kills / self.team_two.deaths))

        # Heroes that survived
        for hero in self.heroes:
            if hero.deaths == 0:
                print("survived from " + hero.team.name + ": " + hero.name)


if __name__ == "__main__":
    arena = Arena('team 1', 'team 2')
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
