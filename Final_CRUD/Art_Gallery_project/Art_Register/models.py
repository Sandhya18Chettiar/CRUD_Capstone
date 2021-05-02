from django.db import models

# Create your models here.
class ArtInformation(models.Model):
    
    Art_Id = models.IntegerField(primary_key=True)
    Art_Title = models.CharField(max_length=1000)
    Description = models.TextField()
    Artist = models.CharField(max_length=1000)
    Completion_Date =  models.DateTimeField(default=False) 
    Category = models.CharField(max_length=1000)
    
    t1 = models.BooleanField(default=False) 
    t2 = models.BooleanField(default=False)
    t3 = models.BooleanField(default=False)
    t4 = models.BooleanField(default=False)
    t5 = models.BooleanField(default=False)
    t6 = models.BooleanField(default=False)
    t7 = models.BooleanField(default=False)
    t8 = models.BooleanField(default=False)
 
    Art_Price = models.IntegerField()
    pic = models.ImageField(null=True, blank=True, upload_to='Images/')