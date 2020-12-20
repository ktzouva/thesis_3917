from django.shortcuts import render
import os.path, math, csv, re, matlab.engine
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

    return render(request, 'datamng/datamng_home.html')
