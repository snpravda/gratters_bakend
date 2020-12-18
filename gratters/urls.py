from django.urls import path
from .views import *

urlpatterns = [
    path('', GrattersView.as_view()),
    path('<int:pk>/', SingleGratterView.as_view())
]