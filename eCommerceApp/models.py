from django.db import models
from userProfileApp.models import User
from django.db.models import Avg, Count

# product image function
def upload_product_image(instance, filename):
    return "uploads/{user}/{filename}".format(user=instance.user, filename=filename)

class ProductCategory(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return f"{self.pk}.{self.title}"

# Create your models here.
class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="productsRelatedName", blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="ProductsCategoryRelatedName", blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(blank=True, null=True, max_length=50)
    image = models.ImageField(upload_to="0_uploads/product_image", null=True, blank=True)


    #average rating
    def AverageRating(self):
        reviews = ProductFeedback.objects.filter(product=self).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    #count total feedback
    def countReview(self):
        reviews = ProductFeedback.objects.filter(product=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count



    def __str__(self):
        return f"{self.pk}.{self.title}({self.user})"

class Banner(models.Model):
    image = models.ImageField(upload_to="0_uploads/banner_image", blank=True, null=True)
    def __str__(self):
        return f"{self.pk}.{self.image}"


# product order
class ProductOrder(models.Model):
    user = models.ForeignKey(User, related_name="ProductOrderUserRelatedName", on_delete=models.CASCADE)
    Title = models.CharField(max_length=250, null=True, blank=True)
    Product = models.ForeignKey(Products, related_name="ProductOrderProductRelatedName", on_delete=models.CASCADE, blank=True, null=True)
    Image = models.ImageField(blank=True, null=True, upload_to="0_uploads/order_product_image")
    Price = models.CharField(blank=True, null=True, max_length=250)
    TotalPrice = models.CharField(max_length=250, blank=True, null=True)
    CustomerName = models.CharField(max_length=250, blank=True, null=True)
    Email = models.EmailField(blank=True, null=True)
    Quantity = models.CharField(max_length=250, blank=True, null=True)
    PostOffice = models.CharField(max_length=250, blank=True, null=True)
    Thana = models.CharField(max_length=250, blank=True, null=True)
    District = models.CharField(max_length=250, null=True, blank=True)
    Zipcode = models.CharField(max_length=250, blank=True, null=True)
    createdDate = models.DateField(auto_now=True)

    ORDER_STATUS_CHOICES = [
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('On the way', 'On the way'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled')
        
    ]
    OrderStatus = models.CharField(max_length=30, choices=ORDER_STATUS_CHOICES, blank=True, null=True)


    def __str__(self):
        return f"{self.pk}.{self.Product.title}({self.user})"

class ProductFeedback(models.Model):
    user = models.ForeignKey(User, related_name="ProductFeedbackUserRelatedName", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name="ProducTFeedbackProductRelatedName", on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)
    feedBACK = models.TextField(blank=True, null=True)
    createdDate = models.DateField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'product'),
                name='add_to_cart_once'
            ) 
        ]

    def __str__(self):
        return f"{self.pk}.{self.rating}."


class ShopingCart(models.Model):
    User = models.ForeignKey(User, related_name='UserShoppingCartRelatedName',on_delete=models.CASCADE)
    Product = models.ForeignKey(Products, related_name='ShoppingCartRelatedName',on_delete=models.CASCADE)
    createdDate = models.DateField(auto_now=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('User', 'Product'),
                name='review_once'
            )   
        ]

    def __str__(self):
        return f'{self.pk}.{self.User}({self.Product})'







