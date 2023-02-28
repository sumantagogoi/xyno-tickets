from .views import *
from django.urls import path


urlpatterns = [
    path('getAllEvents/', GetAllEvents.as_view()),
    
]



