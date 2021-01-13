from django.db import models

# Create your models here.

class Zaklady(models.Model):
    nazwa = models.CharField(max_length=30,default='',blank=False)
    def __str__(self):
        return self.nazwa
    
class Rodzaje(models.Model):
    nazwa = models.CharField(max_length=30,default='',blank=False,unique=True)
    zaklady = models.ForeignKey(Zaklady,related_name='rodzaje_zaklady',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nazwa
    
class Produkty(models.Model):
    nazwa = models.CharField(max_length=30,default='',blank=False)
    rodzaje = models.ForeignKey(Rodzaje,related_name='produkty_rodzaj', on_delete=models.CASCADE)
    poziom = models.IntegerField(blank=False,default=0)
    idr = models.IntegerField(blank=False,default=0)
    
    def __str__(self):
        return self.nazwa
    
class Surowce(models.Model):
    nazwa = models.CharField(max_length=30,default='',blank=False)
    rodzaje = models.ForeignKey(Rodzaje,related_name='surowce_rodzaj', on_delete=models.CASCADE)
    ilosc = models.IntegerField(blank=False,default=0)
    
    def __str__(self):
        return self.nazwa
    
class Narzedzia(models.Model):
    nazwa = models.CharField(max_length = 30,default='',blank=False)
    rodzaje = models.ForeignKey(Rodzaje,related_name='narzedzia_rodzaj', on_delete=models.CASCADE)
    aktywnosc = models.IntegerField(blank=False,default=0)
    
    def __str__(self):
        return self.nazwa
    