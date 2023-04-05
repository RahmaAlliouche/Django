from django.urls import path
from . import views
from .views import UserListView
from .views import getMeds
from .views import MedecineList



urlpatterns = [
    
    path('',views.responce),
    path('rap/',views.getrapp),
    path('med/',views.getMeds),
    
    path('pat/',views.getPat),
    path('log/',views.login),
    path('sin/',views.signin),
    path('up/',views.signUp),
    path('m/',views.menu),
    path('abs/',views.absence),
    path('pro/',views.profile),
    path('plan/',views.planning),
    path('set/',views.settings),
    path('U/',UserListView.as_view()),
    path('create/',views.createRapp),
    path('medecine',views.MedecineList.as_view()),
    path('login/',views. MyLoginView.as_view(),name='login'),
]
   
    
    

