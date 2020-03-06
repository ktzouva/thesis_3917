from django.shortcuts import render
from implementation.models import Nums
from implementation.views import ImplementationView

def savedValues_home(request):
    objects = Nums.objects.all()
    args = {'objects': objects}
    return render(request, 'savedValues/savedValues_home.html', args)
