from django.db import models
class Datatable(models.Model):
    #Product name,Brand_name,Productid,Price Rupees,URL,Prodcut info
    product_name=models.CharField(max_length=300)
    brand_name=models.CharField(max_length=300,blank=True)
    product_id=models.IntegerField()
    price=models.FloatField()
    url=models.URLField()
    product_info=models.CharField(max_length=1000,blank=True)
    


