from django.db import models

class Pitch(models.Model):
    entrepreneur = models.CharField(max_length=120)
    pitchTitle = models.CharField(max_length=120)
    pitchIdea = models.CharField(max_length=300)
    askAmount = models.FloatField()
    equity = models.FloatField()
    offers = models.ManyToManyField('CounterOffer', blank=True)
    def __str__(self):
        return str(self.id)

class CounterOffer(models.Model):
    investor = models.CharField(max_length=120)
    comment = models.CharField(max_length=300)
    amount = models.FloatField()
    equity = models.FloatField()
    def __str__(self):
        return str(self.id)