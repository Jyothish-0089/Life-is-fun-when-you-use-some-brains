'''Okay lets try to make a game here.. more like a turn based RPG?? I actually dont know what im gonna
do i dont have any ideas atm so ill just wait until one pops into my mind'''
'''Ill note down all the thoughts here then maybe i can change it to code.. hopefully XD'''
'''Elements: Fire , Water , Ice, Earth , Dark , Light
Alright so i decided to change the elements cuz the previous elements werent balancing the game 
its FIRE , WATER, EARTH, AIR AND SPACE now
Dmg statistics.. I'm too lazy to explain I'll type it later pls-
Alright here it is below THAT WAS EXHAUSTING TO TYPE


  UPDATE:  YOOO- coming back after more than a year, THIS GAME WAS DUMB LMAO BUT DAYUM I TYPED A LOT

---Battle element reactions---
Fire -> Fire 
Fire -> Water (25% more dmg)
Fire -> Earth
Fire -> Air   (15% more dmg)
Fire -> Space

Water -> Fire  (50% more dmg)
Water -> Water
Water -> Earth (25% more dmg)
Water -> Air
Water -> Space

Earth -> Fire  (25% more dmg)
Earth -> Water (15% more dmg)
Earth -> Earth 
Earth -> Air 
Earth -> Space (5% more dmg)

Air -> Fire  (50% more dmg)
Air -> Water 
Air -> Earth
Air -> Air
Air -> Space (50% more dmg)

Space -> Fire  (50% more dmg)
Space -> Water (15% more dmg)
Space -> Earth
Space -> Air   (50% more dmg)
Space -> Space
'''
print("Pick your Element, Player1\n1.FIRE  2.WATER  3.EARTH  4.AIR  5.SPACE\n")
pe1 = int(input())
if(pe1 == 1):
    pe1 = 'Fire'
elif(pe1 == 2):
    pe1 == 'Water'
elif(pe1 == 3):
    pe1 == 'Earth'
elif(pe1 == 4):
    pe1 == 'Air'
elif(pe1 == 5):
    pe1 == 'Space'
print("Pick your Element, Player1\n1.FIRE  2.WATER  3.EARTH  4.AIR  5.SPACE\n")
pe2 = int(input())
if(pe2 == 1):
    pe2 = 'Fire'
elif(pe2 == 2):
    pe2 = 'Water'
elif(pe2 == 3):
    pe2 = 'Earth'
elif(pe2 == 4):
    pe2 = 'Air'
elif(pe2 == 5):
    pe2 = 'Space'
print("Player_1 chose ",pe1)
print("Player_2 chose ",pe2)

p1hp = 10000
p2hp = 10000
atk = 1500

import random
healstart = 500
healend = 2000
heal = random.randint(healstart,healend)
def p1_healing():
    print("Player_1 Healed +", heal)
    p1hp = p1hp + heal
    print("Player_1 Health: ", p1hp)
def p2_healing():
    print("Player_2 Healed +", heal)
    p2hp = p2hp + heal
    print("Player_1 Health: ", p1hp)
def display_hp():
    print("Player_1: ", p1hp)
    print("Player_2: ", p2hp)
def p1surrender():
    print("Player_1 Surrendered")
    print("Player_2 WINS!!")
def p2surrender():
    print("Player_2 Surrendered")
    print("Player_1 WINS!!")
