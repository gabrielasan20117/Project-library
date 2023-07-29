from django.db import models

# Create your models here.

class Gender(models.Model):
    name = models.CharField(max_length=250, null=False)
    created_date = models.DateTimeField()
    
class Editorial(models.Model):
    name = models.CharField(max_length=250, null=False)
    direction = models.CharField(max_length=100, null=False)
    created_date = models.DateTimeField()
    # created_by = models.ForeignKey()

class Authors(models.Model):
    name = models.CharField(max_length=250, null=False)
    birthday = models.DateTimeField()
    created_date = models.DateTimeField()
    
class Categories(models.Model):
    name = models.CharField(max_length=250, null=False)
    created_date = models.DateTimeField()
    

class Shelves(models.Model):
    name = models.CharField(max_length=250, null=False)
    created_date = models.DateTimeField()

class Books(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.ManyToManyField(Authors)
    anio = models.CharField(max_length=4)
    gender =  models.OneToOneField(Gender, on_delete=models.CASCADE)
    editorial =  models.OneToOneField(Editorial, on_delete=models.CASCADE)
    shelves =  models.OneToOneField(Shelves, on_delete=models.CASCADE)
    categorie =   models.OneToOneField(Categories, on_delete=models.CASCADE)
    