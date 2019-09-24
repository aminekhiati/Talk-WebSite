from django.urls import path
from . import views

urlpatterns =[

    path('',views.home,name='home'),
    #path('',views.homeLogged,name='homelogged')
    path('login/',views.login_request,name ='login'),
    path('logout/',views.logout_request,name='logout'),
]