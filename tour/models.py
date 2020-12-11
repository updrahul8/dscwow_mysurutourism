from django.db import models
from .make_slug import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=250)
    category_discription = models.TextField()

    def __str__(self):
        return self.category_name
    
class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    place_description = models.TextField()
    place_img_1 = models.ImageField(upload_to = 'places', default = '') 
    place_img_2 = models.ImageField(upload_to = 'places', default = '') 
    place_img_3 = models.ImageField(upload_to = 'places', default = '')
    place_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True, blank=True, null=True, editable=False)
    place_location = models.CharField(max_length=500)

    def __str__(self):
        return self.name

def pre_save_receiver(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 

    pre_save.connect(pre_save_receiver, sender = Place) 

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    event_description = models.TextField()
    event_img_1 = models.ImageField(upload_to = 'events', default = '') 
    event_img_2 = models.ImageField(upload_to = 'events', default = '') 
    event_img_3 = models.ImageField(upload_to = 'events', default = '')
    event_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True, blank=True, null=True, editable=False)
    event_location = models.CharField(max_length=500)

    def __str__(self):
        return self.name

def pre_save_receiver_event(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 

    pre_save.connect(pre_save_receiver_event, sender = Event) 