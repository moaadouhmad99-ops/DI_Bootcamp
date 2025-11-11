##  Exercise1:
#Instructions:
#Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.

#Step 1: Create Cat Objects
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 5)
cat3 = Cat("Shadow", 2)

#Step 2: Create a Function to Find the Oldest Cat
def find_oldest_cat(cat_1, cat_2, cat_3):
    oldest_cat = cat_1
    if cat_2.age > oldest_cat.age:
        oldest_cat = cat_2
    if cat_3.age > oldest_cat.age:
        oldest_cat = cat_3
    return oldest_cat
#Step 3: Print the Details of the Oldest Cat
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name} who is {oldest.age} years old.")

##################################################################
######################################################################
##  Exercise2: Dogs
# Step 1: Create the Dog Class
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes Woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create Dog Objects
davids_dog = Dog("Buddy", 30)
sarahs_dog = Dog("Max", 25)
# Step 3: Print Dog Details and Actions
print(f"{davids_dog.name} says {davids_dog.bark()} and jumps {davids_dog.jump()} cm high.")
print(f"{sarahs_dog.name} says {sarahs_dog.bark()} and jumps {sarahs_dog.jump()} cm high.")
##################################################################
######################################################################
##  Exercise3: Who The Song Playlist
# Step 1: Create the Song Class
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
# Step 2: Create Song Objects
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()
##################################################################
######################################################################
##  Exercise4: Afternoon at the Zoo
# Step 1: Create the Zoo Class
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        animal_dict = {}
        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter not in animal_dict:
                animal_dict[first_letter] = []
            animal_dict[first_letter].append(animal)
        return animal_dict
    
    def get_groups(self):
        animal_dict = self.sort_animals()
        for key in animal_dict:
            print(f"Group {key}: {animal_dict[key]}")

# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")
# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Tiger")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Leopard")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Tiger")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
#Bonus: Modify the add_animal() method to get *args so you dont need to repeat the method each time for a new animal, you can pass multiple animals names separated by a comma.
def add_animals(self, *new_animals):
    for new_animal in new_animals:
        if new_animal not in self.animals:
            self.animals.append(new_animal)
Zoo.add_animals = add_animals
# Using the modified method to add multiple animals
brooklyn_safari.add_animals("Giraffe", "Zebra", "Elephant")
brooklyn_safari.get_animals()
