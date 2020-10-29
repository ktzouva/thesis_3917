from django.shortcuts import render
import os.path, math, csv, re

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
                newLine = line.replace(line, "") #delete line with NaNs

                nands = open("./datasets/NaN_dataset.csv", "a")
                Lines = nands.writelines(newLine)
                nands.close()

            else:
                nands = open("./datasets/NaN_dataset.csv", "a")
                Lines = nands.writelines(line)
                nands.close()

        #read single values from csv
        nands = open('./datasets/NaN_dataset.csv', 'r')

        #count lines of file
        counter = 0
        content = f.read()
        dataList = re.split(",|\n", content)

        for i in dataList:
        	if i:
        		counter += 1

        print("dataList:", dataList)
        
        nands.close()
        initialds.close()

    return render(request, 'datamng/datamng_home.html')
