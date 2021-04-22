import random
import sys


#https://www.reddit.com/r/DnDBehindTheScreen/comments/ancztc/50_weird_wonderful_taverns/


# name creation
prefix = ['De','Sin','Kum','Vin','Che','Fre','Roy','Tib','Cen','San','Grab','Gru','Gre','Dir','Vlad','Var','Tok',
          'Tol','Mac','Ada','Sa','Dm','Py','Al','Ar','Jo','Sp','Ti','Gar','Mat','Za','Jer','Att','Bra','Bro','Bri',
          'Re','Ger','Sw','Con','Her','Wi']

middle = ['il','om','aral','et','er','io','deh','ia','ra','th','ud','ub','row','i','ic','ol',]

suffix = ['an','pi','non','is','ich','us','le','wood','ie','elm','der','osk','oft','obe','eim','ra','on','rey','n',
          'or','el','i','etta','anna','ak','rra','ag','ko','mey','bert',]

# npc creation
appearance = ["lots of jewelery","piercings","flamboyant or colorful clothes",
              "Formal attire", "dirty ratty clothes", "Scar/s", "missing teeth",
              "missing fingers", "unusual eye color or 2 different colors",
              "Tattoos","Birthmark","unusual skin color","Bald","Unusual hair color",
              "nervous twitch", "distinctive nose", "good or bad posture", "beautiful",
              "ugly", "nerdy/ bookworm",'long braided blonde hair','very tan','bad posture','very curly hair','allways smiling',
              'allways frowning','wrinkly/old', 'child', 'fake hand/ wood or metal hook','wear glasses']

gender = ['Male', 'female']

race = ["human","elf",'high elf', "halfling", "gnome", "Tiefling","dwarf","orc",'half-elf','half orc']

skilled = ["strong", "agile/graceful","smart","wise/ spiritual","charasmatic", 'hard-ass', 'jokster/prankster',"weak", "clumsy",
           "dumb", "oblivious", "dull/ boring",'night owl']

talent = ['plays an instrument', 'multi langual', 'really lucky', 'perfect memory',
          'animal lover','great with children','great puzzle solver', 'great at one game',
          'great at drawing', 'great at painting', 'great singer', 'great at drinking',
          'master carpenter','expert cook','skilled actor','dancer','knows thieves cant','self taught magic user','pet trainer',
          'ship captain','expert machine tinker','potion maker/herbalist','master thief','master forger','knows the king personally','has a magical item they dont know what it does']

mannerism = ['prone to sing, hum or whistle','speaks in rhyme','speak in low or high voice',
             'drunk ','speaks loudly','whispers','uses long words','uses wrong words','fidgets',
             'constantly jokes','expects doomsday','squints(clint eastwood)','spacey (stares off alot)',
             'chewing','pacing','tap fingers','twist hair', 'bite fingernails', 'makes big hand gestures',
             'never knows the date/ time', 'allways excited','act like on crack','a deep thinker', 'stretches the truth',
             'clean freak', 'horder','stinky','thinks out loud','pregnent/ballsniffer', 'allways smoking','cusses alot','smell really good','innaproperate laughing',
             'wants to be an adventurer']

ideals = ['dedicated to life goal','protective of family','protective of coworkers','loyal to clan/ employer',
          'deep in love','drawn to a place of interest','protective of a possession','seeking revenge', 'very religious']

flaw = ['secret lover ', 'prone to falling in love', 'enjoys luxury ','Arrogant','envies others things',
        'greedy','prone to rage','has a powerful enemy','phobia','previous scandalous history','secret misdeed',
        'dumbly brave', 'lazy', 'never surrenders', 'married', 'in an abusive relationship', 'in a relationship', 'veryyy single', 'single',
        'irrational fear of dumb thing','racist','addicted to drug','sleepwalker','flirty/lustful','abstinate','A bad Bard-barian','experiments on dead bodies',
        'a drow desquised as human','dwarf that wants to be a wizard','a ghost but think they are alive','freaky friday life swapped with a orc warchief','freaky friday life swapped with a Gnome mage',
        'little girl protected by a demon','plants evidence to get people arrested they dont like','secretly a vampire']

# tavern creation
the = 'The '
description = ['cruel ','shaking ','salty ','juicy ','happy ','green ','red ','grey ',
         'Brass ','gold ','armed ','even ','black ','elven ','silver ','dwarvish ','hellish ','crusty ','silver ','tarnished ', 'weathered ',
               'targets ','crumbling ','crimson ','gems ','invisible ','blackened ','charred ','wet ','arrogant ']

