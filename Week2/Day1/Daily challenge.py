#    Old MacDonald’s Farm
# Step 1: Create the Farm Class
class Farm:
    def __init__(self, frm_name):
        self.name = frm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        print(f"{self.name} Farm")
        for animal, count in self.animals.items():
            print(f"{animal}: {count}")
        print("E-I-E-I-O!")
# Step 2: Create a Farm instance
macdonald_farm = Farm("McDonald")
# Step 3: Use the Farm methods
macdonald_farm.add_animal("cow", 5)
macdonald_farm.add_animal("sheep", 3)
macdonald_farm.add_animal("pig")
macdonald_farm.add_animal("cow", 2)
macdonald_farm.get_info()

#Bonus: Expand the fram
def get_animal_types(self):
    return sorted(self.animals.keys())
Farm.get_animal_types = get_animal_types
print(macdonald_farm.get_animal_types())

def get_short_info(self):
    animal_types = self.get_animal_types()
    types_str = ", ".join(animal_types)
    return f"{self.name} Farm has: {types_str}"
Farm.get_short_info = get_short_info
print(macdonald_farm.get_short_info())

#Step 8: upgrade the add_animal Method
#use **kwargs for passing multiple animals. The keys will be the animal name and the value will be the quantity.
#Then you can call the method this way: macdonald.add_animal('cow'= 5, 'sheep' = 2, 'goat' = 12)
def add_animals(self, **kwargs):
    for animal_type, count in kwargs.items():
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
Farm.add_animals = add_animals
macdonald_farm.add_animals(cow=3, goat=4, chicken=10)
macdonald_farm.get_info()
