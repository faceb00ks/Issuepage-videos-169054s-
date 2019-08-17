from django.db import models
from django.db.models.fields.related import ForeignKey

class Fle(models.Model):
    mainn = models.CharField(max_length=100)
    
    def __str__(self):
        return "%s" % (self.mainn)
    
    
    
class fled(models.Model):
    q = ForeignKey(Fle,on_delete= models.CASCADE)
     
    me = models.CharField(max_length=30)
    
    pw = models.CharField(max_length=30)