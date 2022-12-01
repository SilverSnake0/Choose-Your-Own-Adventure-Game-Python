import random

# This list allows the player to type different forms of "yes" for variety.
yes = ['y', 'yes', 'ya', 'yep', 'yup', 'yeh', 'ye', 'yea', 'totally', 'sure', 'ok', 'okay', 'alright', 'alrighty', 'alrighty then', 'certainly', 'definitely', 'glady', 'absolutely', 'indeed', 'undoubtedly', 'fine', 'aye', 'surely', 'mmhmm', 'mhmm', 'of course','k', 'kk', 'very well', 'for sure', 'you bet', 'no problem', 'i guess so', 'why not', 'hell yes', 'hell yea', 'heck yea', 'naturally', 'okie dokie', 'affirmative', 'aye aye', 'uh huh', 'yuppers', 'yes sir', 'yes mam', 'by all means', 'cool', 'no problem', 'sure why not', 'sure no problem', 'i do', 'love to', 'good', 'as you wish', 'i shall', 'sure i can', 'willingly', 'exactly', 'for sure', 'si', 'hao', 'da', 'ja', 'hai', 'sim', 'oui', 'ayo', 'yea sure']
# Used for the bank heist minigame
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Current hero items list which more items will be added to it, depending on player progress in the game.
hero_items = [
    '💰', '🍲 - Chicken soup', '🥢- Chopsticks', '🥐 Croissant', '🧥 - Coat', '🍶 - Jar of Fresh Water', '🛌- Pillow and Sleeping Bag']
# Currently held trade items for the trade mission story.
hero_land_items = {
    '🐎': 0, '☕️': 0, '🌽': 0, '🍯': 0, '🦪': 0, '🍍': 0, '🐡': 0, '🍨': 0, '⚗️': 0
}
# These are ascii art of swords which will be properly displayed in the game vendor menu. \n is new line.
rusty_sword = '    /\n0===[====================-\n    \\'
sword_one = '          ./\n()=@XXXXX@=[0}================--\n          `\_'
sword_two = "            /\ \n/vvvvvvvvvvvv \--------------------------------------,\n`^^^^^^^^^^^^ /=====================================\" \n            \/"
mythic = " ,.\n \%`.\n  `.%`.\n    `.%`.\n      `.%`.\n        `.%`.\n          `.%`.    __\n            `.%`.  \ \\ \n              `.%`./_/\n                `./ /.\n               __/\/:/;.\n               \__/  `:/;.\n                       `:/;.,   \n                    Krogg`:/ ;\n                           `'\n"
mythic_two = "                _\n               /\)\n              /\/\n             /\/\n           _/L/\n          (/\_)\n          /%/  \n         /%/  \n        /%/\n       /%/\n      /%/\n     /%/\n    /%/\n   /%/\n  /%/\n /%/ Krogg\n/,'\n\" "
# Special items that add different abilities in monster battles.
battle_items = [
    '🏺- Invisibility Potion', '🔮Merlin\'s Crystal Ball', '☄️Fireball Spell', '🍶Elixir of the Gods', '👾Ancient Drone']
def exit_game():
    exit()

