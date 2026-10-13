from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "published_at")
    list_filter = ("author", "published_at")
    search_fields = ("title", "content")

    @admin.action(description="Publicar posts selecionados")
    def publish_posts(self, request, queryset):
        for post in queryset:
            post.publish()

    actions = ["publish_posts"]
