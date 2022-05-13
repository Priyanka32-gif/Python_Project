# Mablib Game
from os import name


adj = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
verb = input("Enter a verb: ")
place = input("Enter the place:")
place2= input("Enter another place: ")
name = input("Enter a name: ")
plural_noun = input("Enter a plural name: ")

show = f"Once upon a time, there was a {name} who was {adj} and used to {verb} all the time.. One day, the {name} decided to go to {place}.There {name} experience a {adj2} thing. The {name} had a small hut in the middle of {place2}. The {name} used to meditate and do spritual rituals. Many {plural_noun} used to visit {name} and asked for a advise and sugestations. The {name} doesn't even pluck flowers from the trees."

print(show)
