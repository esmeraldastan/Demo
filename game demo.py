import random
import time
import sys

#INVENTORY
inventory = []

#TIMER
sec = 0 

#Into to the game 
time.sleep(0.5)


print 
print "Welcome to Apoclaiptic City" 
print   

node = None 

#INVENTORY
def addToInventory(item):
    item = raw_input('> what do you want to add?? ')
    inventory.append(item)

#CHARACTERS
#player status 
class player(object):
    
    def __init__(self, health = 49800, attack = 500):
        self.attack = attack 
        self.health = health 
        
        
    def attacks(self, target):
        target.damage(self.attack)
        if target.health <= 0:
            return "Enemy down!"
        else:
            return target.health
            
    def damage(self, amount):
        self.health -= amount
        
me = player()

#HP OF ZOMBIE
class Zombie(object):
    def __init__(self, health = 5000, attack = 1500):
        self.health = health
        self.attack = attack 
        

    #COMMAND TO ATTACK     
    def attacks(self, target):
        target.damage(self.attack)
        if target.health <= 0:
            return "Enemy down!"
        else:
            return target.health
            
    #DAMAGE TAKEN   
    def damage(self, amount):
        self.health -= amount
        
zombie = Zombie()

#start of the map         
class Building:
    
    def __init__(self, name, description, up, down, north, east, south, west, right, left, outside, inside):
        self.name = name
        self.description = description
        self.up = up
        self.down = down
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.right = right
        self.left = left
        self.outside = outside 
        self.inside = inside 
        
    def move(self, direction):
        global node 
        node = globals()[getattr(self, direction)]
         


     
#PATH TO SECOND FLOOR
Stairs1 = Building("Stairs", 'There is something on you path that is blocking you. Type "flashlight" to see what it is.', None, None, None, None, None,'Office1', None, None, None, None)
Elevator2 = Building("Second Floor", 'You are now on the second floor. A loud growl is coming for the stairs.... an infected is charging twards you.\n\nHead "south".', 'Elevator', None, None, None, 'Office1', None , None, None, None, None)
     
#SECOND FLOOR
Office1 = Building('Office 1', 'There are no items in this room to help you defeat the infected.\nHead "west" into the other room. There might be something in there.', None, None, 'Elevator2', None, None , 'Office2', None, None, None, None)
Office2 = Building('Office 2 ', 'Huh, nothing in here as well. The infecteds are coming in closer.\n\nKeep heading "west"', None, None, None, None , None, 'Janitor', None, None, None, None)
Janitor= Building('Janitor Room', 'Cleaning applicances are scattered everywhere. Within the room there is another door.\n\nWEAPONS\n\nit reads.Type "inside" to get in.', None, None, None, 'Office1', 'Secret',None, None, None, None, 'Secret')
Secret = Building('Secret Door', 'Great you made it in. Take a step "north"', None, None, 'Weapon', 'Janitor', None,None, None, None, None, None)
Weapon = Building('Weapon Room', 'A variety of weapons are displayed. Take the ones that you think will be useful. Remember thought there is a limit of 3 weapons you can take.\nType in..\n>add\n\n..to exit and head out Type "east".', None, None, None, 'Elevator3', 'Secret',None, None, None, None, None)
Bathroom = Building('Restroom', 'The smell of rottening meat is rising in here. Place the first bomb in here. ', None, None, None, None, 'Stairs','Elevator', None, None, None, None)

#PATH TO FIRST FLOOR
Stairs2 = Building('Stairs', 'Head down as quick and possible', None, 'Lobby', None, None, None, None, None, None, None, None)
Elevator3 = Building('Elevator', 'Head "down"', None, 'Lobby', None, None, None, None, None, None, None, None)

#FIRST FLOOR
Lobby = Building('Lobby', 'You are now in the first floor. Head "east"', None, None, None, 'Center', None, None, None, None, None, None)
Center = Building('Center', 'There is a bomb here. Head "outside" quick!', None, None, None, None, None, None, None, None, 'Enterence', None)

#PATH TO FIRST FLOORt
node = Stairs1  

while True:
    print "Room: " + node.name
    print 
    print "Description: " + node.description  
    
    response = ['up', 'down', 'north', 'east', 'south', 'west', 'right', 'left', 'outside', 'inside']     
         
    command = raw_input('>').strip().lower()
        
    #MOVE INTO DIFFERNT ROOMS 
    if command in response:
        try:
           node.move(command)
        except:
            print 'You can\'t do that way!'
            
            
        # door 
    if node == Secret :
        print "Figure out the passcode to get inside!"

        password = "3546", "5515", "1651", "4539", "4620" #passwords to open up the doors 
        wordIndex = random.randint(0,len(password)-1)
        code_rip = password[wordIndex]
        user_guesses = ''
        turns = 10 #the player will have only 10 times to try to figure out the code


        while turns > 0:
            left = 0
            for number in code_rip:
                if number in user_guesses:
                    print number,
                else:
                    print "#",
                    left += 1
            if left == 0:
                    print
                    print
                    print "Excellent, move on."# move into the next room 
                    
                    break
            
            print 
            
            guess = raw_input("Guess the four Numbers:")

            user_guesses += guess 
            if guess not in code_rip:
                    turns -=1
                    print "Sorry number not in the secret code. \n\n Please try again"
                    print "You have", +turns, 'left'
            if turns == 0:
                    print "Sorry try again."#change
                    
                    
         #INVENTORY FOR ITEMS/WEAPONS
        
    if command == "add":
        addToInventory(input)
        print (inventory)
    print

    if node == Weapon:
        print '''
                    Weapons Available:
            
                    *axe
                    *sword
                    *cross_bow
                    *dagger
                    *club
                    
                '''
                
                
    #ZOMBIE ATTACK    
    
    if node == Stairs1:
        print 'There is a zombie infront of you. Type "attack".'
        
                
        while me.health > 0:
            command = raw_input('>')
            if command == "attack":
                me.health -= zombie.attack 
                print "Your health is now", me.health 
                print "You attacked your enemy for", me.attacks(zombie),"damage"
        

        
            if zombie.health <= 0:
                print
                print
                print "Great, you have defeated the zombie!!!\n"
                print 'Head "west" now.'
        
                break
        
            print 
    
            if me.health <= 0:
        
                print "Sorry, you died."
                sys.exit(0)
                
    #QUITE THE PROGRAM 
    if node == Lobby:
        print "You have reached the end of the demo Apoclaiptic City"
        sys.exit(0)
        