from django.db import models
from catalog.models import Product


class Reviews(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    body = models.TextField(verbose_name='отзыв')
    product = models.ForeignKey(Product,  on_delete=models.CASCADE, verbose_name='продукт')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания', null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.date}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'