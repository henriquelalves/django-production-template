from django.shortcuts import render

def index(request):
    return render(request, "samplepage/index.html")
