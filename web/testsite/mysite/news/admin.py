from django.contrib import admin
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at',
                    'updated_at', 'is_published',)#добовляем поля в админку
    list_display_links = ('id', 'title',)#принажатии в админки переходит в редактор новости
    search_fields = ('title','content',)#когда аски то регистр любой,у кирилицы только тот что в слове иначе не найдет
    list_editable = ('is_published',)#можно редактировать поле
    list_filter = ('is_published', 'category',)#фильтр и в африке таблица фильтра
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title',)#добовляем поля в админку
    list_display_links = ('id', 'title',)#принажатии в админки переходит в редактор новости
    search_fields = ('title',)

admin.site.register(News,NewsAdmin,)#Сначала регать основную,потом класс дополнительный
admin.site.register(Category,CategoryAdmin,)