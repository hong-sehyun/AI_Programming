from problem import Tsp

import random
import math

# problem/tsp30.txt
LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement


def main():
    p = Tsp()
    # Create an instance of TSP
    p.setVariables()    # 'p': (numCities, locations, distanceTable)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    p.storeResult(solution, minimum)
    # Show the problem and algorithm settings
    p.describe()
    displaySetting(p)
    # Report results
    p.report()
    

def firstChoice(p):
    current = p.randomInit()   # 'current' is a list of city ids
    valueC = p.evaluate(current)
    i = 0
    while i < LIMIT_STUCK:
        successor = p.randomMutant(current)
        valueS = p.evaluate(successor)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC



def randomMutant(current, p): # Apply inversion
    while True:
        i, j = sorted([random.randrange(p[0])
                       for _ in range(2)])
        if i < j:
            curCopy = p.inversion(current, i, j)
            break
    return curCopy

def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print("Max evaluations with no improvement: {0:,} iterations"
          .format(LIMIT_STUCK))

main()