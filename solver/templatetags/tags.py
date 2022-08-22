from django import template
from ..other import data

register = template.Library()

@register.simple_tag(name='get_list')
def get_list():
    return data

# @register.inclusion_tag('news/list_categories.html')
# def show_categories():
#     # category = Category.objects.raw('''SELECT news_category.id, news_category.title as title, COUNT(news_news.id) as count FROM news_news INNER JOIN news_category ON news_category.id = news_news.category_id WHERE news_news.is_published = True GROUP BY news_news.category_id HAVING count > 0''')
#     category = Category.objects.filter(news__is_published=True).annotate(count=Count('news')).filter(count__gt=0)
#     return {"categories": category}
