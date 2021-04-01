from django.db import models
from django.urls import reverse

class Category (models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')


    def __str__(self):
        return self.title

    def get_absolute_url(self):#url тег только в пайтон файлов
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'  # вербозу_нейм можно и в apps.py использовать
        verbose_name_plural = 'Категории'
        ordering = ['title']


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')#blank-значит может быть пустым
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='Фото', blank=True)# автоматом видет даты
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Категория')#связал с ктегорией ниже ,если бы класс категории был бы ниже,то 'Category' в кавычки

    def get_absolute_url(self):#url тег только в пайтон файлов
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'# вербозу_нейм можно и в apps.py использовать
        verbose_name_plural ='Новости'
        ordering = ['created_at']#Порядок сортировки для всего





