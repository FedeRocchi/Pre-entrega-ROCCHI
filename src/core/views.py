from django.shortcuts import render

def index(request):
    return render(request,'core/index.html')



def create_user(request):
    return render(request, 'core/registar_usuario.html', )
# Create your views here.
