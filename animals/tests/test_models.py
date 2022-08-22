from django.test import TestCase
from animals.models import Animal
from groups.models import Group
from traits.models import Trait

class AnimalModelsTests(TestCase):

    @classmethod

    def setUpTestData(cls):     
        cls.animal = {"name": "Carlos", "age": 6, "weight": 23, "sex": "Macho"}
        cls.group = {"name": "Gato", "scientific_name": "cats familiaris"}
        cls.trait1_data = {"name": "peludo"}
        cls.trait2_data = {"name": "médio porte"}

        cls.t1 = Trait.objects.create(**cls.trait1_data)
        cls.t2 = Trait.objects.create(**cls.trait2_data)
        cls.group1 = Group.objects.create(**cls.group)
        cls.animals = Animal.objects.create(**cls.animal, group = cls.group1)
        cls.animals.traits.add(cls.t1)
        cls.animals.traits.add(cls.t2)

    def test_name_field(self):
        self.assertEqual(self.animals.name, self.animal["name"])
    
    def test_sex_field(self):
        self.assertEqual(self.animals.sex, self.animal["sex"])

    def tests_weight_field(self):
        self.assertEqual(self.animals.weight, self.animal["weight"])

    def test_age_field(self):
        self.assertEqual(self.animals.age, self.animal["age"])

    def test_name_max_length(self):
        max_length = self.animals._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)
    
    def test_group_name_max_length(self):
        max_length = self.group1._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_group_scientific_name_max_length(self):
        max_length = self.group1._meta.get_field('scientific_name').max_length
        self.assertEquals(max_length, 50)    

    def test_trait_name_max_length(self):
        max_length = self.t1._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)
        max_length = self.t2._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_sex_max_length(self):
        max_length = self.animals._meta.get_field('sex').max_length
        self.assertEquals(max_length, 15)
    
    def test_group_name(self):
        self.assertEquals(self.group1.name, self.group["name"])
    
    def setUpTestData(cls):
        cls.animal1 = [Animal.objects.create(cache=500000) for _ in range(20)] 
        cls.groups = Group.objects.create({"name": "Gato", "scientific_name": "cats familiaris"})
    
    def test_groups_may_contain_multiple_animals(self):

    #     for film in self.films:
    #         film.company = self.production_company # (4)
    #         film.save()

    #     self.assertEquals(
    #             len(self.films), 
    #             self.production_company.films.count()
    #         ) #(5)

    #     for film in self.films:
    #         self.assertIs(film.company, self.production_company) # (6)