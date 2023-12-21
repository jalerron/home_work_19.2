from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=10, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price_for_one = models.IntegerField(verbose_name='цена за штуку')
    date_of_creation = models.DateField(verbose_name='дата создания')
    date_last_changes = models.DateField(verbose_name='дата последнего изменения')

    is_active = models.BooleanField(default=True, verbose_name='доступно')
    is_new = models.BooleanField(default=True, verbose_name='новинка')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
