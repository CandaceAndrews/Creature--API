from rest_framework import serializers
from .models import Creature, MegaCreature


class MegaCreatureSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = MegaCreature
        fields = (
            'id',
            'name',
            'description',
            'image'
        )

    def get_name(self, obj):
        return f"Mega {obj.creature.name}"


class CreatureSerializer(serializers.ModelSerializer):
    mega_creature = MegaCreatureSerializer(many=True)

    class Meta:
        model = Creature
        fields = (
            'id',
            'name',
            'variation_type',
            'description',
            'image',
            'mega_creature'
        )