animal = ['soldiers ','dragons ','dwarfs ','beholders ','hawks ','hunters ','steeds ','oil lamps ',
         'ravens ','harpy ','manticores ','pixies ','krakens ','giants ','donkeys ',
         'griffon ','rusty ','rats ', 'racoons ', 'spiders ','banshee ','devils ','lichs ','owlbears ','centaurs ']

end = ['pub','inn','hub','den ','bar ','saloon ','house ','eye ','head ','hideout ','hole ', 'watering hole ','lair ']

food= ['owlbear ribs','magical carmelized fritters healing potion','Barbecued tiger fish and papaya','Braised beef and pears with ginger','Pork chop & curds','Honey braised boar ribs','Venison and bean stew','Cooked wolf steak',
       'Mushroom stew with corn bread','Acorn soup','Lizard gruel with nutbread','Porridge','Hot beet soup and fresh bread','giant spider stew','Minted pea soup','Elven bread','Braised duck','fried chicken with honey pepper sauce','pasta with red sauce and scallops','roasted roots with wild salad',
       'meat of the day','honey with berries and cornbread','fig feta flatbread','wild salad','potatoe fries','turnip fries','hashbrown and eggs','fried wolf steak and mashed turnips', 'Damaran Goulash','Parsnip pie','hellblood biscuits','sweet and spicy meatballs',
       'Garlic Fries','Pot Pie','Drow Mushroom Steak','Fey Wild Salad','Heros Feast Stew','roasted honey glazed turkey','pot meat sandwhich','porkbelly cuts with ripe figs','buckwheat pancakes with mullberry syrup','cooked rabit with ground cherry salsa','underdark mushroom meadly','rye swirl bread']


drink = ['Grog','goblin spit ale','turnip wine','moonshine','dwarven ale','Pulsch brown ale','moon mountian ale','spiced ale','spiced squash stout','kings ale','wrymwizz ale','elderberry spiced wine','lotus leaf wine','stonesulder wine (yellow demon plant)','sweetberry wine',
          'mead','ale','pear sour','grape sparkling wine','moon rum','vodka','scotch','berry brandy','moss mead','honeysuckle mead','coffee stout','fireweed wiskey','mushroom moonshine','greensage cider','abyssal ale','ghost ale(become ghost for hr)','goodale(adv for good chr 1 hr)',
          'sweetwater(cure poison)','rutabega ale','gorgondy ale (see a past vision)','future root ale(see future vision)','beet beer','Firesteap Mountian dew','Cloven Mountian Dew','Black Dragons bite','mushroom tea','ground cherry sour','herbal tomato drink','',]

tavern_traits = ['high class', 'shit hole', 'gang hangout', 'running out of supplies', 'average town inn', 'secret club running',
                 'well furnished', 'big', 'small','busy', 'ghost town', 'secret monster/s hiding ','brawling arena', 'monster fighting arena','gambling tables/ machines','haunted',
                 'multidimentional inn(portal inside)','completely run by ','everything shrinks', 'huge tavern','full of advanced machinery','everyone inside gets a magic cantrip ability','food eating contest','drinking contests'
                 ,'pay or fight (pits, portals, teleport etc)','underground rave club','huge tavern /libary. center point of knowlege','suspended over a giant hole in the earth','built around a cave, adventures never come back out','underwater','Band Playing','Glatiator Arena',
                 'jousting arena','Casino','Dog Racing','Horse Racing','Drunk athletic games to win gold','Built In Theater','giant floating ghost ship','head trophies line the walls, adventures come to show off the best trophies','tavern run by a gnome and his clockwork robots/ inventions']

tavern_events= ['intoxicated person knocks over lamp, starts fire','Someone falls out of their seat, but were poisoned','a storm outside blows down a tree falling onto the bar','a storm hits, tree branches break into the window','someone walks in dressed as a horse',
                'someone plays game with the players, cheats the game','a man in tatter clothes is asking people for a meal, the bartender is trying tokick him out','The bar is racist to Elves','a few tables of people are racist to gnomes','a table of non human gang members pick on a human',
                'An investigator is studying his case alone in the corner','someone starts reading from a book to summon a spined devil','a wealthy man tries to buy the bar a round and leave before paying','Bar fight! Love Rivakry','Bar fight! Accidental insult','Bar fight! punching someone on accident',
                'Bar fight! 2 gangs','Bar fight! money']

