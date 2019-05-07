import numpy as np
class NeuralNetwork:
    
    def __init__(self,
                 no_in_nod,
                 no_out_nod,
                 no_hid_nod,
                 learning_rate):
        self.no_in_nod = no_in_nod
        self.no_out_nod = no_out_nod
        self.no_hid_nod = no_hid_nod
        self.learning_rate = learning_rate
        self.create_weight_matrices()
        
    def create_weight_matrices(self):
        
    