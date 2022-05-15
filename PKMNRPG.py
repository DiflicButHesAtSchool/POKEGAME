import json
import math
from fractions import Fraction
from string import ascii_lowercase as a_low
import random
import time
from ursina import *
from ursina.prefabs.health_bar import HealthBar
#from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
import urllib.request
from PIL import Image, ImageSequence
window.borderless = False


#imports for the json files (might make it a universal code depending on if i can get that to work)
with open('pokemonon.json', 'r') as p:
    pkmn = json.load(p)
with open('moves.json') as m:
    moves = json.load(m)
with open('types.json') as t:
    pkmntype = json.load(t)


#detecting to choose what language we want our pokemon to be named in
#Start = turtle.Screen()
#Start.screensize(100,10)
#Word = turtle.Turtle()
print('\n')
input('Please note that when you are setting everyting up all letters start \nuppercase unless you have the use of a number upercase the first letter ')
print('\n')
Lang = str(input("what language do you read pokemon names? \nopt(English, French, Japanese, and Chinese): "))
 
Lang = Lang.lower()
if Lang == "Gun":
    Lang = "???"
global move_seel

#asks user to see the poke dex for every single pokemon to get there number

print('\n')
noice = str(input('do you want to radomize your moves? Y/N: '))
choice = str(input('Would you like a random Pokemon? ("youll select otherwise") Y/N: '))
print('\n')

#dictionary slots for stats names types sprite and moves that i have for my pokemon
pslot1 = {
    "pokemon":[],
    "moveset":[
    
    ],
    "type":[],
    "hp":[],
    "attack":[],
    "defense":[],
    "sp. Attack":[],
    "sp. Defence":[],
    "speed":[],
    "image":[]
}
pslot2 = {
    "pokemon":[],
    "moveset":[

    ],
    "type":[],
    "hp":[],
    "attack":[],
    "defense":[],
    "sp. Attack":[],
    "sp. Defence":[],
    "speed":[],
    "image":[]
}
pslot3 = {
    "pokemon":[],
    "moveset":[

    ],
    "type":[],
    "hp":[],
    "attack":[],
    "defense":[],
    "sp. Attack":[],
    "sp. Defence":[],
    "speed":[],
    "image":[]
}
pslot4 = {
    "pokemon":[],
    "moveset":[

    ],
    "type":[],
    "hp":[],
    "attack":[],
    "defense":[],
    "sp. Attack":[],
    "sp. Defence":[],
    "speed":[],
    "image":[]
}
pslot5 = {
    "pokemon":[],
    "moveset":[

    ],
    "type":[],
    "hp":[],
    "attack":[],
    "defense":[],
    "sp. Attack":[],
    "sp. Defence":[],
    "speed":[],
    "image":[]
}
pslot6 = {
    "pokemon":[],
    "moveset":[

    ],
    "type":[],
    "hp":[],
    "attack":[],
    "defense":[],
    "sp. Attack":[],
    "sp. Defence":[],
    "speed":[],
    "image":[]
}
Enemy = {
    "pokemon":[],
    "moveset":[

    ],
    "type":[],
    "hp":[],
    "attack":[],
    "defense":[],
    "sp. Attack":[],
    "sp. Defence":[],
    "speed":[],
    "image":[]
}
def formula(x): #stat formula and equation , actually one of the easier things i did
    hpEV = int(random.randint(1,4))
    hpIV = int(random.randint(1,15))
    x['hp'][0] = str(floor(0.01 *(2 * int(x['hp'][0]) + hpIV + floor(0.25 *  hpEV))*80)+ 80 + 10)
    atEV = int(random.randint(1,4))
    atIV = int(random.randint(1,15))
    x['attack'][0] = str(floor(0.01 *(2 * int(x['hp'][0]) + atIV + floor(0.25 *  atEV)) * 80 + 5))
    spEV = int(random.randint(1,4))
    spIV = int(random.randint(1,15))
    x['speed'][0] = str(floor(0.01 *(2 * int(x['hp'][0]) + spIV + floor(0.25 *  spEV)) * 80 + 5))
    dfEV = int(random.randint(1,4))
    dfIV = int(random.randint(1,15))
    x['defense'][0] = str(floor(0.01 *(2 * int(x['hp'][0]) + dfIV + floor(0.25 *  dfEV)) * 80 + 5))
    sdEV = int(random.randint(1,4))
    sdIV = int(random.randint(1,15))
    x['sp. Defence'][0] = str(floor(0.01 *(2 * int(x['hp'][0]) + sdIV + floor(0.25 *  sdEV)) * 80 + 5))
    saEV = int(random.randint(1,4))
    saIV = int(random.randint(1,15))
    x['sp. Attack'][0] = str(floor(0.01 *(2 * int(x['hp'][0]) + saIV + floor(0.25 *  saEV)) * 80 + 5))



