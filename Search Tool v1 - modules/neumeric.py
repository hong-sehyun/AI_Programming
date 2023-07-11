import random
import math

DELTA = 0.01   # Mutation step size
LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement
NumEval = 0    # Total number of evaluations


def createProblem(fileName):
    # f = open(filename, "r")
    # expression = f.readline()

    # varNames = []
    # low = []
    # up = []

    # for line in f.readlines():
    #     _temp = line.split(",")
    #     varNames.append(_temp[0])
    #     low.append(float(_temp[1]))
    #     up.append(float(_temp[2]))
    # domain = [varNames, low, up]
    # return (expression, domain)

    fileName = input("Enter the filename of a function : ")
    inFile = open(fileName, 'r')
    expression = inFile.readline()
    varNames = []
    low = []
    up = []

    line = inFile.readline()
    for line in inFile.readlines():
        data = line.split(',')
        varNames.append(data(0))
        low.append(float(data(1)))
        up.append(float(data(2)))
        line = inFile.readline()
    
    
    domain = [varNames, low, up]
    return expression, domain

def inversion(current, i, j):  # Perform inversion
    curCopy = current[:]
    while i < j:
        curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
        i += 1
        j -= 1
        #break
    return curCopy

def randomMutant(current, p): # Apply inversion
    while True:
        i, j = sorted([random.randrange(p[0])
                       for _ in range(2)])
        if i < j:
            curCopy = inversion(current, i, j)
            break
    return curCopy

def randomInit(p):
    domain = p[1]
    init = []
    for i in range(0, len(domain[0])):
        init.append(random.uniform(domain[1][i], domain[2][i]))
    return init

# 기울기 구하는 함수
def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval
   
    NumEval += 1
    expr = p[0]         # p[0] is function expression
    varNames = p[1][0]  # p[1] is domain
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)


def mutate(current, i, d, p):
    curCopy = current[:]
    domain = p[1]
    l = domain[1][i]
    u = domain[2][i]
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy


def describeProblem(p):
    print()
    print("Objective function:")
    print(p[0])
    print("Search space:")
    varNames = p[1][0]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(f"{varNames[i]} : {low[i], up[i]}")

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))
    print(f"Minimum value: {minimum:,.3f}")
    print()
    print(f"Total number of evaluations: {NumEval:,}")


def bestOf(neighbors, p): ###
    best = neighbors[0]
    bestValue = evaluate(best, p)

    for i in range(1, len(neighbors)):
        newValeue = evaluate(neighbors[i], p)
        if newValeue < bestValue:
            best = neighbors[i]
            bestValue = newValeue    
    return best, bestValue


def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

