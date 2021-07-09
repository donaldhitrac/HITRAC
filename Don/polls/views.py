from django.shortcuts import render



def index(request):
    return render(request, 'polls/index.html',)

def home(request):
    return render(request, 'polls/home.html')
