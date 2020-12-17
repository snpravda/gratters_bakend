from rest_framework import serializers
from .models import *


class GratterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gratter
        fields = "__all__"