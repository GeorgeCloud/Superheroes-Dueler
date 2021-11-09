from random import choice

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.kills = 0
        self.deaths = 0

    def add_hero(self, hero):
        self.heroes.append(hero)
        hero.team = self

    def attack(self, other_team):
        living_heroes = [hero for hero in self.heroes]
        living_opponents = [hero for hero in other_team.heroes]

        # import pdb; pdb.set_trace()
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            attacking_hero = choice(living_heroes)
            defending_hero = choice(living_opponents)

            if attacking_hero.is_alive():
                attacking_hero.fight(defending_hero)
            else:
                living_heroes.remove(attacking_hero)
                other_team.kills += 1
                self.deaths += 1

            if defending_hero.is_alive():
                defending_hero.fight(attacking_hero)
            else:
                living_opponents.remove(defending_hero)
                self.kills += 1
                other_team.deaths += 1

        if len(living_heroes) > 0:
            print(f'{self.name} Wins!')
        else:
            print(f'{other_team.name} Wins!')

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            return True

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def view_all_heroes(self):
        return self.heroes

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / (hero.deaths or not hero.deaths)
            print(f"{hero.name} Kill/Deaths:{kd}")
