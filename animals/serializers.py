from rest_framework import serializers
from .models import Animal, Sex
from groups.models import Group
from traits.models import Trait
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer

import math

class AnimalSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices = Sex.choices, default = Sex.undefined)
    idade_humana = serializers.SerializerMethodField("age_in_human_year")

    def age_in_human_year(self, data: Animal):
        
        return math.ceil(16 * math.log(data.age, 3) + 31)

        
    group = GroupSerializer()
    traits = TraitSerializer(many = True)



    def create(self, data: dict):

        grupo = data.pop("group")
        traits = data.pop("traits")

        afiliacao,_ = Group.objects.get_or_create(**grupo)
        animals = Animal.objects.create(**data, group = afiliacao)
        
        for trait in traits:
            mania,_ = Trait.objects.get_or_create(**trait)
            animals.traits.add(mania) 

        return animals    

    def update(self, data: dict):

        grupo = data.pop("group")
        traits = data.pop("traits")

        animals = Animal.objects.create(**data, group = afiliacao)
        
        for trait in traits:
            mania,_ = Trait.objects.patch_or_update(**trait)
            animals.traits.add(mania) 

        return animals    

