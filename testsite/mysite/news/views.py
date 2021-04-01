from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',}
    return render(request, template_name='news/index.html', context=context)

def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})



def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)# заполнение формы
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})

    #return render(request,'news/index.html',
                  #{'news': news,
                   #'title': 'Список новостей'})

#def index(request): Без шаблонов сразу в браузер.
    #news = News.objects.all()
    #res ='<h1>Список новостей</h1>'
    #for item in news:
        #res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>'#<hr> - добавляет всем подчеркивание
    #return HttpResponse(res)

#def test(request):
    #print(dir(request))
    #return HttpResponse('<h1>Фигня такая</h1>')