def stats(x,y): #pokemon state locatior and appender
    x['hp'].append(str(pkmn[y]['base']['HP']))
    x['attack'].append(str(pkmn[y]['base']['Attack']))
    x['defense'].append(str(pkmn[y]['base']['Defense']))
    x['sp. Attack'].append(str(pkmn[y]['base']['Sp. Attack']))
    x['sp. Defence'].append(str(pkmn[y]['base']['Sp. Defense']))
    x['speed'].append(str(pkmn[y]['base']['Speed']))
    formula(x)

def Poke_rando(x,idnum): #not actially a random pokemon , just selects a pokemon given the number either randomized or selected by user
    x['pokemon'].append(idnum + 1)
    x['pokemon'].append(str(pkmn[idnum]['name']['english']))
    y = idnum
    stats(x,y)
    x['type'].append(str(pkmn[idnum]['type']))
    x['image'].append(str(pkmn[idnum]['hires']))
    

possmoves = []
def SelectMoves(PKMN_type):
    z = 0
    for x in moves: #checks for every move 
        z = z + 1
        if z == 591:
            z = z + 3
        for t in PKMN_type['type']: #looks for both types of in every pokemon
            if(t == x['type']):         #checks if your pokemon tying is the same type as the move 
                if noice == 'N':
                    print(str(z) + " " + str(x["ename"]) + 'Power: ' +str(x['power']) + ' Accuracy: ' + str(x['accuracy']))
                possmoves.append(x['id'])
    
def calMove(pokemon_class): #selects random move 4 times
    for i in range(4):
        mid = random.choice(possmoves)
        if mid > 590:
            pokemon_class['moveset'].append(moves[mid - 4]) #the moves skip and dont show up as the correct number so to correct the numbers we add one for every instance of above 590 and subtract 5 if they are below 590
        if mid < 590:
            pokemon_class['moveset'].append(moves[mid - 1])  
    possmoves.clear()
def makeMove(pokemon_class, movenu): #selection for moves based on manual labor
    if movenu >= 590:
        pokemon_class['moveset'].append(moves[movenu - 4])
    if movenu <= 590:
        pokemon_class['moveset'].append(moves[movenu -1])  
    possmoves.clear()

if choice == 'Y': #randomly selects a pokemon out of 808 (gen 8 doesnt have stats in there dicts)
    global idnum
    idnum = random.randint(0,808)
    Poke_rando(pslot1,idnum)
    print('your random pokemon is: ' + str(pslot1['pokemon']))
    print(pslot1)
    SelectMoves(pkmn[idnum])
def manualPkmn(slot): #manualy select a pokemon
    dex = str(input('would you like to see the entire poke dex? Y/N: '))
    if dex == 'Y':
        for x in range(809):
            print(str(pkmn[x]['id']) + str(pkmn[x]['name'][Lang]))
    global dexno
    dexno = int(input("enter pokedex number for pokemon you want to use: "))
    dexno = dexno - 1
    Poke_rando(slot,dexno)
    SelectMoves(pkmn[dexno])
def manualMoves(slot): #manual selection of moves
    SelectMoves(pkmn[dexno])
    print('select from these moves')
    for x in range(4):
        moved = int(input('move number: '))
        makeMove(slot, moved)

if choice == 'N': #runs function to manually select a pokemon and asks if you random moves
    manualPkmn(pslot1)

    
