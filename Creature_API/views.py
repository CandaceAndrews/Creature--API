from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Creature, MegaCreature, Category
from .serializers import CreatureSerializer, MegaCreatureSerializer


def gallery(request):
    return render(request, 'Creature_API/gallery.html')


def viewCreature(request, pk):
    return render(request, 'Creature_API/creature.html')


def addCreature(request):
    return render(request, 'Creature_API/addCreature.html')
