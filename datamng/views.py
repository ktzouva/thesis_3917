from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
# from yellowbrick.classifier import ClassificationReport
import os.path, math, csv, re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def datamng_home(request):
    return render(request, 'datamng/datamng_home.html')

def runalg(request):
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

    dataset1 = dataset.head(n=2) #Data exploration
    print(dataset1)

    sns.set(style="whitegrid", color_codes=True)
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.countplot(x="parity", data=dataset.reset_index(), hue='parity')
    sns.despine(offset=10, trim=True)
    plt.show()

    cols = [col for col in dataset.columns if col not in ['addition','subtraction','multiplication','division']]
    dataset_wo_cols = dataset[cols]
    target = dataset['parity']
    dataset_wo_cols.head(n=2)
    print(dataset_wo_cols)

    data_train, data_test, target_train, target_test = train_test_split(dataset_wo_cols, target, test_size = 0.30, random_state = 10)

    bayes = GaussianNB() #create an object of the type GaussianNB
    prediction = bayes.fit(data_train, target_train).predict(data_test) #train the algorithm on training data and predict using the testing data
    print(prediction.tolist())

    print("Gaussian Naive-Bayes accuracy: ", accuracy_score(target_test, prediction, normalize = True)) #print the accuracy score of the model

    # visualizer = ClassificationReport(bayes, classes=['0','1'])
    # visualizer.fit(data_train, target_train) # Fit the training data to the visualizer
    # visualizer.score(data_test, target_test) # Evaluate the model on the test data
    # g = visualizer.poof()

    return render(request, 'datamng/datamng_home.html')
