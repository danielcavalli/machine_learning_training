import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import truncnorm
from math import sqrt

data_teste = pd.read_csv('data_teste.csv', sep=';', encoding='ISO-8859-1')

dificulty = data_teste['dificulty'].values.tolist()
value = data_teste['cost'].values.tolist()
size = data_teste['size'].values.tolist()
sentiment = data_teste['sentiment'].values.tolist()
number_of_samples = 1200
low = -0.5
high = 0.5

"""
class linear_regression:
    def __init__(self, value, size, sentiment, dificulty):
        self.value = value
        self.size = size
        self.sentiment = sentiment
        self.dificulty = dificulty
        self.vector = np.array([self.value,self.size,self.sentiment,self.dificulty])
        
    def estimate_random_value(self, w1, w2, w3):
        price = 0
        price += self.size*w1
        price += self.sentiment*w2
        price += w3
        return price
"""
def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        ((-1/sqrt(low)) - mean) / sd, ((1/sqrt(upp)) - mean) / sd, loc=mean, scale=sd)

input_vector = np.array([value,size,sentiment,dificulty])
X=truncated_normal(0,0.4,len(input_vector),len(input_vector))

wih = X.rvs((len(input_vector)+1,len(input_vector)))
who = X.rvs((1,5))
