#!/usr/python

class EulerMethod:
    def __init__(self, diffFunc, initX, initY):
        self.func = diffFunc
        self.init = [initX, initY]
        
    def plot(self, stop, step):
        dot = self.init
        while dot[0] <= stop:
            print("(%d,%d)"%(dot[0],dot[1]))
            slope = self.func(dot[0], dot[1])
            dot[1] = dot[1] + slope * step
            dot[0] += step
        

if __name__ == '__main__':
    print("Python Script: Euler's Method\nUseage: calculating value of given differential equation using euler's method")
    
    