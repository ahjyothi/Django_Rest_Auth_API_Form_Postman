from django.contrib import admin

# Register your models here.
from BlogApp.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'body']


admin.site.register(BlogPost, BlogPostAdmin)

