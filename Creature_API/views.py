from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Creature, MegaCreature
from .serializers import CreatureSerializer, MegaCreatureSerializer


# class CreatureListView(generics.ListAPIView):
#     '''List all creatures
#     '''
#     queryset = Creature.objects.all()
#     serializer_class = CreatureSerializer

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return render(request, 'creature.html', {'creatures': serializer.data})

def CreatureListView(request):
    creatures = Creature.objects.all()
    return render(request, 'creature.html', {'creatures': creatures})
