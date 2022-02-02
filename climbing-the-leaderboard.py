from operator import index
from os import remove
from typing import OrderedDict


def climbingLeaderboard(ranked, player):
    indexes = []
    ranked.sort(reverse=True)

    
    for i in range(len(player)):
        ranked.append(player[i])
        ranked.sort(reverse=True)
        removeDuplicates = OrderedDict.fromkeys(ranked)
        ranked = list(removeDuplicates)
        indexes.append(ranked.index(player[i])+1)
        print(ranked)


    return indexes

if __name__ == '__main__':
    testArrayRanked = [100,90,90,80,75,60]
    testArrayPlayer = [50,65,77,90,102]
    print(climbingLeaderboard(testArrayRanked,testArrayPlayer))