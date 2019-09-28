from django.urls import path
from . import views

urlpatterns =[

    path('',views.home,name='home'),
    path('user/',views.homeLogged,name='homeLogged'),
    path('login/',views.login_request,name ='login'),
    path('logout/',views.logout_request,name='logout'),
    path('signUp',views.signUp,name='signUp')
]