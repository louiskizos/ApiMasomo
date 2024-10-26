from django.db import models

# Create your models here.

from django.db import models

class Etablissements(models.Model):
    image = models.ImageField(upload_to='images/')
    designationEcole = models.TextField()
    arreteMin = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    typesEcole = models.CharField(max_length=100)  # PRIVEE ou PUBLIQUE
    degree = models.CharField(max_length=100)  # PRIMAIRE ou SECONDAIRE
    biographie = models.TextField()
    
    def __str__(self):
        return self.biographie



class Test(models.Model):
    
    typesEcole = models.CharField(max_length=100)  # PRIVEE ou PUBLIQUE
    degree = models.CharField(max_length=100)  # PRIMAIRE ou SECONDAIRE
    
    
    def __str__(self):
        return self.typesEcole
