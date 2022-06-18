
from django.shortcuts import redirect, render






def Home(request):
    
    return render(request, 'home.html')