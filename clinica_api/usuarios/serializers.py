from rest_framework import serializers
from .models import Animal, Tutor


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['nome',
                  'raça',
                  'cor',
                  'data_nascimento',
                  'tutor']
        