from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
# class List(ListView):
#     template_name = 'blogApp/index.html'

def List(request):
    return render(request, 'blogApp/index.html')