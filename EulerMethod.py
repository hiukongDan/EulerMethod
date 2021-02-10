#!/usr/python

class EulerMethod:
    def __init__(self, diffFunc, initX, initY):
        self.func = diffFunc
        self.init = [initX, initY]
        
    def plot(self, stop, step):
        dot = [self.init[0], self.init[1]]
        while dot[0] <= stop:
            print("(%f,%f)"%(dot[0],dot[1]))
            slope = self.func(dot[0], dot[1])
            dot[1] = dot[1] + slope * step
            dot[0] += step
        

if __name__ == '__main__':
    print("Python Script: Euler's Method\nUseage: calculating value of given differential equation using euler's method")
    
    print("Example: dy/dx = 6*x*x - 3*x*x*y with f(0) = 3")
    M = EulerMethod(lambda x, y: 6*x*x-3*x*x*y, 0,3)
    print("step = 1")
    M.plot(1,1)
    print("step = 0.1")
    M.plot(1, 0.1)