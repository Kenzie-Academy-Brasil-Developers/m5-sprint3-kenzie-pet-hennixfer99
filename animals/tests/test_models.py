from django.test import TestCase
from animals.models import Animal

class AnimalModelsTests(TestCase):

    @classmethod

    def setUpTestData(cls):     
        cls.name = "Chris"
        cls.age = 7
        cls.weight = 2.3
        cls.sex = ""
        cls.group = {"name": "cão", "scientific_name": "canis familiaris"}

        cls.animal = Animal.objects.create(name = cls.name, age = cls.age, weight = cls.weight, sex = cls.sex, group = cls.group)

    def test_name_max_length(self):
        animal = Animal.objects.get(id=1)
        max_length = animal._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)
