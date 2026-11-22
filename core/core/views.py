from django.shortcuts import render

def home(req):

    src = {
        'title' : "Home",
        'css' : "home",
    }
    return render(req,"home.html",src)