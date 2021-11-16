from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE

# Create your models here.

STATE_CHOICES = (

('Dhaka', 'Dhaka'),
('Rajshahi', 'Rajshahi' ),
('Chittagong', 'Chittagong'),
('Cumilla', 'Cumilla'),

)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField( max_length=200)
    city = models.CharField( max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (

        ('M', 'Mobile'),
        ('L', 'Laptop'),
        ('TW', 'TOP Wear'),
        ('BW', 'Bottom Wear'),

    )

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField( choices= CATEGORY_CHOICES, max_length= 5)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return  self.quantity * self.product.discounted_price
        # @property details 5:50:0

STATUS_CHOICES = (

('Accepted', 'Accepted'),
('Packed', 'Packed'),
('On The Way', 'On The Way'),
('Delivered', 'Delivered'),
('Cancle', 'Cancle'),

)



class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default= 'Pending')
    @property
    def total_cost(self):
        return  self.quantity * self.product.discounted_price


        