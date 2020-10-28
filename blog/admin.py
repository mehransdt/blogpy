from django.contrib import admin

from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','avatar','description']

admin.site.register(UserProfile,UserProfileAdmin)

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title','content']
    list_display = ['title','content','created_at']

admin.site.register(Article,ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','cover']

admin.site.register(Category,CategoryAdmin)

