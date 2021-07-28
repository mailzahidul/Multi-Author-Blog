from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(null=True, upload_to='category/', blank=True)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name
        

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to = "blog/feature_image", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    featured = models.BooleanField(default=True)
    visit_count = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Post"

    def __str__(self):
        return self.title


