from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class IndexPage(TemplateView):
    def get(self, request, **kwargs):
        article_data = []
        all_articles = Article.objects.all().order_by('-created_at')[:9]

        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'created_at': article.created_at.date,
                'article_id': article.pk,
            })

        slider_data = []
        all_slider_articles = Article.objects.filter(slider=True)
        for slider_article in all_slider_articles:
            slider_data.append({
                'category':slider_article.category.title,
                'title':slider_article.title,
                'author':slider_article.author.user.first_name + ' ' + slider_article.author.user.last_name,
                'avatar':slider_article.author.avatar.url if slider_article.author.avatar else None,
                'created_at':slider_article.created_at.date(),
                'cover':slider_article.cover.url if slider_article.cover else None,

            })
            
        context = {
            'article_data': article_data,
            'slider_article_data': slider_data,
        }
        return render(request, 'index.html', context)

class ContactPage(TemplateView):
    template_name = "page-contact.html"

def article_content_view(request,article_id):
    content = Article.objects.get(id=article_id).content
    context = {
        'content':content
    }
    return render(request,'article.html',context)