if noice == 'Y':       #auto picks moves for you based on the type of your pokemon
    calMove(pslot1)
if noice == 'N':       #allows you to select a move manually and shows the moves only by the type of your pokemon
    manualMoves(pslot1)
    choice = 'Y'
    
    



   
class UI(Button): # this is what allows a simple creation for the buttons like attacking and etc
    def __init__(self,UItext, x,y, func):
        super().__init__(x = x,
        y = y,
        scale = .15,
        color = color.cyan.tint(-.4),
        text = UItext,
        on_click = func
        )
class mv(Button): #move buttons 
    def __init__(self,UItext, x,y, func,g,h, color):
        super().__init__(x = x,
        y = y,
        scale = .15,
        color = color,
        text = UItext,
        on_click = lambda: func(g,h)
        )
def dictionaryclear(slot): # clears a dictionary so there can be a re roll or re write
    for y in slot:
        slot[y].clear()
def createEnemy(): #defines how the enemy's states are created
    noice = 'enmpy'
    idnum = random.randint(0,809)
    Poke_rando(Enemy,idnum) 
    SelectMoves(pkmn[idnum]) 
    calMove(Enemy)

#make this into a list
global activePokemon
activePokemon = pslot1
print(activePokemon['pokemon'])
startV1 = str(input('\n''Your ' + str(pslot1['pokemon'][1]) + ' is ' + str(pslot1['type'][0]) + " and knows " + str(pslot1['moveset'][0]['ename']) + " " + str(pslot1['moveset'][1]['ename']) + " " + str(pslot1['moveset'][2]['ename']) +  " " + str(pslot1['moveset'][3]['ename']) + "are you ready to start your adventure Y/N"))

if startV1 == 'Y': #this is how the game starts and if you dont want to start you can pick your pokemon again
    createEnemy()
    print('you will be fighting ' + Enemy['pokemon'][1])
if startV1 == "N":
    createEnemy()
    option = str(input('do you want to select a pokemon? Y/N: '))
    dictionaryclear(pslot1)
    if option == 'Y':
        print('\ndo you reall think im going to code all that by the due date')
        option = "N"
    if option == "N":
        idnum = random.randint(0,808)
        Poke_rando(pslot1,idnum)
        print('your random pokemon is: ' + str(pslot1['pokemon']))
        print(pslot1)
        SelectMoves(pkmn[idnum])
    print('you will be fighting ' + Enemy['pokemon'][1])

global Attack
global Party
global Swap
global Item

def ridof(x,y,z,a): # checks for a entity and makes it disapear from the screen to allow new ui to spawn
    
    x.visible_self = False
    x.text = ' '
    y.visible_self = False
    y.text = ' '
    z.visible_self = False
    z.text = ' '
    a.visible_self = False
    a.text = ' '
    x.disabled = True
    y.disabled = True
    z.disabled = True
    a.disabled = True
def ridrid(): #used in a button because i couldnt figure out how to use it correctly with defined objects
    ridof2(move1, move2, move3, move4,Back)
def ridridrid(): #if game ever needs to return values back like health this is the code needed (i think)
    ridof2(move1, move2, move3, move4,Back)
    Playagain.disabled = True
    Playagain.visible_self = False
    Playagain.text = ' '
    Panel.disabled = True
    Panel.visible_self = False
    Panel.text = ' '
    createEnemy()
    Hpe.value = Enemy['Hp']
    Hp1.value = pslot1['Hp']
def ridof2(x, y, z, a,b): #a disabler for instances that need to go to the first menu 
    x.visible_self = False
    x.text = ' '
    y.visible_self = False
    y.text = ' '
    z.visible_self = False
    z.text = ' '
    a.visible_self = False
    a.text = ' '
    x.disabled = True
    y.disabled = True
    z.disabled = True
    a.disabled = True
    b.disabled = True
    b.visible_self = False
    b.text = ' '
    ofrid()
