from django.db import models

class Sex(models.TextChoices):
    male = "Macho"
    female = "Fêmea"
    undefined = "Não informado."

class Animal(models.Model):

    group = models.ForeignKey(
        "groups.Group", on_delete= models.CASCADE, related_name= "group"
    )

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15, choices= Sex.choices, default = Sex.undefined)

    traits = models.ManyToManyField(
        "traits.Trait", related_name= "trait"
    )

    def __str__(self):
        return f'{self.name}, seu animal tem {self.age} anos humanos'