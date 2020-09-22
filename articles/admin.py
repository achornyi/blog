from django.contrib import admin
from .models import Article
from blog.admin import editor_admin


class EditorAdmin(admin.ModelAdmin):
    search_fields = ['title', 'tags']


admin.site.register(Article, EditorAdmin)

editor_admin.register(Article, EditorAdmin)
