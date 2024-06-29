from django.urls import path
from . import views 

urlpatterns = [
    path('index',views.index,name="index"),
    path('login',views.index,name="login"),
    path('signup',views.index,name="signup")
]


