"""
Author: Richard Davy
Date: 08/17/2013
File: ex36_debuggedDesign
Exercise 36: Designing and Debugging
"""

from sys import exit

def cavernous_caves():
    count = 0
    items = []
    print """Welcome to the Cavernous Caves, the last place
you shall see before your death... If of course you make the 
wrong decision"""
    print """There are so many things you can find in a 
cave, Who knows what you might find."""
    print """These are the things you can do, 1) You can 
scavenge, 2) You can leave; We prefer you to leave and leave our treasure alone """
    
    choice = raw_input("What be your choice... ")
    choice = choice.lower()
    
    if choice == "1":
        print "So be it. These are the items you can carry with you"
        print """1)Rubies, 2)Emeralds, 3)Diamonds, 
4)Sapphires and that is all NO GOLD!!! NO FORBIDDEN 
TREASURE!!! AND BY NO MEANS NO CHOCOLATE (its
poisoned) You may only carry three items from the cave!!!"""
        
        
        while count < 3:
            jewels = raw_input("Proceed but be ware... ")
            jewels = jewels.lower()
            items.append(jewels)
            count += 1
        else:
            print "So you're taking my", items
            if "gold" in items or "forbidden" in items:
                die("I told you not to take the gold or the forbidden treasure you thieving swine... You will now die!!! ")
            elif "chocolate" in items:
                die("You are now poisoned for your pitiful sweet tooth...")
            else:
                pass
            die("You are greedy but obedient... ")
    elif choice == "2":
        die("You shall live to see another day!!! ")
		
    else:
        print "That wasn't a choice on the list you fool... "
        die("You will now be eaten by dragons... ")
    
	
def damsels_paradise():
    count = 0
    demands = []
    print """You have found Damsels Paradise where there are
many beautiful sirens waiting to gouge out your eyes and 
break your limbs!!!"""
    print """You have the unique opportunity of being 
served to the fullness of your dreams, Just ask the 
girls for what you want!"""
    
    
    while count < 5:
        my_dem = raw_input('> ')
        my_dem = my_dem.lower()
        demands.append(my_dem)
        count += 1
    else:
        print "So you would like ", demands
        die("Fantastic decision, seems as if you will live a long happy life.")
    
    if "naked" in demands or "nude" in demands or "sex" in demands:
        die("We'll have none of that, do you not remember the gouged eyes and broken limbs...")
    
def land_o_dead():
    print """This is the land of the dead, the undead/dead 
at that... ZOMBIES"""
    print """You will need weaponry, food, and shelter
you need to gather these things but beware Zombies are everywhere"""
    print "Will you leave the spot you are in"

    ans = raw_input("> ")
    ans = ans.lower()
    if ans == "yes":
        print "Great, what an adventurous spirit"
        print "Where shall we go?"
        print "1) The village grocery, 2) The village gun shop, 3) The village camping outlet"
        dest = raw_input("> ")
        dest = dest.lower()
        if "grocery" in dest or "1" in dest:
            print "Great decision, you will now have food and water"
            die("You can stay here and survive for days, maybe months... ")
        elif "gun"	in dest or "2" in dest:
            print "This is not a bad decision however what shall you eat?"
            die("You will have to fight you're way through but you may survive...")
        elif "camping" in dest or "3" in dest:
            print "Why the hell would you go to a camping store"
            die("A zombie surprises you from a tent and bites you, you will now live eternally as a biter... ")
        else:
            die("You were chased down and are being eaten by zombies...")		
    elif ans == "no":
        print "Seriously!"
        die("You will now starve until you are to weak to move and become zombie dinner... ")
    else:
        print "You are so indecisive and that will cost you... "	
        die("You have been eaten by a zombie!")
    
def start():
    print "You have made it to the land of the lost."
    print "You are on the only road in the land."
    print """This road is more of a trail but it has a 
a distinct set of three paths, one to the left, one to 
the right, and one in the center. Which one do you take?"""

    dec = raw_input('> ')
    dec = dec.lower()
    
    if dec == "left":
        cavernous_caves()
    elif dec == "right":
        damsels_paradise()
    elif dec == "center":
        land_o_dead()
    else:
        die("Indecisive half twits are all bludgeoned by the beast of the dead... bruhahahahaha!!!")


def die(why):
    print why, "Good Job!!"
    exit(0)
	
	

	
	
	
start()
