from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Creature, MegaCreature
from .serializers import CreatureSerializer, MegaCreatureSerializer


class CreatureListView(generics.ListAPIView):
    '''List all creatures
    '''
    queryset = Creature.objects.all()
    serializer_class = CreatureSerializer
