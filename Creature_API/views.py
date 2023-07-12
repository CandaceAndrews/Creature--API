from django.shortcuts import render
from rest_framework import generics

from .models import Creature
from .serializers import CreatureSerializer


class CreatureListView(generics.ListAPIView):
    '''List all animals
    '''
    queryset = Creature.objects.all()
    serializer_class = CreatureSerializer