def ofrid(): #enables first menu button screen
    Attack.visible_self = True
    Attack.text = 'Attack'
    Party.visible_self = True
    Party.text = 'Party'
    Swap.visible_self = True
    Swap.text = 'Swap'
    Item.visible_self = True
    Item.text = 'Item'
    Attack.disabled = False
    Item.disabled = False
    Swap.disabled = False
    Party.disabled = False

def blank(x, m):
    x = 1
    print('hi')
    speedCal(pslot1,Enemy,m,Hpe)

#defines how to make the move buttons and finds what color they need to be in the game themselves
def moves():
    global move1 
    global move2
    global move3
    global move4
    global Back
    for x in pkmntype:
        if x['name'] == pslot1['moveset'][0]['type']:
            global mcolor
            if x['name'] == 'Fire':
                mcolor = color.red
            if x['name'] == 'Water':
                mcolor = color.blue
            if x['name'] == 'Grass':
                mcolor = color.green
            if x['name'] == 'Ice':
                mcolor = color.cyan
            if x['name'] == 'Ground':
                mcolor = color.peach
            if x['name'] == 'Electric':
                mcolor = color.yellow
            if x['name'] == 'Rock':
                mcolor = color.gold
            if x['name'] == 'Flying':
                mcolor = color.white10
            if x['name'] == 'Dark':
                mcolor = color.light_gray
            if x['name'] == 'Psychic':
                mcolor = color.salmon
            if x['name'] == 'Bug':
                mcolor = color.lime
            if x['name'] == 'Ghost':
                mcolor = color.violet
            if x['name'] == 'Fairy':
                mcolor = color.pink
            if x['name'] == 'Steel':
                mcolor = color.gray
            if x['name'] == 'Dragon':
                mcolor = color.blue
            if x['name'] == 'Normal':
                mcolor = color.white
            if x['name'] == 'Fighting':
                mcolor = color.brown
            if x['name'] == 'Poison':
                mcolor = color.magenta
        if x['name'] == pslot1['moveset'][3]['type']:
            global m3color
            if x['name'] == 'Fire':
                m3color = color.red
            if x['name'] == 'Water':
                m3color = color.blue
            if x['name'] == 'Grass':
                m3color = color.green
            if x['name'] == 'Ice':
                m3color = color.cyan
            if x['name'] == 'Ground':
                m3color = color.peach
            if x['name'] == 'Electric':
                m3color = color.yellow
            if x['name'] == 'Rock':
                m3color = color.gold
            if x['name'] == 'Flying':
                m3color = color.white10
            if x['name'] == 'Dark':
                m3color = color.light_gray
            if x['name'] == 'Psychic':
                m3color = color.salmon
            if x['name'] == 'Bug':
                m3color = color.lime
            if x['name'] == 'Ghost':
                m3color = color.violet
            if x['name'] == 'Fairy':
                m3color = color.pink
            if x['name'] == 'Steel':
                m3color = color.gray
            if x['name'] == 'Dragon':
                m3color = color.blue
            if x['name'] == 'Normal':
                m3color = color.white
            if x['name'] == 'Fighting':
                m3color = color.brown
            if x['name'] == 'Poison':
                m3color = color.magenta
        if x['name'] == pslot1['moveset'][2]['type']:
            global m2color
            if x['name'] == 'Fire':
                m2color = color.red
            if x['name'] == 'Water':
                m2color = color.blue
            if x['name'] == 'Grass':
                m2color = color.green
            if x['name'] == 'Ice':
                m2color = color.cyan
            if x['name'] == 'Ground':
                m2color = color.peach
            if x['name'] == 'Electric':
                m2color = color.yellow
            if x['name'] == 'Rock':
                m2color = color.gold
            if x['name'] == 'Flying':
                m2color = color.white10
            if x['name'] == 'Dark':
                m2color = color.light_gray
            if x['name'] == 'Psychic':
                m2color = color.salmon
            if x['name'] == 'Bug':
                m2color = color.lime
            if x['name'] == 'Ghost':
                m2color = color.violet
            if x['name'] == 'Fairy':
                m2color = color.pink
            if x['name'] == 'Steel':
                m2color = color.gray
            if x['name'] == 'Dragon':
                m2color = color.blue
            if x['name'] == 'Normal':
                m2color = color.white33
            if x['name'] == 'Fighting':
                m2color = color.brown
            if x['name'] == 'Poison':
                m2color = color.magenta
        if x['name'] == pslot1['moveset'][1]['type']:
            global m1color
            if x['name'] == 'Fire':
                m1color = color.red
            if x['name'] == 'Water':
                m1color = color.blue
            if x['name'] == 'Grass':
                m1color = color.green
            if x['name'] == 'Ice':
                m1color = color.cyan
            if x['name'] == 'Ground':
                m1color = color.peach
            if x['name'] == 'Electric':
                m1color = color.yellow
            if x['name'] == 'Rock':
                m1color = color.gold
            if x['name'] == 'Flying':
                m1color = color.white10
            if x['name'] == 'Dark':
                m1color = color.light_gray
            if x['name'] == 'Psychic':
                m1color = color.salmon
            if x['name'] == 'Bug':
                m1color = color.lime
            if x['name'] == 'Ghost':
                m1color = color.violet
            if x['name'] == 'Fairy':
                m1color = color.pink
            if x['name'] == 'Steel':
                m1color = color.gray
            if x['name'] == 'Dragon':
                m1color = color.blue
            if x['name'] == 'Normal':
                m1color = color.white33
            if x['name'] == 'Fighting':
                m1color = color.brown
            if x['name'] == 'Poison':
                m1color = color.magenta
    move1 = mv(str(pslot1['moveset'][0]['ename']), -.65, -.25,blank,1,0,mcolor)
    move2 = mv(str(pslot1['moveset'][1]['ename']), -.5, -.25,blank,1, 1,m1color)
    move3 = mv(str(pslot1['moveset'][2]['ename']), -.5, -.40,blank,1, 2,m2color)
    move4 = mv(str(pslot1['moveset'][3]['ename']), -.65, -.40,blank,1, 3,m3color)
    Back = UI('Back', .80, -.25,ridrid)

