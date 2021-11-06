class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.attack_strength = 50

def __str__(self):
    return f'HERO: {self.name}\ncurrent health: {self.current_health}'

def attack(self, opponent):
    print(f'{self.name} attacked {opponent.name} for {self.attack_strength} health!')
    opponent.current_health -= self.attack_strength
    if opponent.current_health <= 0:
        print(opponent.name, 'died!')
    else:
        print('opponent.name\'s current health: {opponent.current_health}')


if __name__ == '__main__':
    hero1 = Hero('Grace Hopper', 200)
    print(hero1)

    print()

    hero2 = Hero('Elon Musk', 250)
    print(hero2)

    hero2.attack(hero1)


