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
        #read single values from csv
        dataset = open('./dataset.csv', 'r')
        content = dataset.read()
        dataset.close()

        #preprocessing
        headers = ["addition","subtraction","multiplication","division", "parity"]
        dataset = pd.read_csv('./dataset.csv', names=headers)

        cols = [col for col in dataset.columns if col not in ['addition','subtraction','multiplication','division']]
        y = dataset[cols]

        cols1 = [col for col in dataset.columns if col not in ['headers', 'parity']]
        X = dataset[cols1]

        data_train, data_test, target_train, target_test = train_test_split(X, y, test_size = 0.45, random_state = 10)

        bayes = GaussianNB() #create an object of the type GaussianNB

        prediction = bayes.fit(data_train, target_train).predict(data_test) #train the algorithm on training data and predict using the testing data

        accuracy = accuracy_score(target_test, prediction, normalize = True)

        bayes.classes_[0]
        visualizer = ClassificationReport(bayes)
        visualizer.fit(data_train, target_train) # Fit the training data to the visualizer
        visualizer.score(data_test, target_test) # Evaluate the model on the test data
        g = visualizer.poof()

        list_content = content.split()
        list_datatrain = data_train.values.tolist()
        list_datatest = data_test.values.tolist()

        args = {'content': list_content, 'data_train': list_datatrain, 'target_train': target_train, 'data_test': list_datatest, 'target_test': target_test, 'prediction': prediction, 'accuracy': accuracy}

        return render(request, 'datamng/datamng_runalg.html', args)
