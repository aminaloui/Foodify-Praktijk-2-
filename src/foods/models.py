from django.db import models
from django.db.models.signals import pre_save, post_save


# Create your models here.
from django.utils.text import slugify


class Food(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(blank=True) #(unique=True)
    description = models.TextField(null=True, default="")
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    def __unicode__(self):
        return self.title

def food_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = "some-slug"

pre_save.connect(food_pre_save_reciever, sender=Food)

# def food_post_save_reciever(sender, instance, *args, **kwargs):
#     if instance.slug != slugify(instance.title):
#         instance.slug = slugify(instance.title)
#         instance.save()
#
# post_save.connect (food_post_save_reciever, sender=Food)