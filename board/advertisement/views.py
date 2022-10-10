from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from django.db import connection
from django.contrib import messages
# Create your views here.
from .forms import UpdateForm
from .models import Musician

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}


def stinsert(request, ):
    music = Musician.objects.all()
    context = {
        "music": music
    }
    return render(request, 'advertisement/Data_index.html', context)


def update(request, id):
    music = Musician.objects.get(pk=id)
    context = {
        "music": music
    }
    return render(request, 'advertisement/update.html', context)


def update_form(request, id):
    music = Musician.objects.get(pk=id)
    form = UpdateForm(request.POST, instance=music)
    if form.is_valid():
        form.save()
        messages.success(request,'Record success')
    return render(request, 'advertisement/update.html', {"music": music})


def news_view(requset, topic, *args, **kwargs):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = '<h1>No page found<h1>'
        raise Http404('404 Generic Error')


def num_page_view(request, num_page):
    topic_list = list(articles.keys())
    topic = topic_list[num_page]
    wegpage = reverse('topic-page', args=[topic])
    return HttpResponseRedirect(wegpage)


def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f'{num1}+{num2} = {add_result}'
    return HttpResponse(str(result))


def home_view(requset, *args, **kwargs):
    return HttpResponse("Home Page")
