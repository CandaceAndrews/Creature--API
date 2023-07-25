from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Creature, MegaCreature, Category
from .serializers import CreatureSerializer, MegaCreatureSerializer


def gallery(request):
    categories = Category.objects.all()
    creatures = Creature.objects.all()
    context = {'categories': categories, 'creatures': creatures}
    return render(request, 'Creature_API/gallery.html', context)


def viewCreature(request, pk):
    creature = Creature.objects.get(id=pk)
    return render(request, 'Creature_API/creature.html', {'creature': creature})


def addCreature(request):
    return render(request, 'Creature_API/addCreature.html')
