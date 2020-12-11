from django.db import models
from .make_slug import unique_slug_generator
from django.db.models.signals import pre_save
from tour.models import Category

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=250)
    post_content = models.TextField()
    post_img = models.ImageField(upload_to = 'blogs', default = '')
    post_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True, blank=True, null=True, editable=False)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.post_title

def pre_save_receiver_post(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance)
pre_save.connect(pre_save_receiver_post, sender = Post)              