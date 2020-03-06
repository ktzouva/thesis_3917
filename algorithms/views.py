from django.shortcuts import render
from .models import Algorithm

def algorithms_home(request):
    algorithms = Algorithm.objects.all().order_by('title')
    return render(request, 'algorithms/algorithms_home.html', {'algorithms': algorithms})

def algorithms_detail(request, slug):
    algorithm = Algorithm.objects.get(slug=slug) #Look for this algorithm in the DB and store it
    return render(request, 'algorithms/algorithms_detail.html', {'algorithm':algorithm})
