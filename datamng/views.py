from django.shortcuts import render
import os.path, math

def datamng_home(request):
    return render(request, 'datamng/datamng_home.html')

def runalg(request):

    isfile = os.path.isfile('./dataset1.csv')

    if isfile == True:

        f = open("dataset1.csv", "r")
        Lines = f.readlines() #read all lines at once and put it in a list

        for line in Lines:
            print("Line: {}".format(line.strip()))
            isNaN = 'NaN' in line

            if isNaN == True:
                newLine = line.replace("NaN,", "")
                print("%s", newLine)
                print("True1")

            if isNaN == True:
                newLine = line.replace(",NaN", "")
                print("%s", newLine)
                print("True")
        f.close()

    return render(request, 'datamng/datamng_home.html')
