from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'homepage.html')

def count(request):
    text=request.GET['ta']
    words=text.split()
    worddictionary={}
    for w in words:
        if w in worddictionary:
            worddictionary[w]+=1
        else:
            worddictionary[w]=1

    return render(request,'count.html',{'t':text,'w':len(words),'wd':worddictionary})
def about(request):
    return render(request,'about.html')
