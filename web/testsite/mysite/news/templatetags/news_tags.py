from django import template
from news.models import Category

register = template.Library()

@register.simple_tag()# создается тег {%get_categories%} только со словарем
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')# создание тега с показом в нем уже есть файл штмл
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}

