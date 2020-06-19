from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request,'home.html',)

def password(request):
    
    characters = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!£$~@#()&%$'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    length = int(request.GET.get('length',12)) #here use request.GEt.get('') to gather information provide by user and inside the string place the value from template like length 
    dani = ''

    for x in range(length):
        dani +=random.choice(characters)
    return render(request,'password.html',{'password': dani})

def about(request):
    return render(request, 'about.html')