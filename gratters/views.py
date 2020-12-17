from django.shortcuts import render
from rest_framework import generics, status, parsers, renderers
from rest_framework.response import Response
from .serializers import *
from .filters import *
from gratters_backend.settings import REST_FRAMEWORK
# Create your views here.

class GratterView(generics.ListCreateAPIView):
    serializer_class = GratterSerializer
    queryset = Gratter.objects.all()
    filter_class  = GratterFilter
    parser_classes = ( parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser)
    renderer_classes = (renderers.JSONRenderer,)