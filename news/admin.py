from django.contrib import admin

# Register your models here.
from .models import Editor, Article, tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Editor)
admin.site.register(Article, ArticleAdmin)
admin.site.register(tags)

