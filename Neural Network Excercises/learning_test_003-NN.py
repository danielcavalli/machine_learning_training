import numpy as np
from itertools import chain
#This represents a skeleton of a neuron. Here the algorithm knows only 
#                how to tell apart a small set of values into weights.
class This_is_a_neuron:
    def __init__(self,input_length,weights=None):
        if weights is None:
            self.weights = np.ones(input_length) *0.5
        else:
            self.weights = weights
    @staticmethod
    def unit_step_function(x):
        if x > 0.5:
            return 1
        return 0
    
    def __call__(self,in_data):
        weighted_input = self.weights * in_data
        weighted_sum = weighted_input.sum()
        return This_is_a_neuron.unit_step_function(weighted_sum)

def call_01():
    #This is only here for the pourpose of not variable spamming the Variable Explorer in Spyder
    p = This_is_a_neuron(2,np.array([0.5,0.5]))
    for x in [np.array([0, 0]), np.array([0, 1]), 
          np.array([1, 0]), np.array([1, 1])]:
        y = p(np.array(x))
        print(x,y)
call_01()
#In this Class the neuron learns to adapt itself to a given Dataset.
#What this means is that it is capable of changin it's weights to better suit the pattern in the Data.
from collections import Counter as C
class Perceptron:
    def __init__(self, input_length,weights=None):
        if weights is None:
            self.weights = np.random.random((input_length)) *2 - 1
        self.learning_rate = 0.1
    
    @staticmethod
    def unit_step(x):
        if x < 0:
            return 0
        return 1
    
    def __call__(self, in_data):
        weighted_input = self.weights * in_data
        weighted_sum = weighted_input.sum()
        return Perceptron.unit_step(weighted_sum)
    
    def adjust(self,
               target_result,
               calculated_result,
               in_data):
        error = target_result - calculated_result
        for i in range(len(in_data)):
            correction = error * in_data[i] * self.learning_rate
            self.weights[i] += correction
#Here it adjusts the line to fit A in one side and B at the other
def above_line(point, line_func):
    x, y = point
    if y > line_func(x):
        return 1
    else:
        return 0
#Given a 100 random points it must fit them on the previous mentioned rule. (It must pass thorough the 0,0 point)
#Sometimes it is not possible using the current logic.
points = np.random.randint(1, 100, (100,2))
p = Perceptron(2)
def lin1(x):
    return x + 4
def call_02():
    for point in points:
        p.adjust(above_line(point,lin1),p(point),point)
    evaluation = C()
    for point in points:
        if p(point) == above_line(point, lin1):
            evaluation["correct"] += 1
        else:
            evaluation["wrong"] += 1
    print(evaluation.most_common())
    return evaluation
eve = call_02()
while eve["wrong"] > 0:
    eve = call_02()
    
#To solve the Origin Only problem some smart boys came with a smart solution: Bias variable. This is it:
from matplotlib import pyplot as plt
%matplotlib inline

def call_03():   
    cls = [[], []]
    for point in points:
        cls[above_line(point, lin1)].append(tuple(point))
    colours = ("r", "b")
    for i in range(2):
        X, Y = zip(*cls[i])
        plt.scatter(X, Y, c=colours[i])
        
    X = np.arange(-3, 120)
        
    m = -p.weights[0] / p.weights[1]
    print(m)
    plt.plot(X, m*X, label="ANN line")
    plt.plot(X, lin1(X), label="line1")
    plt.legend()
    plt.show()
call_03()

def call_04():
    class1 = [(3, 4), (4.2, 5.3), (4, 3), (6, 5), (4, 6), (3.7, 5.8),
              (3.2, 4.6), (5.2, 5.9), (5, 4), (7, 4), (3, 7), (4.3, 4.3) ] 
    class2 = [(-3, -4), (-2, -3.5), (-1, -6), (-3, -4.3), (-4, -5.6), 
              (-3.2, -4.8), (-2.3, -4.3), (-2.7, -2.6), (-1.5, -3.6), 
              (-3.6, -5.6), (-4.5, -4.6), (3.7, 5.8) ]
    def lin1(x):
        return  x + 4
    for point in class1:
        p.adjust(1, 
                 p(point), 
                 point)
    for point in class2:
        p.adjust(0, 
                 p(point), 
                 point)
        
    evaluation = C()
    for point in chain(class1, class2):
        if p(point) == 1:
            evaluation["correct"] += 1
        else:
            evaluation["wrong"] += 1
            
    testpoints = [(3.9, 6.9), (-2.9, -5.9)]
    for point in testpoints:
        print(p(point))
            
    print(evaluation.most_common())
    X, Y = zip(*class1)
    plt.scatter(X, Y, c="r")
    X, Y = zip(*class2)
    plt.scatter(X, Y, c="b")
    x = np.arange(-7, 10)
    y = 5*x + 10 
    m = -p.weights[0] / p.weights[1]
    plt.plot(x, m*x)
    plt.show()

for i in range(5):
    p = Perceptron(2)
    call_04()












