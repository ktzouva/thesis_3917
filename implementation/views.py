from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ImplementationForm
from .models import Nums
import os.path
#from django.contrib.auth.decorators import login_required

class ImplementationView(TemplateView):

    template_name = 'implementation/implementation_home.html'

    #@login_required(login_url="accounts/login/")
    def get(self, request):
        form = ImplementationForm()
        objects = Nums.objects.all()

        args = {'form': form, 'objects': objects}
        return render(request, self.template_name, args)

    #@login_required(login_url="accounts/login/")
    def post(self, request):
        form = ImplementationForm(request.POST)
        if form.is_valid():
            # form.save()
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']

            sNum1 = str(num1)
            sNum2 = str(num2)

            numString = ''
            numString += sNum1
            numString += ','
            numString += sNum2

            userID = request.user.username
            if userID == '':
                userID = 'null'

            addition = num1 + num2
            subtraction = num1 - num2
            multiplication = num1 * num2
            division = num1 / num2

            sAddition = str(addition)
            sSubtraction = str(subtraction)
            sMultiplication = str(multiplication)
            sDivision = str(division)

            resString = ''
            resString += sAddition
            resString += ','
            resString += sSubtraction
            resString += ','
            resString += sMultiplication
            resString += ','
            resString += sDivision

            isfile = os.path.isfile('./datasets/initial_dataset.csv')

            if isfile == False:
                f = open("./datasets/initial_dataset.csv", "w+")
                f.write("%s,%s,%s,%s,%s \r" % (sAddition, sSubtraction, sMultiplication, sDivision, userID))
                f.close()
            elif isfile == True:
                f = open("./datasets/initial_dataset.csv", "a")
                f.write("%s,%s,%s,%s,%s \r" % (sAddition, sSubtraction, sMultiplication, sDivision, userID))
                f.close()

            p = Nums(num1 = num1, num2 = num2, addition = addition, subtraction = subtraction, multiplication = multiplication, division = division, userID = userID, numString = numString, resString = resString)
            p.save()

        args = {'form': form, 'num1': num1, 'num2': num2, 'addition': addition, 'subtraction': subtraction, 'multiplication': multiplication, 'division': division, 'userID': userID, 'numString': numString, 'resString': resString}
        return render(request, self.template_name, args)
