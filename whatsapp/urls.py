from django.urls import path 
from.import views


urlpatterns=[
    path('whatsapp/',views.home_view,name='whatsapp')
]