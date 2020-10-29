from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def accounts_home(request):
    return render(request, 'accounts/accounts_home.html')

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            #login
            user = form.get_user()
            login(request, user)

            return redirect('implementation:implementation_home')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def signup_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            #login
            login(request, user)

            return redirect('implementation:implementation_home')

    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):

    logout(request)

    return render(request, 'accounts/accounts_home.html')