from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Medecine(models.Model):
    id_med=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    image=models.ImageField(upload_to='photo')
    
    email=models.CharField(max_length=50)
    adress=models.CharField(max_length=50)
    password=models.CharField(max_length=8)
    num_téle=models.IntegerField
    num_equipe=models.IntegerField
    spécialité=models.CharField(max_length=50)

    def __str__(self):
        return self.password
    def __get__(self):
        return self.name



class Infermier(models.Model):
    id_infer=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=25)
    prenom=models.CharField(max_length=25)
    image=models.ImageField(upload_to='photo')
    
    email=models.CharField(max_length=50)
    adress=models.CharField(max_length=25)
    password=models.CharField(max_length=8)
    num_téle=models.IntegerField

   

class Patient(models.Model):
    num_pat=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    adress=models.CharField(max_length=50)
    password=models.CharField(max_length=8)
     

class Rapport(models.Model):
    num_rap=models.IntegerField(primary_key=True)
    text=models.TextField(max_length=500)
    id_med=models.ForeignKey(Medecine,on_delete=models.CASCADE)
    id_infer=models.ForeignKey(Infermier,on_delete=models.CASCADE)
    num_pat=models.ForeignKey(Patient,on_delete=models.CASCADE)

class Dossier_medecale(models.Model):
    id_dossier_médical=models.IntegerField(primary_key=True)
    
    num_pat=models.ForeignKey(Patient,on_delete=models.CASCADE)
    id_med=models.ForeignKey(Medecine,on_delete=models.CASCADE)
    num_rap=models.ForeignKey(Rapport,on_delete=models.CASCADE) 

class Planing(models.Model):
    id_plan=models.IntegerField(primary_key=True)
    ref=models.ImageField(upload_to='photo')
    
    
    id_med=models.ForeignKey(Medecine,on_delete=models.CASCADE)
    id_infer=models.ForeignKey(Infermier,on_delete=models.CASCADE)
    

class Abcense(models.Model):
    num_abs=models.IntegerField(primary_key=True)
    date_debu=models.DateField
    date_fine=models.DateField
    raison=models.CharField(max_length=500)
    id_med=models.ForeignKey(Medecine,on_delete=models.CASCADE)
    id_infer=models.ForeignKey(Infermier,on_delete=models.CASCADE)
