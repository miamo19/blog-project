from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse
from django.utils import timezone

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=80)

    def __str__(self):
        return self.name





class Post(models.Model):
    category       = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_posts")
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title          = models.CharField(max_length=200)
    slug           = models.SlugField(max_length=200)
    body           = models.TextField()
    created        = models.DateTimeField(auto_now_add=True)
    update         = models.DateTimeField(auto_now=True)
    status         = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=100)
    publish        = models.DateTimeField(default=timezone.now())
    author         = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='posted')
    objects = models.Manager()        #default manager
    published = PublishedManager()    #custom manager
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


class Comment(models.Model):
    post     = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=100)
    email    = models.EmailField(max_length=100)
    body     = models.TextField()
    created  = models.DateTimeField(auto_now_add=True)
    update   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title