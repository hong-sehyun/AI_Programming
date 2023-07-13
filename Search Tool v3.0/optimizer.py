from Setup import Setup

class HillClimbing:
    def __init__(self):
        Setup.__init__(self)
        self._pType = 0
        self._limitStock = 100

    def run(self):
        pass

    def displaySetting(self):
        if self._pType == 1:
            print()
            print("Mutation step size: ", self._delta)

    def setVariables(self, pType):
        self._pType = pType




class SteepestAscent(HillClimbing):
    def run(self, p):
        current = p.randomInit()
        # current = randomInit(p) # 'current' is a list of values
        valueC = p.evaluate(current)
        # valueC = evaluate(current, p)
        while True:
            neighbors = p.mutants(current)
            # neighbors = mutants(current, p)
            successor, valueS = self.bestOf(neighbors, p)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)


    def bestOf(self, neighbors, p): ###
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
    
    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")
        HillClimbing.displaySetting(self)

class FirstChoice(HillClimbing):
    def run(self, p):
        current = p.randomInit()   # 'current' is a list of values
        valueC = p.evaluate(current)
        i = 0
        while i < self._limitStock:
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
        p.storeResult(current, valueC)

    def displaySetting(self):
        print()
        print("Search algorithm: First-Choice Hill Climbing")
        HillClimbing.displaySetting(self)
        print('max evaluations with no improvement: {:,2f}'.format(self._limitStock))


class GradientDescent(HillClimbing):
    def run(self, p):
        # p = Numeric()
        current = p.randomInit()
        # current = randomInit(p) # 'current' is a list of values
        valueC = p.evaluate(current)
        # valueC = evaluate(current, p)
        while True:
            successor = p.takeStep(current, valueC)
            # neighbors = mutants(current, p)
            valueS = p.evaluate(successor)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)
    
    def bestOf(self, neighbors, p): ###
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

    def displaySetting(self):
        # p = Numeric()
        print()
        print("Search algorithm: Gradient Descent Hill Climbing")
        HillClimbing.displaySetting(self)
        print("update rate: ", self._alpha)
        print("increment for calculating derivatives." , self._dx)

        