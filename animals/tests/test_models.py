from django.test import TestCase
from animals.models import Animal
from groups.models import Group

class AnimalModelsTests(TestCase):

    @classmethod

    def setUpTestData(cls):     
        cls.animal = {"name": "Carlos", "age": 6, "weight": 23, "sex": "Macho"}
        cls.group = {"name": "Gato", "scientific_name": "cats familiaris"}
        trait_data = {"name": "peludo"}

        group1 = Group.objects.create(**cls.group)
        cls.animals = Animal.objects.create(**cls.animal, group = group1)

    def test_name_max_length(self):
        max_length = self.animals.meta.get_field('name').max_length
        self.assertEquals(max_length, 50)
    
