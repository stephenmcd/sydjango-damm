
from django.contrib import admin

from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    pass

    list_display = ("title", "publish_date", "published", "admin_link")
    list_editable = ("published",)
    list_filter = ("published",)
    search_fields = ("title", "content",)
    date_hierarchy = "publish_date"
    ordering = ("-publish_date",)

    fieldsets = (
        (None, {
            "fields": ("title", "content"),
        }),
        ("Other fields", {
            "fields": ("slug", "published", "publish_date"),
            "classes": ("collapse",)
        }),
    )


admin.site.register(BlogPost, BlogPostAdmin)
