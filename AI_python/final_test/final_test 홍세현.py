import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

def measure(func):
    """
    Decorator function
    Logging을 이용해 x값, y값, 계산값을 출력할 수 있는 기능을 추가
    """
    def wrapper(self, idx):
        x = self.x_vals[idx]
        y = self.y_vals[idx]
        r = func(self, idx)
        logging.info(f'(x={x}, y={y}) -> {r}')
        return r
    return wrapper  

class Evaluator:
    def __init__(self, filename):
        """
            filename에 주어진 경로에서 읽기 전용으로 csv 파일을 읽어서
            각 줄에 있는 수식과 변수 값을 저장

            csv 파일은 수식,x값,y값 으로 구성되어 있음

            ex) equations.txt
            10*x + 2*y,2,5
            0.5*x - 1.8*y,7,3
        """

        # open써서 파일 열고 for문으로 줄읽어오고 split 으로 csv값 구분해서 저장
        self.equations = []
        self.x_vals = []
        self.y_vals = []

        with open(filename, 'r') as csvfile:
            for line in csvfile:
                equation, x_val, y_val = line.strip().split(',')
                self.equations.append(equation)
                self.x_vals.append(int(x_val))
                self.y_vals.append(int(y_val))
        

    @measure
    def solve(self, idx):
        """
        idx 번째 수식을 계산한 값을 반환

        ex)
        solve(1) 은 equations.txt 의 0.5*x - 1.8*y가
        x=7, y=3일 때 값을 계산하여 반환

        solve 내부에는 logging이나 print 사용하지 말 것

        exec또는 eval을 잘 쓰면 됨
        exec('x='+eqn[1])
        exec('y='+eqn[2])
        r = eval(eqn[0])
        """
        eqn = self.equations
        exec('x='+str(self.x_vals[idx]))
        exec('y='+str(self.y_vals[idx]))

        r = eval(eqn[idx])
        return r

def main():
    evaluator = Evaluator('equations.txt')
    assert np.allclose(evaluator.solve(0), 30)
    assert np.allclose(evaluator.solve(1), -1.9)

main()