# city creation
shop = ['magic shop','map shop','armory','blacksmith','food market','general store','clothing store','book store','pet store','jeweler',
        'temple','live stock store', 'shipmaker', 'carpenter','taxidermist','potion shop','grain mill','bakery','butcher','beekeeper','Church','Casino','Fish/meat Market','art store',]

city_reason = ['growing spices', 'good hardwood', 'lumber', 'grape growing', 'corn and grain growing', 'fishing', 'hunting', 'oil field',
               'mineral mines','magic mines','fair weather(vacation spot)','metal mines', 'precious metal mines', 'coal mines', 'on trade route']
#idea creation
pronoun = ['you ','we ','he ','she ','good guys ','bad guys ','us ']

verb = ['need ','took ','stole ','pickpocketed ','had ','kept ','killed ','fought ','deliver ','discover ','hates ','likes ','is vunerible to ','is immune to ',
        'explored ','expected ','forgot ','forbid ','gave ','froze ','hid ','lead ','learn ','destroyed ', 'prevented ','hunted ','loved ','lost ','cursed ','kidnapped ',
        'had secret meeting ']

noun = ['sword','bow','eye','girl','child','sickness','health','goverment','sibling','orb','magic item','magic','world','hell','tower','angels','demons','devils','assassins','son',
        'underground', 'cave', 'guards','daughter','old friend']


magic = ['mage hand','minor illusion','mockery','message','speak to dead','friends','prestidigitation']

#monsters
monsters = ['vampires','goblins','succubus','devil','demon','doppleganger','warewolves','ghost','hag','angel','disquised god','undergound abomination(gibber mouths)','skeletons','pixies','drow','dryiad']


locations = ['magic dead zone','wild magic zone', 'bolder carved with talking faces','crystal cave that will anwser questions','old tree with a spirit trapped inside',
            'old battlefield where fog forms and shows human shapes','dimensional portal','wishing well','giant crystal shard in ground','floating earth peices','wrecked ship on land',
            'haunted house','haunted graveyard','river ferry lead by skeleton','battle field with statue people','treeant forest','floating earth with tower on it','pyramid',
            'faces carved in a cliff','giant bronze statues of gods','obelisk with lore','ruined obolisk','fountian','city ruins','wild magic fountian','Ghost reenacting an old event that happened before their death...',
             'a huge pit that seems to have the floating earth peices','a sandstone shrine with 3 giant gongs and a center worm statue','a statue that is a rusted robot made by a genius gnome','a sword in a large stone','a large monolith that you swap bodies with the person to your left','you come to a trail off the main road with bread crumbs going into the forest',
             'a goblin built fighting pit arena','an area where the forest and everything shrinks to about half size', 'many trees have cuts and gouges on them, with DC15 investigation, if you stand in the right spot the cuts spell out "RUN"','a marble sacrifical table with fresh blood on it']

# plot hook

plot_hook = ['a boy runs to you choaking and dies, he was poisoned',' you see 2 guards snatching a boy and girl, they mention something about a ritual','the players are asked to escort goods, guards find it is full of contraband','a mastermind is posting up peoples names, they die the next day mysteriously',
             'this city has banned magic, you could be burned or killed for using magic','an old dwarf warrior wants to fight the best warrior to the death, if you win you get his treasure map','they hear an abandoned baby, if touched they souls swap.','a gnome made golems for the city guard, the golems attacked the city',
             'a palidian is charged for killing someone in public, but everything feels off...','2 demons are having a duel, one demon tries to recruit the party','ground hogs day, they must solve a mystery to continue (another plot hook/idea)','a drow clan has uprooted to the surface pillaging.. Why?',
             'you party with the prince, you wake up the next morning with him dead..','a graveyard slowly starts coming back alive','the royal family has been replaced by dopplegangers','you run into a naked mind flayer that does not know who or what he is','the king has betrayed a devil he has a deal with, the town gets attacked by a balor',
             'a kid runs up to you, guards follow. He stole something powerful but the players dont know it','a brooding pirate wants his rival dead, he is staying at this inn','the mayor wants you to hunt a monster that has been attacking the town, it is a friendly druid firbolg. The mayor just hates firbolg',
             'you see a group of slaves walk by, one ask for help. says they have something of great value','It is time for the BBQ competition, the tavern owner asks you to bring back some powerful herbs/ eggs in the cave up the mountian. The lair of a dragon(unknown to players)']


