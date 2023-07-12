from rest_framework import serializers
from .models import Creature


class CreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creature
        fields = (
            'id',
            'name',
            'variation_type',
            'description',
            'image_url'
        )
