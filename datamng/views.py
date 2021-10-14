from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ClassificationReport
import os.path, math, csv, re, numpy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def datamng_home(request):
    if request.user.is_authenticated:
        return render(request, 'datamng/datamng_home.html')
    else:
        return render(request, 'datamng/datamng_failed.html')

def runalg(request):
    if request.user.is_authenticated:
        checkinitial = os.path.isfile('./datasets/initial_dataset.csv')

        #read single values from csv
        initialds = open('./datasets/initial_dataset.csv', 'r')

        #add lines to a list as separate variables
        content = initialds.read()
        dataList = re.split(",|\n", content)

        print("dataList:", dataList)

        initialds.close()

        #preprocessing
        url = './datasets/initial_dataset.csv'

        headers = ["addition","subtraction","multiplication","division", "parity"]
        dataset = pd.read_csv(url, names=headers)

        cols = [col for col in dataset.columns if col not in ['addition','subtraction','multiplication','division']]
        y = dataset[cols]
        y.head(n=2)
        y = numpy.ravel(y)
        print("y:", y)

        cols1 = [col for col in dataset.columns if col not in ['headers', 'parity']]
        X = dataset[cols1]
        X.head(n=2)
        print("X:", X)

        data_train, data_test, target_train, target_test = train_test_split(X, y, test_size = 0.45, random_state = 10)

        print("data_train:", data_train)
        print("\n")
        print("target_train:", target_train)
        print("\n")
        print("data_test:", data_test)
        print("\n")
        print("target_test:", target_test)
        print("\n")

        bayes = GaussianNB() #create an object of the type GaussianNB
        prediction = bayes.fit(data_train, target_train).predict(data_test) #train the algorithm on training data and predict using the testing data
        print("prediction:", prediction.tolist())

        accuracy = accuracy_score(target_test, prediction, normalize = True)
        print("Gaussian Naive-Bayes accuracy: ", accuracy) #print the accuracy score of the model

        bayes.classes_[0]
        visualizer = ClassificationReport(bayes)
        visualizer.fit(data_train, target_train) # Fit the training data to the visualizer
        visualizer.score(data_test, target_test) # Evaluate the model on the test data
        g = visualizer.poof()

        list_content = content.split()
        list_datatrain = data_train.values.tolist()
        # list_targettrain = target_train.values.tolist()
        list_datatest = data_test.values.tolist()
        # list_targettest = target_test.values.tolist()
        # list_prediction = prediction.values.tolist()

        args = {'content': list_content, 'data_train': list_datatrain, 'target_train': target_train, 'data_test': list_datatest, 'target_test': target_test, 'prediction': prediction, 'accuracy': accuracy}

        return render(request, 'datamng/datamng_home.html', args)
    else:
        return render(request, 'datamng/datamng_failed.html')
