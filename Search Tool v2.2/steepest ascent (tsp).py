from problem import Tsp

import random
import math

# problem/tsp30.txt


def main():
    p = Tsp()
    # Create an instance of TSP
    p.setVariables()
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    p.storeResult(solution, minimum)
    # Show the problem and algorithm settings
    p.describe()
    displaySetting(p)
    # Report results
    p.report()
    

def steepestAscent(p):
    current = p.randomInit()   # 'current' is a list of city ids
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        (successor, valueS) = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC



# def mutants(current, p): # Apply inversion
#     n = p[0]
#     neighbors = []
#     count = 0
#     triedPairs = []
#     while count <= n:  # Pick two random loci for inversion
#         i, j = sorted([random.randrange(n) for _ in range(2)])
#         if i < j and [i, j] not in triedPairs:
#             triedPairs.append([i, j])
#             curCopy = inversion(current, i, j)
#             count += 1
#             neighbors.append(curCopy)
#     return neighbors



def bestOf(neighbors, p): ###
    # find best of neighbor
    best = neighbors[0]
    bestValue = p.evaluate(best)

    for i in range(1, len(neighbors)):
        newValue = p.evaluate(neighbors[i])
        if bestValue > newValue:
            best = neighbors[i]
            bestValue = newValue
    return best, bestValue

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")

main()