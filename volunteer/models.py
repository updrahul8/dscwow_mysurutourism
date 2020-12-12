from django.db import models
from tour.models import Place

# Create your models here.
class Volenteer(models.Model):
    volunteer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.IntegerField(max_length=15)
    area = models.ForeignKey(Place, on_delete=models.CASCADE)
    img = models.ImageField(upload_to = 'volunteers', default = '')

    def __str__(self):
        return self.name

