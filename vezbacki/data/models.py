from django.db import models





class Trainer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    picture = models.FileField(upload_to='users_pic', null=True, blank=True)
    email = models.CharField(max_length=1000)
    Phone = models.CharField(max_length=50)
    about = models.CharField(max_length=2048) 
    CreditCard = models.CharField(max_length=255)
    short_massage = models.CharField(max_length=128,null=True, blank=True)
    def __str__(self):
        return self.first_name



class News(models.Model):
    hedline = models.CharField(max_length=255)
    text = models.TextField() 
    picture = models.FileField(upload_to='news_pic', null=True, blank=True)
    def __str__(self):
        return self.hedline


class TrainingLocation(models.Model):
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)