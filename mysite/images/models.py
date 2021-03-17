from django.db import models
from django.conf import settings
from django.db.models.fields import related
from django.utils.text import slugify

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='images_created',
                            on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField()
    image = models.ImageField(blank=True)
    created = models.DateField(auto_now_add=True,
                                db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_like',
                                        blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.sluf = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
