from django.db import models


class Creature(models.Model):

    VARIATION_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    name = models.CharField(max_length=100)
    variation_type = models.CharField(
        choices=VARIATION_CHOICES, default='A', max_length=20)
    description = models.CharField(max_length=600)
    image_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name} - type: {self.variation_type}"


class MegaCreature(models.Model):
    creature = models.ForeignKey(
        Creature, on_delete=models.CASCADE, related_name='mega_creature')
    description = models.CharField(max_length=600)
    image_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.creature.name} - type {self.creature.variation_type}"
