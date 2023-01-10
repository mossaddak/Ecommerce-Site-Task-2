from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import CustomeUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


    

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True, error_messages={"unique":"The email must be unique!"})
    profile_image = models.ImageField(null = True,blank = True,upload_to = "0_Profile-Picture")
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    post_office = models.CharField(max_length=250, null=True, blank=True)
    thana = models.CharField(max_length=250, null=True, blank=True)
    district = models.CharField(max_length=250, null=True, blank=True)
    zipcode = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=264, null=True, blank=True)
    REQUIRES_FIELDS = ["email"]
    objects = CustomeUserManager()

    def __str__(self):
        return f"{self.pk}.{self.username}"    

    def get_profile_picture(self):
        url = ""
        try:
            url = self.profile_image.url
            
        except:
            url = ""
        return url

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='profileRelatedName')
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profileRelatedName.save()

