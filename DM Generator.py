import random
import sys

# name creation
prefix = ['De','Sin','Kum','Vin','Che','Fre','Roy','Tib','Cen','San','Grab','Gru','Gre','Dir','Vlad','Var','Tok','Tol','Mac','Ada','Sa','Dm','Py','Al','Ar',
          'Jo','Sp','Ti','Gar','Mat','Za','Jer','Att','Bra','Bro','Bri','Re','Ger','Sw','Con','Her','Wi']
middle = ['il','om','aral','et','er','io','deh','ia','ra','th','ud','ub','row','i','ic','ol',]
suffix = ['an','pi','non','is','ich','us','le','wood','ie','elm','der','osk','oft','obe','eim','ra','on','rey','n','or','el','i','etta','anna','ak','rra','ag',
          'ko','mey','bert',]

# npc creation
appearance = ["lots of jewelery","piercings","flamboyant or colorful clothes",
              "Formal attire", "dirty ratty clothes", "Scar/s", "missing teeth",
              "missing fingers", "unusual eye color or 2 different colors",
              "Tattoos","Birthmark","unusual skin color","Bald","Unusual hair color",
              "nervous twitch", "distinctive nose", "good or bad posture", "beautiful",
              "ugly", "nerdy/ bookworm",'long braided blonde hair','very tan','bad posture','very curly hair','allways smiling',
              'allways frowning','wrinkly/old', 'child', 'fake hand/ wood or metal hook']
gender = ['Male', 'female']
race = ["human","elf",'high elf', "halfling", "gnome", "dragonborn", "lizardfolk", "Tiefling",
        "dwarf","orc",'half-elf',]
skilled = ["strong", "agile/graceful","smart","wise/ spiritual","charasmatic", 'hard-ass', 'jokster/prankster']
unskilled = ["weak", "clumsy", "dumb", "oblivious", "dull/ boring"]
talent = ['plays an instrument', 'multi langual', 'really lucky', 'perfect memory',
          'animal lover','great with children','great puzzle solver', 'great at one game',
          'great at drawing', 'great at painting', 'great singer', 'great at drinking',
          'master carpenter','expert cook','skilled actor','dancer','knows thieves cant']
mannerism = ['prone to sing, hum or whistle','speaks in rhyme','speak in low or high voice',
             'drunk ','speaks loudly','whispers','uses long words','uses wrong words','fidgets',
             'constantly jokes','expects doomsday','squints(clint eastwood)','spacey (stares off alot)',
             'chewing','pacing','tap fingers','twist hair', 'bite fingernails', 'makes big hand gestures',
             'never knows the date/ time', 'allways excited','act like on crack','a deep thinker', 'stretches the truth', 'clean freak', 'horder']
ideals = ['dedicated to life goal','protective of family','protective of coworkers','loyal to clan/ employer',
          'deep in love','drawn to a place of interest','protective of a possession','seeking revenge', 'very religious']
flaw = ['secret lover ', 'prone to falling in love', 'enjoys luxury ','Arrogant','envies others things',
        'greedy','prone to rage','has a powerful enemy','phobia','previous scandalous history','secret misdeed',
        'dumbly brave', 'lazy', 'never surrenders', 'married', 'in an abusive relationship', 'in a relationship', 'veryyy single', 'single', 'irrational fear of dumb thing']

# tavern creation
the = 'The '
description = ['cruel ','shaking ','salty ','juicy ','happy ','green ','red ','grey ',
         'Brass ','gold ','armed ','even ','black ','elven ','silver ','dwarvish ','hellish ','crusty ','silver ','tarnished ', 'weathered ','targets ','crumbling ','crimson ',
               'gems ','invisible ','blackened ','charred ','wet ','arrogant ']
animal = ['soldiers ','dragons ','dwarfs ','beholders ','hawks ','hunters ','steeds ','oil lamps ',
         'ravens ','harpy ','manticores ','pixies ','krakens ','giants ','donkeys ',
         'griffon ','rusty ','rats ', 'racoons ', 'spiders ','banshee ','devils ','lichs ','owlbears ','centaurs ']
end = ['pub','inn','hub','den ','bar ','saloon ','house ','eye ','head ','hideout ','hole ', 'watering hole ','lair ']

# city creation
shop = ['magic shop','map shop','armory','blacksmith','food market','general store','clothing store','book store',
        'pet store','jeweler','temple','live stock store', 'shipmaker', 'carpenter','taxidermist','potion shop']

tavern_traits = ['high class', 'shit hole', 'gang hangout', 'running out of supplies', 'average town inn', 'secret club running','well furnished', 'big', 'small','busy', 'ghost town']

city_reason = ['growing spices', 'good hardwood', 'lumber', 'grape growing', 'corn and grain growing', 'fishing', 'hunting', 'oil field', 'mineral mines','magic mines',
               'fair weather(vacation spot)','metal mines', 'precious metal mines', 'coal mines', 'on trade route']
