from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Creature
from .serializers import CreatureSerializer


class CreatureListView(generics.ListAPIView):
    '''List all animals
    '''
    queryset = Creature.objects.all()
    serializer_class = CreatureSerializer
