# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("Redirect to a success page")
        else:
            return HttpResponse("Return a 'disabled account' error message")

@login_required
def logueado(request):
	logout(request)	
	return HttpResponse("La tenes adentro")
