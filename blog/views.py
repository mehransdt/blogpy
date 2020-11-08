from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


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

class AllArticleAPIView(APIView):
    def get(self,request,format=None):
        try:
            all_article = Article.objects.all().order_by('-created_at')[:10]
            data = []
            for article in all_article:
                data.append({
                    'title':article.title,
                    'cover': article.cover.url if article.cover else None,
                    'content': article.content,
                    'created_at': article.created_at,
                    'category': article.category.title,
                    'author': article.author.user.first_name + ' ' + article.author.user.last_name,
                    'slider': article.slider,
                    
                })
            return Response({'data':data},status=status.HTTP_200_OK)
        
        except:
            return Response({'status': 'Internal server error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class SingleArticleAPIView(APIView):
    def get(self,request,format=None):
        try:
            article_title = request.GET['article_title']
            article = Article.objects.filter(title__contains = article_title)
            serialized_data = serializers.SingleArticleSerializer(article,many=True)
            data = serialized_data.data

            return Response({'data':data},status=status.HTTP_200_OK)


        except:
            return Response({'status':'Internal server error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SearchArticleAPIView(APIView):
    def get(self,request,format=None):
        try:
            from django.db.models import Q

            query = request.GET['query']
            articles = Article.objects.filter(Q(content__icontains=query))
            data = []
            for article in articles:
                data.append({
                    'title' : article.title,
                    "cover" : article.cover.url if article.cover else None,
                    "content" : article.content,
                    'slider' : article.slider,

                })
            return Response({'data':data},status = status.HTTP_200_OK)


        except:
            return Response({'status':'Internal server error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    




