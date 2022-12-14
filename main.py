# -*- coding: utf-8 -*-
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
    '🍇': 0, '☕️': 0, '🌽': 0, '🍯': 0, '🦪': 0, '🍍': 0, '🐡': 0, '🍨': 0, '⚗️': 0, 
}
# Special items that add different abilities in monster battles.
battle_items = [
    '🏺- Invisibility Potion', '🔮Merlin\'s Crystal Ball', '☄️Fireball Spell', '🍶Elixir of the Gods', '👾Ancient Drone', '⛣- Ring of Nirvana']

def exit_game():
    exit()

def adventure_game():
    bulletpoint = '✴ ' # Used to emphasize requiring the user's input for the story.
    bulletpoint2 = '◼ '# Regular bulletpoint for sentences not requiring user's input.
       
    def restart():
        vendor_lady_object = 1 
        monster_guild_membership = False
        assassin_guild_membership = False
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
        valkyrie_crossbow = Item('🏹- Valkyrie', 200, 50)
        boomerang = Item('🪃- Boomerang', 0, 15)
        thors_hammer = Item('⚒️- Thor\'s Hammer', 100, 100)
        redempireflag = Item('🚩- Red Empire Flag', 100, 0)
        dragonscale = Item('🛡️- Dragonscale', 200, 0)
        merlins_crystal_ball = Item('🔮Merlin\'s Crystal Ball', 0, 0)
        fireball_spell = Item('☄️Fireball Spell', 0, 0)
        elixir_of_the_gods = Item('🍶Elixir of the Gods', 0, 0)
        ancient_drone = Item('👾Ancient Drone', 0, 0)
        ring_of_nirvana = Item('⛣- Ring of Nirvana', 0, 0)
        ancientriotshield = Item('🛡️ Ancient Riot Shield', 100, 0)
        adamantineblade = Item('🗡 Adamantine Blade', 0, 90)
        warriorshelm = Item('👑 Warrior\'s Helm', 100, 0)

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
        minotaur = Monster('Minotaur', 150, 50, 85)
        beggarbattle = Monster('Beggar', 50, 10, 20)
        emperorbattle = Monster('Emperor', 50, 10, 30)
        cornstalker = Monster('Cornstalker', 200, 80, 180)
        gloopus = Monster('Gloopus', 180, 70, 200)
        behemoth = Monster('Behemoth', 250, 100, 250)
        goldscale = Monster('Goldscale', 250, 100, 400)
        snowfang = Monster('Snowfang', 180, 80, 200)

        available_monster_list = [sandworm, giant, arachne, tiamat, merlin, robots, kitty, fenrir,
                                  alexa9000, griffin, skeletonwarrior, boxer, leviathan, phoenix, 
                                  minotaur, cornstalker, gloopus, behemoth, goldscale, snowfang]
        tamed_monster_list = []

        # Initialized a variable to store the total number of endings
        total_ending_count = 0
        # Created a list of ending values
        ending1 = 1
        ending2 = 1
        ending3 = 1
        ending4 = 1
        ending5 = 1
        ending6 = 1
        ending7 = 1
        ending8 = 1
        ending9 = 1
        ending10 = 1
        ending11 = 1
        ending12 = 1
        ending13 = 1
        ending14 = 1
        ending15 = 1
        ending16 = 1
        ending17 = 1
        ending18 = 1
        ending19 = 1
        ending20 = 1
        ending21 = 1
        ending22 = 1
        ending23 = 1
        ending24 = 1
        ending25 = 1
        ending26 = 1
        ending27 = 1
        ending28 = 1
        ending29 = 1
        ending30 = 1
        ending31 = 1
        list_of_endings = [ending1, ending2, ending3, ending4, ending5, ending6, ending7, ending8, ending9, ending10, ending11, ending12, ending13, ending14, ending15, ending16, ending17, ending18, ending19, ending20, ending21, ending22, ending23, ending24, ending25, ending26, ending27, ending28, ending29, ending30, ending31]
        # Defined a function to handle the endings and add them to the total ending count
        def ending(scenario):
            nonlocal total_ending_count
            congrats1 = '''
                 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄     ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄ 
                █       █       █  █  █ █       █   ▄  █ █      █       █  █ █  █   █   █      █       █   █       █  █  █ █       █  █
                █       █   ▄   █   █▄█ █   ▄▄▄▄█  █ █ █ █  ▄   █▄     ▄█  █ █  █   █   █  ▄   █▄     ▄█   █   ▄   █   █▄█ █  ▄▄▄▄▄█  █
                █     ▄▄█  █ █  █       █  █  ▄▄█   █▄▄█▄█ █▄█  █ █   █ █  █▄█  █   █   █ █▄█  █ █   █ █   █  █ █  █       █ █▄▄▄▄▄█  █
                █    █  █  █▄█  █  ▄    █  █ █  █    ▄▄  █      █ █   █ █       █   █▄▄▄█      █ █   █ █   █  █▄█  █  ▄    █▄▄▄▄▄  █▄▄█
                █    █▄▄█       █ █ █   █  █▄▄█ █   █  █ █  ▄   █ █   █ █       █       █  ▄   █ █   █ █   █       █ █ █   █▄▄▄▄▄█ █▄▄ 
                █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█▄█ █▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█ █▄▄█ █▄▄▄█ █▄▄▄█▄▄▄▄▄▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█▄▄█
                '''
            congrats2 = '''
                ░█▀▄░▄▀▀▄░█▀▀▄░█▀▀▀░█▀▀▄░█▀▀▄░▀█▀░█░▒█░█░░█▀▀▄░▀█▀░░▀░░▄▀▀▄░█▀▀▄░█▀▀░█
                ░█░░░█░░█░█░▒█░█░▀▄░█▄▄▀░█▄▄█░░█░░█░▒█░█░░█▄▄█░░█░░░█▀░█░░█░█░▒█░▀▀▄░▀
                ░▀▀▀░░▀▀░░▀░░▀░▀▀▀▀░▀░▀▀░▀░░▀░░▀░░░▀▀▀░▀▀░▀░░▀░░▀░░▀▀▀░░▀▀░░▀░░▀░▀▀▀░▄'''
            congrats3 = '''
                ┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┏┓┃┃┃┃┓┃┃┃┃┃┏┓┃┃┃┃┃┃┃┃┃┃┃┓
                ┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┛┗┓┃┃┃┃┃┃┃┃┃┛┗┓┃┃┃┃┃┃┃┃┃┃┃
                ┏━━┓━━┓━┓┃━━┓━┓━━┓┃┓┏┛┓┏┓┃┃━━┓┃┓┏┛┓━━┓━┓┃━━┓┃
                ┃┏━┛┏┓┃┏┓┓┏┓┃┏┛┃┓┃┃┃┃┃┃┃┃┃┃┃┓┃┃┃┃┃┫┏┓┃┏┓┓━━┫┛
                ┃┗━┓┗┛┃┃┃┃┗┛┃┃┃┗┛┗┓┃┗┓┗┛┃┗┓┗┛┗┓┃┗┓┃┗┛┃┃┃┃━━┃┓
                ┗━━┛━━┛┛┗┛━┓┃┛┃━━━┛┗━┛━━┛━┛━━━┛┗━┛┛━━┛┛┗┛━━┛┛
                ┃┃┃┃┃┃┃┃┃┃━┛┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃
                ┃┃┃┃┃┃┃┃┃┃━━┛┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃
                '''
            ending_ascii = '''
                        ^^                   @@@@@@@@@
                   ^^       ^^            @@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@              ^^
                                       @@@@@@@@@@@@@@@@@@@@
             ~~~~ ~~ ~~~~~ ~~~~~~~~ ~~ &&&&&&&&&&&&&&&&&&&& ~~~~~~~ ~~~~~~~~~~~ ~~~
             ~         ~~   ~  ~       ~~~~~~~~~~~~~~~~~~~~ ~       ~~     ~~ ~
               ~      ~~      ~~ ~~ ~~  ~~~~~~~~~~~~~ ~~~~  ~     ~~~    ~ ~~~  ~ ~~ 
               ~  ~~     ~         ~      ~~~~~~  ~~ ~~~       ~~ ~ ~~  ~~ ~ 
             ~  ~       ~ ~      ~           ~~ ~~~~~~  ~      ~~  ~             ~~
                   ~             ~        ~      ~      ~~   ~             ~
            '''
            ending_ascii2 = '''
              ........::::::::::::..           .......|...............::::::::........
                 .:::::;;;;;;;;;;;:::::.... .     \   | ../....::::;;;;:::::.......
                     .       ...........   / \\\\_   \  |  /     ......  .     ........./\\
            ...:::../\\\\_  ......     ..._/'   \\\\\_  \###/   /\_    .../ \_.......   _//
            .::::./   \\\\\ _   .../\    /'      \\\\\\\\#######//   \/\   //   \_   ....////
                _/      \\\\\\\\   _/ \\\\\ /  x       \\\\\\\\###////      \////     \__  _/////
              ./   x       \\\\\/     \/ x X           \//////                   \/////
             /     XxX     \\\\/         XxX X                                    ////   x
            -----XxX-------------|-------XxX-----------*--------|---*-----|------------X--
                   X        _X      *    X      **         **             x   **    *  X
                  _X                    _X           x                *          x     X_
            '''
            ending_ascii3 = '''
                                   * *    
                                 *    *  *
                            *  *    *     *  *
                           *     *    *  *    *
                       * *   *    *    *    *   *
                       *     *  *    * * .#  *   *
                       *   *     * #.  .# *   *
                        *     "#.  #: #" * *    *
                       *   * * "#. ##"       *
                         *       "###
                                   "##
                                    ##.
                                    .##:
                                    :###
                                    ;###
                                  ,####.
                      /\/\/\/\/\/.######.\/\/\/\/\
            '''
            congrats_list = [congrats1, congrats2, congrats3]
            ending_ascii_list = [ending_ascii, ending_ascii2, ending_ascii3]
            if scenario > 0:
                print(random.choice(ending_ascii_list))
                print(random.choice(congrats_list))
                input(
                    f'\n{bulletpoint2}You\'ve reached a new ending! Try to discover other secret endings and possibilities...')
                total_ending_count += scenario
                scenario = 0
                return scenario
            else:
                pass
        
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
                # Checks if the type of the person is a Monster
                elif type(person) == Monster:
                    # If the monster is not in the tamed monster list, then this code will add it to the tamed monster list.
                    if person.name not in tamed_monster_list:
                        if monster_guild_membership == True:
                            if hero.health > 0:
                                input(
                                    f'As a member of the Monster Hunter Guild, you possess the skills to tame and train even the most ferocious beasts!\nYour collection of monsters has grown, and with it your power has increased!\n{person.name} has been added to your stable of powerful allies!')
                                tamed_monster_list.append(person.name)
            else:
                pass
        # Function to randomly add a certain amount of money depending on the scenario.
        def add_money(min, max):
            new_money = random.randint(min, max)
            hero.money += new_money
            input(f'{bulletpoint2}{hero.name} earned ${new_money}!')

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
            current_person_health = person.health
            current_monster_health = monster.health
            elixir_hp = person.health
            elixir_turns = 4
            elixir_activated = False
            elixir_count = 1  # Number of times user can use the elixir.
            drone_actived = False
            drone_battery = 10
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
                nonlocal drone_battery, elixir_turns
                if drone_actived == True:
                    if drone_battery > 0:
                        print(f'{bulletpoint2}Incoming Drone Strikes!!!')
                        strike_hit = random.randint(0, 10)
                        if strike_hit > 5:
                            input(f'{bulletpoint2}The strike was successful! {monster.name} was dealt 20 damage!')
                            monster.health -= 20
                        else:
                            input(
                                f'{bulletpoint2}The strike missed.')
                        drone_battery -= 1
                        if drone_battery == 0:
                            input(f'{bulletpoint2}The ancient drone\'s battery has been depleted.')
                if elixir_activated == True:
                    if elixir_turns > 0:
                        person.health = elixir_hp
                        input(f'{bulletpoint2}After drinking the elixir, your wounds stop bleeding and your health state becomes frozen. Any damage dealt to you will be immediately nullified.')
                        elixir_turns -= 1
                    if elixir_turns == 0:
                        input(f'{bulletpoint2}The effects of the elixir have worn off...')
                battle_Health_Menu()
                check_health(monster)
                check_health(person)
            invisibility_count = 3 # Number of times user can use the invisibility potion.
            ringofnirvana_count = 1 # Number of times user can use the ring of nirvana.
            crystal_ball_count = 1 # Number of times user can use the crystal ball.
            fireball_count = 3 # Number of times user can use the fireball.
            drone_count = 1 # Number of times user can use the ancient drone.
            tamed_monster_count = len(tamed_monster_list) # Find out the number of tamed monsters which counts for the amount of summons available
            special_item_command_count = 1 # This is so that the special item command string is printed only once
            while monster.health >= 0:
                # Breaks out of the while loop once monster health reaches less than 0
                if monster.health <= 0:
                    break
                print('\n')
                # If there are items existing in the battle_items list, then it will print the special item commands to be shown in the battle menu.
                if battle_items:
                    for i in battle_items:
                        if i in hero_items: # Checks to make sure battle item exists in hero items
                            if special_item_command_count == 1:
                                print(f'{bulletpoint2}Special Item Commands:')
                            else:
                                pass
                            special_item_command_count = 0
                            if i == '🏺- Invisibility Potion':
                                print(
                                    f'{bulletpoint2}{i} Command: "Abracadabra"  Uses Left: {invisibility_count}')
                            elif i == '⛣- Ring of Nirvana':
                                print(
                                    f'{bulletpoint2}{i} Command: "Estelio"  Uses Left: {ringofnirvana_count}')
                            elif i == '🔮Merlin\'s Crystal Ball':
                                    print(
                                        f'{bulletpoint2}{i} Command: "Annúnadar"  Uses Left: {crystal_ball_count}')
                            elif i == '☄️Fireball Spell':
                                    print(
                                        f'{bulletpoint2}{i} Command: "Caladran"  Uses Left: {fireball_count}')
                            elif i == '👾Ancient Drone':
                                    print(
                                        f'{bulletpoint2}{i} Command: "Robostrike"  Uses Left: {drone_count}')
                            elif i == '🍶Elixir of the Gods':
                                    print(
                                        f'{bulletpoint2}{i} Command: "Ithilien"  Uses Left: {elixir_count}')

                # Checks if the hero is a member of the monster guild, then will print the current tamed monster summons available
                if monster_guild_membership == True:
                    if tamed_monster_list:
                        if tamed_monster_count > 0:
                            print(f'{bulletpoint2}Tamed Monster Commands:')
                            for i in tamed_monster_list:
                                print(f'{i}')
                            print(
                                f'{bulletpoint2}Remaining Monster Summons: {tamed_monster_count}')

                monster_moves = random.choice(monster_potential_moves)
                print(f'The {monster.name} {monster_moves}...')
                person_move = input('Do you defend, counter, or attack?\n')
                if person_move == 'defend': # Scenarios where the hero selected DEFEND
                    if monster_moves == defend:  # If person DEFENDED and monster DEFENDED
                        print(f'Both {person.name} and {monster.name} defended.\n')
                        battlemenu()
                    elif monster_moves == counter:  # If person DEFENDED and monster COUNTERED
                        print(
                            f'{bulletpoint2}{person.name} successfully defended the attack!\n')
                        battlemenu()
                    elif monster_moves == weak:  # If person DEFENDED and monster was WEAK
                        print(f'Nothing happened.\n')
                        battlemenu()
                    else:  # If person DEFENDED and monster ATTACKED
                        print(
                            f'{bulletpoint2}{person.name} successfully blocked the attack!\n')
                        battlemenu()
                elif person_move == 'counter':
                    if monster_moves == defend:  # If person COUNTERED and monster DEFENDED
                        print(
                            f'{person.name} countered and {monster.name} blocked the attack.\n')
                        battlemenu()
                    elif monster_moves == counter:  # If person COUNTERED and monster COUNTERED
                        monster_counter_damage = monster_attack / 2
                        person_counter_damage = person_attack / 2
                        print(f'{bulletpoint}{monster.name} dealt {monster_counter_damage} damage to {person.name}, but was countered and {monster.name} took {person_counter_damage} damage!\n')
                        monster.health -= person_counter_damage
                        person.health -= monster_counter_damage
                        battlemenu()
                    elif monster_moves == weak:  # If person COUNTERED and monster was WEAK
                        print(f'Nothing happened.\n')
                        battlemenu()
                    else:  # If person COUNTERED and monster ATTACKED
                        print(
                            f'{bulletpoint}{monster.name} dealt 0 damage to {person.name}, and was countered. {monster.name} took {person_attack} damage!\n')
                        monster.health -= person_attack
                        battlemenu()
                elif person_move == 'attack':  # Scenarios where the hero selected ATTACK
                    if monster_moves == defend:  # If person ATTACKED and monster DEFENDED
                        print(
                            f'{person.name} tried attacking but {monster.name} blocked the attack.\n')
                        battlemenu()
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
                        input('''
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
                        input('''
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
                        input('>>>>>----------------------->    '*50)
                    elif summoned == summons[4]:
                        input('''
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
                        input('''
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
                    input(
                        f'{bulletpoint}You are surrounded by a protective shield. {person.name} summoned {summoned} and deals 💥{summon_damage} damage to {monster.name}!\n')
                    monster.health -= summon_damage
                    battlemenu()
                    input('Press enter to continue...')
                elif person_move.lower().strip() == 'abracadabra':
                    if '🏺- Invisibility Potion' in hero_items: # Checks if the item is in hero items, otherwise below code won't execute.
                        if invisibility_count > 0:
                            input(
                                f'{bulletpoint}{monster.name} tried to {monster_moves}, but {person.name} vanished and attacked {monster.name} from behind dealing 💥{person.damage} damage!\n')
                            monster.health -= person_attack
                            invisibility_count -= 1 # Reduction of the 3 remaining times the hero can use this item.
                            battlemenu()
                        else:
                            print(
                                f'{bulletpoint2}You have used up all of the invisibility potion for this battle.')
                            input(
                                f'{bulletpoint2}{monster.name} attacked and dealt {monster_attack} damage to {person.name}, while {person.name} was fiddling around with the potion.\n')
                            person.health -= monster_attack
                            battlemenu()
                elif person_move.lower().strip() == 'estelio':
                    # Checks if the item is in hero items, otherwise below code won't execute.
                    if '⛣- Ring of Nirvana' in hero_items:
                        if ringofnirvana_count > 0:
                            input(
                                f'{bulletpoint}As you hold the Ring of Nirvana in your hand, you feel its magic pulsing and swirling around you.\nThe power of the ring flows into your body, filling you with a sense of strength and vitality.\nYou feel your wounds begin to close and your strength returning, as if the ring is infusing you with 50 points of health.\nThe magic of the ring surrounds you like a glowing aura, protecting you from harm and enabling you to continue fighting on the battlefield.\n')
                            person.health += 50
                            # Reduction of the 3 remaining times the hero can use this item.
                            ringofnirvana_count -= 1
                            battlemenu()
                        else:
                            print(
                                f'{bulletpoint2}You have used up all of the ring of nirvana power for this battle.')
                            input(
                                f'{bulletpoint2}{monster.name} attacked and dealt {monster_attack} damage to {person.name}, while {person.name} was fiddling around with the ring.\n')
                            person.health -= monster_attack
                            battlemenu()
                elif person_move.lower().strip() == 'caladran':
                    # Checks if the item is in hero items, otherwise below code won't execute.
                    if '☄️Fireball Spell' in hero_items:
                        if fireball_count > 0:
                            fireball_dmg = random.randint(1, 40)
                            input(
                                f'{bulletpoint}As you stand on the battlefield facing your enemy, you raise your hand and unleash a barrage of fireballs at it. The fireballs streak through the air, leaving trails of sparks and smoke in their wake.\nYour enemy roars in pain as the fireballs hit it dealing {fireball_dmg} damage, setting its body alight and charring its flesh.\n')
                            monster.health -= fireball_dmg
                            # Reduction of the 3 remaining times the hero can use this item.
                            fireball_count -= 1
                            battlemenu()
                        else:
                            print(
                                f'{bulletpoint2}You have used up all of the ring of nirvana power for this battle.')
                            input(
                                f'{bulletpoint2}{monster.name} attacked and dealt {monster_attack} damage to {person.name}, while {person.name} was fiddling around with the ring.\n')
                            person.health -= monster_attack
                            battlemenu()
                elif person_move.lower().strip() == 'robostrike':
                    # Checks if the item is in hero items, otherwise below code won't execute.
                    if '👾Ancient Drone' in hero_items:
                        if drone_count > 0:
                            input(f'{bulletpoint2}As you stand on the battlefield facing your enemy, you turn on an ancient device and hear a low humming sound coming from behind.\nYou turn to see an ancient drone rising into the air, its wings beating steadily as it hovers above the ground. You recognize the drone as one of the ancient weapons that were used in battles long ago.')
                            drone_actived = True
                            drone_count -= 1
                            battlemenu()
                        else:
                            print(
                                f'{bulletpoint2}You have already used the drone for this battle.')
                            input(
                                f'{bulletpoint2}{monster.name} attacked and dealt {monster_attack} damage to {person.name}, while {person.name} was figuring out where the drone was.\n')
                            person.health -= monster_attack
                            battlemenu()
                elif person_move.lower().strip() in ('annunadar','annúnadar'):
                    # Checks if the item is in hero items, otherwise below code won't execute.
                    if '🔮Merlin\'s Crystal Ball' in hero_items:
                        if crystal_ball_count > 0:
                            input(
                                f'{bulletpoint}With a burst of magical energy, you activate the crystal ball\'s power of time reversal. You see the enemy pausing in mid-lunge. Time seems to slow down them reverse as the enemy\'s moves backwards in time.\nUsing the crystal ball\'s power of time reversal, you are able to turn the tide of the battle in your favor to the initial starting state of the battle.\nNew {monster.name} Health: {current_monster_health}\nNew {person.name} Health: {current_person_health}')
                            person.health = current_person_health
                            monster.health = current_monster_health
                            # Reduction of the 1 remaining time the hero can use this item.
                            crystal_ball_count -= 1
                            battlemenu()
                        else:
                            print(
                                f'{bulletpoint2}You have used up all of the crystal ball power for this battle.')
                            input(
                                f'{bulletpoint2}{monster.name} attacked and dealt {monster_attack} damage to {person.name}, while {person.name} was fiddling around with the crystal ball.\n')
                            person.health -= monster_attack
                            battlemenu()
                elif person_move.lower().strip() == 'ithilien':
                    # Checks if the item is in hero items, otherwise below code won't execute.
                    if '🍶Elixir of the Gods' in hero_items:
                        if elixir_count > 0:
                            elixir_activated = True
                            elixir_count -= 1
                            battlemenu()
                        else:
                            print(
                                f'{bulletpoint2}You have already drank the elixir for this battle.')
                            input(
                                f'{bulletpoint2}{monster.name} attacked and dealt {monster_attack} damage to {person.name}, while {person.name} was fiddling around with the empty elixir bottle.\n')
                            person.health -= monster_attack
                            battlemenu()
                elif person_move.lower().strip() == 'iamgod.':
                    input(f'{bulletpoint2}The forces all around you cause the fabric of reality to temporarily break. Your eyes turn white and you have a blinding aura radiating around you as unfathomable power seeps into your human veins. You just turned into a god.')
                    hero.health += 999999
                elif person_move.title().strip() in tamed_monster_list:
                    if tamed_monster_count > 0:
                        # Generate a random number between the minimum and maximum damage of the monster selected by the user
                        tamed_monster = [
                            mon for mon in available_monster_list if mon.name == person_move.title().strip()][0]
                        tamed_monster_damage = random.randint(
                            tamed_monster.min_damage, tamed_monster.max_damage)
                        # Print the damage done by the selected monster
                        input(
                            f'{bulletpoint2}{tamed_monster.name} does {tamed_monster_damage} to {monster.name}')
                        monster.health -= tamed_monster_damage
                        tamed_monster_count -= 1
                        battlemenu()
                    else:
                        pass
                else:
                    input(
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

        def blackjack():
            # Define a list of suits
            suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

            # Define a list of ranks
            cardranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

            # Generate a deck of cards as a list of tuples, with each tuple containing a rank and a suit
            deck = [(rank, suit) for rank in cardranks for suit in suits]

            # Shuffle the deck
            random.shuffle(deck)

            # Define a dictionary to map ranks to numerical values
            rank_values = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

            # Define a function to deal a card to a player
            def deal_card(hand):
                # Draw a card from the deck and append it to the player's hand
                hand.append(deck.pop(0))

            # Define a function to calculate the total value of a player's hand
            def calculate_hand_total(hand):
                # Initialize a variable to store the total value of the hand
                total = 0

                # Iterate over the cards in the hand
                for card in hand:
                    # Add the value of the card to the total
                    total += rank_values[card[0]]

                # Check if the hand contains an Ace
                if any(card[0] == "Ace" for card in hand):
                    # If so, check if adding 10 to the total would not bust the hand (total > 11)
                    if total + 10 <= 21:
                        # If not, add 10 to the total
                        total += 10

                # Return the total value of the hand
                return total

            # Define a function to play a game of Blackjack
            def play_blackjack():
                current_bet = 0
                def bet_result(result):
                    nonlocal current_bet
                    if current_bet > 0:
                        if result == 'lost':
                            input(f'You lost ${current_bet} :(\n')
                            current_bet = 0
                            return hero.money, current_bet
                        elif result == 'won':
                            current_bet *= 2
                            input(f'You gained ${current_bet}! 💰\n')
                            hero.money += current_bet
                            current_bet = 0
                            return hero.money, current_bet
                        else:
                            hero.money += current_bet
                            input(f'The bet has been returned to your wallet.\n')
                            current_bet = 0
                            return hero.money, current_bet


                # Deal the player and dealer two cards each
                player_hand = [deck.pop(0), deck.pop(0)]
                dealer_hand = [deck.pop(0), deck.pop(0)]

                # Cleans up the hands to look nicer when printed
                def clean_hand(hand):
                    card_image = ''
                    if hand is player_hand:
                        card_image ='🃏'
                    else:
                        card_image = '🃟'
                    player_hand_str = ', '.join(
                        [f'{card[0]} of {card[1]}{card_image}' for card in hand])
                    return player_hand_str

                blackjack_bet = 0
                if hero.money > 0:    
                    # Request the player's bet amount. Try and Except added in the event the player doesn't input a valid number which will result in no bet being placed.
                    try:
                        blackjack_bet = int(input(
                            f'\n{bulletpoint2}Would you like to place a bet?\nCurrent money: ${hero.money}\nEnter the number of the bet you want to place, or enter "0" to play for free.\n{bulletpoint}[BET]:'))
                        print(f'You placed down a bet of ${blackjack_bet}')
                        #Checks if the bet is less than or equal to the player's current money
                        if int(blackjack_bet) <= hero.money:
                            hero.money -= int(blackjack_bet) # Hero's money is deducted by the player's bet amount
                            current_bet += int(blackjack_bet) # Current bet amount is updated with the player's bet amount
                    except:
                        input(f'\nNo bet was placed.')
                        pass
                
                def whackjack_results():
                        # Calculate the total value of the dealer's hand
                        dealer_total = calculate_hand_total(dealer_hand)

                        # Print the dealer's hand
                        print(
                            f'Dealer\'s hand: {clean_hand(dealer_hand)} Total: {dealer_total}')

                        # Check if the dealer has 21 (Blackjack)
                        if dealer_total == 21:
                            if player_whackjack == True:
                                input('Player and Dealer both have 21. Push..')
                            else:
                                # If so, end the game and print a message
                                input('Dealer has Whackjack! Dealer wins.')
                                bet_result('lost')
                                return

                        # While the dealer's hand is less than 17, hit
                        while dealer_total < 17:
                            if player_total > 21:
                                break
                            # Deal a card to the dealer
                            input('Dealer draws a card...press enter to continue...')
                            deal_card(dealer_hand)

                            # Calculate the total value of the dealer's hand
                            dealer_total = calculate_hand_total(dealer_hand)

                            # Print the dealer's hand
                            print(
                                f'Dealer\'s hand: {clean_hand(dealer_hand)} Total: {dealer_total}')

                        # Check if the dealer has busted (total > 21)
                        if dealer_total > 21:
                            # Check if the player already has 21
                            if player_total == 21:
                                input('Dealer has busted. Player has 21.')
                            else:
                                input('Dealer has busted! Player wins.')
                            bet_result('won')
                        elif dealer_total == 21:
                            if player_total == 21:
                                input('Player and Dealer both have 21. Push..')
                                bet_result('push')

                        print(
                            f'Current Player Total: {player_total} 🃏\nCurrent Dealer Total: {dealer_total} 🃟')
                        # Compare the player's and dealer's totals
                        if player_total > dealer_total:
                            if player_total <= 21:
                                # If the player's total is greater and less than or equal to 21, the player wins
                                input('Player wins!')
                                bet_result('won')
                        elif player_total < dealer_total:
                            if dealer_total <= 21:
                                # If the dealer's total is greater and less than or equal to 21, the dealer wins
                                input('Dealer wins..')
                                bet_result('lost')
                        else:
                            # If the totals are equal, the game is a push
                            input('Push..')
                            bet_result('push')
                        
                # Calculate the total value of the player's hand
                player_total = calculate_hand_total(player_hand)
                # Print the total value of the player's hand
                print(f'Player\'s hand: {clean_hand(player_hand)} Total: {player_total}')
                player_whackjack = False
                eleven_double_bet = 0
                eleven_ans = ''
                # Check if the player has 21 (Blackjack)
                if player_total == 21:
                    # If so, end the game and print a message
                    input('PLAYER HAS WHACKJACK! Winnings are doubled. Player wins.')
                    bet_result('won')
                    player_whackjack = True
                    current_bet *= 2
                    return player_whackjack, current_bet
                elif player_total == 11:
                    eleven_ans = input(f'Player hit a soft 11! Would you like to double down your bet and play one more hand?')
                if eleven_ans.strip().lower() in (yes):
                    double_down = current_bet
                    if double_down <= hero.money:
                        print('You doubled down!')
                        eleven_double_bet += 1
                        hero.money -= double_down
                        current_bet += double_down
                        # Calculate the total value of the player's hand
                        player_total = calculate_hand_total(player_hand)
                        # Deals another hand
                        deal_card(player_hand)
                        # Calculate the total value of the player's hand
                        player_total = calculate_hand_total(player_hand)
                        # Print the player's hand
                        print(
                            f'Player\'s hand: {clean_hand(player_hand)} Total: {player_total}')
                        whackjack_results()
                    else:
                        input(f'You cannot afford to double down!')
                while eleven_double_bet == 0:
                    # If player has whackjack, this will break the while loop
                    if player_whackjack == True:
                        break
                    # Get the player's decision
                    decision = input(f'\n{bulletpoint2}(You can type ".." or "hit", and "stand" or the enter key to Stand)\n{bulletpoint}Hit or Stand?')

                    # Check if the player decided to hit
                    if decision.lower() in ('hit', '..', '  '):
                        # If so, deal a card to the player
                        print('Player draws a card...press enter to continue...')
                        deal_card(player_hand)

                        # Calculate the total value of the player's hand
                        player_total = calculate_hand_total(player_hand)

                        # Print the player's hand
                        print(f'Player\'s hand: {clean_hand(player_hand)} Total: {player_total}')

                        # Check if the player has busted (total > 21)
                        if player_total > 21:
                            # If so, end the game and print a message
                            input('Player has busted! Dealer wins.')
                            bet_result('lost')
                            break
                    else:
                        print('Player stands 👋')
                        break
                    # If the player decided to stand, break out of the loop
                if eleven_double_bet == 0:
                    whackjack_results()
                    menu()
                else:
                    pass
            # Play a game of Blackjack
            play_blackjack()

        gamble_life = False
        hanged_person = 'inmate'
        the_gamble = 'the game'
        def hangman():
            nonlocal hanged_person, gamble_life, the_gamble
            hanged_person = 'inmate'
            if gamble_life == True:
                hanged_person = hero.name
                the_gamble = 'YOUR LIFE'
            # Define a list of words to use in the game
            words = [
                'elephant','umbrella','sprint','keyboard','volcano','hopscotch','waterfall','jellyfish','frozen', 'giraffe', 'flamingo','peacock','chirping','shipwreck','stretching','crawling','seagull','dolphin','hummingbird',
                'leaping','dancing','whistling','singing','clapping','laughing','giggling','smiling','grinning','candy',
                'icecream','waterfall','cookie','pancake','natural','avalanche','sandwich','woodchip','popcorn','mountain',
                'volcano','kingdom','milkshake','pinstripe','teapot','coffee', 'watermelon', 'blueberry', 'honeydew', ]
            a_z = alphabet
            # Define the individual parts of the hangman image
            background = '☀🏰🚩☁         ☁'
            rope = '     𓍯'
            head = '     🤐'
            left_hand = '  O'
            arm = '='
            chest = '\_/'
            right_hand = 'O'
            left_leg = '     | '
            right_left = '|'
            left_foot = '     l '
            right_foot = 'l'
            hanged_body = [head, left_hand, arm, arm, chest, arm, arm, right_hand, left_leg, right_left, left_foot, right_foot]
            full_body = '''
            ☀🏰🚩☁         ☁
                    𓍯
                😵
                O==\_/==O
                | |
                l l  '''

            # Generate a random word from the list
            word = random.choice(words)

            # Initialize an empty list to store the letters that have been guessed
            guessed_letters = []

            # Initialize a counter to keep track of the number of incorrect guesses
            incorrect_guesses = 0

            # Ask the player if they want to hear the instructions for the game
            hangman_instructions = input(f'Would you like to hear instructions for the Hangman game?')
            if hangman_instructions.strip().lower() in yes:
                input(
                    f'\nHere is a set of instructions for you to play the hangman game:\n\n{bulletpoint2}1. A word will be randomly chosen from a list of words.\n\n{bulletpoint2}2. The letters in the word will be hidden, and you will have to guess the letters in the word one by one.\n\n{bulletpoint2}3. If a letter you guess is in the word, it will be revealed in the correct position in the word.\n\n{bulletpoint2}4. If a letter you guess is not in the word, you will lose one chance. You have a total of 12 chances.\n\n{bulletpoint2}5. You can also choose to guess the full word at any point during the game. If your guess is correct, you will win {the_gamble}. If your guess is incorrect, you will lose one of your remaining chances.\n\n{bulletpoint2}6. You win {the_gamble} if you guess all the letters in the word before running out of chances, or if you correctly guess the full word.\n\n{bulletpoint2}7. You lose {the_gamble} if you run out of chances without guessing all the letters in the word.\nPress enter to continue...\n')
            else:
                pass

            # Print the remaining chances
            remaining_chances = len(hanged_body)
            print(f'Remaining Chances: {remaining_chances}')

            # Start a loop to allow the player to guess letters
            while incorrect_guesses < remaining_chances:
                # Prints the remaining and guessed letters. The code below also cleans up the strings to look more presentable.
                new_a_z = ', '.join(
                [f'{letter}' for letter in a_z])
                new_guessed_letter = ', '.join(
                [f'{letter}' for letter in guessed_letters])
                print(f'\nRemaining Letters: {new_a_z}')
                print(f'Guessed Letters: {new_guessed_letter}')
                # Print the hangman image, up to the number of incorrect guesses made
                print(f'\n{background}\n{rope}\n{head}')

                # Prompt the player to guess a letter
                guess = input(
                    f'\n{bulletpoint}Guess the LETTER or WORD: ').lower()

                # If the letter input is a number like "5" or symbol like "^" then this message will be printed
                while guess not in alphabet:
                    if guess != word:
                        input(
                            f'{bulletpoint2}You must enter a letter in the alphabet. Please try again.')
                    break

                # Check if the letter has already been guessed
                if guess in guessed_letters:
                    input(
                        f'{bulletpoint2}You already guessed that letter. Try again.')
                else:
                    # Add the letter to the list of guessed letters
                    if len(guess) == 1:
                        if guess in alphabet:
                            guessed_letters.append(guess)
                            a_z.remove(guess)
                            # Check if the player has won by guessing all the letters in the word
                            if all(letter in guessed_letters for letter in word):
                                if hanged_person == hero.name:
                                    gamble_life = False
                                input(
                                    f'\n{bulletpoint2}The word was "{word}".\nCongratulations, you won the game! {hanged_person} was freed!')
                                break
                            # If the letter is not in the word, increment the incorrect guess counter
                            if guess not in word:
                                incorrect_guesses += 1
                                print(f'{bulletpoint2}Sorry, please try again.')
                        else:
                            pass
                    # Check if the letter is in the word
                    elif guess in word:
                        # Checks if the guess is more than one letter
                        if len(guess) > 1:
                            # Checks if the guess is the same as the correct word
                            if guess == word:
                                print(f'{bulletpoint2}You guessed the correct word!')
                                if hanged_person == hero.name:
                                    gamble_life = False
                                input(
                                    f'\n{bulletpoint2}The word was "{word}".\nCongratulations, you won the game! {hanged_person} was freed! The word was "{word}"!')
                                break
                            else:
                                # If the guess is not the same as the correct word, then increment the incorrect guess counter
                                input(
                                    f'{bulletpoint2}Please enter another letter. Try again.')
                                incorrect_guesses += 1
                        else:
                            print(
                                f'{bulletpoint2}Good guess! The letter is in the word!')
                            # Check if the player has won by guessing all the letters in the word
                            if all(letter in guessed_letters for letter in word):
                                if hanged_person == hero.name:
                                    gamble_life = False
                                input(
                                    f'\n{bulletpoint2}The word was "{word}".\nCongratulations, you won the game! {hanged_person} was freed! The word was "{word}"!')
                                break
                    else:
                        # If the letter is not in the word and the letters is more than one character, increment the incorrect guess counter
                        incorrect_guesses += 1
                        print(f'{bulletpoint2}Sorry, please try again.')

                    remaining_chances = len(hanged_body)
                    print(f'\nRemaining Chances: {remaining_chances - incorrect_guesses}')

                    # Print the updated state of the game, with correctly guessed letters revealed
                    for letter in word:
                        if letter in guessed_letters:
                            print(letter, end=" ")
                        else:
                            print("_", end=" ")

            # If the player has run out of incorrect guesses, print a message and end the game
            if incorrect_guesses == remaining_chances:
                print(full_body)
                if hanged_person == 'inmate':
                    input(f'\n{bulletpoint2}Sorry, you lost the game. The word was "{word}". You watched in regret as your fellow inmate was hanged by your own doing...\n')
                else:
                    gamble_life = False
                    input(f'\n{bulletpoint2}Sorry, you lost the game. The word was "{word}". As the trapdoor beneath your feet opened and you fell into the dark abyss, your last thoughts were of regret. You had been so close to freedom, but in the end, you had failed.\n\n{bulletpoint2}But even as you breathed your last, Your knew that your spirit would not be broken. You would fight on, even in death, until the Empire of Ice was brought to justice and the Red Dragon Empire was restored to its former glory.\n')
                    hero.health = 0
                    check_health(hero)
                    
        def restaurant_menu():
            import random
            # List of dish items for the restaurant as a dictionary
            dishes = [{
                'name': 'Sushi Burrito',
                'ingredients': [
                        'Sushi Rice',
                        'Norwegian Salmon',
                        'Avocado',
                        'Cucumber',
                        'Sriracha Mayo',
                        {'taste': ['salty', 'spicy', 'tangy']}
                ]
            },
                {
                    'name': 'Pad Thai Tacos',
                    'ingredients': [
                        'Pad Thai Noodles',
                        'Shrimp',
                        'Bean Sprouts',
                        'Scallions',
                        'Peanuts',
                        'Lime',
                        'Taco Shells',
                        {'taste': ['savory', 'spicy', 'tangy']}
                    ]
            },
                {
                    'name': 'Peking Duck Pizza',
                    'ingredients': [
                        'Pizza Dough',
                        'Hoisin Sauce',
                        'Duck Breast',
                        'Scallions',
                        'Cucumber',
                        'Plum Sauce',
                        {'taste': ['savory', 'rich', 'tangy']}
                    ]
            },
                {
                    'name': 'Chicken Tikka Masala Fondue',
                    'ingredients': [
                        'Chicken Tikka Masala',
                        'Bread',
                        'Vegetables',
                        'Fondue Pot',
                        {'taste': ['savory', 'spicy', 'rich']}
                    ]
            },
                {
                    'name': 'Fish and Chips Spring Rolls',
                    'ingredients': [
                        'Fish Fillets',
                        'Chips',
                        'Spring Roll Wrappers',
                        'Tartar Sauce',
                        {'taste': ['savory', 'crispy', 'tangy']}
                    ]
            },
                {
                    'name': 'Tomato Basil Soup',
                    'ingredients': [
                        'Ripe Tomatoes',
                        'Basil',
                        'Garlic',
                        'Onion',
                        'Vegetable Stock',
                        {'taste': ['tangy', 'salty', 'savory']}
                    ]
            },
                {
                    'name': 'Chicken Parmesan',
                    'ingredients': [
                        'Breaded Chicken Breast',
                        'Marinara Sauce',
                        'Mozzarella Cheese',
                        'Parmesan Cheese',
                        'Basil',
                        {'taste': ['savory', 'salty', 'umami']}
                    ]
            },
                {
                    'name': 'Spaghetti Carbonara',
                    'ingredients': [
                        'Spaghetti Noodles',
                        'Bacon',
                        'Eggs',
                        'Parmesan Cheese',
                        'Pepper',
                        {'taste': ['savory', 'salty', 'umami']}
                    ]
            },
                {
                    'name': 'Falafel Pita',
                    'ingredients': [
                        'Falafel Balls',
                        'Pita Bread',
                        'Tomatoes',
                        'Onions',
                        'Tzatziki Sauce',
                        {'taste': ['savory', 'tangy', 'herby']}
                    ]
            },
                {
                    'name': 'Spicy Tofu Stir-Fry',
                    'ingredients': [
                        'Tofu',
                        'Bell Peppers',
                        'Onions',
                        'Soy Sauce',
                        'Sriracha',
                        {'taste': ['savory', 'spicy', 'umami']}
                    ]
            },
                {
                    'name': 'Grilled Salmon Salad',
                    'ingredients': [
                        'Grilled Salmon',
                        'Mixed Greens',
                        'Cherry Tomatoes',
                        'Cucumber',
                        'Lemon Vinaigrette',
                        {'taste': ['savory', 'tangy', 'umami']}
                    ]
            },
                {
                    'name': 'BBQ Pulled Pork Sandwich',
                    'ingredients': [
                        'Pulled Pork',
                        'BBQ Sauce',
                        'Hamburger Bun',
                        'Coleslaw',
                        'Pickles',
                        {'taste': ['savory', 'tangy', 'smoky']}
                    ]
            },
            ]
            # List of dessert items for the restaurant as a dictionary
            desserts = [{
                'name': 'Strawberry Cheesecake Stuffed French Toast',
                'ingredients': [
                    'French bread',
                    'Cream cheese',
                    'Strawberries',
                    'Eggs',
                    'Milk',
                    'Vanilla extract',
                    'Powdered sugar',
                    {'taste': ['sweet', 'rich']}
                ]
            },
                {
                'name': 'Banana Split Waffle Sundae',
                'ingredients': [
                    'Waffle mix',
                    'Bananas',
                    'Strawberry jam',
                    'Whipped cream',
                    'Chocolate sauce',
                    'Pecans',
                    {'taste': ['sweet', 'fruity']}
                ]
            },
                {
                'name': 'Lemon Blueberry Panna Cotta',
                'ingredients': [
                    'Heavy cream',
                    'Sugar',
                    'Gelatin',
                    'Lemon zest',
                    'Blueberries',
                    'Lemon juice',
                    {'taste': ['tart', 'smooth']}
                ]
            },
                {
                'name': 'Peanut Butter and Jelly Donut Milkshake',
                'ingredients': [
                    'Peanut butter',
                    'Jelly',
                    'Vanilla ice cream',
                    'Milk',
                    'Donuts',
                    {'taste': ['sweet', 'peanutty']}
                ]
            },
                {
                'name': 'Chocolate Hazelnut Mousse Cake',
                'ingredients': [
                    'Dark chocolate',
                    'Hazelnuts',
                    'Heavy cream',
                    'Egg whites',
                    'Sugar',
                    {'taste': ['rich', 'chocolatey']}
                ]
            }
            ]

            # order_complete is a flag variable that is used to determine whether the order is complete or not
            order_complete = False

            # if order_complete is False, it prints the restaurant menu
            # otherwise, it prints the user's order
            def generate_menu(dishes):
                if order_complete == False:
                    print('\nLava Ice Kitchen\nRestaurant Menu:')
                else:
                    print('\nYour Order:')
                print('-' * 30)

                # iterate over the list of dishes and print the dish name and ingredients
                for dish in dishes:
                    print(f'{"Dish Name:":<20s} {dish["name"]:<20s}')
                    print(f'{"Ingredients:":<20s} {", ".join(dish["ingredients"][:-1]):<20s}')  
                    print()
                print('-' * 30)

            # prompt the user to press enter to see the main dishes
            input(f'Press enter to see the main dishes...')

            # generate the menu for the main dishes
            generate_menu(dishes)

            # prompt the user to input the dish they would like to try
            # if the dish is not on the menu, generate a random dish instead
            dish_name = input(
                f'(Enter the full dish name)\n{bulletpoint}What dish would you like to try: ').lower().strip()
            selected_dish = next(
                (dish for dish in dishes if dish['name'].lower().strip() == dish_name.lower().strip()), None)
            if selected_dish is None:
                selected_dish = random.choice(dishes)
                input(f'{bulletpoint2}This dish is not on our menu, we\'ll instead give you the chef special!')

            # prompt the user to press enter to see the main desserts
            input(f'Press enter to see the main desserts...')

            # generate the menu for the main desserts
            generate_menu(desserts)

            # prompt the user to input the dessert they would like to try
            # if the dessert is not on the menu, generate a random dessert instead
            dessert_name = input(
                f'(Enter the full dessert name)\n{bulletpoint}What dessert would you like to try: ').lower().strip()
            selected_dessert = next(
                (dessert for dessert in desserts if dessert['name'].lower().strip() == dessert_name.lower().strip()), None)
            if selected_dessert is None:
                selected_dessert = random.choice(desserts)
                input(f'{bulletpoint2}This dessert is not on our menu, we\'ll instead give you the chef special!')

            # set order_complete to True, since the order is complete
            order_complete = True

            # generate the menus for the selected dishes and desserts
            generate_menu([selected_dish])
            generate_menu([selected_dessert])

            # print the tastes of the selected dishes and desserts
            dish_tastes = selected_dish["ingredients"][-1]["taste"]
            dessert_tastes = selected_dessert["ingredients"][-1]["taste"]
            input(
                f'{bulletpoint2}You decided to order the "{selected_dish["name"]}". It arrived at your table a couple minutes later, and you could hardly contain your excitement as you took your first bite.\nThe "{selected_dish["name"]}" has a {", ".join(dish_tastes)} taste!')
            # print the selected dessert and its taste
            input(
                f'{bulletpoint2}You decided to order the "{selected_dessert["name"]}". It arrived at your table after your main dish, and you started drooling as you took the first bite.\nThe "{selected_dessert["name"]}" had a {", ".join(dessert_tastes)} taste!')

            # if the order is complete, print the food bill and prompt the user for a tip
            if order_complete == True:
                input(f'\n{bulletpoint2}Your food bill: $100')
                food_tip = input(f'\n{bulletpoint}How much tip do you pay:')
                if food_tip == '':
                    food_tip = 'nothing'
                input(f'\n{bulletpoint2}Your total bill: $100 plus {food_tip}.')

        def ascii_dice():
            input('''
                  (( _______            
                   /\       \           
                  /()\   ()  \          
                 /    \_______\  ))       
                 \    /()     /         
                  \()/   ()  /          
                   \/_____()/  ))
                   ((
            ''')

        # The story objects that can be mixed and matched depending on the storyline and player decisions.
        def story():
            new_rank = '' # Sets the empty rank for the empire_recruitment scenario.
            current_heir = 'beggar..'
            emperor_life = 'alive'
            current_emperor = 'emperor'
            noble_life = 'alive'
            thugs_life = 'alive'
            new_goons = 'thugs'
            new_goons_list = ['wolves', 'ruffians', 'brutes', 'hoodlums', 'hooligans', 'rowdies', 'gang members', 'enforcers']
            icequeen_life = 'alive'
            current_kingdom_name = 'Ice Kingdom'
            current_empire_name = 'Red Dragon Empire'
            new_monk_replacement = 'monk'
            coin_guess_correctly = False
            victory = 'black'
            new_monk_replacement_list = ['knight', 'healer', 'bard', 'adventurer', 'fairy', 'dwarf', 'elf', 'sorcerer',
                                         'priestess', 'mage', 'paladin', 'priest', 'monk', 'cleric', 'warrior', 'ranger', 'rogue']
            wall_key_count = 1 # For the treasure antique room key
            merlin_in_room = 1

            def rank_promo():
                try: # Find the index of the hero's current rank and then promotes to a higher rank.
                    if new_rank in ranks:
                        index = ranks.index(new_rank)
                        new_rank = ranks[index + 1]
                        input(
                            f'{bulletpoint2}The empire has made a decision to promote you a rank higher to {new_rank}!')
                except: # If hero is already at the max rank, then they're awarded a $ bonus.
                    input(
                        'The empire has made a decision to give you a bonus of $1000! ')
                    hero.money += 1000

            #Vendor Lady
            def show_vendor_menu():
                count = 1

                # These are ascii art of swords which will be properly displayed in the game vendor menu. \n is new line.
                rusty_sword = '    /\n0===[====================-\n    \\'
                sword_one = '          ./\n()=@XXXXX@=[0}================--\n          `\_'
                sword_two = "            /\ \n/vvvvvvvvvvvv \--------------------------------------,\n`^^^^^^^^^^^^ /=====================================\" \n            \/"
                mythic = " ,.\n \%`.\n  `.%`.\n    `.%`.\n      `.%`.\n        `.%`.\n          `.%`.    __\n            `.%`.  \ \\ \n              `.%`./_/\n                `./ /.\n               __/\/:/;.\n               \__/  `:/;.\n                       `:/;.,   \n                    Krogg`:/ ;\n                           `'\n"
                mythic_two = "                _\n               /\)\n              /\/\n             /\/\n           _/L/\n          (/\_)\n          /%/  \n         /%/  \n        /%/\n       /%/\n      /%/\n     /%/\n    /%/\n   /%/\n  /%/\n /%/ Krogg\n/,'\n\" "
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
                                hero.add_item(sold_item) # Add the item's attributes to the hero and add the item's name to hero's items list.
                                input(
                                    f'\n{bulletpoint2}Congratulations on your purchase! I\'m sure you\'ll enjoy it!🎁\nThe {sold_item.name} has been added to your inventory. Press enter to continue...')
                            menu()
                            show_vendor_menu()
                        else:
                            wheat = input(
                                f'{bulletpoint2}\nSorry, you can\'t afford this item. Press enter to continue...')
                            if wheat.lower() == 'gimmethebread':
                                input(f'\n{bulletpoint2}Money magically appeared in your inventory!\n')
                                hero.money += 10000
                            else:
                                pass
                    elif buy_item == '0': # Exit of the vendor menu.
                        menu()
                        best_friend()
                    
                except:
                    input(
                        f'{bulletpoint2}Please try again.')
                else:
                    input(
                        f'{bulletpoint2}Please try again.')
                #Try and except added here to fix a bug where if you visit the vendor lady then die to a monster, this will raise an error.
                try:
                    show_vendor_menu()
                except:
                    pass

            def battlefield():
                def battlefield_roll():
                    input(f'{bulletpoint}Press enter to roll 1 to 100 to determine if you were successfull or not...')
                    battleroll = random.randint(1, 100)
                    if battleroll <= 30:
                        input(f'\n{bulletpoint2}You were unsuccessful.\nYour army disbanded and you had to report your failure back to the emperor.\n')
                        menu()
                        beggar()
                    else:
                        pass

                attack_or_not = input(f'{bulletpoint}You currently hold the emperor\'s entire army. Do you proceed to attack the {current_kingdom_name}?')
                if attack_or_not not in yes:
                    nonlocal current_emperor, emperor_life, new_rank, victory
                    emperor_life = 'dead'
                    current_emperor = hero.name.title()
                    input(f'{bulletpoint2}As the leader of the emperor\'s army, you were given the opportunity to attack the Ice Kingdom.\nBut as you were preparing for battle, you realized that this was the perfect opportunity to seize the throne of the Red Dragon Empire and become the new ruler yourself.')
                    input(f'{bulletpoint2}You quickly gathered your most loyal soldiers and began planning your attack on the emperor\'s throne. With your army at your side, you marched on the emperor\'s palace and launched a surprise attack on the guards.')
                    input(f'{bulletpoint2}The emperor was caught off guard and was unable to defend himself with barely any army. You and your army fought valiantly, and after a decisive battle, you were able to defeat the emperor and claim the throne for yourself.')
                    input(f'{bulletpoint2}With the Red Dragon Empire now under your control, you declared yourself the new ruler and renamed the empire the Kingdom of Dragon. You vowed to rule justly and bring peace to the kingdom, ending the constant wars and conflicts that had plagued it for so long.')
                    input(f'{bulletpoint2}As the new ruler, you worked tirelessly to rebuild the kingdom as it transitions away from the previous "Red Dragon Empire" name and improve the lives of all your people. You introduced new laws and policies that brought prosperity and harmony to the kingdom, and the people hailed you as a hero for bringing peace to the land.')
                    input(
                        f'\n{bulletpoint2}Under your rule, the Kingdom of Dragon flourished and became a beacon of hope and justice in a world of chaos and darkness.')
                    input(f'''\n\n🎜🎜~A bard in the distant future starts singing~🎜🎜
                    Once a land of war and strife,
                    The Red Dragon Empire's grip on life,
                    Was tenuous at best,
                    With battles never at rest.

                    But then {hero.name} the hero did appear,
                    A ruler strong and fair,
                    With armies at their command,
                    They seized the throne with a steady hand.

                    The empire was reborn that day,
                    Into the Kingdom of Dragon, they did say,
                    A land of peace and prosperity,
                    Where beings of all kind live in harmony.

                    Under the new ruler's care,
                    The kingdom began to flourish and grow,
                    Laws were put in place,
                    To ensure that all had a fair place to go.

                    And so the legend of the {hero.name} ruler,
                    Lived on through future generations,
                    Their legacy forever shining,
                    As the one who brought peace everlasting.\n
                    ''')
                    menu()
                    ending(ending30)
                    beggar()
                else:
                    input(f'\n{bulletpoint2}As the leader of the emperor\'s army, you were tasked with attacking the Ice Queen\'s {current_kingdom_name}. You knew that the Ice Queen\'s army was made up of powerful mages, skilled soldiers, and fierce wolves, and you would need to use special battle tactics in order to defeat them.\n')
                    tactic1 = input(f'\n{bulletpoint2}The first army unit you faced was the queen\'s mages. You had two special tactics to choose from: the pincer movement, where you would surround the mages and attack them from both sides, or the feint, where you would make them think you were going to attack one area, but then surprise them by attacking another.\n{bulletpoint}Which tactic do you choose?')
                    battlefield_roll()
                    if 'pincer' in tactic1.strip().lower() or 'surround' in tactic1.strip().lower():
                        input(f'\n{bulletpoint2}You decided to use the pincer movement to surround the queen\'s mages. As you and your army closed in on them from both sides, the mages were caught off guard and unable to defend themselves. Your tactic was successful, and you were able to defeat the mages and move on to the next army unit.\n')
                    else:
                        input(f'\n{bulletpoint2}You decided to use the feint tactic to surprise the queen\'s mages. You made them think you were going to attack one area, but then you surprised them by attacking another. The mages were caught off guard and unable to defend themselves. Your tactic was successful, and you were able to defeat the mages and move on to the next army unit.\n')
                    tactic2 = input(f'\n{bulletpoint2}The second army unit you faced was the queen\'s soldiers. Again, you had two special tactics to choose from: the ambush, where you would hide and surprise the soldiers when they least expected it, or the frontal assault, where you would charge directly at the soldiers and overwhelm them with sheer force.{bulletpoint}Which tactic do you choose?')
                    battlefield_roll()
                    if 'ambush' in tactic2.strip().lower() or 'hide' in tactic1.strip().lower() or 'suprise' in tactic2.strip().lower():
                        input(f'\n{bulletpoint2}You decided to use the ambush tactic to take on the queen\'s soldiers. You and your army hid in the trees and waited for the perfect moment to strike. When the soldiers were passing by, you attacked them from all sides, catching them completely off guard. Your tactic was successful, and you were able to defeat the soldiers and move on to the final army unit.\n')
                    else:
                        input(f'\n{bulletpoint2}You decided to use the frontal assault tactic to take on the queen\'s soldiers. You and your army charged directly at the soldiers, overwhelming them with sheer force. The soldiers were caught off guard and unable to defend themselves. Your tactic was successful, and you were able to defeat the soldiers and move on to the final army unit.\n')
                    tactic3 = input(f'\n{bulletpoint2}The final army unit you faced was the queen\'s wolves. This time, you had two special tactics to choose from: the decoy, where you would use a fake attack to draw the wolves away from the main army, or the shield wall, where you would form a line of shields to protect yourself and your army from the wolves\' attacks.{bulletpoint}Which tactic do you choose?')
                    battlefield_roll()
                    if 'decoy' in tactic3.strip().lower() or 'fake' in tactic3.strip().lower() or 'draw' in tactic3.strip().lower():
                        input(f'\n{bulletpoint2}You decided to use the decoy tactic to deal with the queen\'s wolves. You and a few of your soldiers pretended to attack the wolves, drawing them away from the main army. While the wolves were distracted, the rest of your army was able to surround and defeat them. Your tactic was successful, and you were able to defeat the wolves and win the battle.\n')
                    else:
                        input(f'\n{bulletpoint2}You decided to use the shield wall tactic to deal with the queen\'s wolves. You and your army formed a line of shields to protect yourselves from the wolves\' attacks. The wolves were unable to break through your defense, and you were able to attack them with spears through the small openings. You successfully defeated them and won the battle.\n')
                    input(f'{bulletpoint2}With the Ice Queen\'s army defeated, you were able to claim victory for the emperor\'s army. Your special battle tactics had proven to be successful, and you were hailed as a hero for your bravery and skill in battle.\n')
                    victory = 'red'
                    add_health(hero)
                    add_money(300, 600)
                    menu()
                    ending(ending29)
                    beggar()

            # The Restaurant
            def the_restaurant():
                input(f'{bulletpoint2}It was a cold and rainy day, and you were feeling particularly hungry. You decided to stop by a local restaurant to see if they had any good food.\n\n{bulletpoint2}As you entered the restaurant, you were greeted by the friendly staff. They led you to a table and handed you a menu. \nYou scanned the offerings, and your mouth began to water at the thought of all the delicious dishes that were available.\n')
                restaurant_menu()
                input(f'\n\n{bulletpoint2}As you were just about to pay your meal, you heard a loud commotion. You asked the restaurant staff what was going on, and they explained that there was a disaster happening in the kitchen. A monster that looked like a moving gray glob was attacking the chefs.\n\n{bulletpoint2}You were not about to let this monster get away with ruining your meal. You grabbed a nearby kitchen knife and charged into the kitchen, ready to take on the monster.\n\n{bulletpoint2}You quickly notice a large cauldron of burning hot soup over the monster\'s head.\n\n{bulletpoint}Press enter to roll if you were successful in tipping it over:')
                clean_kill_gloopus = random.randint(1, 10)
                ascii_dice()
                input(f'{bulletpoint2}You rolled a {clean_kill_gloopus}.')
                if clean_kill_gloopus > 5:
                    input(
                        f'\n{bulletpoint2}You took out the monster quick and efficiently! Since gloopus monsters are typically made of a sticky, viscous substance, they would be vulnerable to intense heat, which the cauldron soup caused the monster to rapidly dry out and disintegrate!\n')
                    add_money(300, 600)
                    menu()
                    input(f'\n{bulletpoint2}\nThe chefs were grateful for your help, and they promised to keep the kitchen clean and safe from monsters in the future. You left the restaurant feeling satisfied, not only because you had saved the day, but also because you had enjoyed a delicious complimentary meal earlier ;)\n')
                    ending(ending1)
                    beggar()
                else:
                    print(f'{bulletpoint2}You missed!')
                    block_ans = input(
                        f'{bulletpoint}\nThe {gloopus.name} monster threw some pots and pans at you. You blocked by...\nEnter what happened next:')
                    weak_ans = input(
                        f'{bulletpoint}\nThe {gloopus.name} monster threw a kitchen knife that grazed your leg, you screamed in pain and...\nEnter what happened next:')
                    counter_ans = input(
                        f'{bulletpoint}\nThe {gloopus.name} monster starting gathering more pots, pans, and knives, and you saw multiple moving balls of goo started crawling towards you. You tried to prepare for the attack by...\nEnter what happened next:')
                    attack_ans = input(
                        f'{bulletpoint}\nThe {gloopus.name} monster stopped moving and rested, you attacked by...\nEnter what happened next:')
                    input(f'\n{bulletpoint2}You stopped to think to yourself that this didn\'t look like any gloopus monster you had ever seen before. This one was different. It had a strange  glob shape, and its eyes glinted with a sinister, intelligent light.\n\n{bulletpoint2}You watched in amazement as the glob monster began to morph and change, its body reshaping itself into a humanoid form. And then, to your horror, you realized that it was beginning to look like you.\n\n{bulletpoint2}It had the same face, the same hair, the same clothes. But its eyes were different. They were cold, gray, and piercing, filled with a malevolent intelligence.\n\n{bulletpoint2}You didn\'t hesitate. You lunged at the gloopus monster.\n')
                    add_health(gloopus)
                    battle(hero, gloopus, block_ans,
                            weak_ans, counter_ans, attack_ans)
                    random_health_gain = random.randint(10, 30)
                    print(
                        f'{bulletpoint2} You took some rest and gained {random_health_gain} health back.')
                    hero.health += random_health_gain
                    check_health(hero)
                    add_money(300, 600)
                    menu()
                    input(f'\n{bulletpoint2}You battled the monster for what seemed like an hour, but eventually you managed to defeat it.\n\n{bulletpoint2}The chefs were grateful for your help, and they promised to keep the kitchen clean and safe from monsters in the future. You left the restaurant feeling satisfied, not only because you had saved the day, but also because you had enjoyed a delicious complimentary meal earlier ;)\n')
                    ending(ending2)
                    beggar()

            # Monster Hunter Guild
            def monster_hunter_guild():
                nonlocal monster_guild_membership
                def behemoth_battle():
                    input(f'\n{bulletpoint2}Out of nowhere a beast springs out from the tall grass and lunges at people next to you. You quickly draw your sword and charge at the Behemoth, determined to protect your fellow guild members!\n')
                    add_health(behemoth)
                    battle(hero, behemoth, 'raises massive claws',
                        'becomes reckless and aggressive', 'becomes quick and agile', 'rushes forward with horns and claws')
                    random_health_gain = random.randint(10, 30)
                    print(
                        f'{bulletpoint2} You took some rest and gained {random_health_gain} health back.')
                    hero.health += random_health_gain
                    check_health(hero)
                    add_money(50, 150)
                    menu()
                    input(f'\n{bulletpoint2}You are proud of your accomplishment, and you feel a sense of satisfaction and fulfillment as you continue on your journey as a monster hunter. You know that there will be many more challenges and dangers ahead, but you are ready for whatever comes your way.\n')
                    the_restaurant()
                if monster_guild_membership == False:
                    input(f'\n{bulletpoint2}The leader of the group, a fierce-looking woman with a scar across her face, sizes you up with a critical eye. She seems impressed by your determination and skill, and she agrees to take you on as a member of the guild.\n\n{bulletpoint2}You are excited and eager to begin your new career as a monster hunter. You know that it will be dangerous and challenging, but you are ready for the challenge. You will use your skills and abilities to protect the innocent and keep the world safe from the dangers that lurk in the shadows.\n')
                    input(f'\n{bulletpoint2}As a member of the monster hunter guild, you quickly learn the guild\'s motto: \n\n{bulletpoint2}"To protect the innocent and keep the world safe from the dangers that lurk in the shadows." \n\n{bulletpoint2}This motto guides the guild\'s actions and decisions, and it is a constant reminder of the important role that they play in the world.\n')
                    input(f'\n{bulletpoint2}The guild has a wide range of goals, including tracking and defeating dangerous beasts, protecting civilians from harm, gathering information about the various monsters that inhabit the world, and potentially taming them.\n\n{bulletpoint2}As a new member of the guild, you are tasked with your first mission: to defeat a monster that has been causing havoc in the local farming community. The monster, a massive, hulking plant-like creature known as the "Cornstalker," has been destroying crops and terrorizing the locals.\n\n{bulletpoint2}You and your team set out to track down the Cornstalker and put an end to its reign of terror.\n')
                    input(f'\n{bulletpoint2}Your team found the monster lurking in a field of tall corn. The monster is nearly invisible among the plants, blending in seamlessly with its surroundings.\n\n{bulletpoint2}At first glance, the Cornstalker appears to be a massive, plant-like creature. It has a thick, woody trunk, and its vines and leaves are covered in sharp thorns. Its eyes are glowing orbs of green light, and its mouth is filled with razor-sharp teeth.\n\n{bulletpoint2}As you approach, the Cornstalker stirs to life, its vines and leaves writhing and twisting as it prepares to attack. The monster is powerful and dangerous, and it will take all of the your skill and determination to defeat it.\n')
                    add_health(cornstalker)
                    battle(hero, cornstalker, 'raises its vines',
                        'retreat into its leaves', 'uses a vine whip', 'unleashes a barrage of explosive seeds')
                    random_health_gain = random.randint(10, 30)
                    print(
                        f'{bulletpoint2} You took some rest and gained {random_health_gain} health back.')
                    hero.health += random_health_gain
                    check_health(hero)
                    add_money(50, 150)
                    menu()
                    monster_guild_membership = True
                else:
                    recruit_num = random.randint(1,10)
                    recruit_ans = input(f'\n{bulletpoint}As you and your fellow monster hunter guild members stand before the three potential recruits, you carefully assess each of them.\n\n{bulletpoint2}The first potential recruit is a skinny young man with a timid expression on his face.\n\n{bulletpoint2}The second is a child no older than 10, with a determined look in their eyes.\n\n{bulletpoint2}The third is a short and chubby man, who looks ready for a fight. \n\n{bulletpoint2}You will task one of them to take out the Cornstalker Monster.\n{bulletpoint}Who do you select?\n')
                    if recruit_ans.strip().lower() in ('1', 'first', 'skinny man', 'skinny young man', 'young man', 'first one', 'the first one', 'timid one', 'the timid one', 'the skinny one', 'the first'):
                        input(f'{bulletpoint}Press enter to determine if the recruit was successful or not by rolling from 1 to 10...')
                        ascii_dice()
                        input(f'{bulletpoint2}You rolled a {recruit_num}.')
                        if recruit_num >= 5:
                            input(
                                f'\n{bulletpoint2}The skinny young man, despite his small stature, was quick on his feet and agile. He dodged the Cornstalker\'s vines and thorns with ease, darting in and out to deliver precise blows with his sword. The Cornstalker roared in pain and fury as the young man\'s sword sliced through its thick bark, leaving deep gashes in its woody trunk.\n\n{bulletpoint2}Despite its size and strength, the Cornstalker was no match for the young man\'s skill and determination. With a final, desperate swipe of its vines, the Cornstalker stumbled and fell, its glowing eyes dimming as it lay still on the ground.\n\n{bulletpoint2}The young man, panting and covered in sweat, looked around at the members of the Monster Hunter Guild, who were watching in amazement. The leader of the group, the fierce-looking woman with the scar, nodded in approval. "You have proven yourself worthy to join our ranks," she said. "Welcome to the Monster Hunter Guild."\n')
                            behemoth_battle()
                        else:
                            input(
                                f'\n{bulletpoint2}The skinny young man approached the cornstalker monster with confidence, but as soon as the cornstalker attacked, he realized he was no match for its strength and ferocity. The cornstalker\'s vines and thorns ripped through the young man\'s armor, and its sharp teeth tore into his flesh. Despite his valiant efforts, the young man was no match for the cornstalker and was quickly overpowered and killed.\n')
                            behemoth_battle()
                    elif recruit_ans.strip().lower() in ('2', 'second', 'child', 'the child', 'the 10 year old', 'the youngling', 'the kid', 'the second one', 'the second', 'the 10 yr old'):
                        input(f'{bulletpoint}Press enter to determine if the recruit was successful or not by rolling from 1 to 10...')
                        ascii_dice()
                        input(f'{bulletpoint2}You rolled a {recruit_num}.')
                        if recruit_num >= 5:
                            input(
                                f'\n{bulletpoint2}The child, no older than 10, approaches the Cornstalker with a determined look in their eyes. They quickly notice that the monster\'s glowing orbs of green light are its weak spot, and they begin to circle the creature, dodging its sharp vines and thorns.\n\n{bulletpoint2}Using their agility and quick thinking, the child manages to get close to the Cornstalker and strike its weak spot with a well-placed attack. The monster howls in pain and falls to the ground, defeated.\n\n{bulletpoint2}The child, triumphant, turns to the awe-struck guild members with a triumphant grin. The child says "Looks like I\'m not just a kid anymore"')
                            behemoth_battle()
                        else:
                            input(
                                f'\n{bulletpoint2}As the child faced off against the Cornstalker, it quickly became apparent that the young fighter was no match for the massive plant-like creature. Despite their determination and skill, the child struggled to land a single blow on the Cornstalker. The monster\'s thick trunk and sharp thorns proved to be formidable defenses, and the child was soon overpowered by the Cornstalker\'s vicious attacks. Despite their valiant effort, the child was ultimately defeated by the monster.\n')
                            behemoth_battle()
                    elif recruit_ans.strip().lower() in ('3', 'third', 'chubby', 'the chubby one', 'the man', 'the chubby man', 'the short man', 'the short man', 'the third', 'the third one'):
                        input(f'{bulletpoint}Press enter to determine if the recruit was successful or not by rolling from 1 to 10...')
                        ascii_dice()
                        input(f'{bulletpoint2}You rolled a {recruit_num}.')
                        if recruit_num >= 5:
                            input(
                                f'\n{bulletpoint2}The short and chubby man takes a deep breath and squares up against the Cornstalker. With a determined look on his face, he charges at the monster, dodging its vines and thorns as he weaves in and out of its reach. He lands a few powerful blows to the monster\'s trunk, but the Cornstalker seems unfazed.\n\n{bulletpoint2}The man\'s determination only grows stronger, and he continues to fight with all his might. After a grueling battle, the man finally lands a decisive blow, and the Cornstalker falls to the ground with a mighty crash.\n\n{bulletpoint2}The man stands panting, his chest heaving with exertion, but with a proud grin on his face. "I told you I was ready for a fight," he says, dusting off his hands. "Now let\'s go find some more monsters to defeat."\n')
                            behemoth_battle()
                        else:
                            input(
                                f'\n{bulletpoint2}As the chubby man charged at the Cornstalker monster, he swung his sword wildly in an attempt to cut through the monster\'s thick, woody trunk.\n\n{bulletpoint2}However, the monster easily countered his attacks with its sharp thorns and vines. The chubby man was no match for the Cornstalker\'s strength and speed, and he was quickly overpowered.\n\n{bulletpoint2}The monster grabbed him with its vines and lifted him up to its glowing green eyes. The chubby man struggled and screamed as the monster brought him closer to its razor-sharp teeth.\n\n{bulletpoint2}With one final bite, the Cornstalker monster devoured the chubby man, leaving nothing but a pile of bones on the ground. The other members of the Monster Hunter Guild watched in horror as the Cornstalker let out a triumphant roar.\n')
                            behemoth_battle()
                    else:
                        input(f'\n{bulletpoint2}You decide that none of them are worth recruiting and told them all to get lost!\n')
                        behemoth_battle()

                input(f'\n{bulletpoint2}You are proud of your accomplishment, and you feel a sense of satisfaction and fulfillment as you continue on your journey as a monster hunter. You know that there will be many more challenges and dangers ahead, but you are ready for whatever comes your way.\n')
                menu()
                the_restaurant()

            # Murder of the Three Thugs
            def murder_thugs():
                nonlocal assassin_guild_membership, thugs_life
                if thugs_life == 'alive':
                    input(f'{bulletpoint2}You spend weeks investigating and gathering information about the thugs. You learn their names, their habits, and their weaknesses. You plan and prepare your attack, determined to make the thugs pay for what they have done to you.\nFinally, the day of your revenge arrives. You ambush the thugs one by one, and you kill them with cold and ruthless efficiency. You feel a sense of satisfaction and relief as you see the thugs fall, knowing that you have avenged the attack.\nBut you also feel a sense of guilt and regret. You know that what you have done is wrong, and you wonder if there was a better way to resolve the conflict. You decide to leave town and start a new life, hoping to leave the past behind and find peace and happiness.\n')
                    thugs_life = 'dead'
                    input(f'\n{bulletpoint2}As you make your way out of town, you notice a hooded figure following you at a distance. You become suspicious and wary, and you keep a close eye on the figure.\nEventually, you confront the figure and demand to know who they are and why they are following you.\n"I saw what you did," the old man says, his voice cold and accusing. "I saw you kill those thugs. And now, you must face the consequences."\nBefore you can react, the old man throws a powder in your face. You feel a sudden burning sensation and then everything goes black.\nWhen you awaken, you find yourself lying on the ground in a mysterious city. You are disoriented and confused, and you have no idea how you got there.\nYou look around, trying to make sense of your surroundings. You see a group of hooded people standing nearby, watching you with a mixture of curiosity and suspicion.\nYou realize that the old man must have brought you here, and that you are now at the mercy of this mysterious group. You wonder what they will do with you, and you fear the worst.\nThe old man taps you on the shoulder from behind and has you follow him...\n')
                else:
                    input(f'\n{bulletpoint2}As you approach the scene of the crime, you carefully assess the situation. The three thugs are heavily focused on the couple, leaving them vulnerable to attack.\n\n{bulletpoint2}You silently make your way behind the first thug and deliver a swift kick to the back of his knees, causing him to fall to the ground.\n\n{bulletpoint2}The second thug turns to face you, but you are too quick for him. You dodge his clumsy swings and deliver a series of quick punches, eventually knocking him unconscious.\n\n{bulletpoint2}The third thug tries to run, but you easily catch up to him and grab him by the collar. With a flick of your wrist, you disable his ability to move and leave him on the ground.')
                    if assassin_guild_membership == True:
                        end_new_thugs = input(f'\n{bulletpoint}With your skills in the art of assassination, do you decide to end the lives of these thugs?')
                        if end_new_thugs.strip().lower() in yes:
                            input(f'\n{bulletpoint2}You quickly draw your sword and approach the three thugs. With a single, fluid motion, you strike each of them down.\n\n{bulletpoint2}The couple you had saved looks on in shock and gratitude. You nod at them, indicating that they are safe now.\n\n{bulletpoint2}You then turn to leave, but not before spotting a fellow member of the assassins guild watching from a nearby alley. You nod at them in recognition before making your way towards the City of the Rising Sun, where the guild headquarters is located.\n')
                            menu()
                            assassins_guild()
                        else:
                            input(f'\n{bulletpoint2}As you make your way away from the scene, you spot another hooded figure watching you from a nearby alleyway. You recognize the signature red sash around their waist as a sign of their membership in the assassin guild. The figure approaches you, revealing themselves to be a fellow guild member.\n\n{bulletpoint2}He nods in acknowledgement, pleased with your performance. You both then set off towards the City of the Rising Sun.\n')
                            menu()
                            assassins_guild()
                    else:
                        input(f'\n{bulletpoint2}As you make your way out of town, you notice a hooded figure following you at a distance. You become suspicious and wary, and you keep a close eye on the figure.\n\n{bulletpoint2}Eventually, you confront the figure and demand to know who they are and why they are following you.\n"I saw what you did," the old man says, his voice cold and accusing. "I saw you take down those thugs. And now, you must face the consequences."\nBefore you can react, the old man throws a powder in your face. You feel a sudden burning sensation and then everything goes black.\n\n{bulletpoint2}When you awaken, you find yourself lying on the ground in a mysterious city. You are disoriented and confused, and you have no idea how you got there.\n\n{bulletpoint2}You look around, trying to make sense of your surroundings. You see a group of hooded people standing nearby, watching you with a mixture of curiosity and suspicion.\n\n{bulletpoint2}You realize that the old man must have brought you here, and that you are now at the mercy of this mysterious group. You wonder what they will do with you, and you fear the worst.\n\n{bulletpoint2}The old man taps you on the shoulder from behind and has you follow him...\n')
                        menu()
                        assassins_guild()
                menu()
                assassins_guild()

            # The Secret Item
            def secret_item():
                nonlocal coin_guess_correctly
                input(f'\n{bulletpoint2}As you exit the vendor lady\'s shop, you are approached by the shopkeeper\'s husband. He is a friendly, unassuming man, and he smiles warmly as he greets you.\n\n{bulletpoint2}He couldn\'t help but notice that you were browsing the shop. He asks if you would be interested in playing a little game for a rare item.\n\n{bulletpoint2}Intrigued, you agree to play along. The husband explains that there is a coin hidden under one of the three cups on the table in front of him. He invites you to choose a cup and make a guess as to which one contains the coin.\n\n{bulletpoint2}If you guess correctly he\'ll give you a secret item from the shop. It\'s a small token of appreciation for your patronage.\nAnd even if you don\'t win, don\'t worry. It\'s all in good fun.\n')

                # Define the cups and the coin
                cups = ["A", "B", "C"]
                coin = "⊛"

                # Shuffle the cups
                random.shuffle(cups)

                # Place the coin in a random cup
                coin_cup = random.choice(cups)

                # Print the cups and the coin
                clean_cups = ', '.join([f'{cup}' for cup in cups])
                print(f'Cups: {clean_cups}')
                print(f'Coin: {coin}')

                # Ask the user to guess the cup with the coin
                guess = input('\nGuess the cup with the coin: ')

                # Check if the user's guess is correct
                if guess.lower() == coin_cup.lower():
                    input(f'\nCongratulations, you found the coin!')
                    coin_guess_correctly = True
                else:
                    input(f'\nSorry, the coin was in cup {coin_cup} :(\n')

                if coin_guess_correctly == True:
                    secret_item_list = [valkyrie_crossbow, boomerang, thors_hammer, redempireflag, dragonscale]
                    # Add the item's name to hero's items list.
                    random_secret_item = random.choice(secret_item_list)
                    if random_secret_item.name in hero_items:
                        input(f'{bulletpoint2}It looks like you already have this item in your inventory. I\'ll give you a money gift instead!')
                        add_money(300, 1000)
                        input(
                            f'\n{bulletpoint2}Congratulations, you just earned a nice chunk of change! I\'m sure you\'ll enjoy it!🎁\nThe money has been added to your inventory. Press enter to continue...')
                    else:
                        # Add the item's attributes to the hero and add the item's name to hero's items list.
                        hero.add_item(random_secret_item)
                        input(
                            f'\n{bulletpoint2}Congratulations, you just won the {random_secret_item.name}! I\'m sure you\'ll enjoy it!🎁\nThe {random_secret_item.name} has been added to your inventory. Press enter to continue...')
                else:
                    pass
                menu()
                coin_guess_correctly = False
                if thugs_life == 'alive' and monster_guild_membership == False:
                    thug_or_monster = input(
                        f'\n{bulletpoint2}The husband greets you goodbye and hopes to see you again. Feeling ecstatic, you thank him for the game and turn to leave. As you walk away, you feel a strong desire to punish the three thugs that attacked you now that you\'re empowered with your new earnings. You could track them down but that would be risky and potentially dangerous.\n\n{bulletpoint2}As you ponder your options, you notice a group of people standing nearby. They are dressed in strange, exotic clothing, and they appear to be recruiting for their monster hunter guild. You could join their ranks and get into hunting and defeating dangerous beasts.\n\n{bulletpoint}Either way, you know that you must make a decision... what do you do?\n')
                    if thug_or_monster.strip().lower() in ('thug', 'thugs', 'revenge', 'track', 'track down', 'punish'):
                        input(
                            f'\n{bulletpoint2}You cannot forget the attack, and you want to punish them for what they did to you earlier. You decide to track down the thugs and take justice into your own hands.\n')
                        murder_thugs()
                    else:
                        input(
                            f'\n{bulletpoint2}You approach the group and ask about joining their ranks.\n')
                        menu()
                        monster_hunter_guild()
                elif thugs_life == 'alive' and monster_guild_membership == True:
                    thug_or_monster = input(
                        f'\n{bulletpoint2}The husband greets you goodbye and hopes to see you again. Feeling ecstatic, you thank him for the game and turn to leave. As you walk away, you feel a strong desire to punish the three thugs that attacked you now that you\'re empowered with your new earnings. You could track them down but that would be risky and potentially dangerous.\n\n{bulletpoint2}As you ponder your options, you notice your fellow monster guild members standing nearby. They are dressed in strange, exotic clothing, and they appear to be recruiting for their monster hunter guild. Would you like to help them recruit?\n\n{bulletpoint}Either way, you know that you must do make a decision... what do you do?\n')
                    if thug_or_monster.strip().lower() in ('thug', 'thugs', 'revenge', 'track', 'track down', 'punish'):
                        input(
                            f'\n{bulletpoint2}You cannot forget the attack, and you want to punish them for what they did to you earlier. You decide to track down the thugs and take justice into your own hands.\n')
                        murder_thugs()
                    else:
                        input(
                            f'\n{bulletpoint2}You approach the guild members and assist them in the recruitment.\n')
                        menu()
                        monster_hunter_guild()
                elif thugs_life == 'dead' and monster_guild_membership == False:
                    thug_or_monster = input(
                        f'\n{bulletpoint2}The husband greets you goodbye and hopes to see you again. Feeling ecstatic, you thank him for the game and turn to leave. As you walk away, you see three thugs that are assaulting a couple. You could go after them to help the couple, but that would be risky and potentially dangerous.\n\n{bulletpoint2}As you ponder your options, you notice a group of people standing nearby. They are dressed in strange, exotic clothing, and they appear to be recruiting for their monster hunter guild. You could join their ranks and get into hunting and defeating dangerous beasts.\n\n{bulletpoint}Either way, you know that you must do make a decision... what do you do?\n')
                    if thug_or_monster.strip().lower() in ('thug', 'thugs', 'go after them', 'track', 'track down', 'punish', 'three thugs', 'couple', 'help', 'help the couple'):
                        if assassin_guild_membership == True:
                            input(
                                f'\n{bulletpoint2}You cannot forget the attack, and you want to punish them for what they did to the couple. With your abilities gained from the assassins guild, you easily track down the thugs and take justice into your own hands.\n')
                        else:
                            input(
                                f'\n{bulletpoint2}You cannot forget the attack, and you want to punish them for what they did to the couple. You decide to track down the thugs and take justice into your own hands.\n')
                        murder_thugs()
                    else:
                        input(
                            f'\n{bulletpoint2}You approach the group and ask about joining their ranks.\n')
                        menu()
                        monster_hunter_guild()
                elif thugs_life == 'dead' and monster_guild_membership == True:
                    thug_or_monster = input(
                        f'\n{bulletpoint2}The husband greets you goodbye and hopes to see you again. Feeling ecstatic, you thank him for the game and turn to leave. As you walk away, you see three thugs that are assaulting a couple. You could go after them to help the couple, but that would be risky and potentially dangerous.\n\n{bulletpoint2}As you ponder your options, you notice your fellow monster guild members standing nearby. They are dressed in strange, exotic clothing, and they appear to be recruiting for their monster hunter guild. Would you like to help them recruit?\n\n{bulletpoint}Either way, you know that you must do make a decision... what do you do?\n')
                    if thug_or_monster.strip().lower() in ('thug', 'thugs', 'go after them', 'track', 'track down', 'punish', 'three thugs', 'couple', 'help', 'help the couple'):
                        if assassin_guild_membership == True:
                            input(
                                f'\n{bulletpoint2}You cannot forget the attack, and you want to punish them for what they did to the couple. With your abilities gained from the assassins guild, you easily track down the thugs and take justice into your own hands.\n')
                        else:
                            input(
                                f'\n{bulletpoint2}You cannot forget the attack, and you want to punish them for what they did to the couple. You decide to track down the thugs and take justice into your own hands.\n')
                        murder_thugs()
                    else:
                        input(
                            f'\n{bulletpoint2}You approach the guild members and assist them in the recruitment.\n')
                        menu()
                        monster_hunter_guild()

            # The Assassin Guild
            def assassins_guild():
                nonlocal emperor_life, noble_life, icequeen_life, assassin_guild_membership
                global current_fountain_money
                current_fountain_money = random.randint(1, 150)
                drink_water_ans = input(f'\n{bulletpoint2}As the old man shows you around the City of the Rising Sun, you are struck by the peaceful and serene atmosphere of the city. People from all walks of life can be seen going about their business, and there is a sense of harmony and cooperation among the various different groups.\n\n{bulletpoint2}The old man leads you through the winding streets of the city, pointing out the various landmarks and places of interest. He shows you the central market, where merchants from all over the world come to trade their goods. You also visit the city\'s library, which is filled with ancient books and scrolls that contain knowledge and wisdom from the past.\n\n{bulletpoint2}As you continue your tour, the old man brings you to the city\'s main square, where a large fountain stands in the center. People are gathered around the fountain, enjoying the cool, refreshing water on a hot day. The old man tells you that the water of the fountain has healing properties, and many people come to drink from it to cure their ailments.\n\n{bulletpoint}Do you take a drink of this water?\n')
                if drink_water_ans.strip().lower() in yes:
                    input(f'{bulletpoint}You were healed for 50 health points!')
                    hero.health += 50
                    menu()
                    throw_fountain = input(f'{bulletpoint2}Current Fountain Change: {current_fountain_money}\nSome people throw some money into the fountain for good luck. Would you like to throw anything in or steal the fountain money?')
                    if 'throw' in throw_fountain.strip().lower():
                        money_throw = input(f'{bulletpoint2}Current money: ${hero.money}\nEnter the money amount you would like to throw:')
                        try:
                            if int(money_throw) > 0 and int(money_throw) <= hero.money:
                                hero.money -= int(money_throw)
                                current_fountain_money += int(money_throw)
                                input(
                                    f'{bulletpoint2}You\'ve successfully thrown ${money_throw} into the fountain!\nCurrent Fountain Change: {current_fountain_money}')
                                if current_fountain_money >= 1000:
                                    add_health(goldscale)
                                    input(f'{bulletpoint2}All of a sudden, a fountain monster called Goldscale pops up from the fountain after your threw the money in. This monster has a body made of shimmering gold, with scales covering its skin. Its eyes glowing orbs of pure gold, and a long, serpentine tail that writhes and coils behind it.\n\n{bulletpoint2}When the monster emerges from the fountain, it is enraged by the act of having money thrown into its home. It then starts attacking you, seeking to defend itself and its territory.')
                                    battle(hero, goldscale, 'swims behind a coin chest',
                                        'surrounds itself with coins', 'launches a shower of gold coins', 'surrounds you with coin projectiles')
                                    random_health_gain = random.randint(10, 30)
                                    print(
                                        f'{bulletpoint2} You took some rest and gained {random_health_gain} health back.')
                                    hero.health += random_health_gain
                                    check_health(hero)
                                    add_money(500, 1000)
                                    input(f'{bulletpoint2}In the end, after a long and grueling battle, you emerged victorious. Goldscale, defeated, retreated back into the fountain. The adventurer, triumphant, went on to tell the tale of their victory to all who would listen. And so, the legend of the fountain monster was born.')
                                    menu()
                            elif int(money_throw) == 0:
                                input(f'{bulletpoint2}You changed your mind.')
                            else:
                                input(f'{bulletpoint2}This is not a valid number. You changed your mind and left.')
                        except:
                            input(f'{bulletpoint2}This is not a valid number. You changed your mind and left.')
                    elif 'steal' in throw_fountain.strip().lower():
                        input(f'{bulletpoint2}You decided to take the {current_fountain_money}!\n')
                        hero.money += current_fountain_money
                        current_fountain_money = 0
                        input(f'{bulletpoint2}Current fountain money: ${current_fountain_money}\n')
                        menu()
                    else:
                        input(
                            f'{bulletpoint2}You decided to leave the fountain the way it is.')

                #The assassin guild building
                input("""
                                   ...                            
                                 ;::::;                           
                               ;::::; :;                          
                             ;:::::'   :;                         
                            ;:::::;     ;.                        
                           ,:::::'       ;           OOO\         
                           ::::::;       ;          OOOOO\        
                           ;:::::;       ;         OOOOOOOO       
                          ,;::::::;     ;'         / OOOOOOO      
                        ;:::::::::`. ,,,;.        /  / DOOOOOO    
                      .';:::::::::::::::::;,     /  /     DOOOO   
                     ,::::::;::::::;;;;::::;,   /  /        DOOO  
                    ;`::::::`'::::::;;;::::: ,#/  /          DOOO 
                    :`:::::::`;::::::;;::: ;::#  /            DOOO
                    ::`:::::::`;:::::::: ;::::# /              DOO
                    `:`:::::::`;:::::: ;::::::#/               DOO
                     :::`:::::::`;; ;:::::::::##                OO
                     ::::`:::::::`;::::::::;:::#                OO
                     `:::::`::::::::::::;'`:;::#                O 
                      `:::::`::::::::;' /  / `:#                  
                       ::::::`:::::;'  /  /   `#              
                """)
                print(f'\n{bulletpoint}After exploring the city for a while, the old man leads you to a secluded part of the city, where a mysterious sign stands in front of a hidden door. The sign bears the emblem of a hooded figure holding a curved blade. The old man tells you that this is the entrance to the Assassin Guild, a secretive organization of skilled assassins who serve as protectors.\n\n{bulletpoint2}You thank the old man for showing you around the city, and he tells you that he will be waiting for you if you ever need anything. You stand in front of the mysterious sign, considering whether or not you should enter the Assassin Guild and see what secrets it holds.\n\n')
                if assassin_guild_membership == False:
                    enter_assassin_guild = input(f'{bulletpoint}The choice is yours, do you enter the building and join the guild?')
                else:
                    enter_assassin_guild = input(f'Do you enter the building and catch up with your fellow guild members?')
                if enter_assassin_guild.strip().lower() in yes:
                    if assassin_guild_membership == False:
                        input(f'\n{bulletpoint2}Inside, you are greeted by a group of hooded figures who introduce themselves as members of the assassin guild. They explain that they are a secret society of trained assassins who use their skills and knowledge to serve the greater good.\n\n{bulletpoint2}The guild members offer to train you in the ancient ways of assassination, and you are intrigued by the offer. You decide to accept their offer and become a member of the guild.\n')
                        input(f'...')
                        philosophy_ans = input(f'\n{bulletpoint2}You spend the next few months vigorously training with the guild, learning the art of stealth, deception, and assassination. You undergo rigorous physical and mental training, and you master the use of a variety of weapons and tools.\n\n{bulletpoint2}As you progress in your training, you are taught the secrets of the guild and the philosophy that guides its members. You learn to balance the need for justice with the harsh realities of the world, and you become a skilled and deadly assassin.\n{bulletpoint}Do you want to go over the philosophy of the Assassin guild?\n')
                        if philosophy_ans.strip().lower() in yes:
                            input(f'\n\n\n\n\n\n\n\n\n\n\n{bulletpoint2}The philosophy of the assassin guild is based on the principle of balance. The guild members believe that the world is a complex and dangerous place, and that there is a constant struggle between good and evil, order and chaos.\n\n{bulletpoint2}They believe that the guild has a responsibility to maintain the balance of power and prevent any one side from gaining too much control. To achieve this, the guild members use their skills and knowledge to eliminate threats and protect the innocent.\n\n{bulletpoint2}The guild has a complicated relationship with the {current_kingdom_name} and the Red Dragon Empire. On the one hand, the guild is neutral and does not take sides in political conflicts. On the other hand, the guild members are not afraid to intervene if they believe that the balance of power is being threatened.\n\n{bulletpoint2}In the case of the {current_kingdom_name}, the guild has a positive relationship with the queen and her people. The queen values the guild\'s skills and knowledge, and she often hires the guild members to carry out important missions. In return, the guild members protect the {current_kingdom_name} and its people from threats and dangers.\n\n{bulletpoint2}In the case of the Red Dragon Empire, the guild has a more complicated relationship. The emperor and his followers view the guild as a threat and a nuisance, and they often try to suppress the guild\'s activities. However, the guild members are not afraid to challenge the empire and its corrupt rulers, and they will not hesitate to strike if the balance of power is threatened.\n\n')
                    input(
                        f'{bulletpoint2}You recall the poem they taught you:\n\nThe assassin guild is a secret sect\nOf skilled and deadly powers,\nTheir mission is to keep the check\nIn a world of chaos all hours.\n\nThey move through the shadows unseen,\nSilent and deadly as the night,\nReady to strike at a moment\'s bright\nAnd eliminate any threat in sight.\n\nThey are masters of the blade and the bow,\nTrained in the arts of stealth and deception,\nThey are feared by their enemies\nAnd respected by those who know their profession.\n\nThe guild is a force for right,\nA protector of the innocent and the weak,\nThey will continue to fight\nFor balance and justice in a world that seeks.\n')
                    if assassin_guild_membership == False:
                        new_kill = input(
                            f'\n{bulletpoint}At the end of your training, you are given a mission to complete. You are to assassinate a...\nPlease enter your assassination target: ')
                        assassin_guild_membership = True
                    else:
                        new_kill = input(
                            f'\n{bulletpoint}As a veteran Assassin, you are given a new mission to complete. You are to assassinate a...\nPlease enter your assassination target: ')
                    while new_kill.strip().lower() == hero.name.strip().lower():
                        new_kill = input(
                            f'{bulletpoint2}You cannot kill yourself...\n{bulletpoint}Please enter a new assassination target: ')
                    if new_kill.strip().lower() in ('beggar', 'the beggar'):
                        nonlocal current_heir
                        input(
                            f'\n{bulletpoint2}You are to assassinate a beggar who has been terrorizing the people of the Red Dragon Empire. You accept the mission.\n')
                        input(f'\n{bulletpoint2}You are initially puzzled by the mission. You cannot understand why the guild would want to kill a homeless beggar, who poses no threat to anyone. You decide to question the guild leader about the mission.\n\n{bulletpoint2}The guild leader explains that the beggar is not what he seems. He is actually a spy for the {current_kingdom_name}, who has been gathering information about the empire\'s defenses and plans. The guild has been hired by the empire to eliminate the spy and prevent him from passing on his information.\n\n{bulletpoint2}You are uneasy about the mission, but you trust the guild leader and you decide to carry it out. You disguise yourself as a beggar and approach the beggar outside the castle gates. You strike up a conversation and gain his trust.\nWhen the time is right, you strike the beggar with a hidden blade.\n\n{bulletpoint}Press enter to roll 1 to 10 to determine if the kill was clean...\n')
                        clean_kill_beggar = random.randint(1, 10)
                        ascii_dice()
                        print(f'{bulletpoint2}You rolled a {clean_kill_beggar}.')
                        if clean_kill_beggar > 5:
                            input(
                                f'\n{bulletpoint2}The kill was clean. You dispose of the body and return to the guild, reporting the mission as completed.\n')
                        else:
                            add_health(beggarbattle)
                            battle(hero, beggarbattle, 'hides behind wall',
                                'curses at you', 'picks up a stick', 'throws a rock at you')
                            random_health_gain = random.randint(10, 30)
                            print(
                                f'{bulletpoint2} You took some rest and gained {random_health_gain} health back.')
                            hero.health += random_health_gain
                            check_health(hero)
                            add_money(25, 50)
                            input(
                                f'\n{bulletpoint2}The kill was messy. You dispose of the body and return to the guild, reporting the mission as completed.\n')
                        menu()
                        input(
                            f'\n{bulletpoint2}You go back to strolling along the streets and see a different beggar...\n')
                        ending(ending3)
                        beggar()
                        # This changes the current heir to be the noble lady if you assassinate the beggar, or the emperor's cousin if the noble lady is already dead
                        if 'beggar' in current_heir:
                            if noble_life == 'alive':
                                current_heir = 'noble lady'
                            else:
                                current_heir = 'Emperor\'s cousin'
                    elif new_kill.strip().lower() in ('emperor', 'the emperor'):
                        if emperor_life == 'alive':
                            input(
                                f'\n{bulletpoint2}You are to assassinate a corrupt and evil ruler who has been terrorizing the people of a neighboring kingdom. You accept the mission.\n')
                            input(f'\n{bulletpoint2}As a member of the assassin guild, you are given a mission to carry out. You are to kill the Red Dragon Emperor, the tyrannical ruler of the empire.\n\n{bulletpoint2}You are hesitant about the mission. The emperor is a powerful and dangerous enemy, and killing him will not be easy. It was a mission that many had attempted, and few had survived. But you were determined to succeed. You decide to discuss the mission with the other guild members and seek their advice.\n\n{bulletpoint2}After much debate and deliberation, you and the other guild members agree on a plan. You will infiltrate the emperor\'s palace and gain his trust by pretending to be a loyal servant. Once you are close to the emperor, you will strike and kill him with a hidden blade.\n\n{bulletpoint2}You carry out the plan with precision and stealth. You gain the emperor\'s trust and become one of his most trusted servants. You bide your time and wait for the right moment to strike.\n\n{bulletpoint2}One night, as the emperor is sleeping, you sneak into his chambers and approach his bed. You draw your hidden blade and raise it high, ready to strike.\n\n{bulletpoint}Press enter to roll 1 to 10 to determine if the kill was clean...\n')
                            clean_kill_emperor = random.randint(1, 10)
                            ascii_dice()
                            print(f'{bulletpoint2}You rolled a {clean_kill_emperor}')

                            if clean_kill_emperor == 10:
                                input(
                                    f'\n{bulletpoint2}As you reached the emperor\'s bedside, you unsheathed your blade and struck with precision and speed. The emperor never saw it coming. With a single, clean strike, you ended his reign and claimed your reward.\n\n{bulletpoint2}As you turned to leave, you spotted something out of the corner of your eye. A hidden compartment in the wall, cleverly concealed by a painting. You reached out and touched it, and the painting swung open to reveal an ancient tablet.\n\n{bulletpoint2}You hesitated for a moment, unsure of what to do. But then you noticed a strange inscription on the tablet. It said, "iamgod.". Could it be a command of some sort?\nYou placed your hand on the tablet and spoke the words out loud. "iamgod."\n\n{bulletpoint2}Suddenly, you felt a surge of power coursing through your veins. You could feel your senses heightening, your strength increasing, your reflexes sharpening. You had gained the abilities of a god.\n\n{bulletpoint2}You grinned with excitement and anticipation. With your newfound powers, you could take on any challenge that came your way. You were ready for anything the battlefield might throw at you.\n\n{bulletpoint2}You dispose of the body and return to the guild, reporting the mission as completed.\n')
                            elif clean_kill_emperor > 5:
                                input(
                                    f'\n{bulletpoint2}The kill was clean. You dispose of the body and return to the guild, reporting the mission as completed.\n')
                            else:
                                nonlocal current_emperor
                                add_health(emperorbattle)
                                battle(hero, emperorbattle, 'raises shield',
                                    'groans in pain', 'calls guards over', 'uses sharp end of the shield')
                                random_health_gain = random.randint(10, 30)
                                print(
                                    f'{bulletpoint2} You took some rest and gained {random_health_gain} health back.')
                                hero.health += random_health_gain
                                check_health(hero)
                                add_money(25, 500)
                                input(
                                    f'\n{bulletpoint2}The kill was messy. You dispose of the body and return to the guild, reporting the mission as completed.\n')
                            emperor_life = 'dead'
                            # updates the next in line to the empire which is the current_heir variable
                            current_emperor = current_heir
                            current_heir = 'no one'
                        else:
                            input(
                                f'\n{bulletpoint2}The previous emperor is already dead and has already been quickly replaced by {current_emperor}!')
                        menu()
                        ending(ending4)
                        beggar()
                    elif new_kill.strip().lower() in ('icequeen', 'the ice queen', 'queen', 'ice queen', 'queen of ice', 'ice'):
                        if icequeen_life == 'alive':
                            input(
                                f'\n{bulletpoint2}You are to assassinate a benevolent ruler of the neighboring Ice Kingdom. You accept the mission.\n')
                            input(f'\n{bulletpoint2}As a member of the assassin guild, you are given a mission to carry out. You are a highly trained and skilled killer. You are proficient in a variety of weapons and techniques, and well-versed in the art of stealth and deception.\n\n{bulletpoint2}You carefully plan your attack, studying the queen\'s routine and the layout of her palace in order to find the perfect moment to strike. When the opportunity presents itself, you move in silently, weapons at the ready.\n\n{bulletpoint2}As you approach the queen\'s chambers, you can sense a powerful magical aura emanating from within. You know that the queen is a powerful magician, and you\'re prepared for her to use her powers against you. You focus your mind and steel your resolve, determined to complete the mission.\n\n{bulletpoint2}You burst into the queen\'s chambers, your weapons flashing in the dim light. The queen is taken by surprise, but she quickly recovers and raises her hands, unleashing a powerful spell at you. You dodge and weave, using all of your training and experience to avoid her attacks.\n\n{bulletpoint2}The queen and you engage in a fierce battle, the magic and weapons clashing with explosive force. The room is filled with the sound of crashing thunder and flashing lightning as your both duel. Despite her power, You\'re able to outmaneuver the queen and land a killing blow, silencing her forever.\n\n{bulletpoint}Press enter to roll 1 to 10 to determine whether her Ice Monster pet "Snowfang" wakes up or not...\n')
                            clean_kill_queen = random.randint(1, 10)
                            ascii_dice()
                            print(f'{bulletpoint2}You rolled a {clean_kill_queen}')

                            if clean_kill_queen > 5:
                                input(
                                    f'\n{bulletpoint2}The kill was clean. You dispose of the body and return to the guild, reporting the mission as completed.\n')
                            else:
                                input(f'{bulletpoint2}Snowfang yawned and stretched as she woke up from her long winter\'s nap, then immediately started growling at you!')
                                add_health(snowfang)
                                battle(hero, snowfang, 'creates a wall of solid ice',
                                    'starts creating wall of solid ice', 'does frostbite', 'summons a swirling snowstorm')
                                random_health_gain = random.randint(10, 30)
                                print(
                                    f'{bulletpoint2} You took some rest and gained {random_health_gain} health back.')
                                hero.health += random_health_gain
                                check_health(hero)
                                add_money(50, 200)
                                input(
                                    f'\n{bulletpoint2}The kill was messy. You dispose of the body and return to the guild, reporting the mission as completed.\n')
                            icequeen_life = 'dead'
                        else:
                            input(f'\n{bulletpoint2}The queen is already dead!')
                        menu()
                        ending(ending5)
                        beggar()
                    else:
                        nonlocal new_monk_replacement, new_goons, thugs_life
                        if new_kill.strip().lower() in ('noble', 'noble lady'):
                            noble_life = 'dead'
                        elif new_kill.strip().lower() == new_monk_replacement.strip().lower():
                            new_monk_replacement = random.choice(new_monk_replacement_list)
                        elif new_kill.strip().lower() == new_goons.strip().lower():
                            new_goons = random.choice(new_goons_list)
                            thugs_life = 'dead'
                        input(
                            f'\n{bulletpoint2}You are to assassinate {new_kill}. You accept the mission.')
                        input(f'{bulletpoint2}The night was dark and cold, the perfect conditions for an assassination. You crept through the shadows, senses heightened and your heart pounding with anticipation.\n\n{bulletpoint2}Your target was {new_kill}. You had studied {new_kill}\'s routine and habits, and you knew exactly when and where they would be most vulnerable.\n\n{bulletpoint2}You made your way to the designated spot, a secluded alleyway near their residence. Your waited in the shadows, your weapon of choice at the ready.\n\nAs {new_kill} walked past, you stepped out of the darkness and struck. Your blade sliced through the air with deadly precision, finding its mark in {new_kill}\'s throat. {new_kill} gasped and clutched at their neck, but it was too late. You watched as the life drained from their eyes, and then disappeared into the night, leaving no trace of your presence behind.\n\n{bulletpoint2}The kill was clean and efficient, a testament to your skills as an assassin. you would be rewarded for the successful mission, and you would be ready for the next one. That was the life of an assassin, a life of danger and deception, but one that you embraced wholeheartedly.\n')
                        add_money(25, 100)
                        menu()
                        ending(ending6)
                        beggar()

                else:
                    menu()
                    the_restaurant()

            # The Hidden City
            def hidden_city():
                kingdom_or_empire_var = '.'
                city_ans = input(f'{bulletpoint}As you wander through the streets of the city called “The City of the Rising Sun”, you come across a small shop selling trinkets and souvenirs. You decide to take a look and see if there is anything interesting.\n\n{bulletpoint2}As you browse the shelves, a friendly old man approaches you and says that this city is a safe haven for those who seek refuge from the troubles of the outside world. It is hidden from the eyes of the Red Dragon Empire and the {current_kingdom_name}, and it is a place of harmony. Do you ask him more about the Red Dragon Empire and the {current_kingdom_name}?\n')
                if city_ans.strip().lower() in yes:
                    if icequeen_life == 'alive':
                        city_ans2 = input(f'\n{bulletpoint2}The Red Dragon Empire is a vast and powerful kingdom ruled by a cruel and tyrannical emperor. It is a land of war and conquest, where the strong prey on the weak and the weak must fight to survive.\n\n{bulletpoint2}The Ice Kingdom, on the other hand, is a land of mystery and magic. It is ruled by a wise and benevolent queen, who uses her powers to protect her people and keep the peace.\n{bulletpoint}Do you want to hear more?\n')
                    else:
                        city_ans2 = input(f'\n{bulletpoint2}The Red Dragon Empire is a vast and powerful kingdom ruled by a cruel and tyrannical emperor. It is a land of war and conquest, where the strong prey on the weak and the weak must fight to survive.\n\n{bulletpoint2}The Empire of Ice\'s new ruler was the sister to the original benevolent Queen and had usurped the throne. She is a ruthless and power-hungry individual who is willing to resort to violence and treachery in order to gain and maintain power. The people of the Empire of Ice may be in danger under this ruler\'s rule, and it is possible that there may be political unrest and conflict within the kingdom.\n{bulletpoint}Do you want to hear more?\n')
                    if city_ans2.strip().lower() in yes:
                        # This is to update a variable in the city_ans3 story if the current kingdom name had been changed to Empire of Ice.
                        if current_kingdom_name == 'Empire of Ice':
                            kingdom_or_empire_var = '. now called the Empire of Ice'
                        else:
                            kingdom_or_empire_var = '.'
                        city_ans3 = input(f'\n{bulletpoint2}The old man nods and begins to tell you the history of the Red Dragon Empire. He explains that, long ago, the empire was ruled by a peaceful and benevolent ruler who was loved and respected by his people.\nBut one day, a cruel and ambitious emperor overthrew the peaceful ruler and seized control of the empire.\n\n{bulletpoint2}Under the emperor\'s rule, the Red Dragon Empire became a land of conquest and aggression. The emperor sought to expand his power and territory, and he set his sights on the Ice Kingdom.\n\n{bulletpoint2}But the Ice Kingdom was a land of magic, and its queen was a powerful sorceress. She used her powers to protect her kingdom and repel the emperor\'s armies. Despite his best efforts,\nthe emperor was unable to conquer the Ice Kingdom..{kingdom_or_empire_var}, and the two kingdoms have been in a state of cold war ever since.\n\n{bulletpoint2}The old man concludes his story by saying that the City of the Rising Sun is a safe haven for those who seek refuge from the conflicts and dangers of the outside world. He offers to show you around the city, if you are interested.\n{bulletpoint}What do you say?\n')
                        if city_ans3.strip().lower() in yes:
                            menu()
                            assassins_guild()
                        else:
                            menu()
                            ice_kingdom()
                    else:
                        menu()
                        ice_kingdom()
                else:
                    menu()
                    blackjack_ans = input(
                        f'\n{bulletpoint}A vendor nearby walks up to you and asks if you would like to play Whackjack?\n')
                    if blackjack_ans.strip().lower() in yes:
                        input(
                            f'\n{bulletpoint2}(The goal is to get as close to 21 as possible. "Hit" will draw another card, while "Stand" will stop drawing)\nPress enter to continue...')
                    while blackjack_ans.strip().lower() in yes or blackjack_ans.strip().lower() == '':
                        blackjack()
                        blackjack_ans = input(
                            f'\n{bulletpoint2}(The goal is to get as close to 21 as possible. "Hit" will draw another card, while "Stand" will stop drawing)\n\n{bulletpoint2}(You can also press enter to play again)\n{bulletpoint}Play another round of Whackjack?\n')
                    else:
                        print(f'\n{bulletpoint2}The customer says take care!\n')
                        ice_kingdom()

            #Get Drunk
            def get_drunk():
                drink_ans = input(
                    f'\n{bulletpoint}You are sitting at a table in a local tavern. The tavern bartender asks you if you would like a drink. Do you take it?\n')
                if drink_ans.lower().strip() in yes:
                    first_drink_ans = input(
                        f'\n{bulletpoint2}After the first drink, you feel a warm, relaxed sensation in your chest and limbs, and your inhibitions may start to loosen. You find yourself smiling...\n\n{bulletpoint}The bartender asks if you would like a second drink, what do you say?\n')
                    if first_drink_ans.lower().strip() in yes:
                        second_drink_ans = input(
                            f'\n{bulletpoint}You feel slightly lightheaded and dizzy, and your movements may become slightly more exaggerated and uncoordinated. Suddenly the bartender says they have a special drink for you. It\'s a rare and potent spirit from the {current_kingdom_name}. Are you brave enough to try it?\n\n')
                        if second_drink_ans.lower().strip() in yes:
                            input(
                                f'\n{bulletpoint}You are tempted by the offer. You have always been curious about the {current_kingdom_name} and its exotic liquors. After much hesitation, you decide to take the third drink. You raise the glass to your lips and take a sip. The liquid is fiery and sweet, and it burns all the way down your throat\n\n{bulletpoint2}As you drink, you notice that the other customers in the tavern are starting to get rowdy. Suddenly, one of them bumps into you and spills your drink.\n\n{bulletpoint2}Before you know it, you are locked in a fierce bar fight with the other customer. You throw punches and dodge blows, feeling reckless and invincible.\n\n')
                            if assassin_guild_membership == False:
                                input(f'\n{bulletpoint2}But your drunken state makes you slow and clumsy, and soon you are on the receiving end of a beating. You stumble and fall to the ground, feeling dazed and bruised.\n\n{bulletpoint2}Just as you are about to black out, you hear a loud noise and feel yourself being lifted off the ground. You open your eyes and see that you are being carried away on a cart by a group of good samaritans...\n')
                            else:
                                input(f'\n{bulletpoint2}You quickly realize that your training as an assassin has given you a distinct advantage in the fight. You easily dodge the other customer\'s attacks and counter with precise strikes. Within minutes, the customer is on the ground, unconscious.\n\n{bulletpoint2}The other patrons in the tavern are stunned by your fighting skills and quickly back away, giving you a wide berth. You take a deep breath and survey the scene, feeling a mix of satisfaction and adrenaline. You grab your belongings and make your way to the door, ready to continue your journey and explore the wonders of the City of the Rising Sun.\n')
                            menu()
                            hidden_city()
                        else:
                            input(
                                f'\n{bulletpoint2}you are already feeling a bit drunk and you know that you should probably stop now before you get into trouble. You decide to travel to a hidden city that you discovered after chatting with a nearby customer.\n')
                            menu()
                            hidden_city()
                    else:
                        input(
                            f'\n{bulletpoint2}you are already feeling a bit tipsy and you know that you should probably stop now before you get into trouble. You decide to travel to a hidden city that you discovered after chatting with a nearby customer.\n')
                        menu()
                        hidden_city()
                else:
                    input(
                        f'\n{bulletpoint2}you know that you shouldn\'t drink and pass on the offer. You decide to travel to a hidden city that you discovered after chatting with a nearby customer.\n')
                    menu()
                    hidden_city()
            #Ice Kingdom
            def ice_kingdom():
                nonlocal gamble_life, current_kingdom_name

                def ice_aftermath():
                    input(f'\n{bulletpoint2}You finally arrive at the gates of the Empire of Ice.\n\n{bulletpoint2}The guard stops you and asks for your license to pass.\nUpon seeing your crown bearing the symbol of the Red Dragon Empire, the guard\'s expression immediately changed to one of fear and lets you immediately pass through.\n\nAs you enter the once-prosperous Ice Kingdom, which was replaced by Empire of Ice, now renamed to the Winter Dragon Realm, you are struck by the scenes of destruction that greet you. The once-beautiful ice palaces and frozen towers lie in ruins, shattered by the might of the Red Dragon Empire. The streets are empty and silent, the once-bustling marketplaces now desolate and abandoned.\n\nAs you walk through the silent streets, you catch glimpses of the few remaining citizens of the Winter Dragon Realm. They huddle together in small groups, their eyes filled with fear and despair. Many of them bear the scars of the brutal attack, their bodies bruised and battered. They whisper in hushed tones, afraid to speak too loudly lest they attract the attention of the Red Dragon\'s soldiers.\n\nIn the distance, you see the Red Dragon\'s banner flying over the ruins of the ice palace, a stark reminder of the empire\'s conquest. The once-majestic Empire of Ice has been reduced to a shadow of its former self, a mere puppet state of the Red Dragon Empire.\n')
                    menu()
                    ending(ending31)
                    beggar()
                
                if icequeen_life == 'dead':
                    input(f'\n\n{bulletpoint2}THE QUEEN IS DEAD!!!\n\n{bulletpoint2}On your way to the castle gates, you hear a loud commotion of people shouting and being shocked and confused. You were the one who carried out the kill on the queen. You quickly realize that the commotion is because of you, and you begin to feel a sense of fear and anxiety.\n\n{bulletpoint2}You try to blend in with the crowd of people, hoping that no one will suspect you of being the killer.\n')
                    if victory == 'red':
                        current_kingdom_name = 'Winter Dragon Realm'
                    else:
                        current_kingdom_name = 'Empire of Ice'
                else:
                    current_kingdom_name = 'Ice Kingdom'
                input('''
            ` : | | | |:  ||  :     `  :  |  |+|: | : : :|   .        `              .
                ` : | :|  ||  |:  :    `  |  | :| : | : |:   |  .                    :
                    .' ':  ||  |:  |  '       ` || | : | |: : |   .  `           .   :.
                            `'  ||  |  ' |   *    ` : | | :| |*|  :   :               :|
                    *    *       `  |  : :  |  .      ` ' :| | :| . : :         *   :.||
                        .`            | |  |  : .:|       ` | || | : |: |          | ||
                '          .         + `  |  :  .: .         '| | : :| :    .   |:| ||
                    .                 .    ` *|  || :       `    | | :| | :      |:| |
            .                .          .        || |.: *          | || : :     :|||
                    .            .   . *    .   .  ` |||.  +        + '| |||  .  ||`
                .             *              .     +:`|!             . ||||  :.||`
            +                      .                ..!|*          . | :`||+ |||`
                .                         +      : |||`        .| :| | | |.| ||`     .
                *     +   '               +  :|| |`     :.+. || || | |:`|| `
                                        .      .||` .    ..|| | |: '` `| | |`  +
            .       +++                      ||        !|!: `       :| |
                        +         .      .    | .      `|||.:      .||    .      .    `
                    '                           `|.   .  `:|||   + ||'     `
            __    +      *                         `'       `'|.    `:
            "'  `---"""----....____,..^---`^``----.,.___          `.    `.  .    ____,.,-
                ___,--'""`---"'   ^  ^ ^        ^       """'---,..___ __,..---""'
            --"'                           ^                         ``--..,__ D. Rice
                ''')
                input('''
                                                    
                                . _\/ \/_ .
                                    \  \ /  /             .      .
                    ..    ..    -==>: X :<==-           _\/  \/_
                    '\    /'      / _/ \_ \              _\/\/_
                        \\\\//       '  /\ /\  '         _\_\_\/\/_/_/_
                _.__\\\\\///__._    *  '  *            / /_/\/\_\ \\
                    '  ///\\\\\  '                           _/\/\_
                        //\\\\                               /\  /\\
                    ./    \.                            '      '
                    ''    ''            
                                ''')
                input('''
                                             __ 
                                            (  )
                                             )( 
                                            | | 
                                            | | 
                                           ;  :
                                          /    \\
                                       ,-v|::::|    ,`^,
                                   v.   )/:::::|_  `)v(
                                ,-'),\  |:::::/ ^\   ||
                                 )(||   |:::::"\/"  | |                    _
                                | |||   )`----'||   | |                 __( )
                             __ | || \  |._____||   | |   __           (  )(
                            (  )| || | | v v v|'`|  | |  (  )           )(| |
                             )( | |I |(^)v v v|,.| .' |   )(            | | |
                         __  ||/  |I | )|v v v|I | |  |  | |           _| | |
                        (  ) ||mmm|   \||v v v|I '||  |  | |          (  )| |
                         ||  ||/v,+--'|||v(^)v|I  || ^|  | |           || | |
                         ||  | \ |^ ^^`'`vv||v|vvv|| ^'.|  |           /| | |
                         | \ |-| |^ ^^/  \\v||/^ ^^|/\^^||  |          .'| | |
                         |  || | |    |  |v|||^ ^^|  \^|   |          | '.|.'
                         |  \+-\ |^ ^^|__| |||    |   \|   |          |  | |
                         |--|   \|^ ^,+  |+--+^ ^ |    Y _ | _        |  | |
                         |  |   \|,-.:|  ||  |^ ^ |    |(.) (.)  _   |   | |
                         |   \  \|; `;|  \/--+    | | /--.-._|_ (.)  |   | |
                         |   |   \/ ( |   |  |^ ^d| |/| /|   | `-,-- |   | |,
                         |   |   \ \ \|   |  | ^|8||o |o |  /|  /|   |   | '.
              -hrr-      |   |  _,\--.|   |   | `"||| || | o | o |  |    '. |
                         |\,-|-' _|--.|   |   |^ ^| | || | | | | | o|    ||  |
                        /| |,|,-'   \ |._ |   |^^^|/O\/^\|/^\|/^\|/ |    ||  .
                  _.Y._/ |   |       \|  `|   |  ^|_ / O Y O | O\/ |   ,'||  |
                ,'     `\|   |    |   Y   |`--|  |   |---|.__|  /  |_,'  |   |
             ,-,         )   |   -+-  |   |   | /^\  |   |   |  /  |    ,.   |
            (  \       /\|       ,|.  |   |   |/   \/^\ /\  /\ /\\\\ |   | _'  |
             \  \ \\\\/\//\    _,-_/  `.|   |    | o | o Y  \/  \//\|    ' [  /|
              ) /\,-       ,:--'::-.  `.  |    |,-.|__ | o| o /\\\\\|   |   |/||
             (  \   \/\/\,( ...:::::`-. `.     ( . |. ),-.|,- \\\\//\   |  //||
              `--`-.___  /\-,----,._   `-.`.   /\  `-' `._| .//\\\\\/ _|.,'/||
                       `--//// //|  `-._  `-\  | \_    |   _/\\\\\///\    /|||
                         //// //|,: \\\\ \\\\--._\ |_| `---|__/  //\\\\/\\\\   / ||
                        `-'`'//_|,   \\\\ \\\\ \\\\ /v\/\,      `.//_|| | | /|
                            (_)       \\\\ \\\\ \\\\-._   \/ \;.,.    `-^',' |
                                      (_)) \(_)  `---.__  ` \/\/\  (
                                         `-'            `---._  /   \\
                                                              `(     )
                                                                `---'
                ''')
                if current_heir.strip().lower() == hero.name.strip().lower() or current_emperor.strip().lower() == hero.name.strip().lower():
                    if icequeen_life == 'alive':
                        if gamble_life == False:
                            input(f'\n{bulletpoint2}You finally arrive at the gates of the Ice Kingdom.\n\nThe guard stops you and asks for your license to pass.\nUpon seeing your crown bearing the symbol of the Red Dragon Empire, the guard\'s expression immediately changed to one of suspicion. Without a word, she signaled for her fellow guards to arrest you. You were taken into custody and brought before the queen of the Ice Kingdom, who was known for her benevolent personality.\n\n{bulletpoint2}As you stood before the queen, you could see the anger and resentment in her eyes. She accused you of being a spy and threatened to have you executed. In that moment, you knew that you had to act quickly if you wanted to save your life.\n\n')
                            do_you_promise = input(f'{bulletpoint2}You pleaded with the queen, explaining that you were simply curious and wanted to learn more about the world beyond your own land. You begged for her mercy and offered to pay any price she demanded.\n\n{bulletpoint2}To your surprise, the queen\'s expression softened and she seemed to consider your words. After a long moment of silence, she spoke...\n\n')
                            while do_you_promise.lower().strip() not in (yes,'i promise', 'promise', 'yes i promise', 'i promise never to return', 'i promise to never return', 'okay i promise', 'i promise to not return'):
                                do_you_promise = input(f'{bulletpoint}"I will grant you safe passage out of my kingdom," she said, "but only on the condition that you PROMISE to never return."\nWhat is your response:')
                            gamble_life = True
                            input(f'{bulletpoint2}Relieved and grateful, you accepted the queen\'s offer and you were allowed to leave the Ice Kingdom unharmed. It was a harsh lesson, but one that you would never forget. The world was a dangerous place and your would have to be cautious and wise in your dealings with other kingdoms if you wanted to rule the Red Dragon Empire with honor and dignity.\n')
                            input(f'{bulletpoint2}You were granted a boat with free passage to leave the kingdom, and you sailed off back to the Red Dragon Empire.')
                            menu()
                            trade_mission()
                        else:
                            input(f'{bulletpoint2}YOU WERE CAUGHT!!!\n\n{bulletpoint2}As you approached the gates of the Ice Kingdom, you could feel a sense of trepidation rising within you. Despite the promise you had made to the benevolent ice queen, you couldn\'t shake the feeling that you needed to return.\n\n{bulletpoint2}As you entered the kingdom, the guards immediately seized you and escorted you onto the gallows. You knew that you had betrayed the trust of the ice queen and now you would have to face the consequences.\n')
                            input(f'{bulletpoint2}You were brought before the Ice Queen and she turned away and wouldn\'t even look at you. The crowd gathered around you, their eyes full of anger and resentment. The ice queen herself appeared, her face cold and unforgiving. She glared at you with icy eyes as the executioner placed the noose around your neck.\n\n{bulletpoint2}She then all of a sudden yelled "Halt!", and gave you one last chance to earn your life... ')
                            hangman()
                            input(f'{bulletpoint2}You were allowed to leave the Empire of Ice unharmed. It was a harsh lesson, but one that you would never forget. The world was a dangerous place and your would have to be cautious and wise in your dealings with other kingdoms if you wanted to rule the Red Dragon Empire with honor and dignity.\n')
                            input(
                                f'{bulletpoint2}You were granted a boat with free passage to leave the kingdom, and you sailed off back to the Red Dragon Empire.')
                            menu()
                            trade_mission()
                    else:
                        if victory == 'red':
                            ice_aftermath()
                        else:
                            input(f'\n{bulletpoint2}You finally arrive at the gates of the Empire of Ice.\n\n{bulletpoint2}The guard stops you and asks for your license to pass.\nUpon seeing your crown bearing the symbol of the Red Dragon Empire, the guard\'s expression immediately changed to one of suspicion. Without a word, she signaled for her fellow guards to arrest you. You were taken into custody and brought before the new queen of the Empire of Ice, who was known for her ruthless and cruel nature.\n\n{bulletpoint2}As you stood before the queen, you could see the anger and hatred in her eyes. She accused you of being a spy and threatened to have you executed. In that moment, you knew that you had to act quickly if you wanted to save your life.\n\n')
                            input(f'{bulletpoint2}You pleaded with the queen, explaining that you were simply curious and wanted to learn more about the world beyond your own land. You begged for her mercy and offered to pay any price she demanded.\n\n{bulletpoint2}But the queen was unmoved by your pleas. She sneered at you and ordered her guards to take you to the gallows to be hanged!\n')
                            gamble_life = True
                            if current_emperor.strip().lower() == hero.name.strip().lower():
                                input(f'\n{bulletpoint2}The queen all of a sudden shouted "HALT!"')
                                input(f'{bulletpoint2}She says she just discovered from her spies that you\'re the real emperor of the Red Dragon Empire.\nShe then says "Your presence in my kingdom was a threat to my rule and the safety of my people. Now, you will pay the price for your deception and your treachery. You may be the Red Dragon Emperor, but in my Empire of Ice, you are nothing but a common traitor. May your death serve as a warning to all who would dare to challenge my authority."')
                                print("""
                                    |\|
                                    |\|
                                    |\|
                                    |\|
                                    |\|
                                    |\|
                                    |_| 
                                    (___)
                                    (___)
                                    (___)
                                    (___)
                                    (___)
                                    (___)
                                ,(/   \),
                                ('/     \\')
                                ('/       \\')
                                |/|       |/|
                                |/|       |/|
                                |/|       |/|
                                (-\       /-)
                                \-\     /-/
                                \-\___/-/ 
                                '-----'
                                """)
                                input(
                            f'\n{bulletpoint2}You\'ve reached a bad ending!')
                                ending(ending26)
                                hero.health = 0
                                check_health(hero)
                            else:
                                hangman()
                                input(f'{bulletpoint2}You were allowed to leave the Empire of Ice unharmed. It was a harsh lesson, but one that you would never forget. The world was a dangerous place and your would have to be cautious and wise in your dealings with other kingdoms if you wanted to rule the Red Dragon Empire with honor and dignity.\n')
                                input(
                                    f'{bulletpoint2}You were granted a boat with free passage to leave the kingdom, and you sailed off back to the Red Dragon Empire.')
                                menu()
                                trade_mission()
                else:
                    if victory == 'red':
                        ice_aftermath()
                    else:
                        input(f'\n{bulletpoint2}After many days of travel, you finally arrive at the gates of the {current_kingdom_name}.\n\nThe guard stops you and asks for your license to pass. Since you don\'t have one, the guard says she can let you through if you answer her riddle correctly...\n')
                        # List of riddles
                        riddles = [
                            "\nI'm cold and white, and I'm found in the sky. I'm used for sports, and I'm thrown in the air. What am I?",
                            "\nI'm cold and hard, and I sparkle and shine. I'm used to make ice, and I taste like wine. What am I?",
                            "\nI'm cold and slippery, and I slide on the ground. I'm used for fun, and I make a funny sound. What am I?",
                            "\nI'm cold and wet, and I come from a tap. I'm used to clean, and I'm good for a nap. What am I?",
                            "\nI'm cold and frozen, and I hang from the sky. I'm used for drinks, and I make them cold and dry. What am I?",
                            "\nI'm cold and frozen, and I'm found in a cave. I'm used for drinks, and I'm smooth on the tongue. What am I?",
                            "\nI'm cold and crisp, and I'm good with a beer. I'm used to snack, and I'm salty and clear. What am I?",
                            "\nI'm cold and strong, and I keep you safe at night. I'm used for defense, and I'm made of metal and light. What am I?",
                            "\nI'm cold and soft, and I'm found on your head. I'm used for warmth, and I'm made of fur and thread. What am I?",
                            "\nI'm cold and clear, and I'm frozen in time. I'm used for art, and I make things shine. What am I?"
                        ]

                        # List of answers
                        answers = [
                            "Snowball",
                            "Salt",
                            "Sled",
                            "Water",
                            "Ice Cubes",
                            "Ice Cream",
                            "Pretzel",
                            "Shield",
                            "Hat",
                            "Ice Sculpture"
                        ]

                        # Function to ask a random riddle and check the answer
                        def askRiddle():
                            # Select a random riddle
                            index = random.randint(0, len(riddles) - 1)
                            riddle = riddles[index]
                            answer = answers[index]

                            # Ask the riddle and get the user's answer
                            user_answer = input(f'{bulletpoint}Type "help" for a list of potential answers\n{riddle}\nWhat is your answer: ')

                            # Check if the user's answer is correct
                            if user_answer.lower() == answer.lower():
                                print(f'{bulletpoint2}Correct! You may pass!')
                                pass
                            elif user_answer.lower() == 'help':
                                print(f'{bulletpoint2}Potential Answers:')
                                for i in answers:
                                    print(i)
                                askRiddle()
                            else:
                                print(
                                    f'{bulletpoint2}Incorrect, you may not pass until you answer a riddle correctly.')
                                askRiddle()
                        askRiddle()
                        if icequeen_life == 'alive':
                            input(f'\n{bulletpoint2}The ice kingdom is a breathtaking sight. The city is built of shining white marble and crystal, and it glows with a soft, ethereal light. The streets are filled with people of all shapes and sizes, all dressed in beautiful and colorful clothes.\n\n{bulletpoint2}As you walk through the city, you are amazed by the sights and sounds around you. You see snow-white horses pulling elegant carriages, and you hear the soothing melodies of harps and flutes. You feel a sense of peace and tranquility that you have never experienced before.\n\n{bulletpoint2}You decide to explore the city further and discover its hidden secrets. You visit the palace of the queen, who greets you with kindness and generosity. You learn about the history and culture of the ice kingdom, and you marvel at the wonders of its magical technology.\n')
                        else:
                            input(f'\n{bulletpoint2}The {current_kingdom_name} is a breathtaking sight. The city is built of shining white marble and crystal, and it glows with a soft, ethereal light. The streets are filled with people of all shapes and sizes, all dressed in beautiful and colorful clothes.\n\n{bulletpoint2}As you walk through the city, you are amazed by the sights and sounds around you. You see snow-white horses pulling elegant carriages, and you hear the soothing melodies of harps and flutes. You feel a sense of peace and tranquility that you have never experienced before.\n\n{bulletpoint2}But as you continue to explore the city, you begin to notice signs of unrest and tension. You overhear people talking about the death of the queen, and you hear rumors of a power struggle within the royal family.\n\n{bulletpoint2}You eventually learn that the Ice kingdom is in the process of being usurped by someone in the queen\'s family. The new ruler has declared themselves the emperor of the Ice Kingdom, and they are using their power and authority to oppress the people and crush any opposition.\n\n{bulletpoint2}You are shocked and dismayed by this turn of events. The Ice kingdom was a place of beauty and wonder, but it has now been corrupted and transformed into the Empire of Ice.')
                        go_sailing = input(
                            f'\n{bulletpoint}You see an opportunity to hike a ride on a ship sailing over to the Red Dragon Empire, do you go?\n')
                        if go_sailing.strip().lower() in yes:
                            menu()
                            trade_mission()
                        else:
                            pass
                        # Only accesses the vendor lady scenario if it's been turned on.
                        if vendor_lady_object == 1:
                            vendor_lady()
                        else:
                            input(f'\n{bulletpoint2}As you stand in the {current_kingdom_name}, you gaze upon the majestic high mountain next to it. The mountain is covered in snow and ice, and it towers above the surrounding landscape.\n\n{bulletpoint2}You feel a sudden urge to climb to the highest peak of the mountain. You have never done anything like this before, but you are excited by the challenge and the thrill of the climb.\n\n{bulletpoint2}You gather your gear and supplies, and you set off on your journey. You trudge through the snow, making your way up the mountain. The air is cold and thin, and you feel the strain on your body as you climb higher and higher.\n\n{bulletpoint2}As you reach the higher elevations, you encounter treacherous ice and snow. You must use your climbing skills and your determination to overcome these obstacles.\n\n{bulletpoint2}Finally, after many hours of grueling climb, you reach the summit of the mountain. You are exhausted and exhilarated at the same time. You look out at the stunning view from the top of the mountain, and you feel a sense of accomplishment and pride.\n')
                            mountain_secret()

            # The Forest
            def the_forest():
                ascii_waterfall = '''
                                                                         ---\=,__,>,_`-.     |
                        :  |  `"""V#######,,_ `-  ""##################' --z--;" /_/  `. `.   |
                           |          `/"""".`|`|| } }|.""""""""|"""""  --'//`/'  `    \  '. |
                     :          :      |:     ||   |  |  :   :  |   :   ,_\---_\._   :  `.\ |/
                                    :  /  :   |  |   || :  :      :    //--'> ___ ``-,_   \  \\
                          `"^            :  ` ||   || |   :  :         '=-`',' / `-, __`-. |
                       :    :          : :  : |  |    ||    :     ---  //7;<\     / ,--._ ` |
                          .,      :        :  |   ||| || '       :     -/;\\'/` -='/|(    \ \\
                         %#'            :    `| |||    |  :   :      :  // '\   // | `    | |
                     :         :   `'   :  :  || # | |||    :            `    .        :  | 
                                          :   | ||#|#| | ':    :    :             :       ` 
                          '#"      :   :    : | ||,|, ||   :      /        :           |:  ||
                   ""'                    :  \\\\|\ X XX///`      :|   :    |   :      : |   |
                '''
                forest_ans = input(f'\n{bulletpoint}As you travel through the mysterious forest, you are struck by its beauty and serenity. The trees are tall and majestic, and the air is fresh and clean. You feel a sense of peace and calm as you walk along the forest path.\n\n{bulletpoint2}But you also feel a sense of curiosity and wonder. The forest is filled with strange and exotic plants and animals, and you have never seen anything like them before. You are amazed by the diversity and beauty of the forest, and you cannot help but explore and learn more.\n\n{bulletpoint2}Suddenly, you come across a fork in the path. One path leads to the left, and the other to the right. You are unsure which way to go, and you stop to think. If you choose to take the path on the left, you continue on your journey through the forest and pass by a pond. If you choose to take the path on the right, you pass through a cave. Do you choose the pond route?\n')
                if forest_ans.lower().strip() in yes:
                    input(f'\n{bulletpoint2}You come across a small pond, where you see a family of ducks swimming and playing. You are charmed by their playful antics, and you cannot help but watch them for a while. You eventually come across an ancient waterfall. You are struck by its beauty and majesty, and you cannot help but admire it for a while.\n')
                    input(ascii_waterfall)
                    menu()
                else:
                    damage = random.randint(3, 20)
                    hero.health -= damage
                    input(f'\n{bulletpoint2}You come across a dark and foreboding cave, and you feel a sense of danger and excitement. You decide to enter the cave, and you find yourself in a beautiful and hidden underground world. You are amazed by the beauty and wonder of this hidden place, and you cannot help but explore but you accidently trip and cut yourself and take {damage} damage to your health.\n\n{bulletpoint2}You decided to get back on track and eventually came across an ancient waterfall. You are struck by its beauty and majesty, and you cannot help but admire it for a while.\n')
                    input(ascii_waterfall)
                    menu()
                
                # Ancient Waterfall
                input(f'\n{bulletpoint2}The waterfall is breathtaking, with its powerful and majestic flow of water. You are drawn to the waterfall and you approach it with awe and wonder. As you get closer to the waterfall, you notice ancient markings on the rocks around it. The markings are faint and worn, but you can still make out the symbols and images of an ancient civilization.\n\n{bulletpoint2}You are intrigued by the ancient markings, and you decide to study and decipher them. You spend hours examining the markings and trying to understand their meaning.\n\n{bulletpoint2}You learn that the markings are the remnants of an ancient and advanced civilization that once existed in the forest. The civilization was wiped from existence by a great disaster, and only the markings on the rocks remain to tell its story.\n\n{bulletpoint2}You are filled with wonder and amazement by your discovery. You feel a sense of connection to the ancient civilization, and appreciate the opportunity to learn about its history and culture.\n')
                waterfall_monster = input(f'\n{bulletpoint}you hear a deep and growling voice. You turn a corner, and you see a monstrous creature standing before you. It is a Minotaur, a creature with the body of a man and the head of a bull. The Minotaur roars at you, and charges towards you. You are terrified, but you also feel a sense of excitement and adrenaline. Do you fight this monster?\n')
                if waterfall_monster.lower().strip() in yes:
                    # Adds monster health if it has already been killed.
                    add_health(minotaur)
                    battle(hero, minotaur, 'lowers its head',
                           'pants heavily', 'raises horns', 'charges with horns')
                    random_health_gain = random.randint(10, 30)
                    print(
                        f'{bulletpoint2} You took some rest and gained {random_health_gain} health back.')
                    hero.health += random_health_gain
                    check_health(hero)
                    add_money(50, 150)
                    menu()
                    input(f'\n{bulletpoint2}After a long and fierce battle, you finally manage to defeat the Minotaur. The creature falls to the ground, and you stand victorious. You are exhausted and battered, but you are also proud and triumphant.')
                    input(f'\n{bulletpoint}As you leave the ancient waterfall, you continue on your journey through the forest. The sun is shining, and the birds are singing, and you feel a sense of joy and adventure.\n\n{bulletpoint2}But as you walk, you notice that the air is getting colder and colder. The trees are starting to look more and more frosted, and the ground is covered in snow. You realize that you are entering a new and different part of the forest.\n\n{bulletpoint2}As you continue on your journey, you see a vast and frozen landscape in front of you. The snow is deep and white, and the ice is sparkling and blue. You see tall and majestic mountains in the distance, and you feel a sense of awe and wonder.\n\n{bulletpoint2}You realize that you have entered the {current_kingdom_name}. You are amazed by the beauty and majesty of this frozen land, and you cannot help but explore and learn more.\n\n{bulletpoint2}You continue on your journey, marveling at the ice sculptures and frozen lakes. You see animals that you have never seen before, and you hear music and laughter from hidden villages.\n')
                    ice_kingdom()
                else:
                    input(f'\n{bulletpoint}As you leave the ancient waterfall, you continue on your journey through the forest. The sun is shining, and the birds are singing, and you feel a sense of joy and adventure.\n\n{bulletpoint2}But as you walk, you notice that the air is getting colder and colder. The trees are starting to look more and more frosted, and the ground is covered in snow. You realize that you are entering a new and different part of the forest.\n\n{bulletpoint2}As you continue on your journey, you see a vast and frozen landscape in front of you. The snow is deep and white, and the ice is sparkling and blue. You see tall and majestic mountains in the distance, and you feel a sense of awe and wonder.\n\n{bulletpoint2}You realize that you have entered the {current_kingdom_name}. You are amazed by the beauty and majesty of this frozen land, and you cannot help but explore and learn more.\n\n{bulletpoint2}You continue on your journey, marveling at the ice sculptures and frozen lakes. You see animals that you have never seen before, and you hear music and laughter from hidden villages.')
                    ice_kingdom()
                
            def the_marriage():
                nonlocal current_heir, new_rank
                noble_lady_features = ['intelligence and wit', 'nice hair and eyes', 'grace and poise', 'beauty and charm', 'strength and courage', 'kindness and compassion', 'dignity and honor', 'intelligence and charm', 'elegance and sophistication', 'wisdom and foresight', 'generosity and charity', 'honesty and integrity', 'humility and modesty', 'humor and wit']
                random_noble_feature = random.choice(noble_lady_features)
                noble_quote = ["I have never felt this way about anyone before. I think I am falling in love with you.", "I don't know what it is about you, but you make my heart skip a beat.", "You are the most amazing person I have ever met.", "I can't imagine spending my life with anyone else but you.", "I want to spend every waking moment with you and make a lifetime of memories together.", "Will you be my partner in crime and make all of my dreams come true?", "I love you more than words can express.", "You make me feel like the most special person in the world.", "I can't wait to start our lives together and make our own happily ever after.", "I never thought I would find someone who makes me laugh as much as you do, and I want to be with you forever."]
                random_noble_quote = random.choice(noble_quote)
                marriage_ans = input(f'\n{bulletpoint}As you walk down the castle hallway of the Red Dragon empire, you see a noble standing by a window, looking out at the sunset. You are immediately drawn to her beauty and grace. She turns to you and smiles, and you feel a spark of attraction.\n\n{bulletpoint2}You introduce yourself and think she is a noble from a nearby kingdom. You chat for a while, and you find yourself drawn to her {random_noble_feature}.\n\n{bulletpoint2}As the days pass, you spend more and more time together. You go for walks in the castle gardens, and share meals in the great hall. You find yourself falling more and more in love with her, and you know that she feels the same way.\n\n{bulletpoint2}One evening, as you sit by the fire in the great hall, She turns to you and says, "{random_noble_quote}"\n\n{bulletpoint2}You are overjoyed, and you know that you feel the same way.\n{bulletpoint}You take her hand... Do you decide to propose marriage to her?\n')
                if marriage_ans.strip().lower() in yes:
                    input(f'\n{bulletpoint2}You ask her if she will do you the honor of becoming your wife? She looks at you with tears in her eyes, and says, yes, she will marry you. And so, you become engaged, and begin planning for your future together. You know that no matter what challenges you face, you will face them together, as husband and wife. But little did you know, The noble was actually the Red Dragon emperor\'s daughter. You had fallen in love with the emperor\'s daughter without even realizing it. As you plan your future together, you must decide whether you are willing to marry into the royal family and face the challenges that come with it.')
                    input(f'\n\n{bulletpoint2}the emperor asks you to marry his daughter, a beautiful and noble young woman. You are hesitant at first, but you are drawn to the princess and you decide to accept the emperor\'s offer.\n\n{bulletpoint2}You marry the princess in a grand and lavish ceremony, attended by the nobles and dignitaries of the empire. You are given a title and a position of power and influence in the empire, and you are now a respected and honored member of the royal family.\n\n{bulletpoint2}As the husband of the princess, you live a life of luxury and privilege. You are surrounded by wealth and beauty, and you have everything you could ever want. But you also face challenges and dangers. The nobles and courtiers of the empire are jealous and resentful of your position, and they plot and scheme against you. You must be careful and cautious, and always be on your guard.\n\n{bulletpoint2}Despite the challenges, you are happy and content in your new life. You love your wife and you are grateful for the opportunities and experiences that the empire has given you. You vow to always protect and serve the empire and its people, and to make your marriage a success.')
                    current_heir = hero_name.title()
                    ending(ending7)
                    menu()
                    mysterious_monk()
                else:
                    if icequeen_life == 'dead':
                        if current_emperor.strip().lower() != hero.name.strip().lower():
                            input(f'\n{bulletpoint2}You become a skilled and accomplished warrior, and you earn the respect and admiration of the people of the empire. You become a favorite of the emperor, who rewards you with wealth and privilege.\n\n{bulletpoint2}The emperor is impressed by your skills and loyalty, and he offers you a position as his right-hand man. You decide to accept the emperor\'s offer.\nAs the right-hand man to the emperor, you are given a position of great power and influence in the empire. You are responsible for advising the emperor and carrying out his orders. You are also tasked with protecting the emperor and the empire from threats and dangers.\n\n{bulletpoint2}Your new position is challenging and demanding, but also rewarding and fulfilling. You use your skills and knowledge to serve the emperor and the empire, and you are praised and rewarded for your efforts.\n\n{bulletpoint2}However, you also face challenges and dangers. The nobles and courtiers of the empire are jealous and resentful of your position, and they plot and scheme against you. You must be careful and cautious, and always be on your guard.\n\n{bulletpoint2}Despite the challenges, you are happy and content in your new life. You are proud to serve the emperor and the empire, and you are grateful for the opportunities and experiences that the empire has given you. You vow to always protect and serve the empire and its people, and to make your new position a success.')
                            new_rank = ranks[-1]
                            ending(ending8)
                    input(f'{bulletpoint2}Instead of marriage, you\'ve both decided it was best to remain good friends. You decided to take a walk outside and help out a {new_monk_replacement} that needed some assistance.')
                    menu()
                    mysterious_monk()
                    
            # Kill Best Friend
            def kill_best_friend():
                input(f'\n{bulletpoint2}As you walk up to your best friend\'s house, you feel a heavy weight in your chest. You have never felt so torn in your life. On the one hand, you are loyal to the Red Dragon empire and you don\'t want to disappoint them. On the other hand, you cannot imagine a world without your best friend. You have known him for so long, and you have been through so much together.\n\n{bulletpoint2}You knock on the door, and your friend answers. He looks happy to see you, as always. But as you step inside, you know that you have to do what the empire has asked of you. You have to kill him.\n\n{bulletpoint2}You try to convince yourself that it is for the greater good, that the empire needs you to do this in order to maintain its power and control. But deep down, you know that it is wrong.\n\n{bulletpoint2}As you sit down in the living room and start to chat, you can feel your heart pounding in your chest. You know that you have to act fast, before you lose your nerve. You reach for your concealed knife, and before your friend knows what is happening, you plunge it into his chest.\n\n{bulletpoint2}The shock and betrayal on his face is something that you will never forget. You watch as the light in his eyes fades away, and you know that you have done the unthinkable. You have killed your best friend, and there is no going back.\n\n{bulletpoint2}You flee the scene, knowing that you have to report back to the empire and face the consequences of your actions. You have betrayed your friend and your own morals, and you know that you will have to live with that guilt for the rest of your life.\n')
                add_money(50, 200)
                if noble_life == 'alive':
                    bf_ans = input(f'\n{bulletpoint}After the deed was done you travel into the castle to collect your earnings. You meet an attractive noble inside the castle hallway, but you also see a hidden entrance in the hallway. Do you decide to speak with the noble?')
                    if bf_ans.strip().lower() in yes:
                        menu()
                        the_marriage()
                    else:
                        menu()
                        passageway()
                else:
                    input(
                        f'{bulletpoint2}After the deed was done you travel into the castle to collect your earnings. You happen to a hidden entrance in the hallway and decide to enter it.')
                    menu()
                    passageway()

            # The Secret Job
            def secret_job():
                kill_friend_ans = input(
                    f'\n{bulletpoint2}You are standing in front of the Red Dragon Empire\'s palace, staring at the imposing stone walls and the flags fluttering in the wind. Suddenly, a hooded messenger approaches you and hands you a scroll. The Red Dragon Empire has asked you to kill your best friend. You are horrified by the empire\'s request. You cannot imagine a world without your best friend.\n{bulletpoint2}Do you kill your best friend?')
                if kill_friend_ans.strip().lower() in yes:
                    menu()
                    kill_best_friend()
                else:
                    if noble_life == 'alive':
                        marriage_ans = input(f'\n{bulletpoint2}The hooded messenger says very well, The empire has offered you an alternative. If you agree to marry one of the empire\'s nobles, your friend will be spared. You are torn by the decision. On the one hand, you do not want to marry someone you do not love. On the other hand, you cannot bear the thought of losing your best friend.\n{bulletpoint}Do you decide to get married to this noble?')
                        if marriage_ans.strip().lower() in yes:
                            input(f'\n{bulletpoint2}After much contemplation, you decide that your friendship is more important than your own happiness. You agree to marry the noble to save your best friend\'s life.\n')
                            menu()
                            the_marriage()
                        else:
                            input(f'\n{bulletpoint2}So you don\'t want to kill your best friend and you don\'t want to marry a noble. The empire has instead forced you to go on a task to destroy a mysterious secret. The hooded messenger has guards escort you in a cart. You look next to you and see a mysterious {new_monk_replacement} as one of the passengers who is joining you on this task.\n')
                            menu()
                            the_secret()
                    else:
                        input(f'\n{bulletpoint2}So you don\'t want to kill your best friend. The empire has instead forced you to go on a task to destroy a mysterious secret. The hooded messenger has guards escort you in a cart. You look next to you and see a mysterious {new_monk_replacement} as one of the passengers who would be joining you on this task.\n')
                        menu()
                        the_secret()

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
                snow_castle = '              🎄🎄⛰⛰⁣⛰⁣🏰⛰⛰⛰🎄🎄                    '
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
                sea_start = [clouds1, ' '*20 + '༌ ⭒༌', ship_castle, ship_trees, ship_boat,
                            ship_ocean, ship_ocean, ship_ocean]

                sea_top_left = [clouds2, ' '*22 + '༌ ⭒༌', ship_boat, ship_fish,
                                ship_ocean, ship_ocean, ship_ocean]

                sea_left_2 = [clouds4, ' '*24 + '༌ ⭒༌', ship_boat, ship_ocean,
                            ship_fish, ship_ocean, ship_ocean]

                sea_left_3 = [clouds4, ' '*26 + '༌ ⭒༌', ship_boat, ship_ocean,  
                            ship_ocean, ship_fish, ship_ocean, ship_island]

                sea_island = [clouds4, ' '*26 + '༌ ⭒༌',
                            ship_ocean, ship_ocean, ship_ocean, ship_boat, ship_island] 

                sea_island_south = [clouds2, ' '*26 + '༌ ⭒༌', ship_boat, ship_ocean,
                                    ship_ocean, ship_fish, ship_ocean, ship_ocean] 

                sea_island_south1 = [clouds3, ' '*26 + '༌ ⭒༌', ship_ocean, ship_boat, 
                                    ship_ocean, ship_fish, ship_ocean, ship_ocean]

                sea_island_south2 = [clouds4, ' '*26 + '༌ ⭒༌',  ship_ocean, ship_ocean, 
                                    ship_boat, ship_fish, ship_ocean, ship_ocean]

                new_colony = [clouds4, ' '*26 + '༌ ⭒༌',
                              ship_ocean, ship_ocean, ship_ocean, ship_boat, palm_trees] # same

                sea_left_4 = [clouds4, ' '*28 + '༌ ⭒༌', ship_boat, ship_ocean,
                            ship_ocean, ship_fish, ship_ocean, ship_ocean]
                sea_left_5 = [night1, ' '*30 + '༌ ⭒༌', ship_boat, ship_ocean,
                            ship_ocean, ship_fish, ship_ocean, ship_ocean]
                sea_left_6 = [night2, ' '*32 + '༌ ⭒༌', ship_boat, ship_ocean,
                            ship_ocean, ship_fish, ship_ocean, ship_ocean]
                sea_left_7 = [night3, ' '*34 + '༌ ⭑༌༌', ship_boat, ship_ocean, # Different stars as another clue for navigating to the secret island
                            ship_ocean, ship_fish, ship_ocean, ship_ocean]
                sea_left_8 = [night4, ' '*36 + '༌ ⭒༌', ship_boat, ship_ocean,
                            ship_ocean, ship_fish, ship_ocean, ship_ocean]
                ice_castle = [night4, ' '*38+ '༌ ⭒༌', snow_castle, xmas_trees, ship_boat,
                            ship_ocean, ship_ocean, ship_ocean]
                ship_surf = [night4, ' '*40 + '༌ ⭒༌', snow_castle, xmas_trees, ship_surf,
                            ship_ocean, ship_ocean, ship_ocean]

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
                claimed_land = 1
                #Island Trade Menu
                def land_trade(land_emote, land_dict, item1, item2, item3):
                    nonlocal claimed_land
                    input('Press enter to continue...')
                    open_seas(land_emote) # Displaying the area
                    trade_count = 1
                    while trade_count > 0: # Start of the while loop
                        print(
                            f'\n{bulletpoint2}Local Shop Items for Trade ($100 each):')
                        print([(k, land_dict[k]) for k in land_dict]) # Displaying the Key and Value for the Trade items available.
                        #Player can enter the key string to purchase the value which is an emote of the item.
                        if current_position == new_colony:
                            if claimed_land == 1:
                                print(f'{bulletpoint2}You can try to claim this new continent.')
                            else:
                                print(f'{bulletpoint2}You\'ve claimed this land as your new home.')
                        buy_land = input(
                            f'{bulletpoint2}Current Money: ${hero.money}\n{bulletpoint}Please enter the number for the local item you wish to purchase ({item1}, {item2}, {item3}):\n{bulletpoint2}Type "exit" to exit the menu.\n{bulletpoint}What would you like to do:')
                        print(f'{bulletpoint2}Current Trade Items Held: {hero_land_items}') # Displaying currently held trade items.
                        if buy_land.lower() == 'exit': #Player can exit the menu by typing exit.
                            trade_count -= 1 # Ends the while loop.
                        elif buy_land.lower() == 'claim' or buy_land.lower() == 'claim it':
                            if current_position == new_colony:
                                if claimed_land > 0:
                                    input(f'\n{bulletpoint2}You have decided to embark on a journey to take over a mysterious jungle continent in the south. After months of sailing, you and your crew finally reach the shores of the continent and make your way inland. The jungle is dense and teeming with life, and you soon come across towering mountains and a massive volcano.\n\n{bulletpoint2}As you continue deeper into the jungle, you come across a mysterious abandoned temple and city. The city is in ruins, and it appears that it has been abandoned for many years. Despite this, you are struck by the advanced architecture and impressive stonework of the temple and city.\n\n{bulletpoint2}As you explore the temple, you come across a strange sight. Lava flowing through the temple, creating a surreal and otherworldly atmosphere. You realize that this must be a powerful and sacred place, and you decide to claim it as your new home.\n\n{bulletpoint2}You order your crew to set up camp and begin to explore the city, looking for any clues as to what may have happened to the previous inhabitants. You also send out scouts to explore the surrounding area and see if there are any other civilizations nearby.\n\n{bulletpoint2}As you explore the temple and city, you are filled with a sense of excitement and adventure. You have claimed new land and you are determined to make this new home a thriving and prosperous one!\n')
                                    # Set the claimed_land variable to be 0 to indicate that land has been claimed
                                    claimed_land = 0
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
                    f'{bulletpoint2}You stop by the trade port near the shipyard. The trader needs one of each of these two items ({new_requirement} and {new_requirement2}). If you can acquire them on your journey, you shall be awarded. Note that these items may change due to demand, so it\'s best to stock up on local items.')
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
                        input(f'{bulletpoint2}The trader thanks you for your help and gives you a nice chunk of change!')
                        add_money(500, 1500)
                    else:
                        pass
                set_sail = input(f'{bulletpoint}Would you like to set sail?')
                if set_sail.strip().lower() in yes:
                    pass
                else:
                    input(f'{bulletpoint2}As you leave the bustling trade port and set off on the road back home, you feel a sense of relief and excitement. You have been away for many weeks, and you are eager to see your loved ones again. As you travel down the road, you notice a beggar sitting on the side of the road.')
                    beggar()

                # The below code displays a ship for the player to travel between two different kingdoms.
                while anchor:
                    open_seas(current_position) #opening the first starting scene.
                    if (current_position in land) and (start_count != 0):
                        land_command = input(
                            f'\n{bulletpoint}Would you like to anchor the ship?\n')
                        if land_command in directions:
                            command = land_command
                    else:
                        # If current position is in the storm, the below question will not be asked.
                        if current_position in seastorm:
                            pass
                        else:
                            command = input(
                                f'\n{bulletpoint}Which direction would you like to steer the ship? (north, west, east, south)\n\n')
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
                                beggar()
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
                                          'grapes', 'coffee', 'corn')
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
                                        '\nIt\'s too stormy in these waters, we should steer in a different direction...')
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
                                    f'{bulletpoint2}Current Position: {current_kingdom_name}')
                                print(
                                    f'{bulletpoint2}You reached the destination!')
                                anchor = False # Ends the while loop
                                add_health(leviathan) # Resets leviathan monster health if it has already been killed
                                ice_kingdom()
                            elif command == 'south':
                                current_position = sea_left_8
                            else:
                                current_position = sea_dark
                        elif current_position == sea_dark: # 1st stormy area if player travels outside of the preferred path
                            if saved_direction == 'north':
                                print('\n')
                                open_seas(sea_dark)
                                stormcommand = input(
                                    f'{bulletpoint}Which direction would you like to steer the ship? (north, west, east, south)\n')
                                if stormcommand == 'south':
                                    current_position = previous_position
                                else:
                                    open_seas(sea_stormy) # This is the 2nd stormy area that will teleport the player back to the previous scene, as they have strayed too far away.
                                    input(
                                        '\nIt\'s too stormy in these waters, we should steer in a different direction...')
                                current_position = previous_position
                            elif saved_direction == 'south':
                                open_seas(sea_dark)
                                stormcommand = input(
                                    f'\n{bulletpoint}Which direction would you like to steer the ship? (north, west, east, south)\n')
                                if stormcommand == 'north':
                                    current_position = previous_position
                                else:
                                    open_seas(sea_stormy)
                                    input(
                                        '\nIt\'s too stormy in these waters, we should steer in a different direction...\n')
                                current_position = previous_position
                            elif saved_direction == 'west':
                                open_seas(sea_dark)
                                stormcommand = input(
                                    f'{bulletpoint}Which direction would you like to steer the ship? (north, west, east, south)\n')
                                if stormcommand == 'east':
                                    current_position = previous_position
                                else:
                                    open_seas(sea_stormy)
                                    input(
                                        '\nIt\'s too stormy in these waters, we should steer in a different direction...\n')
                                current_position = previous_position
                            elif saved_direction == 'east':
                                open_seas(sea_dark)
                                stormcommand = input(
                                    f'{bulletpoint}Which direction would you like to steer the ship? (north, west, east, south)\n')
                                if stormcommand == 'west':
                                    current_position = previous_position
                                else:
                                    open_seas(sea_stormy)
                                    input(
                                        '\nIt\'s too stormy in these waters, we should steer in a different direction...\n')
                                current_position = previous_position
                            else:
                                open_seas(sea_stormy)
                                input(
                                    '\nIt\'s too stormy in these waters, we should steer in a different direction...\n')
                                current_position = previous_position
                    else:
                        print('Your input is not valid. Please try again.') # Player did not type a correct cardinal direction or yes/no.

            # Empire Recruitment
            def empire_recruitment():
                global ranks, new_rank
                input('''
                                   (   .                   _ _ _ _ _
                    (   .     .  .=##                      ]-I-I-I-[                    /
                  .=##   .  (      ( .                     \ `  ' /        \\\\\\' ,      / //
                    ( .   .=##  .       .                   |'  []          \\\\\//    _/ //'
                  .     .   ( .    .        _----|          |.  '|           \_-//' /  //<'
                                             ----|_----|    | ' .|             \ ///  >   \\\\\`
                    ]-I-I-I-I-[       ----|      |     |    |. ` |            /,)-^>>  _\`
                     \ `   '_/            |     / \    |    | /^\|            (/   \\\\ / \\\\\\
                      []  `__|            ^    / ^ \   ^    | |*||                  //  //\\\\\\
                      |__   ,|           / \  / ^ ^`\ / \   | ===|                 ((`
                   ___| ___ ,|__        / ^  /=_=_=_=\ ^ \  |, `_|
                   I_I__I_I__I_I       (====(_________)_^___|____|____                 
                   \-\--|-|--/-/       |     I  [ ]__I I_I__|____I_I_|                     
                    |[] `    '|__   _  |_   _|`__  ._[  _-\--|-|--/-/                      
                   / \  [] ` .|  |-| |-| |-| |_| |_| |_| | []   [] |                
                  <===>    `  |.            .      .     |    '    |
                  ] []|  `    |   []    --   []      `   |   [] '  |
                  <===>.  `   |  .   '  .       '  .[]   | '       |             
                   \_/    .   |       .       '          |   `  [] |           
                    | []    . |   .  .           ,  .    | ,    .  |                   
                    |    . '  |       . []  '            |    []'  |
                   / \   ..   |  `      .    .     `[]   | -   `   |                     
                  <===>      .|=-=-=-=-=-=-=-=-=-=-=-=-=-|    .   / \                   
                  ] []|` ` [] |`  .  .   _________   .   |-      <===>            
                  <===>  `  ' | '   |||  |       |  |||  |  []   <===>                      
                   \_/     -- |   . |||  |       |  |||  | .  '   \_/                     
                  ./|' . . . .|. . .||||/|_______|\|||| /|. . . . .|\_
                ''')
                # list of random ranks that can be offered to the player.
                ranks = [
                    'Stable sweep', 'Swordsman', 'Axeman', 'Spearman', 'Archer', 'Cavalry', 'Lieutenant', 'Captain', 
                    'Knight', 'Commander', 'Baron', 'Viscount', 'Earl', 'Marquis', 'Duke', 'Right Hand'
                ]
                empire_recruitment_ans = input(f'\n{bulletpoint} An old guard walks up to you and says they\'re seeking out some new blood into their ranks. Would you be interested in joining the Red Dragon Military?')
                if new_rank in ranks: # Checks if the player already has a rank in the ranks list.
                    input( # If the player already has a rank, they can still roll against the old guard to compare intelligence levels.
                        f'{bulletpoint}It seems that you\'ve already been employed in the Red Dragon Military as {new_rank} {hero_name}. You can still roll from 0 to 10 to see if you have a higher intelligence level than the old guard. Press enter to roll...')
                    ascii_dice()
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
                        ascii_dice()
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
                    input('''
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀
                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⡀⠀⠀⠀⠀⠀⢺⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀
                     ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡇⠀⠀⠀⠀⣠⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
                     ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⢁⣤⣤⣤⣴⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                     ⠀⠀⠀⠀⣠⣾⣿⣷⣀⠙⢉⣠⣾⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                     ⠀⠀⣴⣾⣿⡿⢿⣿⣿⣿⣿⣿⣿⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                     ⠀⠀⣿⡟⠉⠀⠘⣿⣿⣿⣿⣿⣿⠇⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                     ⠀⠀⣿⡇⠀⠀⠀⢿⣿⣿⣿⣿⣿⣠⣴⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
                     ⠀⠀⣿⣷⣄⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⡿⠋⠙⢿⣿⣦⣴⣶⡷⠀⠀⠀⠀⠀
                     ⠀⠀⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠹⣿⠟⠁⠀⠀⡀⠀⠀⠀
                     ⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⣀⣶⣼⣿⠀⠀⠀
                     ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠋⠀⠀⠀
                     ⠀⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⠀⠀⠀⠀
                     ⠀⠀⠀⠀⢀⣤⣤⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⢿⡀⠀⠀⠀
                     ⠀⠀⠀⠀⠙⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠀⠈⠃⠀⠀⠀
                    ''')
                    add_health(giant) # Adds monster health if it has already been killed.
                    battle(hero, giant, 'raises left arm',
                           'breaths heavily', 'makes angry face', 'raises right arm')
                    print(f'\n{bulletpoint2}You won! The empire was very impressed with your ability.')
                    rank_promo()
                    random_health_gain = random.randint(10,30)
                    print(
                        f'{bulletpoint2} You took some rest and gained {random_health_gain} health back.')
                    hero.health += random_health_gain
                    check_health(hero)
                    add_money(50, 200)
                    menu()
                    secret_job()

                else:
                    if emperor_life == 'alive':
                        if icequeen_life == 'dead':
                            if new_rank in ranks[8:]:
                                attack_kingdom_ans = input(f'\n{bulletpoint2}As a {new_rank} of the Red Dragon Empire, you were offered the opportunity to partake in a special assignment by the emperor himself.\n\n{bulletpoint2}He told you that the Ice Kingdom\'s queen had recently passed away, leaving the kingdom vulnerable to attack.\nThe emperor then asked if you would be willing to lead his entire army in a surprise attack?\n{bulletpoint}What do you say?')
                                if attack_kingdom_ans.strip().lower() in yes:
                                    menu()
                                    battlefield()
                                else:
                                    input(f'\n{bulletpoint2}You decided to prove your loyalty instead by taking on an imperial trade assignment and sail the seas.\nYou were tasked with a mission to find the shortest sea path to the {current_kingdom_name}.\n\n{bulletpoint2}The emperor will also be joining on the trip so it\'s best to showcase your ability to navigate the seas!')
                                    menu()
                                    trade_mission()
                            else:
                                input(f'\n{bulletpoint2}You decided to prove your loyalty instead by taking on an imperial trade assignment and sail the seas.\nYou were tasked with a mission to capture the Leviathan monster somewhere in the stormy seas\n\n{bulletpoint2}The emperor will also be joining on the trip so it\'s best to showcase your ability to navigate the seas!')
                                menu()
                                trade_mission()
                        else:
                            input(f'\n{bulletpoint2}You decided to prove your loyalty instead by taking on an imperial trade assignment and sail the seas.\nYou were tasked with a mission to locate Sea Island in the west and trade some imperial goods.\n\n{bulletpoint2}The emperor will also be joining on the trip so it\'s best to showcase your ability to navigate the seas!')
                            menu()
                            trade_mission()
                    else:
                        input(f'\n{bulletpoint2}You decided to prove your loyalty instead by taking on an imperial trade assignment and sail the seas. You were tasked with a mission to locate Sea Storm Island in the west and trade some imperial goods. Since the emperor is dead, it\'s best to showcase your ability to the new ruler and navigate the seas!')
                        menu()
                        trade_mission()

            # The Secret
            def the_secret():
                desert_ans = input(f'\n{bulletpoint}In the mountains at the highest peak, there lies a secret. You must retrieve this secret but you may never open it...\nYou lead the {new_monk_replacement} to the borders of the empire. You see a vast never ending desert, and the map shows that\'s the quickest route. There is another longer route through the forest. \nDo you take the desert route?')
                if desert_ans.strip().lower() in yes or desert_ans.strip().lower() == 'desert':
                    input('''
                        .    _    +     .  ______   .          .
                     (      /|\      .    |      \      .   +
                         . |||||     _    | |   | | ||         .
                    .      |||||    | |  _| | | | |_||    .
                       /\  ||||| .  | | |   | |      |       .
                    __||||_|||||____| |_|_____________\__________
                    . |||| |||||  /\   _____      _____  .   .
                      |||| ||||| ||||   .   .  .         ________
                     . \|`-'|||| ||||    __________       .    .
                        \__ |||| ||||      .          .     .
                     __    ||||`-'|||  .       .    __________
                    .    . |||| ___/  ___________             .
                       . _ ||||| . _               .   _________
                    _   ___|||||__  _ \\\\--//    .          _
                         _ `---'    .)=\oo|=(.   _   .   .    .
                    _  ^      .  -    . \.|
                    ''')
                    print(f'\n{bulletpoint2}As you and the {new_monk_replacement} struggle through the blazing heat. You both hear a roaring rumble underneath your feet...') 
                    menu()
                else:
                    print('You decided to take the forest route.')
                    the_forest()

            # Sand Monster Battle
                add_health(sandworm) # Adds monster health if it has already been killed.
                sand_monster_ans = input(f'\n{bulletpoint}Suddenly, you see a massive, ancient {sandworm.name} rise up from the sand before you.\nIts thousand year old body towers over you, a monstrous behemoth with thousands of sharp teeth lining all edges of its massive cavernous mouth.\nThe {new_monk_replacement} warns you that this creature is legendary, feared by all who have laid eyes upon it. Do you have the courage to face this terrifying beast?\n')
                if sand_monster_ans.strip().lower() in yes:
                    # Cleaning up the hero item strings to play be displayed properly
                    clean_hero_items = ', '.join(
                        [f'{letter}' for letter in hero_items])
                    sand_monster_weapon = input(
                        f'\n{bulletpoint}The {new_monk_replacement} asks you what weapon you plan to fight this thing when we only have {clean_hero_items}?\nYou respond with "I\'ll just use the..."\n')
                    input(f'\n{bulletpoint2}As you try your plan of attacking with the {sand_monster_weapon}... you utterly failed. The {sandworm.name} then surrounded you with a giant wall of sand, preventing your escape...\n') 
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
                    input(f'\n{bulletpoint2}The monster lunged at you, but the {new_monk_replacement} ran towards you and pushed you away. Sand filled the air making it impossible to see. Once the sand dissipated, you saw a shadow in the midst and the {new_monk_replacement} slowly appeared safe and sound. You both successfully managed to escape! ')

            # Frozen Wasteland
                input(f'\n{bulletpoint2}As you and the {new_monk_replacement} walk out of the scorching desert, the landscape around you begins to change.\n\n{bulletpoint2}The ground beneath your feet grows harder and the air grows colder. Soon, you find yourself trudging through the snow, your breath forming plumes of steam in the frigid air.\n\n{bulletpoint2}The sun is a distant memory, replaced by dark storm clouds that loom overhead. You wrap your coat tighter around yourself and keep moving, your companion by your side.\n\n{bulletpoint2}The frozen wasteland stretches out before you, a vast and unforgiving terrain. But you press on, determined to survive and find your way out of this desolate place.\n')
                frozen_wasteland_ans = input(
                    f'\n{bulletpoint}As you and the {new_monk_replacement} walked through the frozen wasteland, you both could feel the cold seeping into your bones. The air was frigid and biting, and your breath came out in white plumes.\n\n{bulletpoint2}After a long journey, you and your companion finally reach the edge of a massive, frozen lake. In the distance, the towering peak of the mountain you are trying to reach looms over the landscape. But first, you must cross the treacherous ice.\n\n{bulletpoint2}As you take your first steps onto the frozen surface, you can\'t help but feel a sense of excitement and fear. Will you make it across, or will the thin ice give way beneath your feet? Only time will tell.\n\n{bulletpoint}Do you still proceed?\n')
                if frozen_wasteland_ans.strip().lower() in yes:
                    kindness_list = ['brings you a warm blanket', 'made a bed to keep you warm', 'shared their food with you', 'checked on you regularly to make sure you\'re okay', 'shared their water with you', 'teaches you how to start a fire', 'provided emotional support and encouragement', 'stayed by your side through the entire ordeal', 'listened to your life concerns and offers advice throughout the night', 'kept you company and helped you pass the time', 'set a small campfire to keep both of you warm']
                    print('''
                               (                 ,&&&.
                               )                .,.&&
                              (  (              \=__/
                                  )             ,'-'.
                            (    (  ,,      _.__|/ /|
                             ) /\ -((------((_|___/ |
                           (  // | (`'      ((  `'--|
                         _ -.;_/ \\--._      \\ \-._/.
                        (_;-// | \ \-'.\    <_,\_\`--'|
                        ( `.__ _  ___,')      <_,-'__,'
                   jrei  `'(_ )_)(_)_)'
                    ''')
                    random_kindness = random.choice(kindness_list)
                    input(f'\n{bulletpoint2}You both start making your way slowly... you took a tentative step onto the ice, and immediately felt a crack beneath your feet. You both froze, unsure of what to do. The ice beneath you felt thin and brittle, and one wrong move could send you both plunging into the icy waters below.\n\n{bulletpoint2} As you continued the journey across the frozen lake, you stumbled upon a strange metal ship that was partially submerged in the ice. You both decided to camp inside the ship for the night, and the {new_monk_replacement} {random_kindness}.\n')
                    menu()

                    #The Betrayal
                    the_betrayal_ans = input(f'\n{bulletpoint}The next morning, as you both were making your way towards the other side of the lake, the {new_monk_replacement} suddenly fell through the ice. You turned around and saw what had happened, but before you could react, the ice beneath your own feet began to crack and break. Do you save yourself and cross the lake? ')
                    if the_betrayal_ans.strip().lower() in yes:

                        input(f'\n{bulletpoint2}You start sprinting towards the end of the lake and saved yourself. There was no point in attempting to save the {new_monk_replacement}.\n\n{bulletpoint2}As you run, the ice beneath your feet cracks and breaks, but you are able to maintain your balance and keep moving forward. You push yourself to your limits, pouring all your energy into reaching the shore.\n\n{bulletpoint2}Eventually, you reach the end of the lake and scramble onto solid ground. You are cold, wet, and exhausted, but you are alive. You take a moment to catch your breath and look back at the lake, knowing that you have made it through a difficult and dangerous situation.\n\n{bulletpoint2}You feel a sense of regret for leaving the {new_monk_replacement} behind, but you also know that you made the best decision for yourself in the moment. You must now continue on your journey, facing whatever challenges and dangers come your way.\n')
                        menu()
                        mountain_secret()

                    else:
                        if current_heir.strip().lower() == hero.name.strip().lower() or current_emperor.strip().lower() == hero.name.strip().lower():   
                            input(f'\n{bulletpoint2}As the {new_monk_replacement} falls through the ice, you decide to turn back and try to save them. You frantically search for a way to rescue your companion, and eventually, you come up with a plan.\n\n{bulletpoint2}You oversee the red dragon empire, and you have some soldiers at your disposal. You call out to them, and they immediately come to your aid. Together, you manage to find a way to pull the {new_monk_replacement} out of the water and onto solid ground.\n\n{bulletpoint2}The {new_monk_replacement} is cold, wet, and shaken, but they are alive. You quickly make arrangements to have them sent back home to get the medical attention they need. You are relieved that you were able to save your companion, and you are grateful for the help of your soldiers.\n\n{bulletpoint2}You continue on your journey, knowing that you were able to overcome a difficult and dangerous situation. You feel a sense of pride and satisfaction for having saved the {new_monk_replacement}.\n')
                        else:
                            input(f'\n{bulletpoint2}As the {new_monk_replacement} falls through the ice, you decide to turn back and try to save them. But as you do, the ice beneath your feet cracks and breaks, and one of your legs gets caught in the numbing cold water below.\n\n{bulletpoint2}You struggle to free yourself, using all your strength and determination to pull yourself out of the water. Finally, after what feels like an eternity, you manage to pull your leg free and scramble back onto the ice.\n\n{bulletpoint2}But it is too late for the {new_monk_replacement}. They have already fallen through the ice and disappeared beneath the frigid waters. You are alone, stranded on the frozen lake, with no way to save your companion.\n\n{bulletpoint2}You are cold, wet, and exhausted, but you are alive. You take a moment to catch your breath and come to terms with what has happened. You feel a sense of regret for attempting to save the {new_monk_replacement}, but you also know that you did everything you could.\n\n{bulletpoint2}You must now continue on your journey, facing whatever challenges and dangers come your way. You will never forget the {new_monk_replacement}, but you must move forward and keep going, no matter what.')
                        menu()
                        mountain_secret()

                else:
                    if current_heir.strip().lower() == hero.name.strip().lower() or current_emperor.strip().lower() == hero.name.strip().lower():
                        input(f'\n{bulletpoint2}Instead of crossing the lake, you and the {new_monk_replacement} decide to go around it. You follow a winding path that leads you along the shore, and eventually, you come to a steep, frozen slope that leads up the side of the mountain.\n\n{bulletpoint2}You begin to climb, using all your skill and determination to make your way up the slope. The ice is treacherous and slippery, and you must be careful with every step you take.\n\n{bulletpoint2}As you near the top of the mountain, the {new_monk_replacement} slips and begins to fall. But you oversee the red dragon empire, and you have some special tools at your disposal. You quickly pull out a special grappling rope and toss it to the {new_monk_replacement}, who manages to grab onto it and halt their fall.\n\n{bulletpoint2}You and the {new_monk_replacement} work together to pull each other up the slope, and eventually, you both make it to the top of the mountain. You are relieved and grateful that you were able to save your companion, and you ask some of the red dragon empire soldiers to help send the {new_monk_replacement} home to rest.\n\n{bulletpoint2}You may feel a sense of pride and satisfaction for having saved the {new_monk_replacement}, and you are determined to face whatever challenges and dangers come your way. You will never forget the treacherous climb up the mountain, but you are stronger for having overcome it.\n')
                    else:
                        input(f'\n{bulletpoint2}Instead of crossing the lake, you and the {new_monk_replacement} decide to go around it. You follow a winding path that leads you along the shore, and eventually, you come to a steep, frozen slope that leads up the side of the mountain.\n\n{bulletpoint2}You begin to climb, using all your skill and determination to make your way up the slope. The ice is treacherous and slippery, and you must be careful with every step you take.\n\n{bulletpoint2}As you near the top of the mountain, the {new_monk_replacement} slips and begins to fall. You immediately extend your hand, trying to grab them and pull them back up. But it is too late. The {new_monk_replacement} falls, tumbling down the steep slope and disappearing from sight.\n\n{bulletpoint2}You are left alone, stranded on the side of the mountain. You may feel a sense of regret and sorrow for what has happened to the {new_monk_replacement}, but you also know that there was nothing you could have done to prevent it.\n\n{bulletpoint2}You must now continue on your journey, facing whatever challenges and dangers come your way. You will never forget the {new_monk_replacement}, but you must move forward and keep going, no matter what.\n')
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

                    white_box_list = [white_square,
                                      mixed_squares, confused_square, white_square, mixed_squares]
                    # Function to count the printed squares.
                    def count_boxes():
                        count = 0
                        for i in white_box_list:
                            for a in i:
                                if a in ('◽', '⯀'):
                                    count += 1
                        return count
                    for item in white_box_list:
                        print(item)
                    box_question = input(
                        f'{bulletpoint}If you are worthy of this secret, you must pass the Counting Test.\nHow many are squares are there?')
                    # Calculate the correct number of squares.
                    correct_box_number = count_boxes()
                    if box_question == '1':
                        print('You cheated!')
                    elif box_question == str(correct_box_number):
                        print(f'{bulletpoint2}You passed!')
                    else:
                        print(f'{bulletpoint2}You failed!')
                    input(
                        f'{bulletpoint2}Your Answer: {box_question} \n{bulletpoint2}Correct Number of Boxes: {correct_box_number}')

                    # Triangle Puzzle
                    double_triangles = '⟁ ' * 8 # Count equals to 16
                    triangle = '🞁 ' * 8 # Count equals to 8
                    confused_triangle = '◤ ◣ ◤ ◣ ◤ ◢ ◤ ⧗' # Count equals to 9

                    triangle_list = [confused_triangle, triangle, double_triangles,
                                     triangle, double_triangles, triangle, double_triangles, confused_triangle]

                    def count_triangles():
                        count = 0
                        for i in triangle_list:
                            if i == confused_triangle:
                                count += 9
                            for a in i:
                                if a == '🞁':
                                    count += 1
                                elif a =='⟁':
                                    count += 2
                        return count

                    for item in triangle_list:
                        print(item)
                    triangle_question = input(f'How many white triangles are there?')
                    correct_triangle_num = count_triangles()
                    print(
                        f'{bulletpoint2}Your Answer: {triangle_question} \n{bulletpoint2}Correct Number of Triangles: {correct_triangle_num}')
                    if triangle_question == '1':
                        print('You cheated!')
                    elif (triangle_question) != str(correct_triangle_num): # If the player input does not equal to the correct answer, they will face a monster.
                        input(
                            f'{bulletpoint}You failed! You hear a rumbling in the snow beneath your feet. Out pops out an ancient man with some gloves on his fists that look like 🥊. The monster starts coming at you!')
                        battle(hero, boxer, 'ducks down','prepares to punch!', 'jumps on rock', 'does a phoenix punch!')
                        check_health(boxer)
                        add_health(hero)
                        check_health(hero)
                        menu()
                    else:
                        print('You passed!')
                input('''
                                     |					
                            .               /				
                             \       I     				
                                         /
                               \  ,g88R_
                                 d888(`  ).                   _
                        -  --==  888(     ).=--           .+(`  )`.
                       )         Y8P(       '`.          :(   .    )
                               .+(`(      .   )     .--  `.  (    ) )
                              ((    (..__.:'-'   .=(   )   ` _`  ) )
                       `.     `(       ) )       (   .  )     (   )  ._
                         )      ` __.:'   )     (   (   ))     `-'.:(`  )
                       )  )  ( )   *    --'   *   `- __.'   *    *:(      ))  *
                       .-'  (_.'    *   *  *     .')   *     *      `(    )  ))  *
                                            _  (_  )     *    *    *  ` __.:'
                         *    *      *     /#\\        *    *    *    *      *
                           *     *        /###\     /\\  *        *      *     *     *
                        *         *   *  /  ###\   /##\  /\\  *     *   *     *    *
                           *   *    *   /      #\ /####\/##\\*    *     *    *   *    *    *
                      *       *  *     /  /      /   # /  ##\   *     *   _   *   /\\  *
                        *      *     // //  /\  /    _/  /  #\ _    *    /#\    _/##\   */\\
                           *      * // /   /  \     /   /    #\ \  * * _/###\_ /   ##\__/ _\\
                        *      *   /  \   / .. \   / /   _   { \ \   _/       / //    /    \\\\
                           /\     /    /\  ...  \_/   / / \   } \ | /  /\  \ /  _    /  /    \ /\\
                        _ /  \  /// / .\  ..%:.  /... /\ . \ {:  \\\\   /. \     / \  /   ___   /  \\
                       /.\ .\.\// \/... \.::::..... _/..\ ..\:|:. .  / .. \\\\  /.. \    /...\ /  \ \\
                      /...\.../..:.\. ..:::::::..:..... . ...\{:... / %... \\\\/..%. \  /./:..\__   \\
                       .:..\:..:::....:::;;;;;;::::::::.:::::.\}.....::%.:. \ .:::. \/.%:::.:..\\
                ''')
                input(f'\n{bulletpoint2}As you reach the peak of the mountain, the bright snowfall surrounds you. From this vantage point, you are treated to a breathtaking view of the frozen lake below and the massive castle of ice that stands at its edge. But something seems off about the peak itself.\n\n{bulletpoint2}Beneath the blanket of snow, you see a faint glow emanating from the ground. As you brush the snow away, you uncover a series of glowing squares that begin to pulsate with light.\n{bulletpoint}A whispering voice fills your ears, asking you a question...')
                box_puzzle() # Asks the first two puzzle questions.
                snowball_question = input( # Third question asked.
                    f'{bulletpoint}The last question is... What kind of ball does not bounce? \nPlease enter your answer:')
                if 'snowball' in snowball_question:
                    print(f'{bulletpoint2}You passed!\nYou hear the ground shake, and one of the boxes you had counted previously had just opened. You take a look inside and you see a letter. There is a message that says that this must be delivered to the beggar just outside the Red Dragon castle.')
                    open_letter = input(f'{bulletpoint}You were told not to open the letter. Do you still decide to open the letter?')
                    if open_letter.strip().lower() in yes:
                        if monster_guild_membership == False:
                            input(
                                f'\n{bulletpoint2} You decided to open the letter. A legendary phoenix with electric feathers pops out and says it is the guardian of this letter. You are not the intended recipient and shall be erased from existence!\n')
                        else:
                            input(f'\n{bulletpoint2}As you stood atop the ice mountain, facing the Phoenix monster, you knew that this would be a battle for the ages. You had trained for years as a member of the Monster Hunter Guild, honing your skills and mastering the art of monster taming. You were ready.\n\n{bulletpoint2}The Phoenix let out a mighty cry and lunged at you, its electric feathers crackling with energy. You dodged its attacks, weaving and ducking to avoid its deadly strikes. You knew that you couldn\'t defeat the Phoenix through sheer strength alone. You needed to outsmart it.\n')
                        input(phoenix_image)
                        add_health(phoenix) # Adds monster health if it has already been killed.
                        battle(hero, phoenix, 'feathers turns into diamond', 'feathers turns into white', 'feathers turn into magnets', 'feathers turns into plasma')
                        add_health(hero)
                        check_health(hero) # Check if the hero died and will restart game if that is the case.
                        check_health(phoenix) # Check if the monster died and will print that the monster has died.
                        add_money(50, 200)
                        if monster_guild_membership == True:
                            input(f'\n{bulletpoint2}The Phoenix\'s eyes glazed over, and it let out a final, pitiful cry before becoming still. You had done it. You had defeated the Phoenix and added it to your collection of tamed monsters.\n\n{bulletpoint2}As you stood there, panting and exhausted, you couldn\'t help but feel a sense of pride and satisfaction. You were a member of the Monster Hunter Guild, and with every monster you defeated, your power grew. Now, every time you faced a new monster, you knew that you could tame it and add it to your collection.\n\n{bulletpoint2}With each new monster you tamed, you gained more chances to summon them into battle. You knew that with your collection of powerful allies at your side, you could take on any challenge that came your way. You were ready for whatever the future might hold.\n\n{bulletpoint2}You are now the Beastmaster! Next time you cannot afford an item at the vendor lady shop, enter "gimmethebread";)')
                        erase_name = input(
                            f'\n{bulletpoint2}The Phoenix had been guarding a secret letter, and now that it was defeated, the letter was revealed. You picked it up and read it...\n\n{bulletpoint2}It says that the next heir to the throne is {current_heir}.\n{bulletpoint}Do you decide to erase this name and change it to something else?\n')
                        if erase_name.strip().lower() in yes:
                            new_heir = input(
                                f'📜 What name would you like to change this to?')
                            current_heir = new_heir.title() # Updating the current_heir variable. Depending on the name, this will change certain parts of the story.
                            # If the player does not input anything, then this will be displayed
                            if new_heir != '':
                                input(
                                    f'{bulletpoint2}The new heir to the Red Dragon Empire shall be {current_heir}!')
                            if 'Beggar' in current_heir.title(): # Checking if the player changed the name back to the beggar.
                                input(
                                    f'\n{bulletpoint2}You remembered that you were told not to open the letter and failed on your promise. You decide to deliver the letter back to the beggar. The beggar opens up the letter and a legendary phoenix with electric feathers pops out.\n\n{bulletpoint2}The phoenix says that it is the guardian of this letter, and that the beggar is the next heir to the Red Dragon Empire. The beggar is in shock and thanks you for delivering this message.\n\n{bulletpoint2}The beggar will hand you a special reward the next time he sees you. The phoenix then kicks some dirt in your face and flies far away...\n')
                            elif hero_name.strip().lower() == current_heir.strip().lower(): # Checking if the player changed the name to hero_name.
                                input(f'\n{bulletpoint2}You are not satisfied with the current heir, and you decide to change the letter. Using your cunning and intelligence, you alter the letter to show that you are the true heir to the Red Dragon Empire.\n\n{bulletpoint2}You have the power and authority that comes with that position.\n\n{bulletpoint2}You have achieved a great victory, but the challenges and dangers that lie ahead are even greater. You must be prepared for whatever comes your way, and use all your skills and abilities to protect your new-found position and power.\n\n{bulletpoint2}You decided to alter the course of humanity for your own benefit!')
                            # If the player does not input anything, then this will be displayed
                            elif new_heir == '':
                                input(f'{bulletpoint2}You\'ve decided to make the current heir no one!')
                                current_heir = 'no one'
                            input("""
                                                      .
                                              .       |         .    .
                                        .  *         -*-          *
                                             \        |         /   .
                            .    .            .      /^\     .              .    .
                               *    |\   /\    /\  / / \ \  /\    /\   /|    *
                             .   .  |  \ \/ /\ \ / /     \ \ / /\ \/ /  | .     .
                                     \ | _ _\/_ _ \_\_ _ /_/_ _\/_ _ \_/
                                       \  *  *  *   \ \/ /  *  *  *  /
                                        ` ~ ~ ~ ~ ~  ~\/~ ~ ~ ~ ~ ~ '
                            """)
                            if current_heir.lower() != 'no one':
                                input(f"""
                                                                                _______________________
                                        _______________________-------------------                       `\\
                                    /:--__                                                              |
                                    ||< > |                                   ___________________________/
                                    | \__/_________________-------------------                         |
                                    |                                                                  |
                                    |                 THE HEIR TO THE RED DRAGON EMPIRE               |
                                    |                                                                 |
                                    |       Oh, {current_heir}, so fair and so bold,                  
                                    |       The next in line to the Red Dragon's hold,               |
                                    |       Your future is bright, your fate is sealed,              |
                                    |       The kingdom's throne, your destiny revealed.             |
                                    |                                                                |
                                        |       With fire in your veins and strength in your heart,     |
                                        |       You'll rule with grace, a true work of art,             |
                                        |       A guardian of peace, a defender of might,               |
                                        |       The Red Dragon Empire's shining light.                  |
                                        |                                                               |
                                        |       So let us raise a glass and toast to you,               |
                                        |       Our future leader, both strong and true,                |
                                        |       May your reign be long and your rule just and fair,     |
                                        |       The next great heir to the Red Dragon's throne,         |
                                        |       you'll wear with care.                                   |
                                    |                                              ____________________|_
                                    |  ___________________-------------------------                      `\\
                                    |/`--_                                                                 |
                                    ||[ ]||                                            ___________________/
                                        \===/___________________--------------------------
                                """)
                            ending(ending9)
                        else:
                            input(
                                f'{bulletpoint2}You decide to leave the name the way it is.')
                            input(
                                f'{bulletpoint2}You start heading your way back down the mountain and return to the Red Dragon Empire.')
                            ending(ending10)
                        menu()
                        beggar()
                    else:
                        input(
                            f'\n{bulletpoint2}You remembered that you were told not to open the letter and kept your promise. You decide to deliver the letter back to the beggar.\n\n{bulletpoint2}The beggar opens up the letter and a legendary phoenix with electric feathers pops out. The phoenix says that it is the guardian of this letter, and that the beggar is the next heir to the Red Dragon Empire.\n\n{bulletpoint2}The beggar is in shock and thanks you for delivering this message. The beggar will hand you a special reward the next time he sees you. The phoenix then flies far away...\n')
                        input(phoenix_image)
                        current_heir = 'Beggar'
                        ending(ending11)
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
                        f'\n{bulletpoint2}You hear horns and guards yelling outside of the treasure room. It seems that you made too much noise and are about to be caught! The only time to escape is now. You escape from the room and saw guards running past you.\n')
                
                print('💰🪙💍'*500) # Treasure room display.
                treasure_ans = input(
                    f'\n{bulletpoint2}You enter a massive room with walls made of pure gold. You only just now realized that you forgot to bring a large enough bag to hold all these valuables. There\'s a large amount of gold in front of you that you can take now and leave. There are also 7 unknown sealed rooms. What do you do?\n 0. Grab the money in front of you and leave.\n 1. Room 1\n 2. Room 2\n 3. Room 3\n 4. Room 4\n 5. Room 5 \n 6. Room 6\n 7. Room 7\n Please enter the number for your choice:\n')
                if treasure_ans == '0':
                    add_money(200,500)
                    ending(ending12)
                    menu()
                    beggar()
                elif treasure_ans == '1':
                    add_health(kitty) # Adds monster health if it has already been killed.
                    input(
                        f'\n{bulletpoint2}When you enter the room, you see a giant cat the size of a whale. The cat sees you and immediately pounces!\n')
                    battle(hero, kitty, 'licks paw',
                           'meow meow', 'roars', 'stalks')
                    input(
                        f'{bulletpoint2}You took care of the Kitty monster! You reach to pick up the Ancient Riot Shield! This item will add 100 health.')
                    hero.add_item(ancientriotshield) # Add the item's attributes to the hero and add the item's name to hero's items list.
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(kitty) # Check if the monster died and will print that the monster has died.
                    treasure_room_ending()
                    ending(ending13)
                    menu()
                    beggar()
        
                elif treasure_ans == '2':
                    add_health(fenrir) # Adds monster health if it has already been killed.
                    input(
                        f'\n{bulletpoint2}When you enter the room, you see a chained up black wolf with glowing red eyes. He growls at runs toward you!\n')
                    battle(hero, fenrir, 'tucks tail',
                           'whimpers', 'growls', 'wags tail')
                    input(
                        f'{bulletpoint2}You took care of the Fenrir monster! You reach to pick up the Adamantine Blade! This item will add 90 attack damage.')
                    hero.add_item(adamantineblade) # Add the item's attributes to the hero and add the item's name to hero's items list.
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(fenrir) # Check if the monster died and will print that the monster has died.
                    treasure_room_ending()
                    ending(ending14)
                    menu()
                    beggar()
        
                elif treasure_ans == '3':
                    input(f'\n{bulletpoint2}When you enter the room, you see a large transparent glass box. Inside this box there are two other transparent boxes. In the middle you see a wine bottle that never stops pouring. You walk over to touch the exterior box and it asks you a question...\n')
                    question_count = 3 # Number of tries the player has remaining to answer each question.
                    #3 riddles with 3 chances per riddle.
                    while question_count > 0:
                        question1 = input(f'\n{bulletpoint}Remaining Chances: {question_count}\nA man goes out drinking every night, returning to his home in the wee hours of every morning. No matter how much he drinks, he never gets a hangover. This drink is very well known, but is rarely consumed, served warm and taken straight from its source. The man is a sucker for a free drink, especially since he can\'t live without it. What is his favorite drink?\n')
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
                                            hero.add_item(elixir_of_the_gods) # Add the item's attributes to the hero and add the item's name to hero's items list.
                                            treasure_room_ending()
                                            ending(ending15)
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
                    add_health(alexa9000) # Adds monster health if it has already been killed.
                    input(
                        f'\n{bulletpoint2}When you enter the room, you see a strange metal object that looks like it hasn\'t been cleaned in decades. All of a sudden the lights on it start lighting up, and it transforms into a large metal monster. It yells "Trespassers shall be terminated"!\n')
                    battle(hero, alexa9000, 'says "beep boop"',
                           'powers down', 'says "beep beep"', 'says "boop beep"')
                    input(
                        f'{bulletpoint2}You took care of the Robot monster! You reach to pick up the ancient drone! This robot will help you attack the enemy in battles.')
                    hero.add_item(ancient_drone) # Add the item's attributes to the hero and add the item's name to hero's items list.
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(alexa9000) # Check if the monster died and will print that the monster has died.
                    treasure_room_ending()
                    ending(ending16)
                    menu()
                    beggar()
        
                elif treasure_ans == '5':
                    input(
                        f'\n{bulletpoint2}When you enter the room, you see a strange crystal ball on a table. When you walk over to it, all of a sudden an invisible force stops you in your path and a voice asks you a question...\n')
                    random_num = random.randint(1,10) # Random number generator
                    tries = 3 # Number of tries
                    while tries != 0:
                        # Guessing Number Minigame
                        guess1 = input(
                            f'\n{bulletpoint}You have three chances to guess the correct number that was randomly selected from 1 to 10. What is your guess?\n')
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
                            f'\n{bulletpoint2}You foresaw the correct answer! You reach to pick up the crystal ball! This item will reveal the enemy\'s actions one time per battle.\n')
                        # Add the item's attributes to the hero and add the item's name to hero's items list.
                        hero.add_item(merlins_crystal_ball)
                        treasure_room_ending()
                        ending(ending17)
                        menu()
                        beggar()
                    else:
                        treasure_room_ending()
                        menu()
                        beggar()
        
                elif treasure_ans == '6':
                    input('''
                                             _
                                            _)\.-.
                            .-.__,___,_.-=-. )\`  a`\_
                        .-.__\__,__,__.-=-. `/  \     `\\
                        {~,-~-,-~.-~,-,;;;;\ |   '--;`)/
                        \-,~_-~_-,~-,(_(_(;\/   ,;/
                        ",-.~_,-~,-~,)_)_)'.  ;;(
                            `~-,_-~,-~(_(_(_(_\  `;\\
                    ,          `"~~--,)_)_)_)\_   \\
                    |\              (_(_/_(_,   \  ;
                    \ '-.       _.--'  /_/_/_)   | |
                        '--.\    .'          /_/    | |
                            ))  /       \      |   /.'
                        //  /,        | __.'|  ||
                        //   ||        /`    (  ||
                        ||    ||      .'       \ \\\\
                        ||    ||    .'_         \ \\\\
                        \\\\   //   / _ `\        \ \\\\__
                    jgs    \\'-'/(   _  `\,;        \ '--:,
                            `"`  `"` `-,,;         `"`",,;
                    ''')
                    add_health(griffin) # Adds monster health if it has already been killed.
                    input(
                        f'\n{bulletpoint2}When you enter the room, you see a magestic griffin monster with the body, tail, and back legs of a lion; the head and wings of an eagle. It turns over to you and starts attacking!\n')
                    battle(hero, griffin, 'tucks wings',
                           'beak turns left', 'flaps wings', 'raises talons')
                    input(
                        f'\n{bulletpoint2}You took care of the Griffin monster! You reach to pick up the Fireball scroll which tells you secret words! You can use this spell during battles to attack the enemy!\n')
                    hero.add_item(fireball_spell) # Add the item's attributes to the hero and add the item's name to hero's items list.
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(griffin) # Check if the monster died and will print that the monster has died.
                    treasure_room_ending()
                    ending(ending18)
                    menu()
                    beggar()
                elif treasure_ans == '7':
                    input("""
                                                  _.--""-._
                      .                         ."         ".
                     / \    ,^.         /(     Y             |      )\
                    /   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
                    |        :|    `>   '.     l_..-------.._l      .'
                    |      __l;__ .'      "-.__.||_.-'v'-._||`"----"
                     \  .-' | |  `              l._       _.'
                      \/    | |                   l`^^'^^'j
                            | |                _   \_____/     _
                            j |               l `--__)-'(__.--' |
                            | |               | /`---``-----'"1 |  ,-----.
                            | |               )/  `--' '---'   \'-'  ___  `-.
                            | |              //  `-'  '`----'  /  ,-'   I`.  \
                          _ L |_            //  `-.-.'`-----' /  /  |   |  `. \
                         '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
                          `._;/7(-.......'  /        ) (     |  |            | |
                          `._;l _'--------_/        )-'/     :  |___.    _._./ ;
                            | |                 .__ )-'\  __  \  \  I   1   / /
                            `-'                /   `-\-(-'   \ \  `.|   | ,' /
                                               \__  `-'    __/  `-. `---'',-'
                                                  )-._.-- (        `-----'
                                                 )(  l\ o ('..-.
                                           _..--' _'-' '--'.-. |
                                    __,,-'' _,,-''            \ \
                                   f'. _,,-'                   \ \
                                  ()--  |                       \ \
                                    \.  |                       /  \
                                      \ \                      |._  |
                                       \ \                     |  ()|
                                        \ \                     \  /
                                         ) `-.                   | |
                                        // .__)                  | |
                                     _.//7'                      | |
                                   '---'                         j_| `
                                                                (| |
                                                                 |  \
                                                                 |lllj
                                                                 |||||  -nabis
                    """)
                    add_health(skeletonwarrior) # Adds monster health if it has already been killed.
                    input(
                        f'\n{bulletpoint2}When you enter the room, you see a skeleton with a shield and sword displayed in the middle of the room. You walk over and touch it. All of a sudden the hand grabs your arm and it starts attacking you!\n')
                    battle(hero, skeletonwarrior, 'raises shield','bones crack', 'cracks knuckles', 'raises sword')
                    input(
                        f'{bulletpoint2}You took care of the Skeleton monster! You reach to pick up the Warrior\'s Helm! This item will add 100 health.')
                    hero.add_item(warriorshelm) # Add the item's attributes to the hero and add the item's name to hero's items list.
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(skeletonwarrior) # Check if the monster died and will print that the monster has died.
                    treasure_room_ending()
                    ending(ending25)
                    menu()
                    beggar()
                else:
                    print(f'{bulletpoint2}Please enter a valid choice number.')
                    menu()
                    treasure_room()
            
            #The Wizard
            def wizard():
                nonlocal vendor_lady_object, merlin_in_room
                # Function to reset all the variables in the story back to the original state except "merlin_in_room"
                def reverse_time():
                    nonlocal current_heir, current_emperor, emperor_life, noble_life, thugs_life, icequeen_life, current_kingdom_name, new_monk_replacement, coin_guess_correctly, wall_key_count, current_empire_name, victory, vendor_lady_object, monster_guild_membership, assassin_guild_membership

                    current_heir = 'the beggar..' # Resets the current heir.
                    current_emperor = 'emperor'
                    emperor_life = 'alive'
                    noble_life = 'alive'
                    thugs_life = 'alive'
                    icequeen_life = 'alive'
                    current_kingdom_name = 'Ice Kingdom'
                    new_monk_replacement = 'monk'
                    coin_guess_correctly = False
                    wall_key_count = 1
                    current_empire_name = 'Red Dragon Empire'
                    victory = 'black'
                    vendor_lady_object = 1
                    monster_guild_membership = False
                    assassin_guild_membership = False
                # Adds health to the Merlin monster battle
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
        '''     # If Merlin has left the room, the following will be displayed.
                if merlin_in_room == 0:
                    empty_wiz_room = input(
                        f'\n{bulletpoint2}As you enter the massive silver-colored room, you are immediately struck by the array of foreign gadgets that litter the space. Some of them beep and whirr, while others hum and glow with a strange light. You quickly realize that this must have been Merlin\'s workshop, where he spent long hours tinkering with his magical inventions.\n\n{bulletpoint}Do you enter the room?')
                    if empty_wiz_room.strip().lower() in yes:
                        touch_crystal_ball = input(f'{bulletpoint2}You remember how you freed Merlin from the previous emperor\'s captivity, and how grateful he was to you. You also remember how he promised to continue his work and to use his powers for the greater good.\n\n{bulletpoint2}As you walk deeper into the room, you notice a strange blue crystal ball resting on a pedestal in the center of the space. The ball seems to pulsate with a soft, otherworldly light, and you feel drawn to it.\n\n{bulletpoint2}You approach the ball and reach out to touch it, wondering what secrets it might hold. As your fingers brush against its surface, the ball begins to glow brighter and the hum of its energy grows louder.\n\n{bulletpoint2}Suddenly, a vision appears before your eyes. You see a world unlike any you have ever known, a world of magic and wonder. In this world, people fly through the air on winged machines, and great cities rise up from the ground like glittering jewels.\n\n{bulletpoint2}You are awestruck by the beauty of this place, and you feel a sudden longing to visit it. But as quickly as the vision appears, it fades away, leaving you standing before the crystal ball with a sense of wonder and mystery.\n\n{bulletpoint2}You know that this crystal ball holds the key to a world beyond your own, and you vow to return to it one day, to uncover its secrets and to explore the magical lands that lie beyond.\n\n{bulletpoint}Do you touch the crystal ball again?')
                        if touch_crystal_ball.strip().lower() in yes:
                            print(
                                f'\n{bulletpoint}All of a sudden you\'ve been sucked into a hole. All you see around you is warped stars and you see a white hole in the distance...\n')
                            input(blackhole)
                            ending(ending28)
                            reverse_time()
                            #This resets Merlin to be in his room
                            merlin_in_room = 1
                            menu()
                            beggar()
                    menu()
                    beggar()
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
                    f'\n{bulletpoint2}You enter a massive silver colored room with various foreign gadgets that make unfamiliar noise. An old man with a long beard and purple hat turns around and is suprised to see you. He starts questioning who you are and if you were sent by the emperor to kill him.\n\n{bulletpoint}Do you say yes or no:')
                if wizard_ans_one.lower() in yes:
                    if current_emperor.strip().lower() == hero.name.strip().lower():
                        input(f'\n{bulletpoint2}You yell "I AM THE EMPEROR!!!😈"\n')
                    input(
                        f'\n{bulletpoint2}The wizard sends three 🤖🤖🤖 magical metal beings to grab a hold of you. They make weird "beep boop noises".\n')
                    battle(hero, robots, 'say TURTLE MODE ACTIVATED!',
                           'say RECOVER MODE!', 'say ANALYZING FIGHT PATTERNS!', 'say ATTACK MODE!')
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(robots) # Check if the monster died and will print that the monster has died.
                    input(f'\n{bulletpoint2} You took care of these metal monsters. The wizard gets visibly furious and takes out a long glowing staff with a ball of electrical energy at the top. He starts cursing and says he\'ll take care of you himself!\n')
                    battle(hero, merlin, 'whispers "siri Beri nin"...',
                           'whispers "siri Rac cin"...', 'whispers "siri Gúl cai"...', 'whispers "siri Naur corn"...')
                    check_health(hero) # Check if the hero died and will restart game if that is the case.
                    check_health(merlin) # Check if the monster died and will print that the monster has died.
                    add_money(200, 600) # Adds random amount of money to hero after boss battle between 200 and 600.
                    menu()
                    print(f'\n{bulletpoint2}The wizard Merlin was murdered. He had been imprisoned by the empire for decades, forced to build gadgets for the empire\'s grand plan. Rumors among the nobility spread that the empire figured out his schemes to take over using his magical metal beings.\n\nRumors also had it that the empire planned to get rid of him before that happened. Back in the wizard\'s lab, you stood over his dead body with blood on your hands. You see a strange blue crystal ball in a separate translucent room and walk over to it.\n')
                    crystal_ball_ans = input(f'{bulletpoint}Do you touch the crystal ball?')
                    if crystal_ball_ans.lower() in yes:
                        vendor_lady_object = 1 # This turns on the vendor lady scenario when you restart
                        menu()
                        print(
                            f'\n{bulletpoint}All of a sudden you\'ve been sucked into a hole. All you see around you is warped stars and you see a black hole in the distance...\n')
                        input(blackhole)
                        ending(ending19)
                        menu()
                        beggar()
                    else:
                        print(
                            f'\n{bulletpoint}The room started sparking all over the place after the battle. All of a sudden you\'ve been sucked into a hole. All you see around you is warped stars and you see a black hole in the distance...\n')
                        input(blackhole)
                        ending(ending20)
                        menu()
                        beggar()
                else:
                    # Reverse Time function resets the state of the game
                    input(
                        f'\n{bulletpoint2}The wizard introduces himself as Merlin. He said he had been imprisoned by the empire for decades, forced to build gadgets for the empire\'s grand plan. He was recently working on these metal beings and planned to copy them on behalf of the empire in order to save human lives.\n')
                    merlin_ans = input(
                        f'''
                        {bulletpoint2}You decided to ask ONE of the following question:
                        1. Were you really going to use these metal beings to save human lives, or did you have ulterior motives?
                        2. How did you make all these gadgets?
                        3. Can I help you escape?

                        {bulletpoint2}Please type the number for the question:
                        ''')
                    if merlin_ans == '1':
                        input(f'\n{bulletpoint2}Merlin tells you that he\'s seen visions of the prior human civilization in his crystal ball. He doesn\'t care about taking over the empire with what he calls the magical metal beings as "machines".\n\n{bulletpoint2}He just wants to better humanity and steer the destruction of humanity to a more positive direction using the empire\'s finances.\n\n{bulletpoint2}He gives you a secret tip that at the entrance of the passageway, you can say the magical phrase "opensesame" to instantly teleport you to the room with the three doors.\n')
                        input(
                            f'\n{bulletpoint2}Merlin says that if you touch the crystal ball, it will bring you to the past. Who wouldn\'t want to change something they regret in their lives! You walk over and see yourself in the crystal ball, you touch it and then all of a sudden you\'ve been sucked into a hole. All you see around you is warped stars and you see a white hole in the distance...\n')
                        input(blackhole)
                        reverse_time()
                        ending(ending21)
                        menu()
                        beggar()
                    elif merlin_ans == '2':
                        input(f'\n{bulletpoint2}Merlin tells you that he only made 25% of the gadgets which were improved on remnant ancient technology. He says that in the ancient past, there was an advanced civilization called the "Hums" that developed flying ships and millions of machines. They were destroyed by war internally and made something called a "bomb" that destroyed cities with the power of a thousand suns.\n\n{bulletpoint2}Speaking of bombs, Merlin reveals to you that if you ever play rock, paper, scissors, and whisper the magic word "bomb", you\'ll instantly win.\n\n{bulletpoint2}Anyways, he says, after that civilization, the "An" civilization had to deal with the legendary dragon that fell from a space egg, which hatched on earth and caused havoc across the lands. They were the ones to help seal the dragon with ancient tech and save humanity. There are only a few kingdoms that managed to preserve some of the ancient technology today and they hold on to them to maintain their power.\n')
                        input(
                            f'\n{bulletpoint2}Merlin says that if you touch the crystal ball, it will bring you to the past. Who wouldn\'t want to change something they regret in their lives! You walk over and see yourself in the crystal ball, you touch it and then all of a sudden you\'ve been sucked into a hole. All you see around you is warped stars and you see a white hole in the distance...\n')
                        input(blackhole)
                        reverse_time()
                        ending(ending22)
                        menu()
                        beggar()
                    elif merlin_ans == '3':
                        if current_emperor.strip().lower() == hero.name.strip().lower():
                            if wall_key_count == 0:
                                input(f'\n{bulletpoint2}You decide to reveal to Merlin that you\'re actually the new emperor of the Red Dragon Empire, and that you\'ve managed to figure out how to replace the previous emperor, taking over the throne in the process.\nYou use your newfound power to free Merlin from imprisonment, granting him full access to the empire\'s treasury. As he leaves the dungeon, Merlin thanks you for your help and begins to make his way out of the castle, promising to use his powers for the greater good. He is relieved to be free and eager to start a new life.\n')
                                input(
                                    f'\n{bulletpoint2}Merlin says that if you touch the crystal ball, it will bring you to the past. Who wouldn\'t want to change something they regret in their lives! You walk over and see yourself in the crystal ball, you touch it and then all of a sudden you\'ve been sucked into a hole. All you see around you is warped stars and you see a white hole in the distance...\n')
                                input(blackhole)
                                reverse_time()
                                merlin_in_room = 0
                                ending(ending27)
                                menu()
                                beggar()
                            
                        input(f'\n{bulletpoint2}Merlin says that\'s an interesting proposition! He tells you that he would love to explore the lands but he would need funding to carry on his experiments. If only we could get hands on the empire\'s treasury, now that\'s a different story...\n')
                        input(
                            f'\n{bulletpoint2}Merlin says that if you touch the crystal ball, it will bring you to the past. Who wouldn\'t want to change something they regret in their lives! You walk over and see yourself in the crystal ball, you touch it and then all of a sudden you\'ve been sucked into a hole. All you see around you is warped stars and you see a white hole in the distance...\n')
                        input(blackhole)
                        reverse_time()
                        ending(ending23)
                        menu()
                        beggar()
                    else:
                        input(f'You decided to leave without asking a question.')
                        menu()
                        beggar()
            # The Red Dragon
            def red_dragon():
                add_health(tiamat)
                print('''
                                                                       ,d888*`
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
                    f'\n{bulletpoint2}You enter a massive cavern that is pitch black. All of a sudden you see flames in front of you and its bone-chilling face appears. You realized that this was the legendary red dragon Tiamat which fell from the heavens onto Earth in the ancient past. You remembered the myth that it caused havoc across the lands, before it was finally captured and sealed by magic by the ancient advanced civilization...\n')
                input(f'\n{bulletpoint2}The doors behind you magically disappeared or blended into the wall. There was no escape. You thought about all the choices you made prior to choosing this door, and what you could have done to avoid this fate. You face death in front of you and it\'s too late to turn back...\n')
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
                input(f'\n{bulletpoint}You beat the Red Dragon Tiamat! All of a sudden... Tiamat\'s body starts moving again. Tiamat starts sprouting two extra wings and its muscles double in size. Its eyes glow red with smoke steaming out as it gets up and flies away. What could this mean...?\n')
                ending(ending24)
                input(f'{bulletpoint2}Press enter to continue...')
                beggar()
            # Passageway
            def passageway():
                ascii_locked_door = '''
                88888888888888888888888888888888888888888888888888888888888888888888888
                88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
                88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
                88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
                88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
                88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
                88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
                88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
                88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
                88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
                88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
                88      |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  88
                88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
                88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
                88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
                88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
                88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
                88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
                88      |_.'|   .' | .' |/                   \  \ |  `.  | `._-Lee|  88
                88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
                88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
                88 8888888888888888888888888888888888888888888888888888888888888(FL)888
                '''
                passageway_ans = input(
                    f'\n{bulletpoint}While walking through the castle, you notice an obscure passageway behind a painting that wasn\'t fully closed. Do you enter it?\n')
                if passageway_ans.lower().strip() in yes:
                    left = 'left'
                    right = 'right'
                    down = 'down'
                    up = 'up'
                    movement = 1
                    spider_alive = 1 # If the spider has already been killed, the spider monster will not show up in the map. 1 represents the spider still being alive, and this wil reset the spider if player is going through another round of the game.

                    def maze():
                        print(
                            f'Movements:\n🠸: "Left"     🠺: "Right" \n🠹: "Up"     🠻: "Down" ')
                        while movement == 1:

                            def wall_2down():
                                print('▄▄▄▄   ▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄           ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄     𐀪 ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄')
                                direction = input(
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
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
                                    f'\n{bulletpoint}Which direction would you like to take:')
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
                                    f'\n{bulletpoint}Which direction would you like to take:')
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
                                        f'\n{bulletpoint}Which direction would you like to take:\n')
                                    if spider_alive == 1: # Opens up the monster scene if spider is still alive.
                                        maze_monster()
                                    wall_2leftdown()
                                else:
                                    input(
                                        f'\n{bulletpoint}Which direction would you like to take:\n')
                                    if spider_alive == 1:  # Opens up the monster scene if spider is still alive.
                                        maze_monster()
                                    wall_2leftdown()

                            def secret_corridor():
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄      𐀪⨔')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                 ▄▄▄▄▄▄')
                                print('▄▄▄▄         ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                if ring_of_nirvana.name not in hero_items:
                                    take_ring = input(
                                        f'\n{bulletpoint}You hear a acoustic humming noise and see a shining ring floating in mid air. Do you take it?\n')
                                    if take_ring.lower() == 'yes':
                                        if ring_of_nirvana not in hero_items:
                                            input(
                                                f'\n{bulletpoint2}You took it and wore the {ring_of_nirvana.name}!\n')
                                            hero.add_item(ring_of_nirvana) # Add the item's attributes to the hero and add the item's name to hero's items list.
                                            menu()
                                    else:
                                        input(
                                            f'\n{bulletpoint}You left it where it stood.\n')
                                else:
                                    input(
                                        f'\n{bulletpoint}You hear a acoustic humming noise and you glance at the ring on your finger.\n')
                                    menu()
                                direction = input(
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
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
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
                                if direction == down:
                                    wall_2down()
                                elif direction == left:
                                    wall_1left()
                                elif direction == up:
                                    print(
                                        f'\n{bulletpoint2}The passageway entrance is locked.\n')
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
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
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
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
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
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
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
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
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
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
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
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
                                if direction == right:
                                    wall_3right()
                                elif direction == down:
                                    wall_3down()
                                elif direction == up:
                                    wall_1leftdownleftupleft()
                                else:
                                    wall_3()

                            def wall_locked_room():
                                input(ascii_locked_door)
                                nonlocal wall_key_count
                                print('▄▄▄▄ 🚪▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄᭄    ᭄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄ᬛ|🚽    ⚙|ᬊ▄▄▄▄▄▄▄▄▄')
                                print('▄▄ᬛ|📠      📯|ᬊ▄▄▄▄▄▄')
                                print('▄ᬛ|📷    𐀪  🔭|ᬊ▄▄▄▄▄▄')
                                print('▄▄ᬛ|        ☎|ᬊ▄▄▄▄▄▄▄')
                                print('▄▄▄ᬛ|📺 ⚽ 🏆|ᬊ▄▄▄▄▄▄')
                                print('▄▄▄▄▄ᬛ🖼𝄩𝄩🖼ᬊ▄▄▄▄▄▄▄▄▄▄')
                                input(f'\n{bulletpoint2}You are currently in a room that appears to have been untouched for a long time. As you look around, you see a variety of ancient artifacts that appear to be examples of advanced technology from a long-gone civilization.\n\n{bulletpoint2}You see an ancient toilet, camera, telescope, phone, trophy, gear piece, trumpet, fax machine, and soccer ball. These objects are all unfamiliar to you, as the civilization that created them has long since disappeared.\n\n{bulletpoint2}You are intrigued by these artifacts and are eager to learn more about them, but without any way to access information about their purpose or how they were used, you are left to simply wonder about their significance.\n')
                                guess_items_ans = input(f'\n{bulletpoint}Would you like to hear your guess on what these items were used for?\n')
                                if guess_items_ans.strip().lower() in yes:
                                    input(
                                        f'\nAn ancient toilet may have been used for storing valuables or for performing rituals.\nA camera may have been used for creating illusions or for studying the movements of celestial bodies.\nA telescope may have been used for divination or for enhancing the senses.\nA phone may have been used for communicating with spirits or for predicting the future.\nA trophy may have been used for displaying the wealth or power of its owner.\nA gear piece may have been used for decorative purposes or as a religious symbol.\nA trumpet may have been used for signaling in battle or for announcing the arrival of important figures.\nA fax machine may have been used for alchemical experiments or for creating magical portals.\nA soccer ball may have been used for divination or for throwing in a game of skill.\n\n{bulletpoint2}You were confident in your ability to guess the item\'s purpose!')
                                if current_emperor.strip().lower() == hero.name.strip().lower():
                                    # Checks if the player has already been in this room, and will set the wall key count variable to 0 if so
                                    if wall_key_count == 1:
                                        input(f'\n{bulletpoint2}You found a key 🔑!')
                                        wall_key_count = 0
                                direction = input(
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
                                if direction == up:
                                    wall_3down()
                                else:
                                    wall_locked_room()

                            def wall_3down():
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄ᬛ')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄ 𐀪 ▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄🚪▄▄▄▄▄▄▄▄▄▄▄')
                                print('The door is locked.')
                                direction = input(
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
                                if direction == up:
                                    wall_3()
                                elif direction == down:
                                    if current_heir.strip().lower() == hero.name.strip().lower() or current_emperor.strip().lower() == hero.name.strip().lower():
                                        input(
                                            f'\n{bulletpoint2}You use your key to access the room.\n')
                                        wall_locked_room()
                                    else:
                                        input(
                                            f'\n{bulletpoint2}The passageway entrance is locked.\n')
                                        wall_3down()
                                else:
                                    wall_3down()

                            def wall_3right():
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                print('▄▄▄▄                             𐀪 ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄           ▄▄▄▄▄▄')
                                direction = input(
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
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
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
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
                                    f'\n{bulletpoint}Would you like to open the door?\n')
                                if opendoor.lower() == 'yes':
                                    input(ascii_locked_door)
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
                                    f'\n{bulletpoint}You\'re in a black colored mirror room with symbols on the walls that are glowing. Which door would you like to open?\n Choices are "Left", or "Down", or "Right":\n')
                                if three_doors_ans.lower() == left:
                                    print(f'{bulletpoint2}Treasure room')
                                    input(
                                        f'\n{bulletpoint2}Press enter to open to door...\n')
                                    menu()
                                    movement -= 1
                                    treasure_room()
                                elif three_doors_ans.lower() == right:
                                    print(f'{bulletpoint2}Wizard room')
                                    input(
                                        f'\n{bulletpoint2}Press enter to open to door...\n')
                                    menu()
                                    movement -= 1
                                    wizard()
                                elif three_doors_ans.lower() == down:
                                    print(f'{bulletpoint2}Dragon room')
                                    input(
                                        f'\n{bulletpoint2}Press enter to open to door...\n')
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
                                input('▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                                input('''
                                               \_______/
                                           `.,-'\_____/`-.,'
                                            /`..'\ _ /`.,'\\
                                           /  /`.,' `.,'\  \\
                                          /__/__/     \__\__\__
                                          \  \  \     /  /  /
                                           \  \,'`._,'`./  /
                                            \,'`./___\,'`./
                                           ,'`-./_____\,-'`.
                                               /       \\
                                              (
                                              )
                                             (
                                       /\  .-"""-.  /\\
                                      //\\\\/  ,,,  \//\\\\
                                      |/\| ,;;;;;, |/\|
                                      //\\\\\;-"""-;///\\\\
                                     //  \/   .   \/  \\\\
                                    (| ,-_| \ | / |_-, |)
                                      //`__\.-.-./__`\\\\
                                     // /.-(() ())-.\ \\\\
                                    (\ |)   '---'   (| /)
                                     ` (|           |) `
                               jgs     \)           (/
                                ''')
                                input(
                                    f'\n{bulletpoint}A Massive 10 foot {arachne.name} dropped from the ceiling! You\'re trapped, there\'s no where to run except to fight!\n')
                                battle(hero, arachne, 'spins web',
                                    'shrieks', 'sprays web', 'shows fangs')
                                check_health(hero)
                                check_health(arachne) # Check if the monster died and will print that the monster has died.
                                spider_alive -= 1 # Spider counter reduced, which opens up secret passageway.
                                add_money(50, 200) # Adds hero money between 50 to 200.
                                menu()
                                input(
                                    f'\n{bulletpoint2}You hear the walls rumbling in the distance...\n')
                                wall_2leftdown()

                            def wall_1entrance():
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄🚪▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 𐀪 ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                 ▄▄▄▄▄▄')
                                print('▄▄▄▄         ▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄')
                                direction = input(
                                    f'\n{bulletpoint}Which direction would you like to take:\n')
                                if direction == down:
                                    wall_1down()
                                elif direction == up:
                                    if current_heir.strip().lower() == hero.name.strip().lower() or current_emperor.strip().lower() == hero.name.strip().lower():
                                        input(ascii_locked_door)
                                        input(
                                            f'\n{bulletpoint2}You use your key to leave.\n')
                                        menu()
                                        beggar()
                                    else:
                                        input(
                                            f'\n{bulletpoint2}The passageway entrance is locked.\n')
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
                    if hero.name.strip().lower() not in (current_emperor.strip().lower(), current_heir.strip().lower()):
                        input(f'\n{bulletpoint2}You walk along the streets to find a job, but no one you encountered would hire you. You then come across a mysterious {new_monk_replacement}.\n')
                    else:
                        input(f'\n{bulletpoint2}You decide to stroll along the streets and you come across a mysterious {new_monk_replacement}.\n')
                    menu()
                    mysterious_monk()

            # The Mysterious Monk
            def mysterious_monk():
                mysterious_monk_ans = input(
                    f'\n{bulletpoint}A mysterious {new_monk_replacement} came to you and asks if you would be so kind to help with a task. The {new_monk_replacement} says it won\'t be easy and there is no pay. Do you still help?\n')
                if mysterious_monk_ans.strip().lower() in yes:
                    input(f'\n{bulletpoint2} You\'ll be joining the {new_monk_replacement} to help lead this journey. The {new_monk_replacement} gives you an ancient map that shows different routes you can take to reach the top.\n')
                    menu()
                    the_secret()
                else:
                    menu()
                    get_drunk()

            # Bestfriend

            def best_friend():
                best_friend_ans = input(
                    f'\n{bulletpoint}After some deep talks, your best friend revealed that he had previously been imprisoned by the empire because of his family line. He still had no idea the true reason but he was imprisoned anyways, and he made several attempts to escape.\n He asks if you would like to play a game to lighten the mood?')
                if best_friend_ans.strip().lower() in yes:
                    game_ans = input(
                        f'\n{bulletpoint2}The game is called Rock Paper Scissors! 🪨 Rock beats ✂ Scissors, 📜 Paper beats 🪨 Rock, ✂ Scissors beats 📜 Paper!\n Enter Rock, Paper, or Scissors:')
                    playGame(game_ans)
                    game_ans2 = input(
                        f'\n{bulletpoint2}Your best friend laughs!\n Enter Rock, Paper, or Scissors:\n')
                    playGame(game_ans2)
                    game_ans3 = input(
                        f'\n{bulletpoint2}Last round to see who\'s the true winner!\n Enter Rock, Paper, or Scissors:\n')
                    playGame(game_ans3)
                    riddle_ans1 = random.choice(alphabet).capitalize()
                    riddle_ans2 = random.choice(['emperor', 'queen', 'dragon'])
                    input(f'\n{bulletpoint2}Good times! Drinks on your best friend\'s tab! After the last drink, your best friend proposed an idea to make some life-changing money. During his extensive time of imprisonment, he overheard the Emperor whispering about some hidden castle passageway. It was apparently located behind a painting of the {riddle_ans2} at tower {riddle_ans1} to access his bank...\n')
                    menu()

                    # The Bank Robbery
                    riddle_ans3 = random.choice(['2:38', '3:28', '3:32'])
                    input(
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
                                        f'\n{bulletpoint2}You were so close! Your best friend says you can think about this job another time.\n')
                                    menu()
                                    secret_job()
                            else:
                                print(
                                    f'\n{bulletpoint2}Nice try! Your best friend says you can think about this job another time.\n')
                                menu()
                                secret_job()
                        else:
                            print(
                                f'\n{bulletpoint2}Perhaps listen carefully! Your best friend says you can think about this job another time.\n')
                            menu()
                            secret_job()
                    else:
                        print(
                            f'\n{bulletpoint2}You\'re not listening! Your best friend says you can think about this job another time.\n')
                        menu()
                        secret_job()
                else:
                    if current_heir.strip().lower() == hero.name.strip().lower() or current_emperor.strip().lower() == hero.name.strip().lower():
                        input(f'\n{bulletpoint2}Perhaps next time then. Your best friend says it\'s getting late and we should leave before the nightwolves start roaming the streets. As you leave a beggar walks up to you...\n')
                        menu()
                        beggar()
                    else:
                        input(f'\n{bulletpoint2}Perhaps next time then. Your best friend says it\'s getting late and we should leave before the nightwolves start roaming the streets. As you leave a hooded person with an insignia of the red dragon empire grabbed you in the darkness...\n')
                        menu()
                        secret_job()

            # Vendor Lady
            def vendor_lady():
                nonlocal vendor_lady_object # Accesses the vendor_lady count.
                vendor_ans = input(f'\n{bulletpoint}An elder vendor lady has some rare and mythical items for sale. She says that she\'s only going to be available now one time, as she needs to leave to a faraway kingdom. Would you like to purchase something?\n') 
                if vendor_ans.strip().lower() in yes:
                    show_vendor_menu()
                    menu()
                    vendor_lady_object -= 1 # Turns off the vendor_lady scenario
                else:
                    if current_heir in (hero.name, 'beggar', 'the beggar'):
                        vendor_lady_object -= 1  # Turns off the vendor_lady scenario
                        secret_item()
                        menu()
                    else:
                        print(f'\n{bulletpoint2}You visit a local tavern and meet someone who became your best friend over the course of months.\n')
                        vendor_lady_object -= 1  # Turns off the vendor_lady scenario
                        best_friend()
                        menu()

            # The Beggar
            def beggar():
                nonlocal current_heir, new_monk_replacement, new_goons
                print('''
                    .                  .-.    .  _   *     _   .
                           *          /   \     ((       _/ \       *    .
                         _    .   .--'\/\_ \     `      /    \  *    ___
                     *  / \_    _/ ^      \/\\'__        /\/\  /\  __/   \ *
                       /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .
                  .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
                     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \\
                   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \\
                  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
                @/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%
                ''')
                print('''
                                                T~~
                                                |
                                                /"\\
                                        T~~     |'| T~~
                                    T~~ |    T~ WWWW|
                                    |  /"\   |  |  |/\T~~
                                    /"\ WWW  /"\ |' |WW|
                                    WWWWW/\| /   \|'/\|/"\\
                                    |   /__\/]WWW[\/__\WWWW
                                    |"  WWWW'|I_I|'WWWW'  |
                                    |   |' |/  -  \|' |'  |
                                    |'  |  |LI=H=LI|' |   |
                                    |   |' | |[_]| |  |'  |
                                    |   |  |_|###|_|  |   |
                                    '---'--'-/___\-'--'---'  
                ''')
                if current_heir == 'Beggar' or current_heir == 'The Beggar':
                    beggar_ans = input(f'\n{bulletpoint}The beggar shows his gratitude for delivering the message and as a small token of appreciation, he hands you a lump of gold that he retrieved from the castle bank.\nHe says he just remembered he needs $5 back since he needs to buy some food from the local shops. Do you give him the money?\n')
                    add_money(100,1000)
                else:
                    beggar_ans = input(f'\n{bulletpoint}You\'re walking through the bustling streets of the Red Dragon Empire. A dirty beggar comes up to you asking $5 for food. Do you give him the money?\n')
                if beggar_ans.strip().lower() in yes:
                    if hero.money >= 5:
                        input(f'\n{bulletpoint2}You hand over $5 and he thanks you for your kindness. The beggar introduces you to a mysterious {new_monk_replacement} who needs some assistance with something.\n') 
                        hero.money -= 5
                    else:
                        input(f'\n{bulletpoint2}You cannot afford to give the beggar money! The beggar thanks you anyways and introduces you to a mysterious {new_monk_replacement} who needs some assistance with something.\n')
                    menu()
                    mysterious_monk()
                elif beggar_ans.strip().lower() == 'm@x':
                    hero.health = 999999
                    hero.money = 999999
                    print(
                        f'\n{bulletpoint2}The beggar understands what you mean😉')
                    beggar_direction = input(
                        f'\nVisit the {new_monk_replacement}\nVisit the Vendor Lady Stall\nVisit the Red Dragon Castle\nVisit the Ice Kingdom\nVisit the Mountain\nVisit the Assassin Guild\nVisit the Monster Hunter Guild\nVisit the Sail Trade Mission?\n{bulletpoint}Where would you like to go:')
                    if beggar_direction.strip().lower() in ('vendor lady', 'vendor', 'stall', 'vendor lady stall'):
                        menu()
                        vendor_lady()
                    elif beggar_direction.strip().lower() in ('castle', 'passageway', 'red', 'red dragon', 'red dragon castle'):
                        menu()
                        passageway()
                    elif beggar_direction.strip().lower() in ('ice', 'ice kingdom', 'icekingdom'):
                        menu()
                        ice_kingdom()
                    elif beggar_direction.strip().lower() in ('mountain', 'mountain secret'):
                        menu()
                        mountain_secret()
                    elif beggar_direction.strip().lower() in ('assassin', 'assassinguild', 'assassin guild'):
                        menu()
                        assassins_guild()
                    elif beggar_direction.strip().lower() in ('monster', 'monster hunter', 'monster hunter guild'):
                        menu()
                        monster_hunter_guild()
                    elif beggar_direction.strip().lower() in ('sail', 'trade', 'trade mission', 'sailing', 'trademission'):
                        menu()
                        trade_mission()
                    else:
                        menu()
                        mysterious_monk()

                else:
                    if current_heir == 'Beggar' or current_heir == 'The Beggar':
                        input(
                            f'\n{bulletpoint2}You kick him, spit on him, and yell that you don\'t acknowledge a dirty beggar as the next heir and walk away laughing.\n')
                        menu()
                    else:
                        print(f'\n{bulletpoint2}You kick his bowl of change, spit on him, and walk away laughing.\n')
                        menu()

                    # Three Thugs
                    if thugs_life == 'alive':
                        new_goons = 'thugs'
                    else:
                        pass
                    three_thugs_ans = input(
                        f'\n{bulletpoint}The beggar calls three {new_goons} over and asks them to rough you up. Do you stay and fight?\n')
                    if three_thugs_ans.strip().lower() in yes:
                        if current_heir.strip().lower() == hero.name.strip().lower() or current_emperor.strip().lower() == hero.name.strip().lower():
                            input(f'\n{bulletpoint}You oversee the red dragon empire, and you have some powerful allies at your disposal. When the {new_goons} arrive, you call out to the castle guards, who immediately come to your aid.\n\n{bulletpoint2}The guards quickly arrest the {new_goons}, who are no match for their superior training and weaponry. You are unharmed, and the beggar is left empty-handed and disappointed.\n')
                        else:
                            damage = random.randint(3,20)
                            input(f'\n{bulletpoint2}The {new_goons} landed a couple large blows to your stomach and did {damage} damage to your health. You managed to run away as fast as possible to a local street vendor nearby to hide.\n')
                            hero.health -= damage
                            menu()
                        if vendor_lady_object == 1: # Only accesses the vendor lady scenario if it's been turned on.
                            vendor_lady()
                        else:
                            secret_item()
                    else:
                        input(
                            f'\n{bulletpoint2}You ran over to the castle guards and the {new_goons} dissapeared.\n')
                        menu()
                        if current_heir.strip().lower() == hero_name.strip().lower():
                            input(f'\n{bulletpoint2}The guards yell to PROTECT THE HEIR! The guards then locate the {new_goons} and proceed to send them to jail. The guards then royally escort you into the castle immediately.\n')
                            new_path = input(
                                f'\n{bulletpoint}One of your advisors tells you that there is a trade mission that you should go on. You also feel like exploring the castle more. What do you do?\n')
                            if 'trade' in new_path.lower() or 'mission' in new_path.lower():
                                menu()
                                input(
                                    f'\n{bulletpoint2}There was new land to the south just recently discovered. Your mission was to conquer it and establish a colony on behalf of the Red Dragon Empire.\n')
                                trade_mission()
                            else:
                                menu()
                                passageway()
                        elif current_emperor.strip().lower() == hero.name.strip().lower():
                            input(f'\n{bulletpoint2}The guards yell to PROTECT THE EMPEROR! The guards then locate the street {new_goons}, beat them up, and then proceed to send them to jail. The guards then royally escort you into the castle immediately.\n')
                            new_path = input(
                                f'\n{bulletpoint}One of your advisors tells you that there is a trade mission that you may want to go on. You also feel like exploring the castle more. What do you do?\n')
                            if 'trade' in new_path.lower() or 'mission' in new_path.lower():
                                menu()
                                input(
                                    f'{bulletpoint2}There was new land to the south just recently discovered. Your mission was to conquer it and establish a colony on behalf of the Red Dragon Empire.\n')
                                trade_mission()
                            else:
                                menu()
                                passageway()
                        else:
                            # Guard Bribe
                            guard_bribe_ans = input(f'\n{bulletpoint}One of the guards suspects you as being an illegal foreigner from the neighboring enemy kingdom, but if you give him some bribe money, he\'ll turn a blind eye. Do you give him the money?\n')
                            if guard_bribe_ans.strip().lower() in yes:
                                bribe = random.randint(1,10)
                                if bribe >= 5:
                                    input(f'\n{bulletpoint2}You give the guard ${bribe}.\n') 
                                    hero.money -= bribe
                                    menu()
                                    empire_recruitment()
                                else:
                                    damage = random.randint(1,10)
                                    input(
                                        f'\n{bulletpoint2}You give the guard ${bribe}. He yells that this is barely anything and slams you into the ground dealing {damage} to you.\n')
                                    hero.health -= damage
                                    hero.money -= bribe
                                    menu()
                                    empire_recruitment()
                            else:
                                input(
                                    f'\n{bulletpoint2}He yells at you, calls you a peasant, and then proceeds to jail you in the castle dungeon.\n')
                                menu()
                                input('''
                                     ================================
                                      ||     ||<(.)>||<(.)>||     || 
                                      ||    _||     ||     ||_    || 
                                      ||   (__D     ||     C__)   || 
                                      ||   (__D     ||     C__)   ||
                                      ||   (__D     ||     C__)   ||
                                      ||   (__D     ||     C__)   ||
                                      ||     ||     ||     ||  dwb||
                                     ================================
                                ''')
                                #Jail Inmate
                                global body_part
                                body_part = 'arm'
                                body_part = input(f'In your jail cell, you see the inmate next to you with one only one...(type which body part)...body part:')
                                jail_inmate_ans = input(
                                    f'\n{bulletpoint}The inmate with only one {body_part} asks if you would like to be his friend?\n')
                                if jail_inmate_ans.strip().lower() in yes:
                                    nonlocal gamble_life
                                    snitch_ans = input(f'\n{bulletpoint}The inmate tells you that for the last year he\'s been digging a hole underneath his bed. He says it\'s finally ready and proposes for you to join him to make the escape. Do you snitch to the prisoner guards of the inmate\'s plans or join the inmate in the escape?\n')
                                    if snitch_ans.strip().lower() in ('tattle', 'tattle tale', 'tell the guards', 'tell the guards about the plan',) or 'snitch' in snitch_ans.strip().lower():
                                        input(
                                            f'\n{bulletpoint2}Initially, you were tempted by the idea of escape, but then you had a change of heart. You decided to tell the prisoner guards about the inmate\'s plans, hoping that they would take appropriate action.\n\n{bulletpoint2}The prisoner guards took the inmate into custody and decided to sentence him to death by hanging. They escorted him to the gallows, where he was to be hanged.\n\n{bulletpoint2}As the inmate was being hanged, you realized that you had made a terrible mistake. You had second thoughts about turning the inmate in, and you felt incredibly guilty about what had happened.\n\n{bulletpoint2}Fortunately, there was a rule in this prison that if you could win a game of hangman, they would release the prisoner.\n')
                                        if gamble_life == True:
                                            gamble_life = False
                                        hangman()
                                        input(f'\n{bulletpoint2}The prisoner guard is impressed by your quick thinking and resourcefulness. He offers to let you go on the condition that you join the ranks of the Red Dragon Empire.\n\n{bulletpoint2}The Red Dragon Empire is a powerful and feared organization that rules over a vast territory. They are known for their martial prowess and their ruthless tactics, and they are always looking for strong and capable individuals to join their ranks.\n\n{bulletpoint2}You are hesitant at first, but you realize that this may be your only chance to escape from the prison and start a new life. You agree to join the Red Dragon Empire, and the prisoner guard lets you go free.\n')
                                        gamble_life = True
                                        menu()
                                        empire_recruitment()
                                    else:
                                        input(
                                            f'\n{bulletpoint2}In the middle of the night, the inmate lifts his bed and you both went into the hole and made your way out from the sewers. You\'re free now! You and the inmate decide to wash up and then celebrate at a local tavern.')
                                        menu()
                                        best_friend()
                                else:
                                    input(f'\n{bulletpoint2}You sleep in the damp dark cell filled with dead rats and a repulsive stench. You wake up the next morning and discover your inmate has disappeared. You discover a hole underneath his bed, and prepare to make your escape...but just as you\'re about to leave, the guards force you out and says the captain wants to speak with you immediately!')
                                    menu()

                                    #Captain Offer
                                    captain_offer_ans = input(f'\n{bulletpoint}The captain says he\'s looking for some prisoners to help get rid of a local monster that\'s been causing problems. He asks if you would like to fight, and in return, you\'ll be freed and provided some money. Do you accept the offer?')
                                    if captain_offer_ans.strip().lower() in yes:
                                        menu()
                                        empire_recruitment()
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
            # Make hero money 0 if it is less than 0
            if hero.money < 0:
                hero.money = 0
            
            def items():

                print('Current Items:')
                current_items_list = ', '.join(
                    [f'{item}' for item in hero_items])
                print(current_items_list)
            
            # This is the menu display that would be shown throughout the game. It shows hero health, money, and a different display if hero health is under a certain amount.
            def display():
                print('\n')
                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                if hero.health <= 25:
                    print('█             █     █          █    ▐        ▐               █    █     █    ▐   █          █   █    █       █ █    ▐   ▐              ')
                    print('▐             ▐     ▐          ▐                             ▐    ▐     ▐        ▐          ▐   ▐    ▐       ▐ ▐                        ')
                
                print(f'█   Money: ${hero.money}                                                                                        Remaining Health: {hero.health}        █')
                if total_ending_count:
                    print(
                        f'Total Endings Found: {total_ending_count} out of {len(list_of_endings)}')
                items()
                print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
                if hero.health <=70:
                    print('        █             █     █          █    ▐        ▐               █    █     █    ▐   █          █   █    █       █ █    ▐   ▐              ')
                    print('        ▐             ▐     ▐          ▐                             ▐    ▐     ▐        ▐          ▐   ▐    ▐       ▐ ▐                        ')
                print('\n')
            display()
        menu()
        story()

    restart()
# The start of the game asks for the player to name their hero. This will be a global variable. They can also exit the game. 
def ask_hero_name():
    global hero_name
    hero_name = input('What is the name of your hero?')
    print(
        f'''
                  _____________________
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

