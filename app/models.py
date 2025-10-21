from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, 
                            verbose_name='Name')
    country = models.CharField(max_length=255, null=False, blank=False, verbose_name='Country')

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Description yay')
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False,verbose_name='Price')
    image_url = models.URLField(null=False, blank=False, verbose_name='Image url')

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name
