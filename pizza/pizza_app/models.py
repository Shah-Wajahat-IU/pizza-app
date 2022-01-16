from django.db import models





# Create your models here.
class CustomerModel(models.Model):
    userid=models.CharField( max_length=10)
    phoneno= models.CharField( max_length=15)

    

class PizzaModel(models.Model):
    name=models.CharField( max_length=50)
    price=models.CharField(max_length=50)

    def __str__(self):
        return self.name