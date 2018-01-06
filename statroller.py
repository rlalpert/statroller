#! /usr/bin/python3
# statroller.py - Simple DnD stat roller

import diceroller

def roll_standard():
    # returns a list of integers
    stats = []
    for i in range(6):
        stats.append(roll_stat_standard())
    return stats

def roll_hardcore():
    # returns a list of integers
    stats = []
    for i in range(6):
        stats.append(roll_stat_hardcore())
    return stats

def roll_stat_standard():
    # returns a single stat, rolled in the standard way
    #   by rolling 4d6 and dropping the lowest roll
    roll = diceroller.roll_detailed("4d6")
    roll_list = roll[1][0]["all_rolls"]
    roll_list.sort()
    accepted_rolls = roll_list[1:4]
    stat = sum(accepted_rolls)
    return stat

def roll_stat_hardcore():
    # returns a single stat by rolling 3d6 with no dropped rolls
    roll = diceroller.roll_detailed("3d6")
    roll_list = roll[1][0]["all_rolls"]
    stat = sum(roll_list)
    return stat

if __name__ == "__main__":
    print("Rolling standard stats...")
    print(roll_standard())
    print("Rolling HARDCORE stats...")
    print(roll_hardcore())