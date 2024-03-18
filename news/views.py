from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request.user.is_authenticated)
    return render(request, "news/index.html", {})
