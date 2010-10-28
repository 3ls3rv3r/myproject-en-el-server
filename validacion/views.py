# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

def index(request):
    c = {}
    c.update(csrf(request))
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("Redirect to a success page",c)
        else:
            return HttpResponse("Return a 'disabled account' error message",c)

@login_required
def logueado(request):
  c = {}
  c.update(csrf(request))
  logout(request)	
  return HttpResponse("La tenes adentro",c)
