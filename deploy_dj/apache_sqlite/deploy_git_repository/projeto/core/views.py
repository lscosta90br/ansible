from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    context= {'home_page': 'active'}
    return render(request, 'index.html', context)
