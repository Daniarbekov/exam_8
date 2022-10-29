from django.db import models


class CategoryChoices(models.TextChoices):
        OTHER = 'other', 'Разное'
        TV = 'tv', 'Телевизор'
        SMARTPHONE = 'Smartphone', 'Смартфон'
        LAPTOP = 'Laptop', 'Ноутбук'
        

class Product(models.Model):
    name = models.CharField(
        verbose_name='Название', 
        max_length=100
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True,
        max_length=2000
    )
    image = models.ImageField(
        verbose_name='Фото', 
        null=True, 
        blank=True, 
        upload_to='products'
    )
    category = models.CharField(
        verbose_name='Категория',
        choices=CategoryChoices.choices, 
        default=CategoryChoices.OTHER,
        max_length=50
        )

    def __str__(self):
          return f"{self.name}"