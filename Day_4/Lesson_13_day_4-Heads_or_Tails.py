#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

#Important, the first letter should be capitalised and spelt exactly like in the example e.g. "Heads", not "heads".

#There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".

#e.g. 1 means Heads 0 means Tails

# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

# player_1 = input(str("Escolha um dos lados da moeda, cara ou coroa: "))
# player_2 = int(random.randint(1,3))
# player_1 = player_1.lower()
# print(player_1)
player = random.randint(0,1)

if player ==1:
  coin = str('Heads')
else:
  coin = str('Tails')
print(coin)