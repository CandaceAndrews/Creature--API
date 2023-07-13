from rest_framework import serializers
from .models import Creature, MegaCreature


class MegaCreatureSerializer(serializers.ModelSerializer):
    mega_name = serializers.CharField(source='creature.name')

    class Meta:
        model = MegaCreature
        fields = (
            'id',
            'mega_name',
            'description',
            'image_url'
        )


class CreatureSerializer(serializers.ModelSerializer):
    mega_creature = MegaCreatureSerializer(many=True)

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
