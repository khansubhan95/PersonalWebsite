from django.contrib import admin
from posts.models import Post
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.
class PostAdmin(MarkdownModelAdmin):
    list_display = ('title', 'date')
    # prepopulated_fields = {'slug':('title'),}
admin.site.register(Post, MarkdownModelAdmin)
