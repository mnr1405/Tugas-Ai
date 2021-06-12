import pandas as pd
from math import *
from random import *
import numpy as np
from collections import *


def train(start,end):
    dataset = pd.read_csv("Diabetes.csv")
    data_train = []
    key = [x for x in dataset]
    train_data = dataset.iloc[start:end, :]
    pregnan = [ i for i in train_data[key[0]] ]
    glucose = [ i for i in train_data[key[1]] ]
    blood_press = [ i for i in train_data[key[2]] ]
    skin_thick = [ a for a in train_data[key[3]] ]
    insulin = [ a for a in train_data[key[4]] ]
    bmi = [ a for a in train_data[key[5]] ]
    diabet_pedigree = [ a for a in train_data[key[6]] ]
    age = [ a for a in train_data[key[7]] ]
    outcome = [ a for a in train_data[key[8]] ]

    for i in range(len(pregnan)):
        data_train.append([pregnan[i], glucose[i], blood_press[i], skin_thick[i],insulin[i], bmi[i],diabet_pedigree[i],age[i]])
    return data_train,outcome

def test(start,end):
    test = []
    dataset = pd.read_csv("Diabetes.csv")
    
    if end == 0:
        test_data = dataset.iloc[start:len(dataset)+1, :]
        key = [x for x in dataset]
        pregnan = [ a for a in test_data[key[0] ] ]
        glucose = [ a for a in test_data[key[1] ] ]
        blood_press = [ a for a in test_data[key[2] ] ]
        skin_thick = [ a for a in test_data[key[3] ] ]
        insulin = [ a for a in test_data[key[4] ] ]
        bmi = [ a for a in test_data[key[5] ] ]
        diabet_pedigree = [ a for a in test_data[key[6] ] ]
        age = [ a for a in test_data[key[7] ] ]
        outcome = [ a for a in test_data[key[8] ] ]
        for i in range(len(pregnan)):
            test.append([pregnan[i], glucose[i], blood_press[i], skin_thick[i],insulin[i], bmi[i],age[i],diabet_pedigree[i]])
        return test,outcome
    
    else:
        test_data = dataset.iloc[start:end, :]
        key = [x for x in dataset]
        pregnan = [ a for a in test_data[key[0] ]]
        glucose = [ a for a in test_data[key[1]] ]
        blod_press = [ a for a in test_data[key[2]] ]
        skin_thick = [ a for a in test_data[key[3]] ]
        insulin = [ a for a in test_data[key[4]] ]
        bmi = [ a for a in test_data[key[5]] ]
        diabet_pedigree = [ a for a in test_data[key[6]] ]
        age = [ a for a in test_data[key[7]] ]
        outcome = [ a for a in test_data[key[8]] ]
        for i in range(len(pregnan)):
            test.append([pregnan[i], glucose[i], blod_press[i], skin_thick[i],insulin[i], bmi[i],age[i],diabet_pedigree[i]])
        return test,outcome


def euclidean_distance(instance1, instance2):
    instance1 = np.array(instance1) 
    instance2 = np.array(instance2)
    return np.linalg.norm(instance1 - instance2)



def harmonic_weights(neighbors, all_results=True):
    class_counter = Counter()   
    number_of_neighbors = len(neighbors)
    for index in range(number_of_neighbors):
        class_counter[neighbors[index][2]] += 1/(index+1)
    labels, votes = zip(*class_counter.most_common())
    winner = class_counter.most_common(1)[0][0]
    voteswinner = class_counter.most_common(1)[0][1]
    if all_results:
        total = sum(class_counter.values(), 0.0)
        for key in class_counter:
             class_counter[key] /= total
        return winner, class_counter.most_common()
    else:
        return winner, voteswinner / sum(votes)

def knn(training_set, labels, test_instance,k, distance=euclidean_distance):
    distances = []
    for index in range(len(training_set)):
        dist = distance(test_instance, training_set[index])
        distances.append((training_set[index], dist, labels[index]))
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]
    return neighbors

# menghitung  akurasi
def akurasi(actual, prediksi):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == prediksi[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0


dataset_train1 = train(0,614)
dataset_test1 = test(614,0)
train1 = dataset_train1[0]
test1 = dataset_test1[0]
label1 = dataset_train1[1]
actual_label1 = dataset_test1[1]


dataset_train2 = train(0,461)
dataset_test2 = test(461,615)
train2 = dataset_train2[0]
train2.extend(train(615,769)[0])
test2 = dataset_test2[0]
label2 = dataset_train2[1]
label2.extend(train(615,769)[1])
actual_label2 = dataset_test2[1]


dataset_train3 = train(0,307)
dataset_test3 = test(307,462)
train3 = dataset_train3[0]
train3.extend(train(462,769)[0])
test3 = dataset_test3[0]
label3 = dataset_train3[1]
label3.extend(train(462,769)[1])
actual_label3 = dataset_test3[1]

dataset_train4 = train(0,154)
dataset_test4 = test(154,308)
train4 = dataset_train4[0]
train4.extend(train(308,769)[0])
test4 = dataset_test4[0]
label4 = dataset_train4[1]
label4.extend(train(308,769)[1])
actual_label4 = dataset_test4[1]

dataset_train5 = train(155,769)
dataset_test5 = test(0,155)
train5 = dataset_train5[0]
test5 = dataset_test5[0]
label5 = dataset_train5[1]
actual_label5 = dataset_test5[1]



data =  [[train1,test1,label1,actual_label1],
        [train2,test2,label2,actual_label2],
        [train3,test3,label3,actual_label3],
        [train4,test4,label4,actual_label4],
        [train5,test5,label5,actual_label5]]

print("dengan nilai k: ",20)
acc = []

for i in range(len(data)):
    train_data = data[i][0]
    test_data = data[i][1]
    label_train_data = data[i][2]
    actual_data = data[i][3]
    compare = []
    for j in range(len(test_data)):
        neighbors = knn(train_data,label_train_data, test_data[j], k=20)
        compare.append(harmonic_weights(neighbors)[0])
    print("akurasi: ",akurasi(actual_data, compare))
acc.append(akurasi(actual_data, compare))
rate_of_acc = sum(acc)/len(acc)
print("rata-rata akurasi: ",rate_of_acc)
