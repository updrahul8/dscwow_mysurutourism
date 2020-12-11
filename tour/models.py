from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=250)
    category_discription = models.TextField()

    def __str__(self):
        return self.category_name
    
class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=250)
    place_description = models.TextField()
    place_img_1 = models.ImageField(upload_to = 'places', default = '') 
    place_img_2 = models.ImageField(upload_to = 'places', default = '') 
    place_img_3 = models.ImageField(upload_to = 'places', default = '')
    place_location = models.CharField(max_length=500)

    def __str__(self):
        return self.place_name