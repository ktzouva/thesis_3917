from django.shortcuts import render
import os.path, math, csv, re, matlab.engine
# import matplotlib.pyplot as plt

def datamng_home(request):
    return render(request, 'datamng/datamng_home.html')

def runalg(request):
    checkinitial = os.path.isfile('./datasets/initial_dataset.csv')
    # checknan = os.path.isfile('./datasets/NaN_dataset.csv')

    # if checknan == False:
    #     nands = open("./datasets/NaN_dataset.csv", "w")
    #     nands.close()
    #
    # if checkinitial == True:
    #     initialds = open("./datasets/initial_dataset.csv", "r")
    #     Lines = initialds.readlines() #read all lines at once and put it in a list
    #
    #     for line in Lines:
    #         print("Line: {}".format(line.strip()))
    #         isNaN = 'NaN' in line
    #
    #         if isNaN == True:
    #             newLine = line.replace(line, "") #delete line with NaNs
    #
    #             nands = open("./datasets/NaN_dataset.csv", "a")
    #             Lines = nands.writelines(newLine)
    #             nands.close()
    #
    #         else:
    #             nands = open("./datasets/NaN_dataset.csv", "a")
    #             Lines = nands.writelines(line)
    #             nands.close()

    #read single values from csv
    nands = open('./datasets/initial_dataset.csv', 'r')

    #add lines to a list as separate variables
    content = nands.read()
    dataList = re.split(",|\n", content)

    print("dataList:", dataList)

    os.chdir("C:/Users/kosta/Desktop/Thesis/thesis_3917/datasets")

    eng = matlab.engine.start_matlab()
    eng.NaN_script(nargout=0)

    os.chdir("C:/Users/kosta/Desktop/Thesis/thesis_3917")

    nands.close()
    #initialds.close()

    return render(request, 'datamng/datamng_home.html')
