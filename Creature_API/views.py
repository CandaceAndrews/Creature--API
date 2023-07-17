from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Creature, MegaCreature
from .serializers import CreatureSerializer, MegaCreatureSerializer


def gallery(request):
    return render(request, 'Creature_API/gallery.html')


def photo(request):
    return render(request, 'Creature_API/photo.html')


def add(request):
    return render(request, 'Creature_API/add.html')
