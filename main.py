from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


#Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Mega Elixer", "elixer", "Fully restores HP/MP of all party members", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


# Create Black Magic
fire = Spell('Fire', 10, 100, "black")
thunder = Spell('Thunder', 12, 124, "black")
blizzard = Spell('Blizzard', 10, 100, "black")
meteor = Spell('Meteor', 20, 200, "black")
quake = Spell('Quake', 14, 140, "black")

#Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

#Instantiate People
player_spells = [fire, thunder, blizzard, meteor, cure]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 5},
                {"item": grenade, "quantity": 5}]

player1 = Person("Valos", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Nick", 460, 65, 60, 34, player_spells, player_items)
player3 = Person("Robot", 460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks!" + bcolors.ENDC)
running = True

while running:

    if enemy.hp == 0:
        print(bcolors.OKGREEN + "You Win" + bcolors.ENDC)
        break
    elif player.hp == 0:
        print(bcolors.FAIL + "Your Enemy has defeated you!" + bcolors.ENDC)
        break


    print("\n Select from the following actions: ")
    player.choose_action()
    choice = player.get_user_action()


    if choice == 1:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("\n The player attacks for " + bcolors.FAIL + bcolors.BOLD + str(dmg) + bcolors.ENDC +  " points." +  "\n Enemy's current HP: " + bcolors.FAIL + bcolors.BOLD +  str(enemy.hp) + bcolors.ENDC + "\n Your HP: " + str(player.hp))

    elif choice == 2:
        player.choose_magic()
        choice = player.get_user_magic()
        if choice == 0:
            continue
        elif choice == "%$#9999":
            print("Invalid Input. Try again \n")
            continue
        else:
            if player.mp < player.magic[choice - 1].cost:
                print("\n You cannot use this spell. Not enough MP. You have " + player.mp + " MP")
                continue

            elif player.magic[choice - 1].type == "white":
                heal = player.magic[choice - 1].generate_damage()
                player.heal(heal)
                player.reduce_mp(player.magic[choice - 1].cost)
                print("\n The player has healed by " + str(heal) + " points. The new HP is " + str(player.hp))

            elif player.magic[choice - 1].type == "black":
                dmg = player.magic[choice - 1].generate_damage()
                enemy.take_damage(dmg)
                player.reduce_mp(player.magic[choice - 1].cost)
                print("\n The player attacks for %s points.\n Enemy's current HP is: %s. \n Your HP is: %s and you currently have %s MP" %(dmg, enemy.hp, player.hp, player.mp))

    elif choice == 3:
        player.choose_item()
        choice = player.get_user_item()
        if choice == 0:
            continue
        elif choice == "%$#9999":
            print("Invalid Input. Try again \n")
            continue
        else:
            item = player.items[choice-1]
            if item["quantity"] == 0:
                print("\n You cannot use this item. Not enough MP. ")
                continue
            elif item["item"].type == "potion":
                player.heal(item["item"].prop)
                item["quantity"] -= 1
                print(bcolors.OKGREEN + "\n" + item["item"].name + " heals for " + str(item["item"].prop) + " HP" + bcolors.ENDC + "\n And you have " + str(item["quantity"]) + " more left")
            elif item["item"].type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                item["quantity"] -= 1
                print(bcolors.OKGREEN + "\n" + item["item"].name + " heals MP and HP to " + str(player.hp) + " and" + str(player.mp) + " respectively." + bcolors.ENDC + "\n And you have " + str(item["quantity"]) + " more left")
            elif item["item"].type == "attack":
                dmg = item["item"].prop
                enemy.take_damage(dmg)
                item["quantity"] -= 1
                print(bcolors.FAIL + "\n" + item["item"].name + " deals " + str(item["item"].prop) + " points of damage" + bcolors.ENDC + "\n And you have " + str(item["quantity"]) + " more left")
    else:
        print("Invalid Action. Try again")
        continue

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("\n Enemy Attacks for", enemy_dmg, "points.\n Player HP is ", player.hp)



print("My name is {}".format("Arnav"))