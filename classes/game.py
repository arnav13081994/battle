import random
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.name = name
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['Attack', 'Magic', 'Items']
        self.items = items

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp = self.hp + dmg
        if self.hp >= self.maxhp:
            self.hp = self.maxhp

    def get_spell_name(self, i):
        return self.magic[i]['name']

    def get_spell_mp_cost(self, i):
        return self.magic[i]['cost']

    def reduce_mp(self, cost):
        self.mp -= cost


    def get_user_magic(self):
        choice = input("\n Choose Magic Spell: ")
        choice = re.sub('[a-zA-Z,.%$#]', "", choice)
        if (choice == ""):
            return "%$#9999"
        elif (int(choice) > len(self.items)):
            return "%$#9999"
        else:
            return int(choice)

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
        print("\n     or enter 0 to go back")

    def choose_action(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ".", item)
            i += 1

    def get_user_action(self):
        choice = input("\n Choose Action: ")
        choice = re.sub('[a-zA-Z,.%$#]', "", choice)
        if (choice == ""):
            return "%$#9999"
        elif (int(choice) > len(self.items)):
            return "%$#9999"
        else:
            return int(choice)

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ". " + item["item"].name + " (x" + str(item["quantity"]) + "): " + item["item"].description)
            i += 1
        print("\n     Or enter 0 to go back")

    def get_user_item(self):
        choice = input("\n Choose Item: ")
        choice = re.sub('[a-zA-Z,.%$#]', "", choice)
        if (choice == ""):
            return "%$#9999"
        elif (int(choice) > len(self.items)):
            return "%$#9999"
        else:
            return int(choice)
