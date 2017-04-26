from django.conf.urls import url,include
from . import views

urlpatterns = [   
    url(r'^$',view.index,name='index'),]
