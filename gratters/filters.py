from django_filters import rest_framework as filters
from .models import *


class GratterFilter(filters.FilterSet):
    class Meta:
        model = Gratter
        fields = ('owner',)