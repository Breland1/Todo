from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        