from django.db import models
from django.utils.translation import gettext_lazy as _

class Home(models.Model):
    name=models.CharField(max_length=120,verbose_name=_('name'))
    logo=models.ImageField(upload_to='logo')
    subtitle=models.TextField(max_length=2000)
    call_us=models.CharField(max_length=120,null=True,blank=True)
    email_us=models.CharField(max_length=120,null=True,blank=True)
    phones=models.TextField(max_length=120,null=True,blank=True)
    android_apps=models.URLField(null=True,blank=True)
    ios_app=models.URLField(null=True,blank=True)
    facebook=models.URLField(null=True,blank=True)
    youtube=models.URLField(null=True,blank=True)
    address=models.TextField(max_length=500)


    def __str__(self):
        return self.name
    

class Delivery_Fee(models.Model):
        fee=models.IntegerField()

        def __str__(self):
            return str(self.fee)

