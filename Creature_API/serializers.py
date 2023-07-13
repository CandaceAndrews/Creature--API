from rest_framework import serializers
from .models import Creature, MegaCreature


class MegaCreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MegaCreature
        fields = (
            'creature',
            'description',
            'image_url'
        )


class CreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creature
        fields = (
            'id',
            'name',
            'variation_type',
            'description',
            'image_url',
            'mega_creature'
        )
