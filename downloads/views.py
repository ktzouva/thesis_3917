from django.shortcuts import render

def downloads_home(request):
    return render(request, 'downloads/downloads_home.html', {'downloads': downloads_home})
