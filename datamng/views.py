import os.path, csv, re, numpy
import pandas as pd
from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ClassificationReport

def datamng_home(request):
    if request.user.is_authenticated:
        return render(request, 'datamng/datamng_home.html')
    else:
        return render(request, 'datamng/datamng_failed.html')

def runalg(request):
    if request.user.is_authenticated:
        #read single values from csv
        dataset = open('./dataset.csv', 'r')

        #add lines to a list as separate variables
        content = dataset.read()
        dataList = re.split(",|\n", content)

        print("\n")
        print("dataList:", dataList)
        print("\n")

        dataset.close()

        #preprocessing
        headers = ["addition","subtraction","multiplication","division", "parity"]
        dataset = pd.read_csv('./dataset.csv', names=headers)

        cols = [col for col in dataset.columns if col not in ['addition','subtraction','multiplication','division']]
        y = dataset[cols]
        y.head(n=2)
        y = numpy.ravel(y)
        print("y:", y)
        print("\n")

        cols1 = [col for col in dataset.columns if col not in ['headers', 'parity']]
        X = dataset[cols1]
        X.head(n=2)
        print("X:", X)
        print("\n")

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
        print("\n")

        accuracy = accuracy_score(target_test, prediction, normalize = True)
        print("Gaussian Naive-Bayes accuracy: ", accuracy) #print the accuracy score of the model
        print("\n")

        bayes.classes_[0]
        visualizer = ClassificationReport(bayes)
        visualizer.fit(data_train, target_train) # Fit the training data to the visualizer
        visualizer.score(data_test, target_test) # Evaluate the model on the test data
        g = visualizer.poof()

        list_content = content.split()
        list_datatrain = data_train.values.tolist()
        list_datatest = data_test.values.tolist()

        args = {'content': list_content, 'data_train': list_datatrain, 'target_train': target_train, 'data_test': list_datatest, 'target_test': target_test, 'prediction': prediction, 'accuracy': accuracy}

        return render(request, 'datamng/datamng_home.html', args)
    else:
        return render(request, 'datamng/datamng_failed.html')
