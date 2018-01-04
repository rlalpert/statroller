#! /usr/bin/python3
# statroller.py - Simple DnD stat roller

import diceroller

def roll_standard():
    # returns a list of integers
    stats = []
    for i in range(5):
        stats.append(roll_stat_standard())
    return stats


def roll_stat_standard():
    # returns a single stat, rolled in the standard way
    #   by rolling 4d6 and dropping the lowest roll
    roll = diceroller.roll_detailed('4d6')
    roll_list = roll[1][0]["all_rolls"]
    roll_list.sort()
    accepted_rolls = roll_list[1:4]
    stat = sum(accepted_rolls)
    return stat

if __name__ == '__main__':
    print('Rolling stats...')
    print(roll_standard())