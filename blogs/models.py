from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    body = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blogs/', verbose_name='Превью')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True, blank=True)
    on_published = models.BooleanField(default=True, verbose_name='статус', null=True, blank=True)
    count_view = models.IntegerField(verbose_name='количество просмотров', default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.title}{self.body}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоговые записи'