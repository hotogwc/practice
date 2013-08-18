"""
This is an expanded version of the LearnPythonTheHardWay exercise 31
Author: Richard Davy 
Date: 08/15/2013
File: ex31_makingDecisions.py
Exercise 31: Making Decisions
"""

print """You enter a dark room with two doors. Do you go through door #1 or door #2"""
print """There are also two more doors, door number #3 and door #4, these doors are forbidden but choose them if you must!!!"""
 
door = raw_input('> ')
 
if door == "1":
    print """There is a giant bear here eating a cheese 
	cake. What do you do? """
    print "1. Take the cake."
    print "2. Scream at the bear."
	
    bear = raw_input('> ')
	
    if bear == "1":
	    print "The bear just ate your face off. Good Job!"
    elif bear == "2":
	    print "The bear just ate your legs off. Good Job!"
    else:
	    print "Well, doing %s is probably better. Bear runs away." % bear
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow Jacket Clothespins."
    print "3. Understanding revolvers yelling meoldies."
	
    insanity = raw_input('> ')
	
    if insanity == "1" or insanity == "2":
	    print "Your body survives powered by a mind of jello. Good Job!"
    else:
	    print "The insanity rots your eyes into a pool of muck. Good Job!"
elif door == "3":
    print "You have found the secret room, a room that you shouldn't be in... NOW LEAVE... /n However if you stay there are some choices to make..."
    print "1. Turn around and leave as I said... YOU'VE BEEN WARNED"
    print "2. Enter this room and witness the horrifying epidemia of Barney the great big purple dinosaur.. HAHAHAHAHA"
    print "3. Guess my name (cough, cough it's not Rumplestiltskin) and I will let you live"
    print "4. Choose your own fate and surprise me...."
	
    fate = raw_input('> ')
	
    if fate == "1":
        print "A wise decision you have made... friend of yours is the force it is..."
    elif fate == "2":
	    print "Please be seated and enjoy the horrifying epidemia of Barney the Purple Dinosaur"
    elif fate == "3":
	    print "Poor choice my boy you now have but one shot to guess my name and it really isn't Rumplestiltskin"
	    name = raw_input('> ')
	    if name == "The Mad Hatter":
		    print "Wow That was amazing!!!"
	    else:
		    print "I told you that was a poor decision you will now be burned at the stake. HAHAHAHAHA"
    elif fate == "4":
        print "Really there is no surprising me... You will now be cursed for the rest of your life..."
    else:
        print "That wasn't an option you will now suffer the wrath of the GODS"
elif door == "4":
    print "This door was forbidden, you opened it anyway. ignorance is bliss!!!"
    print "You should have chosen another door"
    print "1. You could leave and live another day."
    print "2. On the other hand there is a secret to this door choose wisely."

    treasure = raw_input("The choice is yours: ")

    if treasure == "1":
        print "I don't let ignoramous jackylls live... You will be squished by boulders. Good Job!!!"
    elif treasure == "2":
        print "Nooooooo you have found my treasure, its such beautiful treasure, but if you take it you will be struck by lightning on the way out. Good Luck!!!"
else:
    print "You stumble around and fall on a knife and die. Good Job!"
