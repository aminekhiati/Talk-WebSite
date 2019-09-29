from django.urls import path
from . import views

urlpatterns =[

    path('',views.home,name=''),
    path('home',views.homeLogged,name='home'),
    path('login/',views.login_request,name ='login'),
    path('logout/',views.logout_request,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('profile/<int:pk>',views.profile,name='profile')
]