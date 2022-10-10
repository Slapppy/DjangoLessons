from django.urls import path
from . import views

urlpatterns = [
    #path('<int:num_page>', views.num_page_view),
    #path('<str:topic>', views.news_view, name='topic-page'),
    ##path('<int:num1>/<int:num2>', views.add_view),
    path('', views.stinsert, name='list-events'),
    path('update/<int:id>', views.update, name='update'),
    path('update_form/<int:id>', views.update_form),


]
