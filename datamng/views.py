import pandas as pd
from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import classification_report

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

        parityCol = [col for col in dataset.columns if col not in ['addition','subtraction','multiplication','division']]
        y = dataset[parityCol]

        dataCols = [col for col in dataset.columns if col not in ['headers', 'subtraction', 'multiplication','division', 'parity']]
        X = dataset[dataCols]

        data_train, data_test, target_train, target_test = train_test_split(X, y, random_state = 10)

        bayes = GaussianNB() #create an object of the type GaussianNB

        prediction = bayes.fit(data_train, target_train).predict(data_test) #train the algorithm on training data and predict using the testing data

        accuracy = accuracy_score(target_test, prediction, normalize = True)

        classification_report(bayes, data_train, target_train, data_test, target_test, classes = ['Even', 'Odd'])

        list_content = content.split()
        list_datatrain = data_train.values.tolist()
        list_targettrain = target_train.values.tolist()
        list_datatest = data_test.values.tolist()
        list_targettest = target_test.values.tolist()

        return render(request, 'datamng/datamng_runalg.html', {'content': list_content, 'data_train': list_datatrain, 'target_train': list_targettrain, 'data_test': list_datatest, 'target_test': list_targettest, 'prediction': prediction, 'accuracy': accuracy})
