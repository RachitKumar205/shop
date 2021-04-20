from django.shortcuts import render
from .models import Members
from django.contrib.auth.forms import UserCreationForm
import django.contrib.messages

# Create your views here.

def index(request):
    return render(request, "modelshop/index.html", {
        "members": Members.objects.all()
    })

def register(request):

    if request.user.is_authenticated:
        return render(request, "modelshop/register.html")

    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()

    else:
        f = UserCreationForm()

    return render(request, 'modelshop/register.html', {'form': f})