import random


#starting random
for i in range(3):
    print(random.randint(10,20))

#selecting leader
members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)

#rolling dice
dice1 = random.randint(1,7)
dice2 = random.randint(1,7)
print(f"({dice1},{dice2})")

class Dice:
    def roll(self):
        die1 = random.randint(1, 7)
        die2 = random.randint(1, 7)
        return die1, die2
dice = Dice()
print(dice.roll())