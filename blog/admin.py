from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['likes', 'tags', 'author']


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['post', 'author']
    list_display = ['id', 'author', 'post', 'text']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
