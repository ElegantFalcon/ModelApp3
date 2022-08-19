from django.urls import path
from app5 import views


urlpatterns = [
    path('index', views.index, name = 'index') , 
    path('first_api/' , views.firstApi , name ="first_api"),
    path('user_det' , views.u_det , name = 'user_details' ),
    path('signup1' , views.signup , name = 'signup1'),
    path('login1' , views.login , name = 'login1'),
    path('message1' , views.redirect1 , name = 'message1'),
    path('message2' , views.redirect2 , name = 'message2'),

]