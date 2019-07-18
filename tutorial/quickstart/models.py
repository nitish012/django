from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin   
# # Create your models here.


# class Userprofile(AbstractBaseUser,PermissionsMixin):
#     email=models.EmailField(max_length=255,unique=True)
#     name=models.CharField(max_length=255)
#     is_active=models.BooleanField(default=True)
#     is_staff=models.BooleanField(default=False)

#     objects=UserProfileManager()
    
class Reporter(models.Model):
    first_name=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
