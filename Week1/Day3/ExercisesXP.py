##  🌟 Exercise 1: Converting Lists into Dictionaries
#Key Python Topics:
#Creating dictionaries
#Zip function or dictionary comprehension

#Instructions
#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
keys = ['Ten', 'Twenty', 'thirty']
values = [10, 20, 30]
result_dict = dict(zip(keys, values))
print(result_dict)


##############################################################
##############################################################
##  🌟 Exercise 2: Cinemax #2
# Key Python Topics:
# Looping through dictionaries
# Conditionals
# Calculations

# Instructions
# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15

# Family Data:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for member, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    total_cost += price
    print(f"{member.capitalize()} (age {age}): ${price}")
print(f"Total cost for the family: ${total_cost}")

#Bonus:
#Allow the user to input family members’ names and ages, then calculate the total ticket cost.
price = 0
total_cost = 0
while True:
    name = input("Enter family member's name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    age = int(input(f"Enter {name}'s age: "))
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    total_cost += price
    print(f"{name.capitalize()} (age {age}): ${price}")
print(f"Total cost for the family: ${total_cost}")

##############################################################  
##############################################################
##  🌟 Exercise 3: Zara
# Key Python Topics:

# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()


# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.
# Brand Information:

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}
# Change number_stores to 2
brand["number_stores"] = 2
# Print a sentence about Zara's clients
print(f"Zara's clients are: {', '.join(brand['type_of_clothes'])}.")
# Add country_creation
brand["country_creation"] = "Spain"
print(brand)
# Add "Desigual" to international_competitors if it exists
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
# Delete creation_date
brand.pop("creation_date", None)
# Print the last item in international_competitors
print(brand["international_competitors"][-1])
# Print the major colors in the US
print(brand["major_color"]["US"])
# Print the number of keys in the dictionary
print(len(brand))
# Print all keys of the dictionary
print(brand.keys())

#   Bonus:
# nother dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
more_on_zara = {
    "creation_date": 1975, 
    "number_stores": 10000
}
brand.update(more_on_zara)
print(brand)


##############################################################
##############################################################
##  🌟 Exercise 4: Disney Characters
# Key Python Topics:

# Looping with indexes
# Dictionary creation
# Sorting

# Instructions
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:

# Character List:
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# Expected Results:
# 1. Create a dictionary that maps characters to their indices:
char_to_index = {user: index for index, user in enumerate(users)}
print(char_to_index)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}


# 2. Create a dictionary that maps indices to characters:
index_to_char = {index: user for index, user in enumerate(users)}
print(index_to_char)
# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}


# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
sorted_users = sorted(users)
sorted_char_to_index = {user: index for index, user in enumerate(sorted_users)}
print(sorted_char_to_index)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}