def End():
    ridof(Attack, Item, Swap, Party)
    print("yeah so im not your made do it yoruself")
def Fight():
    ridof(Attack, Item, Swap, Party)
    moves()
def Object():
    ridof(Attack, Item, Swap, Party)
    print("You look into your bag and find nothing because you havent picked up anything")
def Replace():
    ridof(Attack, Item, Swap, Party)
    print("You open your bag and notice oh yeah i didnt catch anything so i own nothing ha ha")





    
#these are the buttons with locations functions that read text and action that impact the game
Attack = UI("Attack", .65, -.25,Fight)
Item = UI("Item", .5, -.25,Object)
Swap = UI("Swap", .5, -.40,Replace)
Party = UI("Party", .65, -.40,End)


#calls the pokemon image found on the internet and stores it as a png and so it can be used in game
PKMNACTIVE = pslot1['image'][0]
"""
if activePokemon['pokemon'][0] < 649:
    spriteChange = str(input('would you like to opt in a new sprite? Y/N: '))
    spriteChange = spriteChange.upper()
    if spriteChange == 'Y':
        PKMNACTIVE = "https://img.pokemondb.net/sprites/black-white/back-normal/" + str(activePokemon['pokemon'][1]).lower() + ".png"
"""

urllib.request.urlretrieve( 
            PKMNACTIVE,
            "gfg.png")
ACTIVEENEMY = Enemy['image'][0]
urllib.request.urlretrieve(
            ACTIVEENEMY,
            "ghg.png")





class Pokemon(Button): #this the code that allows my pokemon to spawn and made in a way so i dont have to repeat code
    def __init__(self, x,y,z,pshape, ptexture, pscale ):
        position = x,y,z
        super().__init__(
            parent = scene,
            position = position,
            model = pshape,
            origin_y = 0.5,
            texture = ptexture,
            color=color.color(0,0,1),
            scale = pscale
        )
        
#pokemon seen on screen functions
slot1 = Pokemon(-2,0.20,-5,'cube','gfg.png',2.5)
Enemyed = Pokemon(4,1.75,3,'cube','ghg.png',1.5)


