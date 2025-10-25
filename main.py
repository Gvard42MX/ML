# main.py
from RPS_game import play, quincy, mrugesh, kris, abbey
from RPS import player

# Tes melawan semua bot
print("Testing against Quincy:")
print(play(player, quincy, 1000))

print("\nTesting against Mrugesh:")
print(play(player, mrugesh, 1000))

print("\nTesting against Kris:")
print(play(player, kris, 1000))

print("\nTesting against Abbey:")
print(play(player, abbey, 1000))


