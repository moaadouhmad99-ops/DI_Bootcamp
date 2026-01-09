# Part 1 & 2: Vaccines Management System

class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []  # Part 2: family attribute

    # Part 2: add family member method
    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
        if self not in person.family:
            person.family.append(self)

    def __repr__(self):
        return f"{self.name}({self.age}, Priority={self.priority}, Blood={self.blood_type})"


class Queue:
    def __init__(self):
        self.humans = []

    # Add a person to the queue
    def add_person(self, person):
        # Put priority people or age > 60 at the front
        new_list = []
        inserted = False
        for h in self.humans:
            if not inserted and (person.priority or person.age > 60):
                new_list.append(person)
                inserted = True
            new_list.append(h)
        if not inserted:
            new_list.append(person)
        self.humans = new_list

    # Find the index of a person
    def find_in_queue(self, person):
        for i in range(len(self.humans)):
            if self.humans[i] == person:
                return i
        return None

    # Swap two persons
    def swap(self, person1, person2):
        idx1 = self.find_in_queue(person1)
        idx2 = self.find_in_queue(person2)
        if idx1 is not None and idx2 is not None:
            self.humans[idx1], self.humans[idx2] = self.humans[idx2], self.humans[idx1]

    # Get next person
    def get_next(self):
        if len(self.humans) == 0:
            return None
        next_person = self.humans[0]
        # Remove manually
        new_list = []
        for i in range(1, len(self.humans)):
            new_list.append(self.humans[i])
        self.humans = new_list
        return next_person

    # Get next person with specific blood type
    def get_next_blood_type(self, blood_type):
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                person = self.humans[i]
                # Remove manually
                new_list = []
                for j in range(len(self.humans)):
                    if j != i:
                        new_list.append(self.humans[j])
                self.humans = new_list
                return person
        return None

    # Sort by age and priority
    def sort_by_age(self):
        sorted_list = []
        # First, priority people
        for h in self.humans:
            if h.priority:
                sorted_list.append(h)
        # Then older non-priority people
        for h in self.humans:
            if not h.priority and h.age > 60:
                sorted_list.append(h)
        # Then younger people
        for h in self.humans:
            if not h.priority and h.age <= 60:
                sorted_list.append(h)
        self.humans = sorted_list

    # Part 2: rearrange queue to avoid consecutive family members
    def rearrange_queue(self):
        if len(self.humans) <= 1:
            return
        i = 0
        while i < len(self.humans) - 1:
            current = self.humans[i]
            next_person = self.humans[i+1]
            if next_person in current.family:
                # Find the next person not in current's family
                swap_found = False
                for j in range(i+2, len(self.humans)):
                    if self.humans[j] not in current.family:
                        self.swap(next_person, self.humans[j])
                        swap_found = True
                        break
                if not swap_found:
                    i += 1  # can't swap, move forward
            else:
                i += 1

    def __repr__(self):
        return str(self.humans)


# =========================
# Example usage
# =========================

# Create humans
h1 = Human("001", "Alice", 65, False, "A")
h2 = Human("002", "Bob", 30, True, "B")
h3 = Human("003", "Charlie", 25, False, "O")
h4 = Human("004", "David", 70, False, "AB")
h5 = Human("005", "Eva", 50, True, "A")

# Set family relationships
h1.add_family_member(h3)
h2.add_family_member(h5)

# Create queue
queue = Queue()
queue.add_person(h1)
queue.add_person(h2)
queue.add_person(h3)
queue.add_person(h4)
queue.add_person(h5)

print("Initial Queue:")
print(queue)

queue.sort_by_age()
print("\nSorted Queue by Priority & Age:")
print(queue)

next_person = queue.get_next()
print("\nNext person to vaccinate:")
print(next_person)

blood_person = queue.get_next_blood_type("A")
print("\nNext person with blood type A:")
print(blood_person)

print("\nQueue before rearranging for family:")
print(queue)

queue.rearrange_queue()
print("\nQueue after rearranging for family:")
print(queue)
