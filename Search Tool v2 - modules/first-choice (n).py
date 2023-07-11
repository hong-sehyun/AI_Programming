from problem import Numeric

import random
import math

# 좋은 것
# problem/Convex.txt

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement

def main():
    p = Numeric()
    # Create an instance of numerical optimization problem
    p.setVariables()
    # p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    p.storeResult(solution, minimum)
    # Show the problem and algorithm settings
    p.describe()
    displaySetting(p)
    # Report results
    p.report()


def firstChoice(p):
    current = p.randomInit()   # 'current' is a list of values
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


# def randomMutant(current, p): ###
#     i = random.randint(0, len(current)-1)

#     if random.uniform(0,1) > 0.5:
#         d = DELTA
#     else:
#         d = -DELTA

#     return mutate(current, i, d, p) # Return a random successor

def displaySetting(p):
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())

main()