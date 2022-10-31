from django.shortcuts import render, redirect

# Create your views here.
from .forms import HistoryForm
from .models import CalcHistory


# articles = {
#     'sports': 'Sports Page',
#     'finance': 'Finance Page',
#     'politics': 'Politics Page'
# }
#
#
# def stinsert(request, ):
#     music = Musician.objects.all()
#     context = {
#         "music": music
#     }
#     return render(request, 'advertisement/Data_index.html', context)


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


def get_truth(symbol, a, b):
    oops = {'*': lambda a, b: a * b,
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '/': lambda a, b: a // b
            }
    return oops[symbol](a, b)

#
# def home_view(requset, *args, **kwargs):
#     return HttpResponse("Home Page")


def calculate(request):
    form = HistoryForm()
    if request.method == 'POST':

        result = get_truth(str(request.POST.get('operator')),
                           int(request.POST.get('val1')), int(request.POST.get('val2')))
        form = HistoryForm(request.POST, initial={'result': result})
        if form.is_valid():
            form.save()
            return redirect('calc')

    return render(request, template_name='advertisement/Ex1.html', context={'form': form})


def history_objects(request):
    storage = CalcHistory.objects.all()
    return render(request, "advertisement/obj.html", context={'storage': storage})
