import random

# 1 option
friends = ["Isaias", "Marconi", "Ester", "Rafaela", "Jonas", "Ruan", "Jojo"]
print(random.choice(friends))

# 2nd Option
random_index = random.randint(0,6)
print(friends[random_index])