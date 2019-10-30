from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


def download_media_location(instance, filename):

    return "%s/%s" %(instance.id, filename)


class Food(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    media = models.FileField(blank=True, null=True, upload_to="download_media_location")
    title = models.CharField(max_length=20)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(null=True, default="")
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        view_name = "food_detail_slug_view"
        return reverse(view_name, kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Food.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def food_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(food_pre_save_reciever, sender=Food)

# def food_post_save_reciever(sender, instance, *args, **kwargs):
#     if instance.slug != slugify(instance.title):
#         instance.slug = slugify(instance.title)
#         instance.save()
#
# post_save.connect (food_post_save_reciever, sender=Food)
