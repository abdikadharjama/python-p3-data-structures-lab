def get_names(spicy_foods):
    """Returns a list of names of each spicy food."""
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Returns a list of dictionaries where the heat level is greater than 5."""
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    """Prints each spicy food in a specific format."""
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns a dictionary for the spicy food that matches the given cuisine."""
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    """Prints ONLY the spicy foods with a heat level greater than 5."""
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    """Returns an integer representing the average heat level of all spicy foods."""
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, new_spicy_food):
    """Returns the original list with the new spicy food added."""
    spicy_foods.append(new_spicy_food)
    return spicy_foods

# Example spicy_foods list
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# Example of adding a new spicy food
new_spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

create_spicy_food(spicy_foods, new_spicy_food)

# Testing the functions 
print(get_names(spicy_foods))
print(get_spiciest_foods(spicy_foods))
print_spicy_foods(spicy_foods)
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))
print_spiciest_foods(spicy_foods)
print("Average heat level:", get_average_heat_level(spicy_foods))
