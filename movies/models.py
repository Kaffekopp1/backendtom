from django.db import models

# Create your models here.
class Movies(models.Model):
    movie = models.CharField(max_length=10)
    betyg = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.movie +" "+ str(self.betyg)
