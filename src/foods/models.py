from django.db import models

# Create your models here.


class Food(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, default="Description will be placed here")
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    def __unicode__(self):
        return self.title

