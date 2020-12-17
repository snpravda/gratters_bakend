from django.urls import path
from .views import *

urlpatterns = [
    path('gratter/', GratterView.as_view())
]