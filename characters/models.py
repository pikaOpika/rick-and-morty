from django.db import models


class Character(models.Model):
    class StatusChoices(models.TextChoices):
        ALIVE = 'Alive'
        DEAD = 'dead',
        UNKNOWN = 'unknown' 

    class GenderChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        GENDERLESS = 'G', 'Genderless'
        UNKNOWN = 'U', 'Unknown' 

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=StatusChoices)
    species = models.CharField(max_length=100)
    gender = models.CharField(max_length=55, choices=GenderChoices)
    image = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.name
