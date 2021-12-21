from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70,unique=True)
    img = models.ImageField(upload_to='prdctcatimages')

    def __str__(self):
        return self.name
    
    @property
    def image_url(self):
        if self.img and hasattr(self.img,'url'):
            return self.img.url

class Products(models.Model):
    product_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    desc = models.TextField()
    price=models.IntegerField()
    slug = models.SlugField(unique=True)
    img=models.ImageField(upload_to='productimages')
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name[:15]
    
    @property
    def image_url(self):
        if self.img and hasattr(self.img,'url'):
            return self.img.url