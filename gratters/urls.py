from django.urls import path
from .views import *

urlpatterns = [
    path('gratter/', GrattersView.as_view()),
    path('gratter/<int:pk>', SingleGratterView.as_view())
]