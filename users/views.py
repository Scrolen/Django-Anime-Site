from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from anime.models import WatchList


# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            newUser = User.objects.get(username = username)
            list = WatchList.objects.create(user = newUser)
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

 #this is a decorator, makes the user have to be logged in to use the view. different in class based views
def profile_view(request, username):
    user = User.objects.get(username=username)
    return render(request, 'users/profile.html',{'profile':user}) #PROFILE IS THE NAME OF THE USERS PROFILE YOU ARE VIEWING