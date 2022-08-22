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
        max_length = self.animals.objects.get('name').max_length
        self.assertEquals(max_length, 50)
    
    def test_sex_max_length(self):
        max_length = self.animals.objects.get('sex').max_length
        self.assertEquals(max_length, 15)
    
    def test_age_is_integer(self):
        is_integer = self.animals.objects.get('age').integer
        self.assertEquals(self.animal.age, is_integer)

    def test_group_name(self):
        group_name = self.animals.objects.get('group').integer
        self.assertEquals(self.group1.name, group_name)

