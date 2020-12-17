from django.shortcuts import render
from rest_framework import generics, status, parsers, renderers, mixins
from rest_framework.response import Response
from .serializers import *
from .filters import *
from gratters_backend.settings import REST_FRAMEWORK
# Create your views here.

class GratterView(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = GratterSerializer
    queryset = Gratter.objects.all()
    filter_class  = GratterFilter
    parser_classes = ( parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser)
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
