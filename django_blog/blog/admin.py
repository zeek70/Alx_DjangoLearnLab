from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','published_date')
    list_filter=('published_date','author')
    search_fields=('title','content')
    readonly_fields=('published_date',)
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        obj.save()

