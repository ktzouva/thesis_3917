from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ImplementationForm
from .models import ImplementationModel

class ImplementationView(TemplateView):

    template_name = 'implementation/implementation_home.html'

    def get(self, request):
        form = ImplementationForm()
        objects = ImplementationModel.objects.all()

        args = {'form': form, 'objects': objects}
        return render(request, self.template_name, args)

    def post(self, request):
        form = ImplementationForm(request.POST)
        if form.is_valid():
            form.save()
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']

            addition = num1 + num2
            subtraction = num1 - num2
            multiplication = num1 * num2
            division = num1 / num2

        args = {'form': form, 'num1': num1, 'num2': num2, 'addition': addition, 'subtraction': subtraction, 'multiplication': multiplication, 'division': division}
        return render(request, self.template_name, args)

def SavedValuesView(request):
    return render(request, './saved_values.html', {'implementation': saved_values})