def start():
    print("""
what do you want to generate?

type "npc" for random npc
type "tavern" for random tavern
type "name" for random name
type "end" to close
type "dice" to roll a die
type "city" to gen city
type "shop" to gen shops
type "idea" to gen idea spark
type "poi" to gen a point of interest
type "hook" to gen plot hook"""  
        )
    pick = input(': ')
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
    elif pick.lower() == 'menu':
        gen_menu()
    elif pick.lower() == 'city':
        gen_city()
    elif pick.lower() == 'poi':
        gen_location()
    elif pick.lower() == 'hook':
        gen_hook()
    elif pick.lower() == 'shop':
        gens = int(input('how many shops do you want to make? : '))
        print()
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



def gen_hook():
    num = input('how many hooks?: ')
    for hook in range(int(num)):
        print(random.choice(plot_hook))
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

def gen_menu(items):
    print()
    genmenu=[]
    for item in range(int(items)):
        genmenu.append(random.choice(food))
        genmenu.append(random.choice(drink))
    return genmenu
    

def gen_menus():
    print()
    items = input('how many menu items do you want?')
    foods = round(int(items)/2,0)
    drinks = round(int(items)/2,0)
    print()
    print()
    for item in range(int(foods)):
        print(random.choice(food))
    print()
    print()
    for item in range(int(drinks)):
        print(random.choice(drink))
    print()
    start()
    
def gen_tavern_event(num):
    res = []
    for event in range(int(num)):
        res.append(random.choice(tavern_events))
    return res
    

def gen_tavern():

    print()
    gen_begin = random.choice(description)
    gen_mid = random.choice(animal)
    gen_end = random.choice(end)
    choose = random.randrange(1,4)
    tav_trait = random.choice(tavern_traits)
    menu = gen_menu(3)
    event = gen_tavern_event(2)
    if tav_trait == 'secret monster/s hiding ':
        tav_trait = tav_trait + random.choice(monsters)
    if tav_trait == 'completely run by ':
        tav_trait = tav_trait + random.choice(monsters)
    if tav_trait == 'everyone inside gets a magic cantrip ability':
        tav_trait = tav_trait + random.choice(magic)
    if choose == 1:
        tavern = (the + gen_begin + gen_end)
    elif choose == 2:
        tavern = (the + gen_begin + gen_mid)
    else:
        tavern = (the + gen_begin + gen_mid + gen_end)
        
    return tavern, tav_trait, menu,event



def gen_taverns():

    loop = int(input('how many names do you want?'))
    print()
    for gen in range(loop):
        tavern, tav_trait,menu,event = gen_tavern()
        print(tavern + " : " + tav_trait)
        print("Menu: " + str(menu))
        print()
        print('Events: ' + str(event))
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
    npc.append(random.choice(talent))
    npc.append(random.choice(mannerism))
    npc.append(random.choice(ideals))
    npc.append(random.choice(flaw))
    npc.append('----------------------------------------------')
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
    dice_type = int(input('what die do you want to role? (4,6,8,10,12,20) : '))
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
    city_num = int(input('how many cities?: '))
    if city_size.lower() == 's':
        total_inns = 1
        shops = 4
    elif city_size.lower() == 'm':
        total_inns = 2
        shops = 6
    elif city_size.lower() == 'l':
        total_inns = 3
        shops = 10
    for num in range(city_num):
        print()
        print("city name -------------------------------------------------------------------")
        print()
        print('reason for city: ' + random.choice(city_reason))
        for bar in range(total_inns):
            tavern, tav_trait,menu,event = gen_tavern()
            print("Tavern: " + str(tavern) + ' : ' + tav_trait)
            print("barkeep: ")
            print('Menu: ' + str(menu))
            print()
            print('Event: ' + str(event))
            barkeep = gen_npc()
            for trait in barkeep:
                print(trait)

            print()
            print('---------------------------------------------------------------------------')
        gen_shops(shops)
    start()
    
def gen_location():
    poi = int(input('how many random points of intrest would you want? : '))
    for item in range(poi):
        print()
        print(random.choice(locations))
    print()
    start()

def gen_villain():
    num = int(input('how many villains do you want? : '))
    for item in range(num):
        scheme = random.choice(villain_scheme)
        print()
        objective = random.choice(scheme)
        print(objective)
        print()
        print()
    


    
start()  

