import numpy as np
from sklearn import datasets
from collections import Counter
from cavalli_basics import levenshtein
from time import time

"""Preciso estudar sobre Orientação a Objeto em Python
_____________________________

class k_nearest_n:
    def __init__(self, dataset, data, label):
        self.dataset = dataset
        self.data = data
        self.label = label
    def seed(self):
        np.random.seed(42)
        indices = np.random.permutation(len(self.data))
        n_training_samples = 12
        learn_data = self.data
        return True
_____________________________
"""
iris = datasets.load_iris()
iris_data = iris.data
iris_label = iris.target
np.random.seed(42)
indices = np.random.permutation(len(iris_data))
nts = 12
learn_data = iris_data[indices[:-nts]]
learn_labels = iris_label[indices[:-nts]]
test_data = iris_data[indices[-nts:]]
test_labels = iris_label[indices[-nts:]]

def distance(instance1, instance2):
    # just in case, if the instances are lists or tuples:
    instance1 = np.array(instance1) 
    instance2 = np.array(instance2)
    
    return np.linalg.norm(instance1 - instance2)

def get_neigh(train_set, labels,test_instance,k,distance=distance):
    distances=[]
    for i in range(len(train_set)):
        dist = distance(test_instance, train_set[i])
        distances.append((train_set[i],dist,labels[i]))
    distances.sort(key=lambda x:x[1])
    neigh = distances[:k]
    return neigh

def OPEN_DEMOCRACY(neighbors):
    class_counter = Counter()
    for neighbor in neighbors:
        class_counter[neighbor[2]] += 1
    labels, votes = zip(*class_counter.most_common())
    winner = class_counter.most_common(1)[0][0]
    votes4winner = class_counter.most_common(1)[0][1]
    return winner, votes4winner/sum(votes)

def DEMOCRACY(neighbors):
    class_counter = Counter()
    for neighbor in neighbors:
        class_counter[neighbor[2]] += 1
    return class_counter.most_common(1)[0][0]

def AUTOCRACY(neigh,all_results=True):
    class_counter = Counter()
    nOn = len(neigh)
    for i in range(nOn):
        dist = neigh[i][1]
        label = neigh[i][2]
        class_counter[label] += 1/(dist**2+1)
    labels, votes = zip(*class_counter.most_common())
    winner = class_counter.most_common(1)[0][0]
    votes4winner = class_counter.most_common(1)[0][1]
    if all_results:
        total = sum(class_counter.values(), 0.0)
        for key in class_counter:
            class_counter[key] /= total
        return winner, class_counter.most_common()
    else:
        return winner, votes4winner / sum(votes)

def DEMOCRACY_is_BROKEN(neigh,all_results=True):
    class_counter = Counter()
    nOn = len(neigh)
    for i in range(nOn):
        class_counter[neigh[i][2]] += 1/(i+1)
    labels, votes = zip(*class_counter.most_common())
    winner = class_counter.most_common(1)[0][0]
    votes4winner = class_counter.most_common(1)[0][1]
    if all_results:
        total = sum(class_counter.values(), 0.0)
        for key in class_counter:
            class_counter[key] /= total
        return winner, class_counter.most_common()
    else:
        return winner, votes4winner / sum(votes)

def local_calls(nts, 
                learn_data = learn_data, 
                learn_labels=learn_labels,
                test_data=test_data,
                distance=distance):
    for i in range(nts):
        neighbors = get_neigh(learn_data,learn_labels,test_data[i],6,distance=distance)
        print("index: ", i, 
          ", result of vote: ", 
          AUTOCRACY(neighbors,
                                all_results=True))
    return neighbors
neighbors = local_calls(nts)
#An Auto Corrector made using K-NN and Levenshtein Distance technique.
def auto_correct(dictionaire):
    start_time = time()
    words = []
    correction = []
    neigh = []
    i = -1
    with open("british-english.txt") as fh:
        for line in fh:
            word = line.strip()
            words.append(word)
    for word in dictionaire:
        i += 1
        neigh.append(get_neigh(words,words,word,3,distance=levenshtein))
        correction.append(DEMOCRACY_is_BROKEN(neigh[i], all_results=False))
    elapsed_time = time() - start_time
    print(elapsed_time)
    return correction

corrected = auto_correct(["Harse", "Abril", "Hame"])
#Calculating precision





