chance = 1
hp = min(p1hp,p1hp)
turns = 2
while(hp>0):
    hp = min(p1hp,p2hp)
    print("\nPlayer_1, Choose an action below\n1.ATTACK     2.HEAL     3.SURRENDER")
    action = int(input())
    if(turns%2 == 0):
        '''--------------------------FIRE ELEMENT--------------------'''
        if(pe1 == 'Fire'):
            if(pe2 == 'Fire'):
                if(action == 1):
                    print("Player_1 Attacks Player_2\n{No effect}")
                    p2hp = p2hp-atk
                    display_hp()
                if(action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if(action == 3):
                    p1surrender()
                    break
            if(pe2 == 'Water'):
                if(action == 1):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 25%}")
                    p2hp = (p2hp-atk)-((25/100)*atk)
                    display_hp()
                if(action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if(action == 3):
                    p1surrender()
                    break
            if(pe2 == 'Earth'):
                if(action == 1):
                    print("Player_1 Attacks Player_2\n{No effect}")
                    p2hp = p2hp-atk
                    display_hp()
                if(action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if(action == 3):
                    p1surrender()
                    break
            if(pe2 == 'Air'):
                if(action ==1 ):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 15%}")
                    p2hp = p2hp-atk-((15/100)*atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if(pe2 == 'Space'):
                if(action == 1):
                    print("Player_1 Attacks Player_2\n{No effect}")
                    p2hp = p2hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
        if(pe1 == 'Water'):
            if(pe2 == 'Fire'):
                if(action == 1):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 50%}")
                    p2hp = p2hp-atk-((50/100)*atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Water'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{No effect}")
                    p2hp = p2hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Earth'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 25%}")
                    p2hp = p2hp-atk-((25/100)*atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Air'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{No effect}")
                    p2hp = p2hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Space'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{No effect}")
                    p2hp = p2hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            '''---------------------------EARTH ELEMENT---------------------------'''
        if(pe1 == 'Earth'):
            if (pe2 == 'Fire'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 25%}")
                    p2hp = p2hp - atk - ((25 / 100) * atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Water'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 15%}")
                    p2hp = p2hp - atk - ((15 / 100) * atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Earth'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{No effect}")
                    p2hp = p2hp-atk
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Air'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{No effect}")
                    p2hp = p2hp - atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Space'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 5%}")
                    p2hp = p2hp - atk - ((5 / 100) * atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            '''------------------------------------AIR ELEMENT---------------------------------------'''
        if(pe1 == 'Air'):
            if (pe2 == 'Fire'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 50%}")
                    p2hp = p2hp - atk - ((50 / 100) * atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Water'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 5%}")
                    p2hp = p2hp - atk - ((5 / 100) * atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Earth'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{No effect}")
                    p2hp = p2hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Air'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{No effect}")
                    p2hp = p2hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Space'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 50%}")
                    p2hp = p2hp - atk - ((50 / 100) * atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
        '''-----------------------------SPACE ELEMENT---------------------------------'''
        if(pe1 == 'Space'):
            if (pe2 == 'Fire'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 50%}")
                    p2hp = p2hp - atk - ((50 / 100) * atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Water'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 15%}")
                    p2hp = p2hp - atk - ((15 / 100) * atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Earth'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{No effect}")
                    p2hp = p2hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Air'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{Dmg increased by 50%}")
                    p2hp = p2hp - atk - ((50 / 100) * atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break
            if (pe2 == 'Space'):
                if (action == 1):
                    print("Player_1 Attacks Player_2\n{No effect}")
                    p2hp = p2hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_1 Healed +", heal)
                    p1hp = p1hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p1surrender()
                    break




    if(turns%2 == 1):
        '''--------------------------FIRE ELEMENT--------------------'''
        if(pe2 == 'Fire'):
            if(pe1 == 'Fire'):
                if(action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if(action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if(action == 3):
                    p2surrender()
                    break
            if(pe1 == 'Water'):
                if(action == 1):
                    print("Player_2 Attacks Player_1\n{Dmg increased by 25%}")
                    p1hp = (p1hp - atk) - ((25 / 100) * atk)
                    display_hp()
                if(action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if(action == 3):
                    p2surrender()
                    break
            if(pe1 == 'Earth'):
                if(action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if(action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if(action == 3):
                    p2surrender()
                    break
            if(pe1 == 'Air'):
                if(action ==1 ):
                    print("Player_2 Attacks Player_1\n{Dmg increased by 15%}")
                    p1hp = (p1hp-atk)-((15/100)*atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if(pe1 == 'Space'):
                if(action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
        if(pe2 == 'Water'):
            if(pe1 == 'Fire'):
                if(action == 1):
                    print("Player_2 Attacks Player_1\n{Dmg increased by 50%}")
                    p1hp = p1hp-atk-((50/100)*atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Water'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Earth'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{Dmg increased by 25%}")
                    p1hp = (p1hp-atk)-((25/100)*atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Air'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Space'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            '''---------------------------EARTH ELEMENT---------------------------'''
        if(pe2 == 'Earth'):
            if (pe1 == 'Fire'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{Dmg increased by 25%}")
                    p1hp = (p1hp - atk) - ((25 / 100) * atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Water'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{Dmg increased by 15%}")
                    p1hp = (p1hp-atk)-((15/100)*atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Earth'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Air'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{Dmg increased by 5%}")
                    p1hp = (p1hp - atk) - ((5 / 100) * atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Space'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            '''------------------------------------AIR ELEMENT---------------------------------------'''
        if(pe2 == 'Air'):
            if (pe1 == 'Fire'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{Dmg increased by 50%}")
                    p1hp = (p1hp - atk) - ((50 / 100) * atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Water'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Earth'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Air'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Space'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{Dmg increased by 50%}")
                    p1hp = (p1hp-atk)-((50/100)*atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
        '''-----------------------------SPACE ELEMENT---------------------------------'''
        if(pe2 == 'Space'):
            if (pe1 == 'Fire'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{Dmg increased by 50%}")
                    p1hp = (p1hp-atk)-((50/100)*atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Water'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{Dmg increased by 15%}")
                    p1hp = (p1hp-atk)-((15/100)*atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Earth'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Air'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{Dmg increased by 50%}")
                    p1hp = (p1hp-atk)-((50/100)*atk)
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
            if (pe1 == 'Space'):
                if (action == 1):
                    print("Player_2 Attacks Player_1\n{No effect}")
                    p1hp = p1hp-atk
                    display_hp()
                if (action == 2):
                    heal = random.randint(healstart, healend)
                    print("Player_2 Healed +", heal)
                    p2hp = p2hp + heal
                    print("Player_1 Health: ", p1hp)
                if (action == 3):
                    p2surrender()
                    break
    turns = turns + 1

