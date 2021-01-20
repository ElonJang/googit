from django.shortcuts import render
from .models import Cafe
# Create your views here.


def index(request):
    cafelist = Cafe.objects.all()
    return render(request, 'main/index.html', {'cafelist':cafelist})
