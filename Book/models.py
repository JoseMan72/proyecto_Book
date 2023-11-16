from django.db import models

# Create your models here.
class Book(models.Model):
   title = models.CharField(max_length=50)
   author = models.CharField(max_length=50)
   rating = models.IntegerField()
   sinopsis = models.TextField()

   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.title