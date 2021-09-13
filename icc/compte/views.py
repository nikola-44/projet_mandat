from django.shortcuts import render

def inscriptionPage(request):
    context={}
    return render(request,'inscription.html', context)
# Create your views here.
