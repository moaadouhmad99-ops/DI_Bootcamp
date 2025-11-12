# 🌟 Exercise 1: Pets
# Given classes (example base code)
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{self.name} sings {sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{self.name} sings {sounds}'



# Step 1: Create the Siamese class

class Siamese(Cat):
    def sing(self, sounds):
        return f'{self.name} sings {sounds} in a soft tone'


# Step 2: Create a list of cat instances
bengal_obj = Bengal("Simba", 3)
chartreux_obj = Chartreux("Milo", 4)
siamese_obj = Siamese("Luna", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

# Step 3: Create a Pets instance
sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
sara_pets.walk()

print("****"*6)

##############################################################################
##############################################################################
# 🌟 Exercise 2: Dogs
#Goal: Create a Dog class with methods for barking, running speed, and fighting.
#Step 1: Create the Dog Class
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} wins the fight against {other_dog.name}"
        else:
            return f"{other_dog.name} wins the fight against {self.name}"
        
# Step 2: Create Dog Instances
dog1 = Dog("Buddy", 5, 30)
dog2 = Dog("Max", 4, 25)
# Step 3: Test the Methods
print(dog1.bark())
print(dog1.run_speed())
print(dog1.fight(dog2))

