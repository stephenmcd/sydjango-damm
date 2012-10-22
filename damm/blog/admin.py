
from django.contrib import admin
from django.shortcuts import redirect

from .models import BlogPost, Homepage


class BlogPostAdmin(admin.ModelAdmin):

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


class SingletonAdmin(admin.ModelAdmin):

    def singleton_redirect(self):
        try:
            obj = self.model.objects.get()
        except self.model.DoesNotExist:
            return None
        else:
            info = obj._meta.app_label, obj._meta.module_name
            return redirect("admin:%s_%s_change" % info, obj.id)

    def add_view(self, *args, **kwargs):
        response = self.singleton_redirect()
        if response:
            return response
        return super(SingletonAdmin, self).add_view(*args, **kwargs)

    def changelist_view(self, *args, **kwargs):
        response = self.singleton_redirect()
        if response:
            return response
        return super(SingletonAdmin, self).changelist_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        kwargs.setdefault("extra_context", {})
        kwargs["extra_context"]["singleton"] = True
        return super(SingletonAdmin, self).change_view(*args, **kwargs)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Homepage, SingletonAdmin)
