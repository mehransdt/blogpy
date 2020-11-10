from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name = 'index'),
    url(r'^contact/$', views.ContactPage.as_view(), name = 'contact'),
    path('article/<int:article_id>/', views.article_content_view,name= 'article_content'),
    url(r'^article/api/$',views.AllArticleAPIView.as_view(),name='article_api'),
    path('article/single/',views.SingleArticleAPIView.as_view(),name='single_article'),
    path('article/search/',views.SearchArticleAPIView.as_view(),name='Search_article'),
    path('article/submit/',views.SubmitArticleAPIView.as_view(),name='submit_article'),
    path('article/update-cover/',views.UpdateArticleAPIView.as_view(),name='update_cover'),
    
]
