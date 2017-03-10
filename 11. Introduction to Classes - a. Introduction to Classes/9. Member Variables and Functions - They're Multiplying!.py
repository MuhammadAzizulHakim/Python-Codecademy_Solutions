class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("Charles", "24")
sloth = Animal("Albert", "25")
ocelot = Animal("Percy", "26")
        
hippo.description()
sloth.description()
ocelot.description()

print hippo.health
print sloth.health
print ocelot.health
