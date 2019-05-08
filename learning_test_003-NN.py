import numpy as np
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

def no_waste_in_here():
    #This is only here for the pourpose of not variable spamming the Variable Explorer in Spyder
    p = This_is_a_neuron(2,np.array([0.5,0.5]))
    for x in [np.array([0, 0]), np.array([0, 1]), 
          np.array([1, 0]), np.array([1, 1])]:
        y = p(np.array(x))
        print(x,y)
no_waste_in_here()
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
#Given a 100 random points it must fit them on the previous mentioned rule. 
#Sometimes it is not possible, those are one of the cases where we can see that a more robust models would
                                                                                          # learn to adapt
points = np.random.randint(1, 100, (100,2))
p = Perceptron(2)
def lin1(x):
    return x + 4
def no_waste_in_here():
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
eve = no_waste_in_here()
while eve["wrong"] > 0:
    eve = no_waste_in_here()
    
#Next: Making a network of neurons out of a Perceptron.