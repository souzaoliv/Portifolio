from django.contrib import admin
from .models import Post, PostTags
from ckeditor.widgets import CKEditorWidget
from django.db import models

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    search_fields = ('title', 'body')
    list_filter = ('status', 'created', 'publish', 'author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    ordering = ('status', 'publish')
    date_hierarchy = 'publish'
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(PostTags)