def adventure_game():
    bulletpoint = '✴ ' # Used to emphasize requiring the user's input for the story.
    bulletpoint2 = '◼ '# Regular bulletpoint for sentences not requiring user's input.
    body_part = 'arm' # Fixed string to be inserted into parts of the story. This variable can be changed later.
       
    def restart():
        vendor_lady_object = 1 

        class Item:
            # Constructor function for the Item class.
            def __init__(self, name, health_bonus, attack_bonus):
                self.name = name
                self.health_bonus = health_bonus
                self.attack_bonus = attack_bonus

            def bonus(self):
                print(
                    f'Item Name: {self.name}  Bonus Health: {self.health_bonus}  Bonus Attack: {self.attack_bonus}')
        # Vendor items plus various items that can be found in the game.
        hunting_knife = Item('🗡- Rusty Hunting Knife', 2, 2)
        invisibility_potion = Item('🏺- Invisibility Potion', 0, 0)
        old_rusty_sword = Item('🗡- Old Rusty Sword', 0, 5)
        jeweled_blade = Item('🗡- Jeweled Blade', 0, 20)
        masamune_katana = Item('🗡- Masamune Katana', -99, 150)
        krogg_moon_blade = Item('🗡- Krogg Moon Blade', 200, 0)
        krogg_moon_katana = Item('🗡- Krogg Moon Katana', 0, 50)
        ringofnirvana= Item('⛣- Ring of Nirvana', 200, 0)
        valkyrie_crossbow = Item('🏹- Valkyrie', 200, 50)
        boomerang = Item('🪃- Boomerang', 0, 15)
        thors_hammer = Item('⚒️- Thor\'s Hammer', 100, 100)
        redempireflag = Item('🚩- Red Empire Flag', 100, 0)
        dragonscale = Item('🛡️- Dragonscale', 200, 0)


        class Hero:

            health = 0
            money = 0
            morality = 0
            damage = 25
            # Constructor function for the hero class.
            def __init__(self, name, health, money, morality):
                self.name = name
                self.health = health
                self.money = money
                self.morality = morality
            # Hero attacks a fixed amount of damage, which is currently 25.
            def attack(self):
                print(self.damage)
                return self.damage
            # Adds item's health and attack attributes to the main hero. This also checks if it's not in hero items and will add the name to the list, which will be shown in the menu.
            def add_item(self, item):
                self.health += item.health_bonus
                self.damage += item.attack_bonus
                if item.name not in hero_items:
                    hero_items.append(item.name)
        # Instantiating the main basic hero.
        hero = Hero(hero_name, 100, 20, 50)

        class Monster:
            # Constructor function for the Monster class.
            def __init__(self, name, health, min_damage, max_damage):
                self.name = name
                self.health = health
                self.min_damage = min_damage
                self.max_damage = max_damage
            # Everytime a new monster attacks, it generates a random damage amount between the minimum and maximum number set. This amount will change depending on chance everytime you encounter the monster.
            def attack(self):
                damage = (random.randint(self.min_damage, self.max_damage))
                print(damage)
                return damage
        # Current monsters list. The paramaters are the name, health, minimum damage, and max damage.
        sandworm = Monster('Sandworm', 100, 20, 80)
        giant = Monster('Giant', 100, 15, 70)
        arachne = Monster('Arachne', 100, 15, 80)
        tiamat = Monster('Tiamat', 999, 99, 250)
        merlin = Monster('Merlin', 250, 80, 300)
        robots = Monster('Robots', 90, 25, 50)
        kitty = Monster('Kitty Kat', 120, 75, 130)
        fenrir = Monster('Fenrir', 200, 85, 200)
        alexa9000 = Monster('Alexa 9000', 160, 80, 150)
        griffin = Monster('Griffin', 125, 80, 180)
        skeletonwarrior = Monster('Skeleton Warrior', 100, 60, 180)
        boxer = Monster('Boxer', 150, 60, 150)
        leviathan = Monster('Leviathan', 999, 99, 200)
        phoenix = Monster('Phoenix', 350, 90, 200)
        
        # Function that 1. Checks if the monster has died, 2. Checks if person has died and then restarts/exits game
        def check_health(person):
            if person.health <= 0:
                print(f'{person.name} has lost all health and died!')
                if type(person) == Hero:
                    try_again = input('=( Restart Game..?')
                    if try_again.strip().lower() in yes:
                        restart()
                    else:
                        print(''' ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄   ▄ ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄      ▄▄▄▄▄▄▄ ▄▄▄     ▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ 
█       █  █ █  █      █  █  █ █   █ █ █       █  █       █       █   ▄  █    █       █   █   █      █  █ █  █   █  █  █ █       █
█▄     ▄█  █▄█  █  ▄   █   █▄█ █   █▄█ █  ▄▄▄▄▄█  █    ▄▄▄█   ▄   █  █ █ █    █    ▄  █   █   █  ▄   █  █▄█  █   █   █▄█ █   ▄▄▄▄█
  █   █ █       █ █▄█  █       █      ▄█ █▄▄▄▄▄   █   █▄▄▄█  █ █  █   █▄▄█▄   █   █▄█ █   █   █ █▄█  █       █   █       █  █  ▄▄ 
  █   █ █   ▄   █      █  ▄    █     █▄█▄▄▄▄▄  █  █    ▄▄▄█  █▄█  █    ▄▄  █  █    ▄▄▄█   █▄▄▄█      █▄     ▄█   █  ▄    █  █ █  █
  █   █ █  █ █  █  ▄   █ █ █   █    ▄  █▄▄▄▄▄█ █  █   █   █       █   █  █ █  █   █   █       █  ▄   █ █   █ █   █ █ █   █  █▄▄█ █
  █▄▄▄█ █▄▄█ █▄▄█▄█ █▄▄█▄█  █▄▄█▄▄▄█ █▄█▄▄▄▄▄▄▄█  █▄▄▄█   █▄▄▄▄▄▄▄█▄▄▄█  █▄█  █▄▄▄█   █▄▄▄▄▄▄▄█▄█ █▄▄█ █▄▄▄█ █▄▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█''')
                        exit_game()
            else:
                pass
        # Function to randomly add a certain amount of money depending on the scenario.
        def add_money(min, max):
            new_money = random.randint(min, max)
            hero.money += new_money
            print(f'{bulletpoint2}{hero.name} earned ${new_money}!')

        def add_health(person):
            try: # Try and except added for monsters that have already been killed. This is in case the function is called before the monster, so it won't add health to monsters that have not been encountered yet.
                if type(person) == Monster: # adding health to monsters that have been killed already.
                    if person.health <= 0:
                        if person.name == 'Tiamat':
                            person.health = random.randint(999, 10000)
                        else:
                            person.health = random.randint(250, 500)
                    else:
                        pass
                else: # Adding health to heroes by a random interval between 25 to 100.
                    random_health_gain = random.randint(25, 100)
                    print(
                        f'{bulletpoint2} You took some rest and gained {random_health_gain} health.')
                    person.health += random_health_gain
                    if hero.health <= 0: # In the scenario where the hero gained health, but health is still below 0, they will still die and game will restart.
                        print(
                            f'{bulletpoint2} Although you tried to rest and regain some health, you still died from your injuries. You did not make it =(')
                    check_health(hero) # Used to restart the game since hero is below 0 health.
            except:
                pass
            # Leviathan image to be used for both in the battle summons and the sailing trade mission.
        levi_image = '''
                    ⠈⠻⡗⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡤⠤⠶⠿⣶⣦⣄⣙⣦⠙⢿⡓⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠭⣉⠓⠒⠚⠽⡄⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣋⡿⠀⠀⠀⣀⡽⠀⠀⠀⠘⢈⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡆⢠⠖⠚⣇⠀⣙⡶⠄⠈⠰⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠐⣧⣾⡄⣄⠘⣆⡈⠷⠄⣤⣶⠈⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠛⣦⣘⢿⣇⣿⣿⠉⠹⣗⠦⣈⠘⣾⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢱⡾⠛⣏⠿⠧⡀⠈⠳⣄⡙⠊⠉⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡤⣤⡴⠉⠀⠀⠈⢳⡀⠑⠦⡀⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣬⠷⢮⣙⣒⣤⡤⠀⠀⢹⡄⡄⢱⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠛⠳⣄⠀⠀⠀⠀⠠⣌⣩⠿⠀⠒⣼⡇⠇⠈⠳⡄⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣹⣤⣖⣸⣍⣿⠽⠤⠒⠚⠋⠀⠀⠀⠀⢸⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠋⠉⠉⠀⠀⠀⠀⣠⡤⠂⠀⠀⢠⡀⢰⠋⠀⢠⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⠤⣶⡾⠅⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⢺⠀⠀⠀⢈⣇⠜⠃⠀⣾⡈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⠇⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠋⠈⠀⠀⢠⠞⠋⠀⢀⡾⠁⠉⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣏⡼⠁⠀⠀⠀⢀⡤⠤⠔⠊⢉⣡⠼⠓⠀⠀⢀⣴⣋⣀⡠⠶⠻⣄⡀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⡿⠁⢠⠔⠒⠚⢋⡤⠖⠊⢩⡟⠀⠀⢀⣠⠞⠋⠉⠁⠀⠀⠀⠀⠀⠉⢹⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢼⢻⠇⡤⠇⠀⢀⣴⠋⠀⠀⠀⣼⣠⠴⠚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⣀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⣿⡰⠂⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡇⠀⠀⣏⢻⡀⢀⣠⠴⠛⠉⠓⠢⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢿⣄⡀⠘⢆⡙⠋⠀⢀⡠⠔⠦⠐⠒⣚⠙⣲⡦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⢧⡀⠀⠈⠉⠉⠁⣀⠀⣀⡴⠚⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⣶⣤⡀⠉⠘⠛⠻⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠳⡌⠁⠒⢄⠀⠈⠑⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠤⣄⣁⣀⣀⣀⣛⣲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
        levi_image2 = '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣷⣄⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠿⣤⣾⣿⣽⡿⠛⣆⣬⣿⣅⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⡟⣟⠁⠀⠀⠀⠉⠁⡀⠀⡚⠉⠀⠈⠹⡶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣤⠶⠶⠒⢛⣉⡭⠞⠁⠈⠙⢷⡤⠴⠶⢤⡴⠞⠋⢻⣧⡤⣦⡀⠀⠀⠈⣇⡈⠛⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡴⠛⣡⠤⠖⠚⠛⠉⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⡏⠁⠀⠀⠙⢦⡀⠀⠨⣧⠀⠀⣿⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣤⠴⠛⠁⣠⠞⠁⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⣡⠏⠀⠀⠀⠀⣀⡠⢿⡀⢰⠿⣤⠀⢘⠋⠉⠻⣆⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠋⠁⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⣰⠋⠀⠀⠀⣰⠞⠁⠀⠀⠉⠁⠀⠹⠗⠻⡆⠀⠀⠻⣯⡉⢣⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣾⠀⠀⠀⠀⣰⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠰⡏⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⢀⣀⡀⠀⠈⣽⡄⠀⠀⣼⡿⣾⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢻⣤⠀⠀⠀⠹⡆⠀⠠⡄⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⣶⣧⠀⠀⠀⡇⠀⠀⠀⠀⣠⠞⠉⣸⡿⠿⠿⡶⣽⣦⣶⠿⢦⠈⠳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⢹⡀⠀⠀⠀⠹⣆⠀⠙⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠋⣿⠀⠀⣇⡇⠀⢀⠀⣼⠁⡤⠟⠁⣀⣀⣰⣖⣚⠋⠀⠀⢸⠀⠀⢘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡄⠀⠀⠈⢧⡀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⢳⠀⠀⢸⣇⠀⡿⠇⣿⡾⢁⡴⣋⣉⣀⣉⠃⠉⢢⡀⠀⢸⠀⠀⠀⢿⣤⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⢦⣀⣀⠀⠙⠢⣄⠀⠀⠀⠈⠳⢦⡀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠉⢀⡇⡇⣷⢃⣏⡾⠉⠀⠀⠉⠙⢶⣶⣿⣄⣿⡄⠀⠀⠘⢿⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠙⠲⢤⣀⡉⠳⠦⣄⡀⠀⠙⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⡇⡟⣺⡿⠀⠀⠀⠀⠀⠀⠀⠻⢿⠁⠙⣷⡀⠀⠀⠀⣇⠘⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢢⣶⢄⡀⠀⠀⠀⠀⠉⠓⠦⠤⣉⣓⠦⣄⡀⠙⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠿⣧⡀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣄⢹⣿⡄⠀⠀⣿⠤⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠓⢭⣓⠒⠒⠒⠒⠲⠤⣄⡀⠀⠉⠛⠛⠿⠦⣄⣙⠳⢤⡀⠀⠀⠀⠀⠀⠸⡄⠈⢧⢷⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢯⢏⣿⣶⡄⢹⡇⢈⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠓⠲⢤⣤⣀⣀⠀⠉⠓⠲⠤⠔⠶⢴⣤⣭⣉⠀⠈⠓⠦⣄⠀⠀⠀⢻⡄⠈⣞⣆⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠻⣞⢿⣼⣧⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣶⣤⣀⠀⠀⠀⠀⠉⠙⠦⣤⣤⣀⣤⣤⣤⣀⣀⡀⠉⠳⢦⣀⠀⠀⠀⠀⠀⠙⣄⡈⢯⢪⡻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢾⣽⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢹⣦⡍⠓⠶⠤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠲⠤⣍⣙⣳⣦⡀⠀⠀⠀⠙⠶⣷⣹⣟⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⠿⣇⡀⠀⠀⠀⠀⠉⠛⠛⠒⠒⠦⠤⢤⣤⣀⡀⠀⠀⠀⠀⠈⠙⠀⠀⢤⠀⠀⠀⠀⠀⠻⢧⡉⠳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠲⠤⣄⡀⠀⠀⠀⣦⣄⣀⣀⡐⠺⠯⣤⣀⣀⣀⣀⣀⡀⠀⠀⠈⠓⢄⡀⠀⠀⠀⠀⠉⠲⢬⡙⠳⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠲⢤⣌⣓⠮⣭⣉⠙⠓⠒⠒⠦⠬⠭⢭⣽⣷⠶⣦⣀⠀⠙⠲⣤⡀⠀⠀⠀⠀⠉⠳⢤⣉⠛⠲⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠷⣄⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠑⠚⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠳⣄⠀⠀⠉⠉⠒⠲⠶⣄⠀⠀⠈⠙⠲⠶⠮⢝⣲⡦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⠶⢾⠏⠉⠋⠙⠲⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⡿⢕⡲⠶⢤⣀⠀⠀⠙⣄⠈⠳⢄⡀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠉⠑⠚⠿⠷⠦⣄⣀⡀⠀⠀⠀⠀
⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⣄⡀⠀⠰⠴⣤⡤⠤⠤⠾⠋⠙⠃⢀⣀⣨⠿⠦⠀⠈⠑⢄⡀⠙⠲⢤⣄⡀⠀⠀⠈⠙⠲⠤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠒⠤⢄
⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣀⣀⠙⢦⡀⠀⠈⠉⠓⠢⢤⣀⠀⠘⠿⢤⣄⡀⠀⠀⠀⠀⠀⠉⠒⢦⣄⣈⡉⠒⠦⣤⣀⠀⠀⠀⠉⠙⠒⠲⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠉⠓⠚⠓⠦⣄⡀⠀⠀⠀⠉⠑⠺⣭⡑⠛⠂⠀⠀⠀⠀⠀⠈⠙⠲⢦⣀⣈⣙⠓⠦⣄⡀⠀⠀⠀⠀⠀⠉⠉⠙⠒⠒⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠓⠒⠲⠦⠤⣤⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⢦⡀⠀⠀⠀⠀⠉⠓⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠈⠉⠑⠾⢍⣦⣄⠀⠀⠀⠀⠀⠀⠀⠤⠤⠤⠤⠤⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣚⣇⡀⠀⠀⠀⠀⠀⠈⠙⠲⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣛⣷⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠓⠲⠤⠤⣄⣀⠀⠀⠈⠙⠲⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 '''
        # Simulate a Battle system between a hero and a monster. This implements a block, counter, and attack style system. The first two arguments take two entities that are battling, and then the rest are the string names of the monster moves.
        def battle(person, monster, defend, weak, counter, attack):
            print('Monster Attack Damage:')
            monster_attack = monster.attack()  # Returns random monster damage number
            print('Player Attack Damage:')
            person_attack = person.attack()  # Returns fixed person damage number
            monster_potential_moves = [defend, weak, counter, attack]
            print('The Monster has the option to defend, counter, or attack you. They also have a weak point...')
            # Display the health and attack damage of hero and monster, and added the menu bar
            def battle_Health_Menu():
                print(
                    f'''▛▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▜\n Hero Health: {person.health}            Monster Health: {monster.health}\n Hero Attack Damage: {person_attack}      Monster Attack Damage: {monster_attack}''')
            # Combined the battle menu with the checking health function together to make it easier to call for the code below.
            battle_Health_Menu()
            def battlemenu():
                battle_Health_Menu()
                check_health(monster)
                check_health(person)
            invisibility_count = 3 # Number of times user can use the invisibility potion.
            while monster.health >= 0:
                # Breaks out of the while loop once monster health reaches less than 0
                if monster.health <= 0:
                    break
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
                # If there are items existing in the battle_items list, then it will print the special item commands to be shown in the battle menu.
                if battle_items:
                    for i in battle_items:
                        if i in hero_items: # Double checks to make sure battle item exists in hero items
                            print(f'{bulletpoint2}Special Item Commands:')
                            if i == '🏺- Invisibility Potion':
                                print(
                                    f'{bulletpoint2}{i} Command: "abracadabra"  Uses Left: {invisibility_count}')
                            
                monster_moves = random.choice(monster_potential_moves)
                print(f'The {monster.name} {monster_moves}...')
                person_move = input('Do you defend, counter, or attack?\n')
                if person_move == 'defend': # Scenarios where the hero selected DEFEND
                    if monster_moves == defend:  # If person DEFENDED and monster DEFENDED
                        print(f'Both {person.name} and {monster.name} defended.\n')
                    elif monster_moves == counter:  # If person DEFENDED and monster COUNTERED
                        print(
                            f'{bulletpoint2}{person.name} successfully defended the attack!\n')
                    elif monster_moves == weak:  # If person DEFENDED and monster was WEAK
                        print(f'Nothing happened.\n')
                    else:  # If person DEFENDED and monster ATTACKED
                        print(
                            f'{bulletpoint2}{person.name} successfully blocked the attack!\n')
                elif person_move == 'counter':
                    if monster_moves == defend:  # If person COUNTERED and monster DEFENDED
                        print(
                            f'{person.name} countered and {monster.name} blocked the attack.\n')
                    elif monster_moves == counter:  # If person COUNTERED and monster COUNTERED
                        monster_counter_damage = monster_attack / 2
                        person_counter_damage = person_attack / 2
                        print(f'{bulletpoint}{monster.name} dealt {monster_counter_damage} damage to {person.name}, but was countered and {monster.name} took {person_counter_damage} damage!\n')
                        monster.health -= person_counter_damage
                        person.health -= monster_counter_damage
                        battlemenu()
                    elif monster_moves == weak:  # If person COUNTERED and monster was WEAK
                        print(f'Nothing happened.\n')
                    else:  # If person COUNTERED and monster ATTACKED

                        print(
                            f'{bulletpoint}{monster.name} dealt 0 damage to {person.name}, and was countered. {monster.name} took {person_attack} damage!\n')
                        monster.health -= person_attack
                        battlemenu()
                elif person_move == 'attack':  # Scenarios where the hero selected ATTACK
                    if monster_moves == defend:  # If person ATTACKED and monster DEFENDED
                        print(
                            f'{person.name} tried attacking but {monster.name} blocked the attack.\n')
                    elif monster_moves == counter:  # If person ATTACKED and monster COUNTERED
                        print(
                            f'{person.name} dealt 0 damage to {monster.name}, {person.name} was countered and took {monster_attack} damage.')
                        person.health -= monster_attack
                        battlemenu()
                    elif monster_moves == weak:  # If person ATTACKED and monster was WEAK
                        print(
                            f'{bulletpoint}{person.name} dealt {person_attack} damage to {monster.name}!\n')
                        monster.health -= person_attack
                        battlemenu()
                    else:  # If person ATTACKED and monster ATTACKED
                        print(f'{bulletpoint}{person.name} dealt {person_attack} damage to {monster.name}, {monster.name} also attacked and dealt {monster_attack} damage to {person.name}.\n')
                        monster.health -= person_attack
                        person.health -= monster_attack
                        battlemenu()
                # Random summons generated.
                elif person_move.lower().strip() == 'summonthegods': 
                    summons = [
                        'Bahamut. A massive colossal monster that holds up the structure of Gaia. The earth below shakes and then everyone is lifted into the air from the forces of gravity. Bahamut throws a cosmic moon',
                        'Leviathan. A legendary sea serpent monster which is the embodiment of chaos and encapsulates the space of the material world. You hear the crashing of water, and then all of a sudden you see a massive blue wall in the distance. Leviathan summoned a 1,000 foot high wave that crashes', 
                        'Hellfire. A demon that lies in the underbelly of the earth with the temperature of 1,000 burning suns. The ground turns to lava and you see everything nearby melting. Hellfire\'s eyes glow red, blowing fire from its mouth', 
                        'Shiva. The supreme being known to create and also known as "The Destroyer". The atmosphere becomes so windy, that it\'s faster than the most violent tornado. Shiva assembled 10,000 diamond tipped arrows in the air which shoots across',
                        'Odin. A highly revered god wielding a spear. Odin summons a dark storm that shadows the battlefield. A powerful lightning bolt shoots down']
                    summoned = random.choice(summons) # Selects a random summon from the summoned list.
                    if summoned == summons[0]:
                        print('''
                                        .                                            .
     *   .                  .              .        .   *          .
  .         .                     .       .           .      .        .
        o                             .                   .
         .              .                  .           .
          0     .
                 .          .                 ,                ,    ,
 .          \          .                         .
      .      \   ,
   .          o     .                 .                   .            .
     .         \                 ,             .                .
               #\##\#      .                              .        .
             #  #O##\###                .                        .
   .        #*#  #\##\###                       .                     ,
        .   ##*#  #\##\##               .                     .
      .      ##*#  #o##\#         .                             ,       .
          .     *#  #\#     .                    .             .          ,
                      \          .                         .
____^/\___^--____/\____O______________/\/\---/\___________---______________
   /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __

Robert Casey
                        ''')
                    elif summoned == summons[1]:
                        print(levi_image)
                        print(levi_image2)
                    elif summoned == summons[2]:
                        print('''
                            ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      \\
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \\`\ |  |  | /,//' \,'  \\
eViL        /   /     ||--+--|--+-/-|     \   \\
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'
                        ''')
                    elif summoned == summons[3]:
                        print('>>>>>----------------------->    '*50)
                    elif summoned == summons[4]:
                        print('''
                                  ⢰⡖⢺⡟⠛⠛⣗⠒⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠞⣿⠈⢷⠀⢸⠇⣰⠟⠶⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⢿⡦⠖⠚⣿⡆⠸⣆⡏⢀⣿⡛⠲⠦⣽⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡏⢀⡿⠀⠀⣰⠏⢻⡄⠀⢀⣼⠉⣧⡀⠀⢹⡇⠘⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡾⠁⡇⢸⠓⠚⠻⣷⠤⠈⣿⣿⢻⡇⠀⣼⡟⠛⠚⠷⢀⡇⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠛⡇⢠⡷⠖⠒⣾⠛⣡⣤⠞⣁⡿⣆⡛⢦⣌⡙⢿⡛⠒⠾⡇⠈⡟⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⡇⣨⣤⣴⠞⠻⠟⢹⣿⠟⠉⠀⠈⠙⢶⡏⠙⠿⠻⣶⣤⣄⣀⡇⢸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⡇⠀⠛⠁⣴⠇⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⢷⡀⠙⠓⢸⡟⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣺⠁⢷⠀⣠⣾⡏⠀⢠⣤⣤⣤⣤⣀⣤⣤⣤⣄⣠⣤⣤⣤⣄⠀⠘⣿⣦⡀⢸⠇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠸⠟⠉⢸⡇⠀⢈⣶⡷⣷⣤⣹⣆⠀⢰⡟⣭⣾⠷⢶⣅⠀⠁⣷⠈⠻⠟⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⢠⡟⣷⠀⠀⠙⠛⠛⠉⠀⢻⠀⢸⡇⠈⠛⠛⠛⠁⠀⣸⠿⣇⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⢀⡞⠁⣸⣧⡀⠀⠀⠀⠀⢀⣏⠀⢸⣇⠀⠀⠀⠀⠀⣠⡟⠀⠹⣄⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡟⠀⠀⣽⡏⠙⠶⠆⠀⣶⠋⣷⡀⣸⡏⢳⠀⠀⠰⠞⢡⣿⡀⠀⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⡾⠁⢻⣄⠀⠀⢀⣹⠶⠾⣿⠿⠦⢾⣀⠀⠀⢀⡼⠁⢻⡄⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⣼⠇⠀⡾⠙⢦⡴⠏⠁⣀⣴⠟⢦⣀⡀⠙⢷⣤⠎⢹⡄⠀⢷⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡿⠀⢸⠃⠀⣾⢿⣶⣿⠛⠓⣷⡓⠛⢻⣷⡶⢿⡄⠀⣿⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⢸⠀⠀⡇⢰⡏⠈⢻⡟⠋⠛⣟⠉⠘⣇⠀⡇⠀⣿⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠸⡆⢰⣷⣼⠁⠀⡿⠁⠀⠀⢸⡄⠀⢹⣰⡇⠀⡿⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⢇⠸⡝⣿⠀⠀⡇⠀⠀⠀⠀⡇⠀⢸⠟⡇⢸⢃⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢾⣧⣷⠀⠀⠀⡇⠀⠀⠀⠀⣗⠀⠀⣰⢳⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠾⣷⡀⠀⢷⡀⠀⠀⣸⠁⢀⣴⡿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⣈⢷⡀⣰⢇⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
                        print('''
      _, .--.
    (  / (  '-.
jgs .-=-.    ) -.
   /   (  .' .   \\
   \ ( ' ,_) ) \_/
    (_ , /\  ,_/
      '--\ `\--`
         _\ _\\
         `\ \\
          _\_\\
          `\\
            \\
        -.'.`\.'.-''')

                    summon_damage = random.randint(99,10000)
                    print(
                        f'{bulletpoint}You are surrounded by a protective shield. {person.name} summoned {summoned} and deals 💥{summon_damage} damage to {monster.name}!\n')
                    monster.health -= summon_damage
                    battlemenu()
                    input('Press enter to continue...')
                elif person_move.lower().strip() == 'abracadabra':
                    if '🏺- Invisibility Potion' in hero_items: # Checks if the item is in hero items, otherwise below code won't execute.
                        if invisibility_count > 0:
                            print(
                                f'{bulletpoint}{monster.name} tried to {monster_moves}, but {person.name} vanished and attacked {monster.name} from behind dealing 💥{person.damage} damage!\n')
                            monster.health -= person_attack
                            invisibility_count -= 1 # Reduction of the 3 remaining times the hero can use this item.
                            battlemenu()
                        else:
                            print(
                                f'{bulletpoint2}You have used up all of the invisibility potion for this battle.')
                            print(
                                f'{bulletpoint2}{monster.name} attacked and dealt {monster_attack} damage to {person.name}, while {person.name} was fiddling around with the potion.\n')
                            person.health -= monster_attack
                            battlemenu()
                elif person_move.lower().strip() == 'iamgod.':
                    input(f'{bulletpoint2}The forces all around you cause the fabric of reality to temporarily break. Your eyes turn white and you have a blinding aura radiating around you as unfathomable power seeps into your human veins. You just turned into a god.')
                    hero.health += 999999
                else:
                    print(
                        f'{bulletpoint}{person.name} did nothing... {monster.name} attacked and dealt {monster_attack} damage to {person.name}.\n')
                    person.health -= monster_attack
                    battlemenu()

        # Function for the rock paper scissors game
        def getUserChoice(choice):
            choices = ['rock', 'paper', 'scissors', 'bomb']
            if choice in choices:
                return choice
            else:
                print(
                    "Error: This is not a valid option. Choices are Rock, Paper, or Scissors.")
                
        # Function to obtain the computer choice randomly from the three possible choices

        def getComputerChoice():
            compChoice = ['rock', 'paper', 'scissors']
            computerChoice = random.choice(compChoice)
            return computerChoice
        # Function to determine who will win out of the possible outcomes

        def determineWinner(userChoice, computerChoice):
            try: # Try and except added in the event the player doesn't type anything and hits enter. This will prevent the game from crashing.
                if userChoice.lower() == computerChoice:
                    return 'The game was a tie!'
                elif userChoice.lower() == 'bomb':
                    return 'You have won the round! :)'
                elif userChoice.lower() == 'rock' and computerChoice == 'scissors':
                    return 'You have won the round! :)'
                elif userChoice.lower() == 'paper' and computerChoice == 'rock':
                    return 'You have won the round! :)'
                elif userChoice.lower() == 'scissors' and computerChoice == 'paper':
                    return 'You have won the round! :)'
                return 'Your best friend has won the round :('
            except:
                return 'Your best friend has won the round :('

        # Function to utilize the earlier functions and find the winner
        def playGame(userChoice):
            userChoice = getUserChoice(userChoice)
            computerChoice = getComputerChoice()
            print(
                f'{hero.name} played: {userChoice}.\n Best Friend Played: {computerChoice}.\n {determineWinner(userChoice, computerChoice)}')

        # The story objects that can be mixed and matched depending on the storyline and player decisions.
        def story():
            new_rank = '' # Sets the empty rank for the empire_recruitment scenario.
            current_heir = 'the beggar..'

            #Vendor Lady
            def show_vendor_menu():
                count = 1
                # Printing ascii art
                vendor_display = [rusty_sword, sword_one,
                                sword_two, mythic, mythic_two]
                # Current stock for the vendor menu. The items have already been created.
                vendor_stock = [old_rusty_sword,
                                jeweled_blade, masamune_katana, krogg_moon_blade, krogg_moon_katana, invisibility_potion]
                vendor_price = [5, 200, 1500, 850, 850, 1500]
                # Vendor names is what is displayed in the vendor menu.
                vendor_names = {
                    '0: Exit Vendor Store' : 0,
                    '1: Old Rusty Sword - Adds 5 attack damage': 5,
                    '2: Jeweled Blade - Adds 20 attack damage': 200,
                    '3: Masamune Katana - Adds 150 attack damage but Subtracts 99 health': 1500,
                    '4: Krogg Moon Blade - Adds 200 health': 850,
                    '5: Krogg Moon Katana - Adds 50 attack damage': 850,
                    '6: Invisibility Potion - Allows you to attack while invisible. Use 3 times each battle': 1500}
                print(f'{bulletpoint2}Displayed items on the wall:')
                # Code for displaying the vendor items. vendor_display is a list of strings, and vendor_names is a dictionary.
                if count > 0:
                    for i in vendor_display:
                        print(i)
                    count -= 1
                for k, v, in vendor_names.items(): 
                    print(f'\nItem: {k}\nPrice: ${v}\n')
                
                buy_item = (input(
                    f'{bulletpoint2}Would you like to purchase an item? [Current Money: ${hero.money}]\nPlease type the item number you wish to purchase, or type "0" to exit the vendor.'))
                try:
                    if int(buy_item) in range(1, len(vendor_stock) + 1): # Checking if user input is within the vendor stock list range.
                        sold_item = vendor_stock[int(buy_item) - 1] # Selects the item from the vendor_stock based on the index and saves to the sold_item variable.
                        if hero.money >= vendor_price[int(buy_item) - 1]:# Checking if the player's hero has enough money to purchase the item.
                            if sold_item.name in hero_items: # If hero already has the item, then they aren't able to purchase it.
                                input(
                                    f'{bulletpoint2}\nYou already own {sold_item.name} in your inventory!. Press enter to continue...')
                            else:
                                hero.money -= vendor_price[int(buy_item) - 1] # Deduction of hero's money of the item's price.
                                hero_items.append(sold_item.name) # Add the item's name to hero's items list.
                                hero.add_item(sold_item) # Add the item's attributes to the hero.
                                input(
                                    f'\n{bulletpoint2}Congratulations on your purchase! I\'m sure you\'ll enjoy it!🎁\nThe {sold_item.name} has been added to your inventory. Press enter to continue...')
                            menu()
                            show_vendor_menu()
                        else:
                            wheat = input(
                                f'{bulletpoint2}\nSorry, you can\'t afford this item. Press enter to continue...')
                            if wheat.lower() == 'gimmethebread':
                                hero.money += 5000
                            else:
                                pass
                    elif buy_item == '0': # Exit of the vendor menu.
                        menu()
                        best_friend()
                    
                except:
                    input(
                        f'{bulletpoint2}The number you entered is not a valid item in the vendor\'s inventory. Please try again.')
                    show_vendor_menu()
                else:
                    input(
                        f'{bulletpoint2}The number you entered is not a valid item in the vendor\'s inventory. Please try again.')
                    show_vendor_menu()

            def secret_job():
                input(
                    f'{bulletpoint2}A hooded man approached you and said the empire needs your skills in handling a special task. ')

            # The Trade Mission
            def trade_mission():
                global current_position
                clouds1 = '''⁣☀       ☁           ☁           ☁              ☁  
       ☁          ☁         ☁      ☁
                                                                                   '''
                clouds2 = '''⁣☀                ☁           ☁            ☁       
        ☁            ☁         ☁            ☁
                                                                                   '''
                clouds3 = '''⁣☀                ☁           ☁           ☁       
           ☁            ☁           ☁            ☁
                                                                                   '''
                clouds4 = '''⁣☀                ☁       ☁            ☁       
        ☁        🕊   ☁            ☁        ☁
                                                                                   '''

                night1 = '''       ☁           ☁           ☁           ☁   🌙
   ☁          ☁         ☁        ☁
                                                                                   '''
                night2 = '''           ☁           ☁            ☁         🌙 
     ☁            ☁            ☁               ☁
                                                                                   '''
                night3 = '''                ☁           ☁           ☁   🌙
         ☁            ☁           ☁          ☁
                                                                                   '''
                night4 = '''                ☁       ☁            ☁    🌙
    ☁        🕊   ☁                  ☁           ☁
                                                                                   '''
                stormy = '''🌦🌧☁ 🌧🌧☁  🌧🌧🌧🌧🌧  🌧🌧🌧 🌧🌧🌧🌧   ☁☁🌧🌧🌧   🌧  ☁☁ 
  🌧🌧🌧     🌧🌧🌧🌧    🌧🌧 🌧🌧🌧🌧🌧🌧     🌧🌧🌧🌧🌧🌧 🌧🌧🌧🌧
                                                                                '''
                stormy2 = '''🌩🌩🌪 🌧🌧🌪  🌧🌩🌧🌧🌧  🌧🌧🌧 🌧🌩🌧🌧   🌩🌪🌧🌩🌧   🌧  🌪🌧
  🌧🌧🌧     🌧🌧🌩🌧    🌧🌧 🌧🌧🌩🌧🌧🌧     🌧🌧🌧🌩🌧🌧 🌧🌧🌩🌧
   ⛆⛆⛆⛆⛆⛆🗲⛆⛆⛆    ⛆⛆⛆⛆🗲⛆⛆⛆⛆     ⛆⛆⛆⛆🗲⛆ ⛆⛆⛆⛆ '''
                stormy3 = '''🌧☁ 🌧🌧☁  🌧🌧🌧🌧🌧  🌧🌧🌧 🌧🌧🌧🌧   ☁☁🌧🌧🌧   🌧  ☁☁ 
  🌧🌧🌧     🌧🌧🌧🌧    🌧🌧 🌧🌧🌧🌧🌧🌧   ༌ ⭑༌༌ 🌧🌧🌧🌧🌧🌙🌧🌧🌧🌧🌧
                                                                                '''
                stormy4 = '''🌩🌩🌪 🌧🌧🌪  🌧🌩🌧🌧🌧  🌧🌧🌧 🌧🌩🌧🌧 🌙 🌩🌪🌧🌩🌧   🌧  🌪🌧
   🌧🌧🌧     🌧🌧🌩🌧    🌧🌧 🌧🌧🌩🌧🌧🌧  ༌ ⭑༌༌ 🌧🌧🌧🌩🌧🌧 🌧🌧🌩🌧
  ⛆⛆⛆⛆⛆⛆🗲⛆⛆⛆    ⛆⛆⛆⛆🗲⛆⛆⛆⛆     ⛆⛆⛆⛆🗲⛆ ⛆⛆⛆⛆ '''

                ship_castle = '              🌳🌳⛰⛰⁣⛰⁣🏰⛰⛰⛰🌳🌳                    '
                ice_castle = '              🎄🎄⛰⛰⁣⛰⁣🏰⛰⛰⛰🎄🎄                    '
                ship_island = '🌊⁣🌊🌊🌊🌊🌊⁣🌊🌊🏝⁣🏝🏝🏝🏝🌊⁣🌊🌊🌊🌊🌊⁣🌊🌊🌊⁣🌊🌊🌊'
                ship_trees = '🌊🌊🌊🌊🌊🌊🌊🌊🌳🌳🌳🌳🌳🌳🌊🌊⁣🌊🌊🌊🌊🌊⁣🌊🌊'
                xmas_trees = '🌊🌊🌊🌊🌊🌊🌊🌊🎄🎄🎄🎄🎄🌊🌊⁣🌊🌊🌊🌊🌊⁣🌊🌊'
                palm_trees = '🌊🌊🌊🌊🌊🌊🌊🌊🏝️🏝️🏝️🏝️🏝️🏝️🌊⁣🌊🌊🌊🌊🌊⁣🌊🌊🌊🌊🌊⁣🌊'
                palm_trees2 = '🌊🌊🌊🌊🌊🌊⛱️🗿🌴🌴⛩️🌴🌴🗿⛱️🌊🌊🌊🌊🌊⁣🌊🌊'
                palm_trees3 = '🌊🌊🌊🌊🌊⛱️🌴🌴🛖🌴🌴🌴🛖🌴🌴⛱️🌊🌊🌊🌊⁣🌊🌊'
                palm_trees4 = '🌊🌊🌊🌊⛱️🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴⛱️🌊🌊🌊⁣🌊'
                palm_trees5 = '🌊🌊🌊⛱️🌴🌴🌴🌴🛖🌴🛕🌴🛖🌴🌴🌴🌴⛱️🌊🌊⁣🌊🌊🌊'
                palm_trees6 = '🌊🌊🌊🏝️🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🏝️🌊🌊⁣🌊'
                palm_trees7 = '🌊🌊🌊🏝️🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🏝️🌊🌊⁣🌊'
                palm_trees8 = '🌊🌊🌊🌊🌴🌴🛖🌴🌴🌴🏔️🏔️🌴🌴🌴🌴🛖🌴🏝️🌊🌊⁣🌊🌊'
                palm_trees9 = '🌊🌊🌊🏝️🌴🌴🌴🌴🌴🏔️🗻🗻⛰️🌴🌴🌴🌴🌴🏝️🌊🌊⁣🌊'
                palm_trees10 = '🌊🌊🌊🌊🌴🌴🌴🌴🌴🗻🌋🗻⛰️🌴🌴🌴🌴🌴🏝️🌊🌊⁣🌊'
                palm_trees11 = '🌊🌊🌊🏝️🌴🌴🌴🌴🌴🏔️🗻🏔️🌴🌴🌴🌴🌴🌴🏝️🌊🌊⁣🌊'
                palm_trees12 = '🌊🌊🌊🌊🌴🛖🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🛖🌴🏝️🌊🌊⁣🌊'
                palm_trees13 = '🌊🌊🌊🏝️🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🌴🏝️🌊🌊⁣🌊'
                palm_trees14 = '🌊🌊🌊🏝️🌴🌴🌴🌴🛖🌴🌴🌴🛖🌴🌴🌴🌴🌴🏝️🌊🌊⁣🌊'

                colony = [palm_trees2, palm_trees3,
                          palm_trees4, palm_trees5, palm_trees6, palm_trees7, palm_trees8, palm_trees9, palm_trees10, palm_trees11, palm_trees12, palm_trees13, palm_trees14]

                island_dict = {
                    '0': '🍇', '1': '☕️', '2': '🌽'
                }
                sea_island_dict = {
                    '0': '🍯', '1': '🦪', '2': '🍍'
                }
                storm_island_dict = {
                    '0': '🐡', '1': '🍨', '2': '⚗️'
                }
                trade_requirements = [
                    '🍇', '☕️', '🌽', '🍯', '🦪', '🍍', '🐡', '🍨', '⚗️'
                ]
                ship_boat = '🌊🌊🌊🌊🌊🌊🌊🌊⁣🌊🌊𖠳 🌊🌊⁣🌊🌊🌊🌊🌊⁣🌊🌊🌊🌊🌊'
                ship_surf = '🌊🌊🌊🌊🌊🌊🌊🌊⁣🌊🌊🏄🏻 🌊🌊⁣🌊🌊🌊🌊🌊⁣🌊🌊🌊🌊🌊'
                ship_shark = '🌊🌊🌊🌊🦈🌊🌊🌊⁣🌊🌊🦑🌊🌊⁣🌊🌊🌊🌊🦈⁣🌊🌊🌊🌊🌊'
                ship_octo = '🌊🌊🌊🌊🦈🌊🌊🌊⁣🌊🌊🐙🌊🌊⁣🌊🌊🌊🌊🦈⁣🌊🌊🌊🌊🌊'

                ship_whale = ['🌊🌊🌊🌊🌊🌊🌊🌊⁣🌊🌊🐋🌊🌊⁣🌊🌊🌊🌊🌊⁣🌊🌊🌊🌊🌊',
                            '🌊🌊🌊🌊🐟🌊🌊🌊⁣🌊🌊🌊🌊🌊⁣🌊🌊🌊🌊🌊⁣🌊🌊🌊🌊🌊', '🌊🌊🌊🌊🌊🌊🌊⁣🌊🌊🌊🌊⁣🌊🌊🌊🐟🌊⁣🌊🌊🌊🌊🌊🌊🌊',
                            '🌊🌊🌊🌊🌊🌊🌊⁣🌊🌊🌊🌊⁣🐬🌊🌊🌊⁣🌊🌊🌊🌊🌊🌊🌊🌊',
                            '🌊🌊🌊🌊🌊🌊🌊⁣🐠🌊🌊🌊⁣🌊🌊🌊🌊⁣🌊🌊🌊🌊🌊🌊🌊🌊',
                            '🌊'*23, '🌊'*23, '🌊'*23]
                # Displays a random choice of the whale selection to show either a whale, dolphin, or fish.
                ship_fish = random.choice(ship_whale)

                ship_ocean = '🌊'*23
                # Below are the different scenes that are displayed depending on the player's location in the ocean.
                sea_down_middle = [ship_ocean, ship_ocean, ship_ocean, ship_ocean, ship_boat,
                                ship_ocean, ship_ocean, ship_ocean, ship_ocean]
                # Different multiplied empty strings are used for a clue to the player for navigation purposes
                sea_start = [clouds1, ' '*36 + '༌ ⭒༌', ship_castle, ship_trees, ship_boat,
                            ship_ocean, ship_ocean, ship_ocean]

                ice_castle = [night4, ' '*20 + '༌ ⭒༌', ice_castle, xmas_trees, ship_boat,
                            ship_ocean, ship_ocean, ship_ocean]
                ship_surf = [night4, ' '*20 + '༌ ⭒༌', ice_castle, xmas_trees, ship_surf,
                            ship_ocean, ship_ocean, ship_ocean]

                sea_top_left = [clouds2, ' '*34 + '༌ ⭒༌', ship_boat, ship_fish,
                                ship_ocean, ship_ocean, ship_ocean]

                sea_left_2 = [clouds4, ' '*32 + '༌ ⭒༌', ship_boat, ship_ocean,
                            ship_fish, ship_ocean, ship_ocean]

                sea_left_3 = [clouds4, ' '*30 + '༌ ⭒༌', ship_boat, ship_ocean,
                            ship_ocean, ship_fish, ship_ocean, ship_island]

                sea_island = [clouds4, ' '*30 + '༌ ⭒༌',
                            ship_ocean, ship_ocean, ship_ocean, ship_boat, ship_island]

                sea_island_south = [clouds2, ' '*30 + '༌ ⭒༌', ship_boat, ship_ocean,
                                    ship_ocean, ship_fish, ship_ocean, ship_ocean]

                sea_island_south1 = [clouds3, ' '*30 + '༌ ⭒༌', ship_ocean, ship_boat, 
                                    ship_ocean, ship_fish, ship_ocean, ship_ocean]

                sea_island_south2 = [clouds4, ' '*30 + '༌ ⭒༌',  ship_ocean, ship_ocean, 
                                    ship_boat, ship_fish, ship_ocean, ship_ocean]

                new_colony = [clouds4, ' '*30 + '༌ ⭒༌',
                              ship_ocean, ship_ocean, ship_ocean, ship_boat, palm_trees]

                sea_left_4 = [clouds4, ' '*28 + '༌ ⭒༌', ship_boat, ship_ocean,
                            ship_ocean, ship_fish, ship_ocean, ship_ocean]
                sea_left_5 = [night1, ' '*26 + '༌ ⭒༌', ship_boat, ship_ocean,
                            ship_ocean, ship_fish, ship_ocean, ship_ocean]
                sea_left_6 = [night2, ' '*24 + '༌ ⭒༌', ship_boat, ship_ocean,
                            ship_ocean, ship_fish, ship_ocean, ship_ocean]
                sea_left_7 = [night3, ' '*22 + '༌ ⭑༌༌', ship_boat, ship_ocean, # Different stars as another clue for navigating to the secret island
                            ship_ocean, ship_fish, ship_ocean, ship_ocean]
                sea_left_8 = [night4, ' '*20 + '༌ ⭒༌', ship_boat, ship_ocean,
                            ship_ocean, ship_fish, ship_ocean, ship_ocean]

                sea_dark = [stormy, ship_ocean, ship_boat, ship_ocean,
                            ship_ocean, ship_ocean]

                sea_stormy = [stormy2, ship_ocean, ship_ocean,
                            ship_boat, ship_shark, ship_ocean]

                sea_stormy_west = [stormy3, ship_ocean,
                                ship_boat, ship_ocean, ship_shark, ship_ocean]
                sea_stormy_south = [stormy4, ship_ocean,
                                    ship_ocean, ship_boat, ship_octo, ship_island]
                sea_storm_island = [stormy4, ship_ocean,
                                    ship_ocean, ship_octo, ship_boat, ship_island]
                sea_storm_island_south = [stormy4, ship_island,
                                    ship_ocean, ship_octo, ship_boat, ship_ocean]

                directions = ['east', 'west', 'north', 'south', 'yes', 'no']
                # Single function to help print out all the different scenes from the lists above.
                def open_seas(ocean_list):
                    for row in ocean_list:
                        print(row)

                new_colony_name = 'Mysterious Continent'
                sea_island_name = 'MuaLuna'
                storm_name = 'Sea Storm Island'
                
                land = [sea_start, sea_island, sea_storm_island, ice_castle, new_colony] # These are scenes that the ship anchor option will be displayed.
                seastorm = [sea_dark, sea_stormy] # These two scenes are displayed when the player travels outside of the preferred path, and will eventually return them if they stray too far.

                anchor = True
                current_position = sea_start # Current position starts at the red dragon kingdom. This can be changed along with the starting scene depending on location in the game tree.
                previous_position = '' # Important variable to keep track of the last position. This will help return the player to their previous location if they enter the opposite cardinal direction.
                start_count = 0
                saved_direction = ''

                #Island Trade Menu
                def land_trade(land_emote, land_dict, item1, item2, item3):
                    input('Press enter to continue...')
                    open_seas(land_emote) # Displaying the area
                    trade_count = 1
                    while trade_count > 0: # Start of the while loop
                        print(
                            f'\n\n\n\n\n\n\n\n\n{bulletpoint2}Local Shop Items for Trade ($100 each):')
                        print([(k, land_dict[k]) for k in land_dict]) # Displaying the Key and Value for the Trade items available.
                        #Player can enter the key string to purchase the value which is an emote of the item.
                        buy_land = input(
                            f'{bulletpoint2}Current Money: ${hero.money}\n{bulletpoint}Please enter the number for the local item you wish to purchase ({item1}, {item2}, {item3}):\n{bulletpoint2}Type "exit" to exit the menu.')
                        print(f'{bulletpoint2}Current Trade Items Held: {hero_land_items}') # Displaying currently held trade items.
                        if buy_land.lower() == 'exit': #Player can exit the menu by typing exit.
                            trade_count -= 1 # Ends the while loop.
                        else: # Player to enter the item number they wish to purchase.
                            try: # Try and Except to make sure the player inputs a valid number and not a word.
                                # Player to enter the item amount they wish to purchase from the dictionary for the island.
                                buy_land_amount = int(input(
                                    f'{bulletpoint}You\'ve selected {land_dict[buy_land]}. How many would you like to purchase:'))
                                if hero.money >= (buy_land_amount * 100): # Checks if hero has enough money to purchase the item times the cost.
                                    purchase_land = input(
                                        f'{bulletpoint}Total cost is ${buy_land_amount * 100}\nCurrent money: ${hero.money}\nWould you like to complete this purchase?')
                                    if purchase_land.strip().lower() in yes:
                                        if land_dict[buy_land] in hero_land_items.keys(): # Checks if the item exists in hero's land items dictionary keys.
                                            hero.money -= (buy_land_amount * 100) # Deducts the cost from the hero's money amount.
                                            hero_land_items[land_dict[buy_land]] += buy_land_amount # Adds the item to the hero's land items dictionary.
                                            print(f'{bulletpoint2}You\'ve made the trade successfully!')
                                            input(
                                                f'{bulletpoint2}{hero_name}\'s Current Trade Items Held: {hero_land_items}')
                                            open_seas(land_emote) # Displaying the area.
                                else:
                                    input(f'{bulletpoint2}Current money: ${hero.money}\nYou cannot afford this trade :(')
                            except:
                                input(
                                    f'{bulletpoint2}You did not enter a valid option. Please try again.')

                new_requirement = random.choice(trade_requirements)
                new_requirement2 = random.choice(trade_requirements)
                input(
                    f'{bulletpoint2}You stop by the trade port near the shipyard. The empire needs one of each of these two items ({new_requirement} and {new_requirement2}). If you can acquire them on your journey, you shall be awarded. Note that these items may change due to demand, so it\'s best to stock up on local items.')
                if hero_land_items[new_requirement] > 0 and hero_land_items[new_requirement2] > 0: # Checks if hero's land item stock is more than 0 for the two item requirements.
                    hand_item = input(
                        f'{bulletpoint}It looks like you already have these items in your inventory! Would you like to hand them over?')
                    if hand_item.strip().lower() in yes:
                        hero_land_items[new_requirement] -= 1 # Deducts from hero's land item stock.
                        hero_land_items[new_requirement2] -= 1 # Deducts from hero's land item stock.
                        print(
                            f'{bulletpoint2}You\'ve made the trade successfully!')
                        input(
                            f'{bulletpoint2}{hero_name}\'s Current Trade Items Held: {hero_land_items}')
                        input(f'{bulletpoint2}The empire thanks you for your service.')
                    else:
                        pass
                set_sail = input(f'{bulletpoint}Would you like to set sail?')
                if set_sail.strip().lower() in yes:
                    pass
                else:
                    print(f'You decided instead to do...')

                # The below code displays a ship for the player to travel between two different kingdoms.
                while anchor:
                    open_seas(current_position) #opening the first starting scene.
                    if (current_position in land) and (start_count != 0):
                        land_command = input(
                            f'{bulletpoint}Would you like to anchor the ship?\n\n\n\n\n\n\n\n\n\n\n')
                        if land_command in directions:
                            command = land_command
                    else:
                        # If current position is in the storm, the below question will not be asked.
                        if current_position in seastorm:
                            pass
                        else:
                            command = input(
                                f'{bulletpoint}Which direction would you like to steer the ship? (north, west, east, south)\n\n\n\n\n\n\n\n\n\n\n')
                    # Start count being at 0 prevents the "Would you like to anchor the ship?" string from being displayed.
                    start_count -= 1
                    # Below are the different scenes and each of their connections depending on how the user travels. Venturing too far from the path will put them in stormy weather.
                    if command.lower() in directions:
                        saved_direction = command # Saved direction to be used again when the player encounters the storm. They will need to enter the opposite direction to escape.
                        if current_position == sea_start:
                            previous_position = sea_start
                            if command == 'west':
                                current_position = sea_top_left
                            elif command == 'no':
                                current_position = sea_start
                                start_count = 0
                            elif command == 'yes':
                                current_position = sea_start
                                print(
                                    f'{bulletpoint2}Current Position: Red Dragon Castle')
                                print(
                                    f'{bulletpoint2}You reached the destination!')
                                anchor = False
                                trade_mission()
                            else:
                                current_position = sea_dark
                        elif current_position == sea_top_left: # Current position is the current scene.
                            previous_position = sea_top_left  # Previous position will save the current scene if they travel in the stormy areas, and need to return to the same scene.
                            if command == 'west':
                                current_position = sea_left_2 # This is the new scene the hero will travel to if they go west.
                            elif command == 'east':
                                current_position = sea_start # This is the new scene the hero will travel to if they go east.
                            else:
                                current_position = sea_dark # If they go any other direction, they will travel into the stormy areas.
                        elif current_position == sea_left_2:
                            previous_position = sea_left_2
                            if command == 'west':
                                current_position = sea_left_3
                            elif command == 'east':
                                current_position = sea_top_left
                            else:
                                current_position = sea_dark
                        elif current_position == sea_left_3:
                            previous_position = sea_left_3
                            if command == 'south':
                                current_position = sea_island
                            elif command == 'east':
                                current_position = sea_left_2
                            elif command == 'west':
                                current_position = sea_left_4
                            else:
                                current_position = sea_dark
                        elif current_position == sea_island:
                            previous_position = sea_island
                            if command == 'north':
                                current_position = sea_left_3
                            elif command == 'yes':
                                current_position = sea_island
                                print(
                                    f'{bulletpoint2}Current Position: {sea_island_name}')
                                print(f'{bulletpoint2}You reached the destination!')
                                land_trade(sea_island, sea_island_dict,
                                           'honey', 'pearls', 'pinneaple')
                            elif command == 'no':
                                current_position = sea_island
                                start_count = 0
                            elif command == 'south':
                                current_position = sea_island_south
                            else:
                                current_position = sea_dark
                        elif current_position == sea_island_south:
                            previous_position = sea_island_south
                            if command == 'south':
                                current_position = sea_island_south1
                            elif command == 'north':
                                current_position = sea_island
                            else:
                                current_position = sea_dark
                        elif current_position == sea_island_south1:
                            previous_position = sea_island_south1
                            if command == 'south':
                                current_position = sea_island_south2
                            elif command == 'north':
                                current_position = sea_island_south
                            else:
                                current_position = sea_dark
                        elif current_position == sea_island_south2:
                            previous_position = sea_island_south2
                            if command == 'south':
                                current_position = new_colony
                            elif command == 'north':
                                current_position = sea_island_south1
                            else:
                                current_position = sea_dark
                        elif current_position == new_colony:
                            previous_position = new_colony
                            if command == 'south':
                                current_position = new_colony
                            elif command == 'no':
                                current_position = new_colony
                                start_count = 0
                            elif command == 'yes':
                                current_position = new_colony
                                print(
                                    f'{bulletpoint2}Current Position: {new_colony_name}')
                                print(
                                    f'{bulletpoint2}You reached the destination!')
                                land_trade(colony, island_dict,
                                          'horse', 'coffee', 'corn')
                            elif command == 'north':
                                current_position = sea_island_south2
                            else:
                                current_position = sea_dark
                        elif current_position == sea_left_4:
                            previous_position = sea_left_4
                            if command == 'west':
                                current_position = sea_left_5
                            elif command == 'east':
                                current_position = sea_left_3
                            else:
                                current_position = sea_dark
                        elif current_position == sea_left_5:
                            previous_position = sea_left_5
                            if command == 'west':
                                current_position = sea_left_6
                            elif command == 'east':
                                current_position = sea_left_4
                            else:
                                current_position = sea_dark
                        elif current_position == sea_left_6:
                            previous_position = sea_left_6
                            if command == 'west':
                                current_position = sea_left_7
                            elif command == 'east':
                                current_position = sea_left_5
                            else:
                                current_position = sea_dark
                        elif current_position == sea_left_7:
                            previous_position = sea_left_7
                            if command == 'west':
                                current_position = sea_left_8
                            elif command == 'east':
                                current_position = sea_left_6
                            elif command == 'south':
                                current_position = sea_down_middle
                            else:
                                current_position = sea_dark
                        elif current_position == sea_down_middle:
                            previous_position = sea_down_middle
                            if command == 'north':
                                current_position = sea_left_7
                            elif command == 'west':
                                current_position = sea_stormy_west
                            else:
                                current_position = sea_dark
                        elif current_position == sea_stormy_west:
                            previous_position = sea_stormy_west
                            if command == 'south':
                                current_position = sea_stormy_south
                            elif command == 'east':
                                current_position = sea_down_middle
                            else:
                                current_position = sea_dark
                        elif current_position == sea_stormy_south:
                            previous_position = sea_stormy_south
                            if command == 'south':
                                current_position = sea_storm_island
                            elif command == 'north':
                                current_position = sea_stormy_west
                            else:
                                current_position = sea_dark
                        elif current_position == sea_storm_island:
                            previous_position = sea_storm_island
                            if command == 'no':
                                current_position = sea_storm_island
                                start_count = 0
                                command == '' # Added this so that it won't trigger the leviathan boss automatically if the command variable was still "south"
                            elif command == 'yes':
                                current_position = sea_storm_island
                                print(
                                    f'{bulletpoint2}Current Position: {storm_name}')
                                print(
                                    f'{bulletpoint2}You reached the destination!')
                                land_trade(sea_storm_island, storm_island_dict,
                                           'puffer fish', 'ice cream', 'mysterious liquid')
                                add_health(leviathan) # Resets leviathan monster health if it has already been killed
                            elif command == 'north':
                                current_position = sea_stormy_south
                            elif command == 'south':
                                open_seas(sea_storm_island_south)
                                if leviathan.health >= 0:
                                    levi_ques = input(f'The skies have never been this dark in this part of the ocean. You try to make your way back to the island, but behind you is a gargantuan shadow of something flying in the storm. Do you go to see what it is?')
                                    if levi_ques.lower() in yes:
                                        input(levi_image2)
                                        input(levi_image)
                                        battle(hero, leviathan, 'makes a waterfall', 'sings a song',
                                            'makes a whirlpool', 'initiates a hydro blast')
                                        check_health(hero)
                                        input(
                                            f'Congratulations you defeated the Leviathan God!')
                                        add_health(hero)
                                        add_money(50, 200)
                                else:
                                    input(
                                        '\n\n\n\n\n\n\n\n\n\n\nIt\'s too stormy in these waters, we should steer in a different direction...')
                                current_position = sea_storm_island
                            else:
                                current_position = sea_dark
                        elif current_position == sea_left_8:
                            previous_position = sea_left_8
                            if command == 'north':
                                current_position = ice_castle
                            elif command == 'east':
                                current_position = sea_left_7
                            else:
                                current_position = sea_dark
                        elif current_position == ice_castle:
                            previous_position = ice_castle
                            if command == 'no':
                                current_position = ice_castle
                                start_count = 0
                            elif command == 'yes':
                                current_position = ice_castle
                                print(
                                    f'{bulletpoint2}Current Position: Ice Kingdom')
                                print(
                                    f'{bulletpoint2}You reached the destination!')
                                anchor = False # Ends the while loop
                                add_health(leviathan) # Resets leviathan monster health if it has already been killed
                            elif command == 'south':
                                current_position = sea_left_8
                            else:
                                current_position = sea_dark
                        elif current_position == sea_dark: # 1st stormy area if player travels outside of the preferred path
                            if saved_direction == 'north':
                                print('\n\n\n\n\n\n\n\n\n\n')
                                open_seas(sea_dark)
                                stormcommand = input(
                                    f'{bulletpoint}Which direction would you like to steer the ship? (north, west, east, south)\n\n\n\n\n\n\n\n\n\n\n')
                                if stormcommand == 'south':
                                    current_position = previous_position
                                else:
                                    open_seas(sea_stormy) # This is the 2nd stormy area that will teleport the player back to the previous scene, as they have strayed too far away.
                                    input(
                                        '\n\n\n\n\n\n\n\n\n\n\nIt\'s too stormy in these waters, we should steer in a different direction...')
                                current_position = previous_position
                            elif saved_direction == 'south':
                                print('\n\n\n\n\n\n\n\n\n\n')
                                open_seas(sea_dark)
                                stormcommand = input(
                                    f'{bulletpoint}Which direction would you like to steer the ship? (north, west, east, south)\n\n\n\n\n\n\n\n\n\n\n')
                                if stormcommand == 'north':
                                    current_position = previous_position
                                else:
                                    open_seas(sea_stormy)
                                    input(
                                        '\n\n\n\n\n\n\n\n\n\n\nIt\'s too stormy in these waters, we should steer in a different direction...')
                                current_position = previous_position
                            elif saved_direction == 'west':
                                print('\n\n\n\n\n\n\n\n\n\n')
                                open_seas(sea_dark)
                                stormcommand = input(
                                    f'{bulletpoint}Which direction would you like to steer the ship? (north, west, east, south)\n\n\n\n\n\n\n\n\n\n\n')
                                if stormcommand == 'east':
                                    current_position = previous_position
                                else:
                                    open_seas(sea_stormy)
                                    input(
                                        '\n\n\n\n\n\n\n\n\n\n\nIt\'s too stormy in these waters, we should steer in a different direction...')
                                current_position = previous_position
                            elif saved_direction == 'east':
                                print('\n\n\n\n\n\n\n\n\n\n')
                                open_seas(sea_dark)
                                stormcommand = input(
                                    f'{bulletpoint}Which direction would you like to steer the ship? (north, west, east, south)\n\n\n\n\n\n\n\n\n\n\n')
                                if stormcommand == 'west':
                                    current_position = previous_position
                                else:
                                    open_seas(sea_stormy)
                                    input(
                                        '\n\n\n\n\n\n\n\n\n\n\nIt\'s too stormy in these waters, we should steer in a different direction...')
                                current_position = previous_position
                            else:
                                open_seas(sea_stormy)
                                input(
                                    '\n\n\n\n\n\n\n\n\n\n\nIt\'s too stormy in these waters, we should steer in a different direction...')
                                current_position = previous_position
                    else:
                        print('Your input is not valid. Please try again.') # Player did not type a correct cardinal direction or yes/no.

            # Empire Recruitment
            def empire_recruitment():
                global ranks
                nonlocal new_rank
                # list of random ranks that can be offered to the player.
                ranks = [
                    'Stable sweep', 'Swordsman', 'Axeman', 'Spearman', 'Archer', 'Cavalry',
                    'Lieutenant', 'Captain', 'Knight', 'Commander', 'Baron', 'Viscount', 'Earl', 'Marquis', 'Duke'
                ]
                empire_recruitment_ans = input(f'\n{bulletpoint} An old guard walks up to you and says they\'re seeking out some new blood into their ranks. Would you be interested in joining the Red Dragon Military?')
                if new_rank in ranks: # Checks if the player already has a rank in the ranks list.
                    input( # If the player already has a rank, they can still roll against the old guard to compare intelligence levels.
                        f'{bulletpoint}It seems that you\'ve already been employed in the Red Dragon Military as {new_rank} {hero_name}. You can still roll from 0 to 10 to see if you have a higher intelligence level than the old guard. Press enter to roll...')
                    hero_smart_level = random.randint(0, 10)
                    old_guart_smart = random.randint(0, 10)
                    if hero_smart_level == old_guart_smart:
                        input(
                            f'{bulletpoint2} Old Guard rolled a {old_guart_smart}. {hero_name} rolled a {hero_smart_level}.\nIt looks like you and the old guard have the same intelligence level.')
                    elif hero_smart_level >= old_guart_smart:
                        input(
                            f'{bulletpoint2} Old Guard rolled a {old_guart_smart}. {hero_name} rolled a {hero_smart_level}.\nIt looks like you\'re more intelligent than the old guard!')
                    else:
                        input(
                            f'{bulletpoint2} Old Guard rolled a {old_guart_smart}. {hero_name} rolled a {hero_smart_level}.\nHaha. It looks like the old guard is much more wiser than you...')
                else: # If player doesn't already have a rank, they can roll for a new rank.
                    if empire_recruitment_ans.strip().lower() in yes:
                        new_rank = input(
                            f'{bulletpoint}Your rank depends on your intelligence level and luck...mostly luck. Press enter to roll from 1 to 10:')
                        roll = random.randint(1, 10)
                        new_rank = ranks[roll] # Player rolls for the rank. The higher the number, the higher the rank.

                        input(
                            f'{bulletpoint2}You rolled {roll} and have been granted a position at the Red Dragon Military as: {new_rank} {hero_name}! Congratulations!')
                    else:
                        new_rank = ranks[0]
                        input(
                            f'\n{bulletpoint2}the guard says too bad, he needs to reach his recruitment quota so you\'ll be forced to join as a {new_rank}.')
                        menu()


                # Empire Mission
                empire_mission_ans = input(f'\n{bulletpoint}The empire\'s mission was to take care of a {giant.name} that was blocking the way of the empire\'s deforestation plan. But be wary that this {giant.name} has already taken out several experienced knights. Are you able to prove your loyalty to the empire and take care of this monster?')
                if empire_mission_ans.strip().lower() in yes:
                    print(f'{bulletpoint2}You come across a valley with beautiful golden trees, an arched bridge, and a glistening river. On top of the bridge you see the sleeping {giant.name} blocking the way. You start walking over to the bridge and the {giant.name} immediately wakes up and stands 30 feet tall over you.')
                    input('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⡀⠀⠀⠀⠀⠀⢺⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡇⠀⠀⠀⠀⣠⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⢁⣤⣤⣤⣴⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣷⣀⠙⢉⣠⣾⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣾⣿⡿⢿⣿⣿⣿⣿⣿⣿⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⡟⠉⠀⠘⣿⣿⣿⣿⣿⣿⠇⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⡇⠀⠀⠀⢿⣿⣿⣿⣿⣿⣠⣴⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣷⣄⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⡿⠋⠙⢿⣿⣦⣴⣶⡷⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠹⣿⠟⠁⠀⠀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⣀⣶⣼⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⣤⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⢿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠀⠈⠃⠀⠀⠀
                    ''')
                    add_health(giant) # Adds monster health if it has already been killed.
                    battle(hero, giant, 'raises left arm',
                           'breaths heavily', 'makes angry face', 'raises right arm')
                    print(f'\n{bulletpoint2}You won! The empire was very impressed with your ability.')
                    try: # Find the index of the hero's current rank and then promotes to a higher rank.
                        if new_rank in ranks:
                            index = ranks.index(new_rank)
                            new_rank = ranks[index + 1]
                            input(
                                f'{bulletpoint2}The empire has made a decision to promote you a rank higher to {new_rank}!')
                    except: # If hero is already at the max rank, then they're awarded a $ bonus.
                        input(
                            'The empire has made a decision to give you a bonus of $100! ')
                        hero.money += 100
                    random_health_gain = random.randint(10,30)
                    print(
                        f'{bulletpoint2} You took some rest and gained {random_health_gain} health back.')
                    hero.health += random_health_gain
                    check_health(hero)
                    add_money(50, 200)
                    menu()

                else:
                    input(f'\n{bulletpoint2}You decided to prove your loyalty instead by taking on an imperial trade assignment and sail the seas. You were tasked with a mission to locate Sea Storm Island in the west and trade some imperial goods. The emperor will also be joining on the trip so it\'s best to showcase your ability to navigate the seas!')
                    menu()
                    trade_mission()


            # The Secret
            def the_secret():
                desert_ans = input(f'\n{bulletpoint}In the mountains at the highest peak, there lies a secret. You must retrieve this secret but you may never open it...\nYou lead the monk to the borders of the empire. You see a vast never ending desert, and the map shows that\'s the quickest route. There is another longer route through the forest. \nDo you take the desert route?')
                if desert_ans.strip().lower() in yes or desert_ans.strip().lower() == 'desert':
                    print(f'\n{bulletpoint2}As you and the monk struggle through the blazing heat. You both hear a roaring rumble underneath your feet...') 
                    menu()
                else:
                    print('You decided to take the forest route.')
                    pass
                    #the_forest()

            # Sand Monster Battle
                add_health(sandworm) # Adds monster health if it has already been killed.
                sand_monster_ans = input(f'\n{bulletpoint}You see something like a mountain rise up from the sand. The monk says that this must be the legendary 1000 year old {sandworm.name}. You stare up and see a massive hole with thousands of sharp teeth at every corner of its mouth. Do you even attempt to fight this thing?')
                if sand_monster_ans.strip().lower() in yes:

                    sand_monster_weapon = input(
                        f'\n{bulletpoint}The monk asks you what weapon you plan to fight this thing when we only have {hero_items}? You respond with "I\'ll just use the..."')
                    input(f'\n{bulletpoint2}As you try your plan of attacking with the {sand_monster_weapon}... you utterly failed. The {sandworm.name} then surrounded you with a giant wall of sand, preventing your escape...') 
                    battle(hero, sandworm, 'digs at ground',
                           'twists body', 'shrieks', 'moves underground')
                    random_health_gain = random.randint(10,30) # Adds health to the hero between 10 and 30.
                    print(
                        f'{bulletpoint2} You both rested and you gained {random_health_gain} health back.')
                    hero.health += random_health_gain
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(sandworm) # Check if the monster died and will print that the monster has died.
                    add_money(50, 200)
                    menu()
                else:
                    input(f'\n{bulletpoint2}The monster lunged at you, but the monk ran towards you and pushed you away. Sand filled the air making it impossible to see. Once the sand dissipated, you saw a shadow in the midst and the monk slowly appeared safe and sound. You both successfully managed to escape! ')

            # Frozen Wasteland
                frozen_wasteland_ans = input(f'\n{bulletpoint}After walking for miles, you face a frozen wasteland with a massive thin-ice lake you needed to cross to reach the mountain. You take one step and see a crack in the ice. Do you still proceed?')
                if frozen_wasteland_ans.strip().lower() in yes:

                    input(f'\n{bulletpoint2}You both start making your way slowly... there were some cracks that appeared while you walk, but halfway in the lake you managed to find a strange metal ship that you decided to camp in. The monk started a small campfire to keep you warm.') 
                    menu()

                    #The Betrayal
                    the_betrayal_ans = input(f'\n{bulletpoint}You both started making your way again to finish crossing the lake at first daylight. As you almost reach the end, the monk had fallen through the ice. You turn around and saw what happened, but the ice under your feet immediately started breaking as well. Do you save yourself and cross the lake? ')
                    if the_betrayal_ans.strip().lower() in yes:

                        input(f'\n{bulletpoint2}You start sprinting towards the end of the lake and saved yourself. There was no point in attempting to save the monk.')
                        menu()
                        mountain_secret()

                    else:
                        input(f'\n{bulletpoint2}You turn back, but the ice under you breaks, and one of your legs gets caught in the numbing cold water below the ice. You manage to pull free, but the monk had already fallen through... never to be seen again. ')
                        menu()
                        mountain_secret()

                else:
                    input(f'\n{bulletpoint2}You were frozen in fear of crossing this lake. You luckily found a way around but you would need to climb up the frozen part of the mountain. As you climbed up the mountain and almost reached the top, the monk slipped. You immediately extended your hand but to no avail... the monk had fallen, and shall never be seen again. ')
                    menu()
                    mountain_secret()

            # Mountain Secret
            def mountain_secret():
                nonlocal current_heir
                phoenix_image = ''' Art by :nathaN
   _,="( _  )"=,_
_,'    \_>\_/    ',_
.7,     {  }     ,\.
 '/:,  .m  m.  ,:\\\'
   ')",(/  \),"('
      '{'!!'}'
'''
                # Box and Triangle counting mini game.
                def box_puzzle():
                    add_health(boxer) # Adds monster health if it has already been killed.
                    #Box Puzzle
                    white_square = '◽' * 16

                    mixed_squares = '◽◽⯀◽◽◽◽⯀◽◽◽⯀◽◽⯀◽'
                    confused_square = '◽◽⯀◽◽◽◽●◽◽◽⯀◽◽⯀◽'

                    white_box_list = (mixed_squares, white_square) * 4
                    # Function to count the printed squares.
                    def count_boxes(list):
                        count = 0
                        for i in list:
                            for a in i:
                                count += 1
                        return count

                    for item in white_box_list:
                        print(item)
                    print(confused_square)
                    for item in white_box_list:
                        print(item)
                    box_question = input(
                        f'{bulletpoint}If you are worthy of this secret, you must pass the test. How many squares are there?')
                    correct_box_number = (count_boxes(white_box_list) * 2) - 1
                    print(
                        f'{bulletpoint2}Your Answer: {box_question} \n{bulletpoint2}Correct Number of Boxes: {correct_box_number}')
                    if box_question == '1':
                        print('You cheated!')
                    elif box_question != str(correct_box_number):
                        print(f'{bulletpoint2}You failed!')
                    else:
                        print(f'{bulletpoint2}You passed!')

                        # Triangle Puzzle
                        double_triangles = '⟁ ' * 8
                        triangle = '🞁 ' * 8
                        confused_triangle = '◤ ◣ ◤ ◣ ◤ ◢ ◤ ⧗'

                        triangle_list = (triangle, double_triangles) * 6

                        print(confused_triangle)
                        for item in triangle_list:
                            print(item)
                        triangle_question = input(f'How many white triangles are there?')
                        print(
                            f'{bulletpoint2}Your Answer: {triangle_question} \n{bulletpoint2}Correct Number of Triangles: 153')
                        if triangle_question == '1':
                            print('You cheated!')
                        elif (triangle_question) != '153': # If the player input does not equal to 153, then they will face a monster.
                            input(
                                f'{bulletpoint}You failed! You hear a rumbling in the snow beneath your feet. Out pops out an ancient man with some gloves on his fists that look like 🥊. The monster starts coming at you!')
                            battle(hero, boxer, 'ducks down','prepares to punch!', 'jumps on rock', 'does a phoenix punch!')
                            check_health(boxer)
                            add_health(hero)
                            check_health(hero)
                            menu()
                        else:
                            print('You passed!')

                input(f'\n{bulletpoint2}You finally reach the peak of the mountain. The weather is bright and snowing. You see a breathtaking view of the frozen lake, and a large castle made of ice below the mountain. You don\'t see anything on top except something that seems to be glowing underneath the snow. You try to wipe the snow and then all of a sudden glowing squares pop up from the ground. A whispering voice asks you a question...')
                box_puzzle() # Asks the first two puzzle questions.
                snowball_question = input( # Third question asked.
                    f'{bulletpoint}The last question is... What kind of ball does not bounce? \nPlease enter your answer:')
                if 'snowball' in snowball_question:
                    print(f'{bulletpoint2}You passed!\nYou hear the ground shake, and one of the boxes you had counted previously had just opened. You take a look inside and you see a letter. There is a message that says that this must be delivered to the beggar just outside the Red Dragon castle.')
                    open_letter = input(f'{bulletpoint}You were told not to open the letter. Do you still decide to open the letter?')
                    if open_letter.strip().lower() in yes:
                        input(
                            f'{bulletpoint2} You decided to open the letter. A legendary phoenix with electric feathers pops out and says it is the guardian of this letter. You are not the intended recipient and shall be erased from existence!')
                        input(phoenix_image)
                        add_health(phoenix) # Adds monster health if it has already been killed.
                        battle(hero, phoenix, 'feathers turns into diamond', 'feathers turns into white', 'feathers turn into magnets', 'feathers turns into plasma')
                        add_health(hero)
                        check_health(hero) # Check if the hero died and will restart game if that is the case.
                        check_health(phoenix) # Check if the monster died and will print that the monster has died.
                        add_money(50, 200)
                        erase_name = input(
                            f'{bulletpoint}You read the letter and it says that the next heir to the throne is {current_heir}. Do you decide to erase this name and change it to something else?')
                        if erase_name.strip().lower() in yes:
                            new_heir = input(
                                f'📜 What name would you like to change this to?')
                            current_heir = new_heir.title() # Updating the current_heir variable. Depending on the name, this will change certain parts of the story.
                            input(
                                f'{bulletpoint2}The new heir to the Red Dragon Empire shall be {current_heir}!')
                            if 'Beggar' in current_heir.title(): # Checking if the player changed the name back to the beggar.
                                input(
                                    f'{bulletpoint2}You remembered that you were told not to open the letter and failed on your promise. You decide to deliver the letter back to the beggar. The beggar opens up the letter and a legendary phoenix with electric feathers pops out. The phoenix says that it is the guardian of this letter, and that the beggar is the next heir to the Red Dragon Empire. The beggar is in shock and thanks you for delivering this message. The beggar will hand you a special reward the next time he sees you. The phoenix then kicks some dirt in your face and flies far away...')
                            elif hero_name.title() == current_heir: # Checking if the player changed the name to hero_name.
                                print(f'You decided to alter the course of humanity for your own benefit!')
                            input(
                                f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                        else:
                            input(
                                f'{bulletpoint2}You decide to leave the name the way it is.')
                            input(
                                f'{bulletpoint2}You start heading your way back down the mountain and return to the Red Dragon Empire.')
                            input(
                                f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                        menu()
                        beggar()
                    else:
                        input(
                            f'{bulletpoint2}You remembered that you were told not to open the letter and kept your promise. You decide to deliver the letter back to the beggar. The beggar opens up the letter and a legendary phoenix with electric feathers pops out. The phoenix says that it is the guardian of this letter, and that the beggar is the next heir to the Red Dragon Empire. The beggar is in shock and thanks you for delivering this message. The beggar will hand you a special reward the next time he sees you. The phoenix then flies far away...')
                        input(phoenix_image)
                        current_heir = 'Beggar'
                        input(
                            f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                        menu()
                        beggar()
                else:
                    print(
                        f'{bulletpoint2}you failed...you gave up trying to retrieve the secret and decided to leave. ')
                    menu()
                    beggar()

            # The Treasure Room
            def treasure_room():
                def treasure_room_ending():
                    input(
                        f'{bulletpoint2}You hear horns and guards yelling outside of the treasure room. It seems that you made too much noise and are about to be caught! The only time to escape is now. You escape from the room and saw guards running past you.')
                # Item creation for the treasure room.
                ancientriotshield = Item('🛡️ Ancient Riot Shield', 100, 0)
                adamantineblade = Item('🗡 Adamantine Blade', 0, 90)
                elixirofthegods = Item('🍶 Elixir of the Gods', 0, 0)
                ancientdrone = Item('👾 Ancient Drone', 0, 0)
                merlinscrystalball = Item('🔮 Merlin\'s Crystal Ball', 0, 0)
                fireball = Item('🔥 Fireball Spell', 0, 0)
                warriorshelm = Item('👑 Warrior\'s Helm', 100, 0)
                
                print('💰🪙💍'*500) # Treasure room display.
                treasure_ans = input(
                    f'{bulletpoint2}You enter a massive room with walls made of pure gold. You only just now realized that you forgot to bring a large enough bag to hold all these valuables. There\'s a large amount of gold in front of you that you can take now and leave. There are also 7 unknown sealed rooms. What do you do?\n 0. Grab the money in front of you and leave.\n 1. Room 1\n 2. Room 2\n 3. Room 3\n 4. Room 4\n 5. Room 5 \n 6. Room 6\n 7. Room 7\n Please enter the number for your choice:\n')
                if treasure_ans == '0':
                    add_money(200,500)
                    print(
                        f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                    menu()
                    beggar()
                elif treasure_ans == '1':
                    add_health(kitty) # Adds monster health if it has already been killed.
                    input(
                        f'{bulletpoint2}When you enter the room, you see a giant cat the size of a whale. The cat sees you and immediately pounces!')
                    battle(hero, kitty, 'licks paw',
                           'meow meow', 'roars', 'stalks')
                    input(
                        f'{bulletpoint2}You took care of the Kitty monster! You reach to pick up the Ancient Riot Shield! This item will add 100 health.')
                    hero.add_item(ancientriotshield) # Adds item attributes and to hero item list if the monster was killed.
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(kitty) # Check if the monster died and will print that the monster has died.
                    treasure_room_ending()
                    print(
                        f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                    menu()
                    beggar()
        
                elif treasure_ans == '2':
                    add_health(fenrir) # Adds monster health if it has already been killed.
                    input(
                        f'{bulletpoint2}When you enter the room, you see a chained up black wolf with glowing red eyes. He growls at runs toward you!')
                    battle(hero, fenrir, 'tucks tail',
                           'whimpers', 'growls', 'wags tail')
                    input(
                        f'{bulletpoint2}You took care of the Fenrir monster! You reach to pick up the Adamantine Blade! This item will add 90 attack damage.')
                    hero.add_item(adamantineblade) # Adds item attributes and to hero item list if the monster was killed.
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(fenrir) # Check if the monster died and will print that the monster has died.
                    treasure_room_ending()
                    print(
                        f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                    menu()
                    beggar()
        
                elif treasure_ans == '3':
                    input(f'{bulletpoint2}When you enter the room, you see a large transparent glass box. Inside this box there are two other transparent boxes. In the middle you see a wine bottle that never stops pouring. You walk over to touch the exterior box and it asks you a question...')
                    question_count = 3 # Number of tries the player has remaining to answer each question.
                    #3 riddles with 3 chances per riddle.
                    while question_count > 0:
                        question1 = input(f'{bulletpoint}Remaining Chances: {question_count}\nA man goes out drinking every night, returning to his home in the wee hours of every morning. No matter how much he drinks, he never gets a hangover. This drink is very well known, but is rarely consumed, served warm and taken straight from its source. The man is a sucker for a free drink, especially since he can\'t live without it. What is his favorite drink?')
                        if question1 == 'blood':
                            question2_count = 3
                            question_count = 0   # Resets the first count
                            while question2_count > 0:
                                input(
                                    f'{bulletpoint2}You\'re on the second box!')
                                question2 = input(
                                    f"{bulletpoint}Remaining Chances: {question2_count}\nWhat starts with a 't' ends with a 't' and is full of 't' ?")
                                if question2 == 'teapot':
                                    question3_count = 3
                                    question2_count = 0  # Resets the second count
                                    while question3_count > 0:
                                        input(
                                            f'{bulletpoint2}You\'re working on the last box!')
                                        question3 = input(
                                            f'{bulletpoint}Remaining Chances: {question3_count}\nI can help you clean your shirt, and always fall but I\'m never hurt. Look for me to beat the heat, I can run without any feet.')
                                        if question3 == 'water':
                                            question3_count = 0  # Resets the third count
                                            input(
                                                f'{bulletpoint2}You opened the final box! The door opens and you reach to pick up the Elixir of the Gods! This item will help heal you 100 health once per battle.')
                                            hero.add_item(elixirofthegods)
                                            treasure_room_ending()
                                            print(
                                                f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                                            menu()
                                            beggar()
                                        else:
                                            question3_count -= 1
                                            if question3_count == 0:
                                                treasure_room_ending()
                                                menu()
                                                beggar()
                                else:
                                    question2_count -= 1
                                    if question2_count == 0:
                                        treasure_room_ending()
                                        menu()
                                        beggar()
                                    
                        else:
                            question_count -= 1
                    treasure_room_ending()
                    menu()
                    beggar()
        
                elif treasure_ans == '4':
                    add_health(ancientdrone) # Adds monster health if it has already been killed.
                    input(
                        f'{bulletpoint2}When you enter the room, you see a strange metal object that looks like it hasn\'t been cleaned in decades. All of a sudden the lights on it start lighting up, and it transforms into a large metal monster. It yells "Trespassers shall be terminated"!')
                    battle(hero, alexa9000, 'says "beep boop"',
                           'powers down', 'says "beep beep"', 'says "boop beep"')
                    input(
                        f'{bulletpoint2}You took care of the Robot monster! You reach to pick up the ancient drone! This robot will help you attack the enemy in battles.')
                    hero.add_item(ancientdrone) # Adds item attributes and to hero item list if the monster was killed.
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(ancientdrone) # Check if the monster died and will print that the monster has died.
                    treasure_room_ending()
                    print(
                        f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                    menu()
                    beggar()
        
                elif treasure_ans == '5':
                    input(
                        f'{bulletpoint2}When you enter the room, you see a strange crystal ball on a table. When you walk over to it, all of a sudden an invisible force stops you in your path and a voice asks you a question...')
                    random_num = random.randint(1,10) # Random number generator
                    tries = 3 # Number of tries
                    while tries != 0:
                        # Guessing Number Minigame
                        guess1 = input(
                            f'{bulletpoint}You have three chances to guess the correct number that was randomly selected from 1 to 10. What is your guess?')
                        if int(guess1) == random_num:
                            print(f'You guessed the correct number!')
                            tries = 0
                        else:
                            try:
                                if random_num > int(guess1): # If randon number is over the integer version of the guess.
                                    print(f'Remaining chances: {tries}\nYour guess was low, please try again...')
                                    tries -= 1
                                else:
                                    print(
                                        f'Remaining chances: {tries}\nYour guess was high, please try again...')
                                    tries -= 1
                            except:
                                print('Invalid answer.')
                                tries -= 1
                    if int(guess1) == random_num:
                        input(
                            f'{bulletpoint2}You foresaw the correct answer! You reach to pick up the crystal ball! This item will reveal the enemy\'s actions one time per battle.')
                        hero.add_item(merlinscrystalball) # Adds item attributes and to hero item list if the monster was killed.
                        treasure_room_ending()
                        print(
                            f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                        menu()
                        beggar()
                    else:
                        treasure_room_ending()
                        menu()
                        beggar()
        
                elif treasure_ans == '6':
                    add_health(griffin) # Adds monster health if it has already been killed.
                    input(
                        f'{bulletpoint2}When you enter the room, you see a magestic griffin monster with the body, tail, and back legs of a lion; the head and wings of an eagle. It turns over to you and starts attacking!')
                    battle(hero, griffin, 'tucks wings',
                           'beak turns left', 'flaps wings', 'raises talons')
                    input(
                        f'{bulletpoint2}You took care of the Griffin monster! You reach to pick up the Fireball scroll which tells you secret words! You can use this spell during battles to attack the enemy!')
                    hero.add_item(fireball) # Adds item attributes and to hero item list if the monster was killed.
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(griffin) # Check if the monster died and will print that the monster has died.
                    treasure_room_ending()
                    print(
                        f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                    menu()
                    beggar()
                elif treasure_ans == '7':
                    add_health(skeletonwarrior) # Adds monster health if it has already been killed.
                    input(
                        f'{bulletpoint2}When you enter the room, you see a skeleton with a shield and sword displayed in the middle of the room. You walk over and touch it. All of a sudden the hand grabs your arm and it starts attacking you!')
                    battle(hero, skeletonwarrior, 'raises shield','bones crack', 'cracks knuckles', 'raises sword')
                    input(
                        f'{bulletpoint2}You took care of the Skeleton monster! You reach to pick up the Warrior\'s Helm! This item will add 100 health.')
                    hero.add_item(warriorshelm) # Adds item attributes and to hero item list if the monster was killed.
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(skeletonwarrior) # Check if the monster died and will print that the monster has died.
                    treasure_room_ending()
                    print(
                        f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                    menu()
                    beggar()
                else:
                    print(f'{bulletpoint2}Please enter a valid choice number.')
                    menu()
                    treasure_room()
            
            #The Wizard
            def wizard():
                nonlocal current_heir
                nonlocal vendor_lady_object
                add_health(merlin)
                blackhole = '''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣋⡀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣶⣭⣻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣡⡴⠟⠋⡀⠶⠆⣀⣀⣀⣉⣘⠺⠷⣦⣌⡛⢿⣷⣬⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⡿⢋⣤⢘⣡⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣦⣉⠛⣶⣙⢻⣿⣾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢣⣿⠏⣰⣟⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣏⡿⣤⠙⠿⣿⣮⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⣿⡏⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢿⣧⣀⠈⠉⠻⢷⣬⣉⡛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣿⡿⢠⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢿⣯⠀⠀⠀⠀⠈⠉⠉⠛⠻⢶⡄⠀⣀⣨⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣾⡿⠃⣿⠋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠘⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣶⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢡⣾⠋⠀⠈⠿⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠛⠉⠉⠉⠸⠀⠀⠀⠀⢶⠾⠿⣟⣫⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢁⣼⠏⠀⠀⠀⠀⠀⠀⠹⡿⠋⣿⣿⡿⠿⠟⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣰⣆⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡿⠟⠋⠀⠒⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣰⡿⢱⡶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠁⣈⣉⣀⣀⣀⢀⣀⠀⣤⣤⣤⡀⢲⣶⣦⣄⠀⠀⠀⠀⠀⢠⣄⠀⣀⣀⠀⠀⠀⣀⣤⣶⣿⡿⠋⣴⡿⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⣤⣴⣭⣭⣽⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣾⣿⣿⣓⠻⢷⣄⡀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⣠⣾⠟⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⠙⣿⣷⣦⣄⣉⠉⠉⠉⢉⣡⣤⣶⡿⠋⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣭⣙⠛⠿⠿⡿⠿⠟⠛⠋⠁⠀⢀⣮⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠂⠀⢀⣀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        '''
                print('''Art by Morfina
                    ____
                  .'* *.'
               __/_*_*(_
              / _______ \\
             _\_)/___\(_/_
            / _((\- -/))_ \\
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \\
           / _ \ - | - /_  \\
          (   ( .;\'''; . .')
          _\\"__ / {o})\ __"/_
            \/  \   ' /  \/
             .'  '...' ' )
              / /  |  \ \\
             / .   .   . \\
            /   .     .   \\
           /   /   |   \   \\
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._ 
 _.-'       |      BBb       '-.  '-. 
(________mrf\____.dBBBb.________)____)''')
                wizard_ans_one = input(
                    f'{bulletpoint2}You enter a massive silver colored room with various foreign gadgets that make unfamiliar noise. An old man with a long beard and purple hat turns around and is suprised to see you. He starts questioning who you are and if you were sent by the emperor to kill him. Do you say yes or no:')
                if wizard_ans_one.lower() in yes:
                    input(
                        f'{bulletpoint2}The wizard sends three 🤖🤖🤖 magical metal beings to grab a hold of you. They make weird "beep boop noises".')
                    battle(hero, robots, 'say TURTLE MODE ACTIVATED!',
                           'say RECOVER MODE!', 'say ANALYZING FIGHT PATTERNS!', 'say ATTACK MODE!')
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(robots) # Check if the monster died and will print that the monster has died.
                    input(f'{bulletpoint2} You took care of these metal monsters. The wizard gets visibly furious and takes out a long glowing staff with a ball of electrical energy at the top. He starts cursing and says he\'ll take care of you himself!')
                    battle(hero, merlin, 'whispers "siri Beri nin"...',
                           'whispers "siri Rac cin"...', 'whispers "siri Gúl cai"...', 'whispers "siri Naur corn"...')
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(merlin) # Check if the monster died and will print that the monster has died.
                    add_money(200, 600) # Adds random amount of money to hero after boss battle between 200 and 600.
                    menu()
                    print(f'{bulletpoint2}The wizard Merlin was murdered. He had been imprisoned by the empire for decades, forced to build gadgets for the empire\'s grand plan. Rumors among the nobility spread that the empire figured out his schemes to take over using his magical metal beings. Rumors also had it that the empire planned to get rid of him before that happened. Back in the wizard\'s lab, you stood over his dead body with blood on your hands. You see a strange blue crystal ball in a separate translucent room and walk over to it.')
                    crystal_ball_ans = input(f'{bulletpoint}Do you touch the crystal ball?')
                    if crystal_ball_ans.lower() in yes:
                        vendor_lady_object = 1 # This turns on the vendor lady scenario when you restart
                        menu()
                        print(f'{bulletpoint}All of a sudden you\'ve been sucked into a hole. All you see around you is warped stars and you see a white hole in the distance...')
                        input(blackhole)
                        print(
                            f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                        beggar()
                    else:
                        print(
                            f'{bulletpoint}The room started sparking all over the place after the battle. All of a sudden you\'ve been sucked into a hole. All you see around you is warped stars and you see a black hole in the distance...')
                        input(blackhole)
                        print(
                            f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                        menu()
                        beggar()
                else:
                    input(
                        f'{bulletpoint2}The wizard introduces himself as Merlin. He said he had been imprisoned by the empire for decades, forced to build gadgets for the empire\'s grand plan. He was recently working on these metal beings and planned to copy them on behalf of the empire in order to save human lives.')
                    merlin_ans = input(
                        f'''
                        {bulletpoint}You decided to ask ONE of the following question:
                        1. Were you really going to use these metal beings to save human lives, or did you have ulterior motives?
                        2. How did you make all these gadgets?
                        3. Can I help you escape?

                        Please type the number for the question:
                        ''')
                    if merlin_ans == '1':
                        input(f'{bulletpoint2}Merlin tells you that he\'s seen visions of the prior human civilization in his crystal ball. He doesn\'t care about taking over the empire with what he calls the magical metal beings as "machines". He just wants to better humanity and steer the destruction of humanity to a more positive direction using the empire\'s finances. He gives you a secret tip that at the entrance of the passageway, you can say the magical phrase "opensesame" to instantly teleport you to the room with the three doors.')
                        input(
                            f'{bulletpoint2}Merlin says that if you touch the crystal ball, it will bring you to the past. Who wouldn\'t want to change something they regret in their lives! You walk over and see yourself in the crystal ball, you touch it and then all of a sudden you\'ve been sucked into a hole. All you see around you is warped stars and you see a white hole in the distance...')
                        input(blackhole)
                        current_heir = 'the beggar..' # Resets the current heir.
                        print(
                            f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                        menu()
                        beggar()
                    elif merlin_ans == '2':
                        input(f'{bulletpoint2}Merlin tells you that he only made 25% of the gadgets which were improved on remnant ancient technology. He says that in the ancient past, there was an advanced civilization called the "Hums" that developed flying ships and millions of machines. They were destroyed by war internally and made something called a "bomb" that destroyed cities with the power of a thousand suns.Speaking of bombs, Merlin reveals to you that if you ever play rock, paper, scissors, and whisper the magic word "bomb", you\'ll instantly win. Anyways, he says, after that civilization, the "An" civilization had to deal with the legendary dragon that fell from a space egg, which hatched on earth and caused havoc across the lands. They were the ones to help seal the dragon with ancient tech and save humanity. There are only a few kingdoms that managed to preserve some of the ancient technology today and they hold on to them to maintain their power. ')
                        input(
                            f'{bulletpoint}Merlin says that if you touch the crystal ball, it will bring you to the past. Who wouldn\'t want to change something they regret in their lives! You walk over and see yourself in the crystal ball, you touch it and then all of a sudden you\'ve been sucked into a hole. All you see around you is warped stars and you see a white hole in the distance...')
                        input(blackhole)
                        current_heir = 'the beggar..' # Resets the current heir.
                        print(
                            f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                        menu()
                        beggar()
                    elif merlin_ans == '3':
                        input(f'{bulletpoint2}Merlin says that\'s an interesting proposition! He tells you that he would love to explore the lands but he would need funding to carry on his experiments. If only we could get hands on the empire\'s treasury, now that\'s a different story...')
                        input(
                            f'{bulletpoint}Merlin says that if you touch the crystal ball, it will bring you to the past. Who wouldn\'t want to change something they regret in their lives! You walk over and see yourself in the crystal ball, you touch it and then all of a sudden you\'ve been sucked into a hole. All you see around you is warped stars and you see a white hole in the distance...')
                        input(blackhole)
                        current_heir = 'the beggar..' # Resets the current heir.
                        print(
                            f'{bulletpoint2}Congratulations, on reaching the end! Try to discover other secret endings and possibilities...')
                        menu()
                        beggar()
            # The Red Dragon
            def red_dragon():
                add_health(tiamat)
                print(
                    '''                                                ,d888*`
                                              ,d888`
                                            ,d888`
                                           ,d88`
                                         ,d88`
                                        ,d8`
                                      ,d8*                 ..d**
                                    ,d88*             ..d**`
                                  ,d88`         ..d8*`
                                ,d888`    ..d8P*`
                        .     ,d8888*8888*`
                      ,*     ,88888*8P*
                    ,*      d888888*8b.
                  ,P       dP  *888.*888b.
                ,8*        8    *888  `**88888b.
              ,dP                *88           *88b.
             d8`                  *8b               *8b.
           ,d8`                    *8.                  *88b.
          d8P                       88.                    *88b
        ,88P                        888
       d888*       .d88P            888
      d8888b..d888888*              888
    ,888888888888888b.              888
   ,8*;88888P*****788888888ba.      888
  ,8;,8888*        `88888*          d88*
  )8e888*          ,88888be.        888
 ,d888`           ,8888888***     d888
,d88P`           ,8888888Pb.     d888`
888*            ,88888888**   .d8888*
`88            ,888888888    .d88888b
 `P           ,8888888888bd888888*
              d888888888888d888*
              8888888888888888b.
              88*. *88888888888b.        .db
              `888b.`8888888888888b. .d8888P
               **88b.`*8888888888888888888888b...
                *888b.`*8888888888P***7888888888888e.
                 88888b.`********.d8888b**`88888P*
                 `888888b     .d88888888888**`8888.
                  )888888.   d888888888888P   `8888888b.
                 ,88888*    d88888888888**`    `8888b
                ,8888*    .8888888888P`          `888b.
               ,888*      888888888b...            `888P88b.
      .db.   ,d88*        88888888888888b          `8888
  ,d888888b.8888`         `*888888888888888888P`   `888b.
 /*****8888b**`              `***8888P*``8888`       `8888b.
      /**88`                 .ed8b..  .d888P`            `88888
                           d8**888888888P*               `88b
                          (*``,d8888***`                    `88
                             (*`                             `88
                                                              88
                                                              88
                                                             `8
                                                             d8
                ''')
                input(
                    f'{bulletpoint2}You enter a massive cavern that is pitch black. All of a sudden you see flames in front of you and its bone-chilling face appears. You realized that this was the legendary red dragon Tiamat which fell from the heavens onto Earth in the ancient past. You remembered the myth that it caused havoc across the lands, before it was finally captured and sealed by magic by the ancient advanced civilization... ')
                input(f'{bulletpoint2}The doors behind you magically disappeared or blended into the wall. There was no escape. You thought about all the choices you made prior to choosing this door, and what you could have done to avoid this fate. You face death in front of you and it\'s too late to turn back...')
                # Same boss, but different health and moves depending if the hero already killed the first one.
                if tiamat.health <= 1000:
                    battle(hero, tiamat, 'raises all wings',
                        'lifts right wing', 'flaps wings', 'lifts left wing')
                else:
                    battle(hero, tiamat, 'raises all four wings',
                           'slowly lifts wing', 'raises left wing', 'shoots red fireballs from mouth')
                    input(f'{bulletpoint}Congratulations on defeating Tiamat for the second time! You\'ve unlocked the ability to summon different gods to the battlefield with the phrase "summonthegods"! Enjoy!')
                check_health(hero) # Check if the hero died and will restart game if that is the case.
                add_money(200, 1000) # Adds random amount of money to hero after boss battle between 200 and 1000.
                menu()
                input(f'{bulletpoint}You beat the Red Dragon Tiamat! All of a sudden... Tiamat\'s body starts moving again. Tiamat starts sprouting two extra wings and its muscles double in size. Its eyes glow red with smoke steaming out as it gets up and flies away. What could this mean...?\nCongratulations, on reaching the end! Try to discover other secret endings and possibilities... ')
                input(f'{bulletpoint2}Press enter to continue...')
                beggar()
            # Passageway
            def passageway():

                passageway_ans = input(
                    f'\n{bulletpoint}While walking through the castle, you notice an obscure passageway behind a painting that wasn\'t fully closed. Do you enter it?\n\n\n\n\n\n\n\n\n\n')
                if passageway_ans.lower().strip() in yes:
                    left = 'left'
                    right = 'right'
                    down = 'down'
                    up = 'up'
                    movement = 1
                    spider_alive = 1 # If the spider has already been killed, the spider monster will not show up in the map. 1 represents the spider still being alive, and this wil reset the spider if player is going through another round of the game.

                    def maze():
                        input(
                            f'Movements:\n🠸: "Left"     🠺: "Right" \n🠹: "Up"     🠻: "Down" ')
                        while movement == 1:

                            def wall_2down():
                                print('▄▄▄▄   ▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄           ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄     𐀪 ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄')
                                direction = input(
                                    f'{bulletpoint}Which direction would you like to take:')
                                if direction == up:
                                    wall_1down()
                                elif direction == left:
                                    wall_2left()
                                else:
                                    wall_2down()

                            def wall_2left():
                                print('▄▄▄▄   ▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄           ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 𐀪     ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == down:
                                    wall_2leftdown()
                                elif direction == right:
                                    wall_2down()
                                else:
                                    wall_2left()

                            def wall_2leftdown():
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▩              𐀪 ▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == left:
                                    wall_2leftdownleft()
                                elif direction == up:
                                    wall_2left()
                                else:
                                    wall_2leftdown()

                            def wall_2leftdownleft():
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▩𐀪               ▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                openchest = input(
                                    f'{bulletpoint}Would you like to open the chest?')
                                if openchest == 'yes':
                                    print('Chest opened. Nothing inside.')
                                    input(
                                        f'{bulletpoint}Which direction would you like to take:\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                    if spider_alive == 1: # Opens up the monster scene if spider is still alive.
                                        maze_monster()
                                    wall_2leftdown()
                                else:
                                    input(
                                        f'{bulletpoint}Which direction would you like to take:\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                    if spider_alive == 1:  # Opens up the monster scene if spider is still alive.
                                        maze_monster()
                                    wall_2leftdown()

                            def secret_corridor():
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄      𐀪⨔')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                 ▄▄▄▄▄▄')
                                print('▄▄▄▄         ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                if ringofnirvana.name not in hero_items:
                                    take_ring = input(
                                        f'{bulletpoint}You hear a acoustic humming noise and see a shining ring floating in mid air. Do you take it?')
                                    if take_ring.lower() == 'yes':
                                        if ringofnirvana not in hero_items:
                                            input(
                                                f'{bulletpoint2}You took it and wore the {ringofnirvana.name}. You feel your health increase by {ringofnirvana.health_bonus}!')
                                            hero.add_item(ringofnirvana)
                                            menu()
                                    else:
                                        input(
                                            f'{bulletpoint}You left it where it stood.')
                                else:
                                    input(
                                        f'{bulletpoint}You hear a acoustic humming noise and you glance at the ring on your finger.')
                                    menu()
                                direction = input(
                                    f'{bulletpoint}Which direction would you like to take:')
                                if direction == left:
                                    wall_1down()
                                else:
                                    secret_corridor()


                            def wall_1down():
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                if spider_alive == 1: #Prints the closed room below if spider is still alive.
                                    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                else: # Secret passageway opens up after spider is killed.
                                    print(
                                        '▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       ⨔')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄               𐀪 ▄▄▄▄▄▄')
                                print('▄▄▄▄         ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == down:
                                    wall_2down()
                                elif direction == left:
                                    wall_1left()
                                elif direction == up:
                                    print(
                                        f'{bulletpoint2}The passageway entrance is locked.')
                                    wall_1entrance()
                                elif direction == right:
                                    if spider_alive == 0:
                                        secret_corridor()
                                    else:
                                        wall_1down()
                                else:
                                    wall_1down()

                            def wall_1left():
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 𐀪               ▄▄▄▄▄▄')
                                print('▄▄▄▄         ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == down:
                                    wall_1leftdown()
                                elif direction == right:
                                    wall_1down()
                                else:
                                    wall_1left()

                            def wall_1leftdown():
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                 ▄▄▄▄▄▄')
                                print('▄▄▄▄         ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄         𐀪 ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == left:
                                    wall_1leftdownleft()
                                elif direction == up:
                                    wall_1left()
                                else:
                                    wall_1leftdown()

                            def wall_1leftdownleft():
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                 ▄▄▄▄▄▄')
                                print('▄▄▄▄         ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄ 𐀪         ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == up:
                                    wall_1leftdownleftup()
                                elif direction == right:
                                    wall_1leftdown()
                                else:
                                    wall_1leftdownleft()

                            def wall_1leftdownleftup():
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                 ▄▄▄▄▄▄')
                                print('▄▄▄▄       𐀪 ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄           ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == left:
                                    wall_1leftdownleftupleft()
                                elif direction == down:
                                    wall_1leftdownleft()
                                else:
                                    wall_1leftdownleftup()

                            def wall_1leftdownleftupleft():
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                 ▄▄▄▄▄▄')
                                print('▄▄▄▄ 𐀪       ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄           ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == down:
                                    wall_3()
                                elif direction == right:
                                    wall_1leftdownleftup()
                                else:
                                    wall_1leftdownleftupleft()

                            def wall_3():
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄ 𐀪                             ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄           ▄▄▄▄▄▄')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == right:
                                    wall_3right()
                                elif direction == down:
                                    wall_3down()
                                elif direction == up:
                                    wall_1leftdownleftupleft()
                                else:
                                    wall_3()

                            def wall_3down():
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄ᬛ')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄ 𐀪 ▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄🚪▄▄▄▄▄▄▄▄▄▄▄')
                                print('The door is locked.')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == up:
                                    wall_3()
                                else:
                                    wall_3down()

                            def wall_3right():
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄                             𐀪 ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄           ▄▄▄▄▄▄')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == left:
                                    wall_3()
                                elif direction == down:
                                    wall_3rightdown()
                                else:
                                    wall_3right()

                            def wall_3rightdown():
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄                               ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄         𐀪 ▄▄▄▄▄▄')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == left:
                                    wall_3_rightdownleft()
                                elif direction == up:
                                    wall_3right()
                                else:
                                    wall_3rightdown()

                            def wall_3_rightdownleft():
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 𐀪         ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄🚪▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                opendoor = input(
                                    f'{bulletpoint}Would you like to open the door?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                if opendoor.lower() == 'yes':
                                    vaulted_chambers()
                                else:
                                    wall_3rightdown()

                            def vaulted_chambers():
                                nonlocal movement
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄🚪▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄᭄    ᭄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄ᬛ|       |ᬊ▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄ᬛ|         |ᬊ▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄ᬛ|      𐀪    |ᬊ▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄ᬛ|          |ᬊ▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄ᬛ|        |ᬊ▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄🚪𐀐𝄩𐀢𝄩𐀩🚪▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄🚪▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄🚪▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                three_doors_ans = input(
                                    f'{bulletpoint}You\'re in a black colored mirror room with symbols on the walls that are glowing. Which door would you like to open?\n Choices are "Left", or "Down", or "Right":')
                                if three_doors_ans.lower() == left:
                                    print(f'{bulletpoint2}Treasure room')
                                    input(
                                        f'{bulletpoint2}Press enter to open to door...')
                                    menu()
                                    movement -= 1
                                    treasure_room()
                                elif three_doors_ans.lower() == right:
                                    print(f'{bulletpoint2}Wizard room')
                                    input(
                                        f'{bulletpoint2}Press enter to open to door...')
                                    menu()
                                    movement -= 1
                                    wizard()
                                elif three_doors_ans.lower() == down:
                                    print(f'{bulletpoint2}Dragon room')
                                    input(
                                        f'{bulletpoint2}Press enter to open to door...')
                                    menu()
                                    movement -= 1
                                    red_dragon()
                                else:
                                    wall_3_rightdownleft()

                            def maze_monster():
                                nonlocal spider_alive
                                add_health(arachne)
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 🕷▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▩               𐀪▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                input(
                                    f'{bulletpoint}A Massive 10 foot {arachne.name} dropped from the ceiling! You\'re trapped, there\'s no where to run except to fight!')
                                battle(hero, arachne, 'spins web',
                                    'shrieks', 'sprays web', 'shows fangs')
                                check_health(hero)
                                check_health(arachne) # Check if the monster died and will print that the monster has died.
                                spider_alive -= 1 # Spider counter reduced, which opens up secret passageway.
                                add_money(50, 200) # Adds hero money between 50 to 200.
                                menu()
                                input(
                                    f'{bulletpoint2}You hear the walls rumbling in the distance...')
                                wall_2leftdown()

                            def wall_1entrance():
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄🚪▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 𐀪 ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                 ▄▄▄▄▄▄')
                                print('▄▄▄▄         ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                direction = input(
                                    f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bulletpoint}Which direction would you like to take:')
                                if direction == down:
                                    wall_1down()
                                elif direction == up:
                                    print(
                                        f'{bulletpoint}The passageway entrance is locked.')
                                    wall_1entrance()
                                elif direction == 'opensesame':
                                    vaulted_chambers()

                            wall_1entrance()
                        # Full Passageway Map
                        #'▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄🚪▄▄▄▄▄▄'
                        #'▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 𐀪 ▄▄▄▄▄▄'
                        #'▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄'
                        #'▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄'
                        #'▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                 ▄▄▄▄▄▄'
                        #'▄▄▄▄         ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄           ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▩                 ▄▄▄▄▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄'
                        #'▄▄▄▄                               ▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄           ▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄🚪▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄᭄    ᭄▄▄▄▄▄▄▄▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄ᬛ|       |ᬊ▄▄▄▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄ᬛ|         |ᬊ▄▄▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄ᬛ|           |ᬊ▄▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄ᬛ|          |ᬊ▄▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄ᬛ|        |ᬊ▄▄▄▄▄▄▄▄'
                        #'▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄🚪𐀐𝄩𐀢𝄩𐀩🚪▄▄▄▄▄▄▄▄▄'
                        #'▄▄▄▄🚪▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄🚪▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄'
                    
                    maze()
                    
                else:
                    input(f'\n{bulletpoint2}You walk along the streets to find a job, but no one you encountered would hire someone with a missing {body_part}. You then come across a mysterious monk.')
                    menu()
                    mysterious_monk()

            # The Mysterious Monk
            def mysterious_monk():
                mysterious_monk_ans = input(
                    f'\n{bulletpoint}A mysterious monk came to you and asks if you would be so kind to help with a task. The monk says it won\'t be easy and there is no pay. Do you still help?')
                if mysterious_monk_ans.strip().lower() in yes:
                    print(f'\n{bulletpoint2} You\'ll be joining the monk to help lead this journey. The monk gives you an ancient map that shows different routes you can take to reach the top. ') 
                    hero.morality += 10
                    menu()
                    the_secret()
                else:
                    pass

            # Bestfriend

            def best_friend():
                best_friend_ans = input(
                    f'\n{bulletpoint}After some deep talks, your best friend revealed that he had previously been imprisoned by the empire because of his family line. He still had no idea the true reason but he was imprisoned anyways, and he made several attempts to escape.\n He asks if you would like to play a game to lighten the mood?')
                if best_friend_ans.strip().lower() in yes:
                    game_ans = input(
                        f'\n{bulletpoint2}The game is called Rock Paper Scissors! 🪨 Rock beats ✂ Scissors, 📜 Paper beats 🪨 Rock, ✂ Scissors beats 📜 Paper!\n Enter Rock, Paper, or Scissors:')
                    playGame(game_ans)
                    game_ans2 = input(
                        f'\n{bulletpoint2}Your best friend laughs!\n Enter Rock, Paper, or Scissors:')
                    playGame(game_ans2)
                    game_ans3 = input(
                        f'\n{bulletpoint2}Last round to see who\'s the true winner!\n Enter Rock, Paper, or Scissors:')
                    playGame(game_ans3)
                    riddle_ans1 = random.choice(alphabet).capitalize()
                    riddle_ans2 = random.choice(['emperor', 'queen', 'dragon'])
                    input(f'{bulletpoint2}Good times! Drinks on your best friend\'s tab! After the last drink, your best friend proposed an idea to make some life-changing money. During his extensive time of imprisonment, he overheard the Emperor whispering about some hidden castle passageway. It was apparently located behind a painting of the {riddle_ans2} at tower {riddle_ans1} to access his bank...\n\n\n\n\n\n\n\n\n\n')
                    menu()

                    # The Bank Robbery
                    riddle_ans3 = random.choice(['2:38', '3:28', '3:32'])
                    bank_robbery_ans = input(
                        f'\n{bulletpoint2}You meet with your best friend to discuss the plan. He proposed that we first meet outside the tavern at precisely {riddle_ans3} in the morning. Then we take out the two guards and wear their black and red clothing...')
                    tavern_ans = input(f'\n{bulletpoint}He says we need to remember this plan. He asks you if you remember where outside we meet again?\n\n\n\n\n\n\n\n\n\n')
                    if tavern_ans.lower().strip() in ['tavern','the tavern']:
                        riddle_question1 = input(
                            f'\n{bulletpoint}Very good. Do you remember what was the painting that the passageway is hidden behind?\n\n\n\n\n\n\n\n\n\n')
                        if riddle_question1.lower().strip() == riddle_ans2:
                            riddle_question2 = input(
                                f'\n{bulletpoint}Not bad. Do you recall the exact time we need to meet in the morning?\n\n\n\n\n\n\n\n\n\n')
                            if riddle_question2.lower().strip() == riddle_ans3:
                                riddle_question3 = input(
                                    f'\n{bulletpoint}Last question! What letter was the tower located at?')
                                if riddle_question3.lower().strip() == riddle_ans1.lower():
                                    print(f'{bulletpoint2}You\'re ready! You and your best friend get some early rest to prepare for this dangerous mission.')
                                    random_health_gain = random.randint(10, 20)
                                    print(
                                        f'{bulletpoint2} You slept and gained {random_health_gain} health back.')
                                    hero.health += random_health_gain
                                    check_health(hero)
                                    menu()
                                    passageway()
                                else:
                                    print(
                                        f'{bulletpoint2}You were so close! Your best friend says you can think about this job another time.')
                                    menu()
                                    # Add The secret() or this will lead back to the vendor menu
                            else:
                                print(
                                    f'{bulletpoint2}Nice try! Your best friend says you can think about this job another time.')
                                menu()
                                # Add The secret() or this will lead back to the vendor menu
                        else:
                            print(f'{bulletpoint2}Perhaps listen carefully! Your best friend says you can think about this job another time.')
                            menu()
                            # Add The secret() or this will lead back to the vendor menu
                    else:
                        print(f'{bulletpoint2}You\'re not listening! Your best friend says you can think about this job another time.')
                        menu()
                        # Add The secret() or this will lead back to the vendor menu
                else:
                    input(f'\n{bulletpoint2}Perhaps next time then. Your best friend says it\'s getting late and we should leave before the nightwolves start roaming the streets. As you leave a hooded person with an insignia of the red dragon empire grabbed you in the darkness... ')
                    menu()
                    # Add The secret() or this will lead back to the vendor_lady

            # Vendor Lady
            def vendor_lady():
                nonlocal vendor_lady_object # Accesses the vendor_lady count.
                vendor_ans = input(f'\n{bulletpoint}An elder vendor lady has some rare and mythical items for sale. She says that she\'s only going to be available now one time, as she needs to leave to a faraway kingdom. Would you like to purchase something?') 
                if vendor_ans.strip().lower() in yes:
                    show_vendor_menu()
                    menu()
                    vendor_lady_object -= 1 # Turns off the vendor_lady scenario
                else:
                    print(f'\n{bulletpoint2}You visit a local tavern and meet someone who became your best friend over the course of months.')
                    vendor_lady_object -= 1  # Turns off the vendor_lady scenario
                    best_friend()
                    menu()

            # The Beggar
            def beggar():
                if current_heir == 'Beggar' or current_heir == 'The Beggar':
                    beggar_ans = input(f'\n{bulletpoint}The beggar shows his gratitude for delivering the message and as a small token of appreciation hands you a lump of gold that he retrieved from the castle bank.\nHe says he just remembered he needs $5 back since he needs to buy some food from the local shops. Do you give him the money?')
                    add_money(100,1000)
                else:
                    beggar_ans = input(f'\n{bulletpoint}You\'re walking through the bustling streets of the Red Dragon Empire. A dirty old beggar comes up to you asking $5 for food. Do you give him the money?')
                if beggar_ans.strip().lower() in yes:
                    print(f'\n{bulletpoint2}You hand over $5 and he thanks you for your kindness. The beggar introduces you to a mysterious monk who needs some assistance with something.') 
                    hero.money -= 5
                    hero.morality += 5
                    menu()
                    mysterious_monk() 
                else:
                    if current_heir == 'Beggar' or current_heir == 'The Beggar':
                        print(
                            f'\n{bulletpoint2}You kick him, spit on him, and yell that you don\'t acknowledge a dirty beggar as the next heir and walk away laughing.')
                        hero.morality -= 5
                        menu()
                    else:
                        print(f'\n{bulletpoint2}You kick his bowl of change, spit on him, and walk away laughing.')
                        hero.morality -= 5
                        menu()

                    # Three Thugs
                    three_thugs_ans = input(f'\n{bulletpoint}The beggar calls three muscular street thugs over and asks them to rough you up. Do you stay and fight?')
                    if three_thugs_ans.strip().lower() in yes:
                        damage = random.randint(3,20)
                        input(f'\n{bulletpoint2}The thugs landed a couple large blows to your stomach and did {damage} damage to your health. You managed to run away as fast as possible to a local street vendor nearby to hide.') 
                        hero.health -= damage
                        menu()
                        if vendor_lady_object == 1: # Only accesses the vendor lady scenario if it's been turned on.
                            vendor_lady()
                        else:
                            pass
                            #secret_item()
                    else:
                        input(f'\n{bulletpoint2}You ran over to the castle guards and the street thugs dissapeared. ')
                        menu()
                        if current_heir == hero_name.title():
                            input(f'{bulletpoint2}The guards yell to PROTECT THE HEIR! The guards then locate the street thugs and proceed to send them to jail. The guards then royally escort you into the castle immediately.')
                            new_path = input(f'\n{bulletpoint}One of your advisors tells you that there is a trade mission that you should go on. You also feel like exploring the castle more. What do you do?')
                            if 'trade' or 'mission' in new_path:
                                menu()
                                input(f'{bulletpoint2}There was new land to the south just recently discovered. Your mission was to conquer it and establish a colony on behalf of the Red Dragon Empire.')
                                trade_mission()
                            else:
                                menu()
                                passageway()
                        else:
                            # Guard Bribe
                            guard_bribe_ans = input(f'\n{bulletpoint}One of the guards suspects you as being an illegal foreigner from the neighboring enemy kingdom, but if you give him some bribe money, he\'ll turn a blind eye. Do you give him the money?')
                            if guard_bribe_ans.strip().lower() in yes:
                                bribe = random.randint(1,10)
                                if bribe >= 5:
                                    print(f'\n{bulletpoint2}You give the guard ${bribe}.') 
                                    hero.money -= bribe
                                    menu()
                                    empire_recruitment()
                                else:
                                    damage = random.randint(1,10)
                                    print(f'\n{bulletpoint2}You give the guard ${bribe}. He yells that this is barely anything and slams you into the ground dealing {damage} to you.')
                                    hero.health -= damage
                                    hero.money -= bribe
                                    menu()
                                    empire_recruitment()
                            else:
                                print(f'\n{bulletpoint2}He yells at you, calls you a peasant, and then proceeds to jail you in the castle dungeon. ')
                                menu()

                                #Jail Inmate
                                global body_part
                                body_part = 'arm'
                                body_part = input(f'In your jail cell, you see the inmate next to you with one only one...(type which body part)...body part:')
                                jail_inmate_ans = input(f'\n{bulletpoint}The inmate with only one {body_part} asks if you would like to be his friend?')
                                if jail_inmate_ans.strip().lower() in yes:
                                    input(f'\n{bulletpoint2}The inmate tells you that for the last year he\'s been digging a hole underneath his bed. He say\'s it\'s finally ready and wants you to join him to make the escape.')
                                    input(
                                        f'\n{bulletpoint2}In the middle of the night, the inmate lifts his bed and you both went into the hole and made your way out from the sewers. You\'re free now! You and the inmate decide to wash up and then celebrate at a local tavern.')
                                    best_friend()
                                    menu()
                                else:
                                    input(f'\n{bulletpoint2}You sleep in the damp dark cell filled with dead rats and a repulsive stench. You wake up the next morning and discover your inmate has disappeared. You discover a hole underneath his bed, and prepare to make your escape...but just as you\'re about to leave, the guards force you out and says the captain wants to speak with you immediately!')
                                    menu()

                                    #Captain Offer
                                    captain_offer_ans = input(f'\n{bulletpoint}The captain says he\'s looking for some prisoners to help get rid of a local monster that\'s been causing problems. He asks if you would like to fight, and in return, you\'ll be freed and provided some money. Do you accept the offer?')
                                    if captain_offer_ans.strip().lower() in yes:
                                        empire_recruitment()
                                        menu()
                                    else:
                                        damage = random.randint(5, 15)
                                        hero.health -= damage
                                        input(f'\n{bulletpoint2}The captain says that they will chop off your {body_part} since they caught you trying to escape the dungeon. You try to run and immediately get beaten up badly by the nearby guards. They do {damage} damage to you.')
                                        menu()

                                        #Torture Room
                                        torture_room_ans = input(f'\n{bulletpoint}You are moved to a locked room with a table, and surrounded by various horrifying devices. You see the guard get ready to chop off your {body_part}, and he turns around to pick up a sharp object. While he\'s not noticing, you see a small nail on the ground that is within your reach. Do you reach for the nail? ')
                                        if torture_room_ans.strip().lower() in yes:
                                            input(f'\n{bulletpoint2}You managed to pick up the nail and just as the guard is about to saw your arm off, you stab him in the eye! You found the door keys on his person, and used the saw to cut off the ropes tying you down to make your escape.')
                                            menu()
                                        else:
                                            damage = random.randint(30,80)
                                            hero.health -= damage
                                            print(f'\n{bulletpoint2}Feeling helpless, you\'ve lost any hope in trying to escape, and the guard proceeds to cut off your {body_part}. You start screaming in agony as the guard does {damage} damage to your health.\n...')
                                            if current_heir == 'Beggar' or current_heir == 'The Beggar':
                                                input(
                                                    f'\n{bulletpoint2}As you lay on the ground, you see the beggar laughing at you and proceeded to spit and kick you. You blackout from the pain.\n')
                                            menu()
                                            check_health(hero) # Check if the hero died and will restart game if that is the case.
                                            input(f'\n{bulletpoint2}A year has passed. You wake up on the last day of your sentence and glance at the hole that had been sealed up by the guards. You\'ve recovered a little bit after losing your {body_part}, and you\'ve learned to cope. They finally let you free.')
                                            hero.health += 30 # Adds 30 health points to hero
                                            check_health(hero) # Check again if the hero died if the hero hp is still below 0.
                                            menu()
                                            passageway()
            beggar()

        def menu():
            
            def items():

                if hero.morality >= 80:
                    print('( ͡ᵔ ͜ʖ ͡ᵔ)')
                elif hero.morality >= 60:
                    print('( ͡❛ ͜ʖ ͡❛)')
                elif hero.morality >= 40:
                    print('( ͡❛ ▭ ͡❛)')
                elif hero.morality >= 20:
                    print('( ͡❛ 皿 ͡❛)')
                else:
                    print('( ͡❛ 益 ͡❛)')
                print('Current Items:')
                
                print([i for i in hero_items])
            
            # This is the menu display that would be shown throughout the game. It shows hero health, money, morality, and a different display if hero health is under a certain amount.
            def display():
                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                if hero.health <= 25:
                    print('█             █     █          █    ▐        ▐               █    █     █    ▐   █          █   █    █       █ █    ▐   ▐              ')
                    print('▐             ▐     ▐          ▐                             ▐    ▐     ▐        ▐          ▐   ▐    ▐       ▐ ▐                        ')
                
                print(f'█   Money: ${hero.money}                                        Morality: {hero.morality}                                    Remaining Health: {hero.health}        █')
                items()
                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                if hero.health <=50:
                    print('        █             █     █          █    ▐        ▐               █    █     █    ▐   █          █   █    █       █ █    ▐   ▐              ')
                    print('        ▐             ▐     ▐          ▐                             ▐    ▐     ▐        ▐          ▐   ▐    ▐       ▐ ▐                        ')
                print('\n\n\n\n\n\n\n\n\n\n\n')
            display()
        menu()
        story()

    restart()
# The start of the game asks for the player to name their hero. This will be a global variable. They can also exit the game. 
def ask_hero_name():
    global hero_name
    hero_name = input('What is the name of your hero?')
    print(
        f'''              _____________________
            / \                    \\
           |   |     Welcome        \  
           \_ |      {hero_name}       
              |      to              |
              |      Choose          |
              |      Your Own        |                Ascii art from:       asciiart.eu
              |      Adventure Game! |                Emotes from:          texteditor.com
              |                      |                Game developed by:    James L.
              |   _________________ _|__
              |  /                     /
              \_/_____________________/''')
    continue_game = input('Would you like to continue? "yes" or "no"?')
    if continue_game.strip().lower() in yes:
        print('You have only one life... be cautious...')
        adventure_game()
    else:
        print('You have successfully exited the game.')
        pass

ask_hero_name()

# Exit function.
def exit():
    pass

