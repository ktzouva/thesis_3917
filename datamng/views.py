from django.shortcuts import render
import os.path, math

def datamng_home(request):
    return render(request, 'datamng/datamng_home.html')

def runalg(request):
    checkinitial = os.path.isfile('./datasets/initial_dataset.csv')
    checknan = os.path.isfile('./datasets/NaN_dataset.csv')

    if checknan == False:
        nands = open("./datasets/NaN_dataset.csv", "w")
        nands.close()

    if checkinitial == True:
        initialds = open("./datasets/initial_dataset.csv", "r")
        Lines = initialds.readlines() #read all lines at once and put it in a list

        for line in Lines:
            print("Line: {}".format(line.strip()))
            isNaN = 'NaN' in line

            if isNaN == True:
                newLine = line.replace("NaN,", "")
                newLine = line.replace(",NaN", "")

                nands = open("./datasets/NaN_dataset.csv", "a")
                Lines = nands.writelines(newLine)
                nands.close()

            else:
                nands = open("./datasets/NaN_dataset.csv", "a")
                Lines = nands.writelines(line)
                nands.close()

        initialds.close()

    return render(request, 'datamng/datamng_home.html')
