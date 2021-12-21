from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70,unique=True)
    img = models.ImageField(upload_to='catimages')

    def __str__(self):
        return self.name
    
    @property
    def image_url(self):
        if self.img and hasattr(self.img,'url'):
            return self.img.url

class Post(models.Model):
    title = models.CharField(max_length=100)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    desc = models.TextField()
    slug = models.CharField(max_length=130,unique=True)
    img=models.ImageField(upload_to='postimages')
    author = models.CharField(max_length=13)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + "by" + self.author
    
    @property
    def image_url(self):
        if self.img and hasattr(self.img,'url'):
            return self.img.url