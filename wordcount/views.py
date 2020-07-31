from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def hola(request):
    return HttpResponse("Hola Amigo")

def about(request):
    return render(request, 'about.html')

def count(request):
    text = request.GET['fulltext']


    wordlist = text.split()

    worddict = {}

    for x in wordlist:
        if x in worddict:
            # increment
            worddict[x]+=1
        else:
            #add
            worddict[x]=1

    sortwords = sorted(worddict.items())

    return render(request, 'count.html',{'text': text, 'words': len(wordlist),'worddict':worddict,'sortwords':sortwords})