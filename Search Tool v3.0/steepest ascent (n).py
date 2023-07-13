# from numeric import *

from problem import Numeric

# 제일 좋은 것
# problem/Convex.txt

def main():
    # Create an instance of numerical optimization problem
    p = Numeric()
    p.setVariables()
    # Call the search algorithm
    solution, value = steepestAscent(p)
    p.storeResult(solution, value)
    # Show the problem and algorithm settings
    # describeProblem(p)
    p.describe()
    displaySetting(p)
    # Report results
    # displayResult(solution, minimum)
    p.report()



def steepestAscent(p):
    # p = Numeric()
    current = p.randomInit()
    # current = randomInit(p) # 'current' is a list of values
    valueC = p.evaluate(current)
    # valueC = evaluate(current, p)
    while True:
        neighbors = p.mutants(current)
        # neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC



# def mutants(current, p): ###
#     neighbors = []
#     for i in range(len(current)):
#         mutant = mutate(current, i, DELTA, p)
#         neighbors.append(mutant)
#         mutant = mutate(current, i, -DELTA, p)
#         neighbors.append(mutant)

#     return neighbors     # Return a set of successors


def bestOf(neighbors, p): ###
    # p = Numeric()
    best = neighbors[0]
    bestValue = p.evaluate(best)
    # bestValue = evaluate(best, p)

    for i in range(1, len(neighbors)):
        newValue = p.evaluate(neighbors[i])
        if bestValue > newValue:
            best = neighbors[i]
            bestValue = newValue

    return best, bestValue

def displaySetting(p):
    # p = Numeric()
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())  # p._delta 라고 변수에 직접적으로 접근하면 안됨

main()