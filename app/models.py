from django.db import models

# Create your models here.
class Productcatagory(models.Model):
    product_catagory_id=models.PositiveIntegerField()
    product_catagory_name=models.CharField(max_length=100)

    def __str__(self):
        return self.product_catagory_name
    
class Product(models.Model):
    product_catagory_name=models.ForeignKey(Productcatagory,on_delete=models.CASCADE)
    pname=models.CharField(max_length=100)
    pid=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField()

    def __str__(self):
        return self.pname