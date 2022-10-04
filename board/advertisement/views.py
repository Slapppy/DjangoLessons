from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def advertisement_list(requset, *args, **kwargs):
    return render(requset, 'advertisement/advertisement_list.html', {})


def advertisement_list2(requset, *args, **kwargs):
    return render(requset, 'advertisement/advertisement_list2.html', {})
