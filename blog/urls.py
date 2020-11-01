from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name = 'index'),
    url(r'^contact/$', views.ContactPage.as_view(), name = 'contact'),
    path('article/<str:id>/', views.article_content_view,name= 'article_content'),


]