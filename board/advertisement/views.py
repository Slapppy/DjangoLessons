from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from django.db import connection
from django.contrib import messages
import operator
# Create your views here.
from .forms import HistoryForm
from .models import Musician, CalcHistory

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


# def update(request, id):
#     music = Musician.objects.get(pk=id)
#     context = {
#         "music": music
#     }
#     return render(request, 'advertisement/update.html', context)


# def update_form(request, id):
#     music = Musician.objects.get(pk=id)
#     form = UpdateForm(request.POST, instance=music)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'Record success')
#     return render(request, 'advertisement/update.html', {"music": music})


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


def get_truth(inp, relate, cut):
    ops = {'*': operator.mul,
           '/': operator.truediv,
           '+': operator.concat,
           '-': operator.sub, }

    return ops[relate](inp, cut)


def home_view(requset, *args, **kwargs):
    return HttpResponse("Home Page")


def calculate(request):
    form = HistoryForm()
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            result = get_truth(int(request.POST['val1']), request.POST['operator'], int(request.POST['val2']))
            form = HistoryForm(request.POST, initial={'result':result})
            form.save()
            return HttpResponse(request.POST['val1'])
    return render(request, template_name='advertisement/Ex1.html', context={'form': form})
