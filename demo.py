print "There isn\'n much time left. You need head to safty."

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

Office1 = Building('Office 1', 'There seems nothing to be in here to help you defeat the infected.\nHead "west" into the other room. There might be something in there.', None, None, 'Elevator2', None, None , 'Office2', None, None, None, None)
Office2 = Building('Office 2 ', 'Huh, nothing in here as well. The infecteds are coming in closer.\nKeep heading "west"', None, None, None, None , None, 'Janitor', None, None, None, None)
Janitor= Building('Janitor Room', 'Cleaning applicances are scattered everywhere. Within the room there is another door.\n\nWEAPONS\n\nit reads.Type "inside" to get in', None, None, None, 'Office1', 'Secret',None, None, None, None, 'Secret')
Secret = Building('Secret Door', 'Great you made it in. Take a step "north"', None, None, 'Weapon', 'Janitor', None,None, None, None, None, None)
Weapon = Building('Weapon Room', 'A variety of weapons are displayed. They are ones that you think will be useful. Remember thought there is a limit to what you can take\n>add\n\n..to exit and head out Type "east".', None, None, None, 'Elevator3', 'Secret',None, None, None, None, None)
Bathroom = Building('Restroom', 'The smell of rottening meat is rising in here. Place the first bomb in here. ', None, None, None, None, 'Stairs','Elevator', None, None, None, None)


while True:
    print "Room: " + node.name
    print 
    print "Description: " + node.description 