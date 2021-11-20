from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ImplementationForm
from .models import Nums
import os.path

class ImplementationView(TemplateView):
    template_name = 'implementation/implementation_home.html'

    def get(self, request):
        if request.user.is_authenticated:
            form = ImplementationForm()
            objects = Nums.objects.all()
            args = {'form': form, 'objects': objects}

            return render(request, self.template_name, args)
        else:
            return render(request, 'implementation/implementation_failed.html')

    def post(self, request):
        if request.user.is_authenticated:
            form = ImplementationForm(request.POST)

            if form.is_valid():
                num1 = form.cleaned_data['num1']
                num2 = form.cleaned_data['num2']

                userID = request.user.username

                addition = num1 + num2
                subtraction = num1 - num2
                multiplication = num1 * num2
                division = num1 / num2

                addition = round(addition, 3)
                subtraction = round(subtraction, 3)
                multiplication = round(multiplication, 3)
                division = round(division, 3)

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
                resString += ','

                if (addition%2) == 0:
                   resString += 'Even'
                else:
                   resString += 'Odd'

                resString += '\r'

                isfile = os.path.isfile('./dataset.csv')

                if isfile == False:
                    f = open("./dataset.csv", "w")
                    f.write(resString)
                    f.close()
                elif isfile == True:
                    f = open("./dataset.csv", "a")
                    f.write(resString)
                    f.close()

                p = Nums(num1 = num1, num2 = num2, addition = addition, subtraction = subtraction, multiplication = multiplication, division = division, userID = userID)
                p.save()

            args = {'form': form, 'num1': num1, 'num2': num2, 'addition': addition, 'subtraction': subtraction, 'multiplication': multiplication, 'division': division, 'userID': userID, 'resString': resString}
            return render(request, self.template_name, args)
        else:
            return render(request, 'implementation/implementation_failed.html')
