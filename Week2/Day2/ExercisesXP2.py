#  Exercise 3: Dogs Domesticated

from ExercisesXP import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self,*arge):
        print(f"{arge} all play together")

    def do_a_trick(self):
        import random
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f'{self.name} {random.choice(tricks)}')
        
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()


#####################################################################################
#####################################################################################
# 🌟 Exercise 4: Family and Person Classes
# Goal:
# Practice working with classes and object interactions by modeling a family and its members.
class person():
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ' '

    def is_18(self):
        return self.age>=18
    
class Family():
    def __init__(self, last_name):
        self.last_name =last_name
        self.members = []

    def born(self, first_name, age):
        new_person = person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)
    
    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name :
                if member.is_18():
                    print(f"{first_name} You are over 18, your parents Jane and John accept that you will go out with your friends")
                else :
                    print(f"{first_name} Sorry, you are not allowed to go out with your friends.")
            
    def family_presentation(self):
        print(f"{self.last_name} family membres")
        for member in self.members:
            print(f"{member.first_name}, age:{member.age}")
        
Family_name = Family("John")
Family_name.born('Jon',24)
Family_name.born('Lica', 22)
Family_name.born('Max', 5)
Family_name.born('Alix', 18)

Family_name.check_majority('Joh')
Family_name.check_majority('Max')

Family_name.family_presentation()
        
