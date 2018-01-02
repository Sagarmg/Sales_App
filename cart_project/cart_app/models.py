from django.db import models

# Create your models here.

CUSTOMER_STATUS = (
                  (0,"Active"),
                  (1,"InActive")
		)
CART_STATUS = (
	      (0,"Initiated"),
	      (1,"Completed")
	     )

class Customer(models.Model):
    name 		= models.CharField(max_length=50)
    code 		= models.CharField(max_length=10, unique=True)
    address 		= models.CharField(max_length=100)
    city		= models.CharField(max_length=50,null=True,blank=True)  
    zipcode 		= models.CharField(max_length=10,null=True,blank=True)
    status		= models.IntegerField(choices=CUSTOMER_STATUS, default=0)
    added_on		= models.DateTimeField(auto_now_add=True)
    updated_on		= models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return self.name


class SKU(models.Model):
    ean_code		= models.CharField(max_length=13, unique=True)
    description		= models.CharField(max_length=50,null=True,blank=True)
    brand               = models.CharField(max_length=100,  blank=True, null=True)
    category            = models.CharField(max_length=100,  blank=True, null=True)
    colour              = models.CharField(max_length=100,  blank=True, null=True)
    size                = models.CharField(max_length=100,  blank=True, null=True)
    mrp                 = models.CharField(max_length=100,  default=0)
    length              = models.FloatField(default=0)
    width               = models.FloatField(default=0)
    weight              = models.FloatField(default=0)
    added_on            = models.DateTimeField(auto_now_add=True)
    updated_on          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ean_code


class CartDetail(models.Model):
    customer		= models.ForeignKey(Customer)
    sku			= models.ManyToManyField(SKU)
    order_number = models.CharField(max_length=100, blank=True, null=True)
    status		= models.IntegerField(choices=CART_STATUS, default=0)
    added_on            = models.DateTimeField(auto_now_add=True)
    updated_on          = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.customer.name




    
