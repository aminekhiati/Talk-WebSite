from django.urls import path
from . import views

urlpatterns =[

    path('',views.home,name='home'),
    path('user/<int:pk>',views.homeLogged,name='homeLogged'),
    path('login/',views.login_request,name ='login'),
    path('logout/',views.logout_request,name='logout'),
    path('signup',views.signup,name='signup')
]