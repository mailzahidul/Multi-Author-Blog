from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=True)
    image = models.ImageField(null=True, upload_to='category/')
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name