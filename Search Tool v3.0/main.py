from problem import *
from optimizer import *

def main():
    p, pType = selectProblem()
    alg = selectAlgorithm(pType)

    alg.run(p)

    p.describe()
    alg.displaySetting()
    p.report()


def selectProblem():
    print("select the problem type: ")
    print("1: Numeric")
    print("2: Tsp")

    pType = int(input("Enter the number: "))

    if pType == 1:
        p = Numeric()

    elif pType == 2:
        p = Tsp()

    else:
        print("Wrong input")
        
    p.setVariables()
    return p, pType


def selectAlgorithm(pType):
    print("select the Algorithm type: ")
    print("1: SteepestAscent")
    print("2: FirstChoice")
    print("3: GradientDescent")   

    aType = int(input("Enter the number: "))
    optimizers = {1: 'SteepestAscent()', 2: 'FirstChoice()', 3: 'GradientDescent()'}

    alg = eval(optimizers[aType])
    alg.setVariables(pType)

    return alg


    # if aType == 1:
    #     alg = SteepestAscent()

    # elif aType == 2:
    #     alg = FirstChoice()

    # elif aType == 3:
    #     alg = GradientDescent()

    # else:
    #     print("Wrong input")

    # return alg, aType

main()


