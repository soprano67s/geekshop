from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя категории', max_length=128)
    image = models.ImageField(upload_to='product_img', blank=True)
    mini_description = models.CharField(verbose_name='Краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='Описание товара', blank=True)
    price = models.DecimalField(verbose_name='Стоимость',max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