class Health(HealthBar): #health bar code
    def __init__(self,hmax_value,x,y):
        super().__init__(
            bar_color = color.lime.tint(-.25),
            roundness = .5,
            scale = (.5, .06),
            max_value = hmax_value,
            x = x,
            y = y
        )
        
        
global Hp1
global Hpe
Hp1 = Health(int(pslot1['hp'][0]), -.4, -.3)  #prints out the healthbar
Hpe = Health(int(Enemy['hp'][0]), .4, .3)

def effectType(pktype,m, poke,deffending): #calculates supereffectiveness 
    global effective
    for x in pkmntype:
        if poke['moveset'][m]['type'] == x['name']:
            for t in x['weaknesses']:
                if t == deffending['type'][0][0]:
                    effective = 2
                if t == deffending['type'][0][1]:
                    effective = 2
            for y in x['strengths']:
                if y == deffending['type'][0][1]:
                    effective = .5
                if y == deffending['type'][0][0]:
                    effective = .5
        else:
            effective = 1

def AttackAction(pwer, A, D, pktype,m,attacking,deffending,hp): #
    print(A)
    print(D)
    effectType(pktype,m,attacking,deffending)
    if pwer != None:
        d = 160/5 + 2 
        a = d * pwer * int(A)/int(D)
        e = a/50 + 2
        damage = e * effective
        print(str(damage) + " wow thats alot of damage")
        hp.value -= damage
    else:
        print('HA! nothing happend')
    
def playmove():
    movenum = random.randint(0,3)
    AttackAction(Enemy['moveset'][movenum]['power'], Enemy['attack'][0], pslot1['defense'][0], Enemy['type'][0],movenum,Enemy,pslot1,Hp1)
def checkHp():
    global Playagain
    if Hp1.value <= 0:
        global Panel
        Panel(z=1, scale=10, model='quad')
        t = Text(f'player\nlost!', scale=3, origin=(0,0), background=True)
        t.create_background(padding=(.5,.25), radius=Text.size/2)
        t.background.color = color.blue
        move1.visible_self = False
        move1.text = ' '
        move2.visible_self = False
        move2.text = ' '
        move3.visible_self = False
        move3.text = ' '
        move4.visible_self = False
        move4.text = ' '
        move1.disabled = True
        move2.disabled = True
        move3.disabled = True
        move4.disabled = True
        Back.disabled = True
        Back.visible_self = False
        Back.text = " "
    elif Hpe.value <= 0:
        Panel(z=1, scale=10, model='quad')
        t = Text(f'player\nwon!', scale=3, origin=(0,0), background=True)
        t.create_background(padding=(.5,.25), radius=Text.size/2)
        t.background.color = color.blue
        move1.visible_self = False
        move1.text = ' '
        move2.visible_self = False
        move2.text = ' '
        move3.visible_self = False
        move3.text = ' '
        move4.visible_self = False
        move4.text = ' '
        move1.disabled = True
        move2.disabled = True
        move3.disabled = True
        move4.disabled = True
        Back.disabled = True
        Back.visible_self = False
        Back.text = " "

def speedCal(pkmn1,enmy,m,hp): #checks to see who goes first you or your Enemy
    if int(pkmn1['speed'][0]) >= int(enmy['speed'][0]):
        print("Hi your faster")
        AttackAction(pkmn1['moveset'][m]['power'], pkmn1['attack'][0], enmy['defense'][0], pkmn1['type'][0],m,pkmn1,enmy,hp)
        checkHp()
        playmove()
        checkHp()
        #Hpe.value - Uturn
    elif int(pkmn1['speed'][0]) <= int(enmy['speed'][0]):
        print("Hi your slowers")
        playmove()
        checkHp()
        AttackAction(pkmn1['moveset'][m]['power'], pkmn1['attack'][0], enmy['defense'][0], pkmn1['type'][0],m,pkmn1,enmy,hp)
        checkHp()
        #Hp1.value - Eturn()


#while int(pslot1['hp'][0]) > 0:



#player = FirstPersonController()

app.run()



