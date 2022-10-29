from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=User,
        related_name='reviews',
        on_delete=models.CASCADE)
    product = models.ForeignKey(
        verbose_name='Товар',
        to='webapp.Product',
        related_name='products',
        on_delete=models.CASCADE
        )
    text=models.TextField(
        verbose_name='Текст',
        max_length=3000,
    )
    rating = models.IntegerField(
        verbose_name='Оценка',
        validators=[
            MaxValueValidator(5), 
            MinValueValidator(1)
            ]
    )
