from django.shortcuts import render
from rest_framework import generics, status, parsers, renderers, mixins
from rest_framework.response import Response
from .serializers import *
from .filters import *
from gratters_backend.telethon import *

# Create your views here.

class GratterView(generics.ListCreateAPIView):
    serializer_class = GratterSerializer
    queryset = Gratter.objects.all()
    filter_class  = GratterFilter
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser)
    renderer_classes = (renderers.JSONRenderer,)
    #
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     client = TelegramClient(phone, api_id, api_hash)
    #     client.connect()
    #     message = serializer.validated_data.get('message')
    #     person_to = serializer.validated_data.get('person_to')
    #     # client.send_message(person_to, message)
    #     client.disconnect()
    #     return self.create(request, *args, **kwargs)
