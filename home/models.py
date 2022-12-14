from django.db import models

# Create your models here.
class Event(models.Model):
    class EventType(models.TextChoices):
        Upcoming = 'UE'
        Past = 'PE'

    image = models.TextField(max_length=100)
    name = models.TextField(max_length=50)
    description =models.TextField(max_length=500)
    date = models.DateField()
    status = models.CharField(
        max_length=8,
        choices=EventType.choices,
        default=EventType.Past
    )


    def __str__(self):
        return self.name