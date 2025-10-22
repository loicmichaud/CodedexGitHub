import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
    return name.capitalize()

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

capitalized_suffixes = list(map(capitalize_suffix, suffixes))
random_names = [create_fantasy_name(prefixes, random.choice(capitalized_suffixes)) for _ in range(10)]

def fire_in_name(name):
    return 'f' in name.lower()

def concatenate_names(name1, name2):
    return name1 + ' ' + name2

filtered_names = list(filter(fire_in_name, random_names))
reduced_name = reduce(concatenate_names, filtered_names, '')

def display_name_info():
    print("Noms générés :", random_names)
    print("Noms avec 'Fire' :", filtered_names)
    print("Noms concaténés :", reduced_name)

display_name_info()