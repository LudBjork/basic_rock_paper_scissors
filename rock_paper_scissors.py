import random as rnd
import numpy as np

def play(inn):
    try:
        rps = {"rock": 0, "paper": 1, "scissors": 2}
        rng = rnd.randint(0,2)
        if rng == rps[inn]:
            print("Draw.")
        elif rps[inn] == 1 and rng == 0:
            print("You win!")
        elif rps[inn] == 0 and rng == 2:
            print("You win!")
        else: 
            print("You lose!") 
    except KeyError as K:
        print(K, "is not rock, paper or scissors")

if __name__ == "__main__":
    x = input("rock/paper/scissors:")
    play(x)
