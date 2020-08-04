"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Warrior:
    def ___init__(self, health, power):
        self.health = health
        self.power = power 

class Hero(Warrior):
    def __init__(self, health, power):
        super.()__init__(health, power)

class Goblin(Warrior):
    def __init__(self, health, power):
       super.()__init__(health, power)

hiro = Hero(10, 5)
spike = Goblin(6, 2)

    while spike_health > 0 and hiro_health > 0:
        print("You have %d health and %d power." % (hiro_health, hiro_power))
        print("The goblin has %d health and %d power." % (spike_health, spike_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            spike_health -= hiro_power
            print("You do %d damage to the goblin." % hiro_power)
            if spike_health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if spike_health > 0:
            # Goblin attacks hero
            hiro_health -= spike_power
            print("The goblin does %d damage to you." % spike_power)
            if hiro_health <= 0:
                print("You are dead.")

main()
