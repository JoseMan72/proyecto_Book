from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Book(models.Model):
   title = models.CharField(max_length=50)
   author = models.CharField(max_length=50)
   # maximo hasta el 5 en rating
   rating = models.IntegerField(validators=[MaxValueValidator(5)])
   sinopsis = models.TextField()

   created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True: Cuando se crea el registro, se guarda la fecha y hora
   updated_at = models.DateTimeField(auto_now=True) # auto_now=True: Cuando se actualiza el registro, se guarda la fecha y hora

   def __str__(self):
      return self.title