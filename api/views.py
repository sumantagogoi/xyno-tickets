from django.shortcuts import render
from .serializers import *
from ticketing.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
class GetAllEvents(APIView):
    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        serializers = EventSerializer(events, many=True, context={'request':request})
        return Response(serializers.data,status = status.HTTP_200_OK)