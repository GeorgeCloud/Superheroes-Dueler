class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_heroes(self, heroes=[]):
        for hero in heroes:
            self.heroes.append(hero)

    def remove_hero(self, hero):
        self.heroes.remove(hero)

    def view_all_heroes(self):
        return self.heroes

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")
