from django.db import models

# Create your models here.


# Code for models for 3 tables modified from:
# https://betterprogramming.pub/optimizing-django-admin-6a1187ddbb09 &
# https://stackoverflow.com/questions/47843241/django-admin-how-to-populate-select-options-depending-on-another-select
class Category(models.Model):
    """
    Model for Category table
    """
    name = models.CharField(max_length=254, db_index=True)
    slug = models.SlugField(
        max_length=150, unique=True, db_index=True, default='NULL')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """
    Model for Subcategory table
    """
    category = models.ForeignKey(
        'Category', related_name='subcategories',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=254, db_index=True)
    slug = models.SlugField(
        max_length=150, unique=True, db_index=True, default='NULL')

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model for Product table
    """
    name = models.CharField(max_length=254, db_index=True)
    slug = models.SlugField(
        max_length=150, unique=True, db_index=True, default='NULL')
    category = models.ForeignKey(
        'Category', related_name='products',
        on_delete=models.CASCADE)
    subcategory = models.ForeignKey(
        'SubCategory', related_name='products',
        on_delete=models.CASCADE)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    brand = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
