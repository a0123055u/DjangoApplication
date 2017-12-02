from django.conf.urls import url
from . import views
from webapp.views import save,singin,SignUp,HomePage,ReLogIn,checkOut,popOut

urlpatterns=[
url(r'^$',views.index, name='index'),
url(r'^testpost',save, name='save'),
url(r'^signin',singin,name='signin'),
url(r'^signup',SignUp.as_view(), name='signup'),
url(r'^home',HomePage.as_view(), name='home'),
url(r'^relogin',ReLogIn.as_view(), name='relogin'),
url(r'^checkout',checkOut,name='checkOut'),
url(r'^popUp',popOut.as_view(),name='popUp'),
# url(r'^popup',popOut.as_view(),name='popup'),

]