#idea creation
pronoun = ['you ','we ','he ','she ','good guys ','bad guys ']
verb = ['need ','took ','stole ','had ','kept ','killed ','fought ','deliver ','discover ','hates ','likes ','is vunerible to ','is immune to ','explored ','expected ','forgot ','forbid ','gave ','froze ','hid ','lead ','learn ']
noun = ['sword','bow','eye','girl','child','sickness','health','goverment','sibling','orb','magic item','magic','world','hell']
def start():
    pick = input('what do you want to generate?\n type "npc" for random npc \n type "tavern" for random tavern \n type "name" for random name \n type "end" to close\n type "dice" to roll a die \n type "city" to gen city\n type "shop" to gen shops \n type "idea" to gen idea spark\n: ')
    if pick.lower() == "npc":
        gen_npcs()
    elif pick.lower() == "tavern":
        gen_taverns()
    elif pick.lower() == "name":
        gen_names()
    elif pick.lower() == "end":
        sys.exit()
    elif pick.lower() == 'dice':
        roll_dice()
    elif pick.lower() == 'city':
        gen_city()
    elif pick.lower() == 'shop':
        gens = int(input('how many shops do you want to make? : '))
        gen_shops(gens)
        start()
    elif pick.lower() == 'idea':
        gen_idea()
    else:
        print('Please try again...')
        print()
        start()


def gen_idea():
    loop = int(input('how many ideas? : '))
    for gen in range(loop):
        gen = random.choice(pronoun) + random.choice(verb)+ random.choice(noun)
        print(gen)
    print()
    start()



def gen_name():

        choice = random.randrange(1,5)
        if choice == 1:
            name = random.choice(prefix) + random.choice(middle) + random.choice(suffix)
        elif choice == 2:
            name = random.choice(prefix) + random.choice(suffix)
        elif choice == 3:
            name = random.choice(prefix) + random.choice(middle)
        elif choice == 4:
            name = random.choice(middle) + random.choice(suffix)
        return name
        print()




def gen_names():
    numofnames = input('how many names? : ')
    
    for name in range(int(numofnames)):
        name = gen_name()
        print(name)
        print()
    start()




def gen_shops(_num):
    for store in range(_num):
        name = gen_npc()
        print(random.choice(shop))
        print()
        print("    Owner: " )
        for trait in name:
            print(trait)
        print('---------------------------------------------------------------')
        print()




def gen_tavern():

    print()
    gen_begin = random.choice(description)
    gen_mid = random.choice(animal)
    gen_end = random.choice(end)
    choose = random.randrange(1,4)
    tav_trait = random.choice(tavern_traits)
    if choose == 1:
        tavern = (the + gen_begin + gen_end)
    elif choose == 2:
        tavern = (the + gen_begin + gen_mid)
    else:
        tavern = (the + gen_begin + gen_mid + gen_end)
        
    return tavern, tav_trait



def gen_taverns():

    loop = int(input('how many names do you want?'))
    print()
    for gen in range(loop):
        tavern, tav_trait = gen_tavern()
        print(tavern + " : " + tav_trait)
        print()
    start()


def gen_npc():
    npc = []
    npc.append(gen_name())
    npc.append("")
    npc.append(random.choice(appearance))
    npc.append(random.choice(race))
    npc.append(random.choice(gender))
    npc.append(random.choice(skilled))
    npc.append(random.choice(unskilled))
    npc.append(random.choice(talent))
    npc.append(random.choice(mannerism))
    npc.append(random.choice(ideals))
    npc.append(random.choice(flaw))
    return npc

  

def gen_npcs():
    loop = int(input('how many npcs do you want? : '))
    for gen in range(loop):
        npc = gen_npc()
        for trait in npc:
            print(trait)
        print()
    start()




def roll_dice():
    dice_type = int(input('what die do you want to role? : '))
    rolls = int(input('how many dice? : '))
    total = 0
    for roll in range(rolls):
        roll = random.randrange(1,(dice_type + 1))
        print(roll)
        total += roll
    print('total: ' + str(total))
    print()
    start()




def gen_city():
    city_size = input('what size city do you want? type s,m or l. : ')
    if city_size.lower() == 's':
        total_inns = 1
        shops = 4
    elif city_size.lower() == 'm':
        total_inns = 2
        shops = 6
    elif city_size.lower() == 'l':
        total_inns = 3
        shops = 10
    print()
    print("city name -------------------------------------------------------------------")
    print()
    print('reason for city: ' + random.choice(city_reason))
    for bar in range(total_inns):
        tavern, tav_trait = gen_tavern()
        print("Tavern: " + str(tavern) + ' : ' + tav_trait)
        print("barkeep: ")
        barkeep = gen_npc()
        for trait in barkeep:
            print(trait)

        print()
        print('---------------------------------------------------------------------------')
    gen_shops(shops)
    start()
    

start()  

