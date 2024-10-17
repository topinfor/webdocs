from django.contrib import admin
from django.utils.text import slugify
from .models import Blog, Category, Sector


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class SectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.action(description='Publicar')
def active_published(modeladmin, request, queryset):
    for obj in queryset:
        obj.is_published = True
        obj.save()

@admin.action(description='Despublicar')
def deactive_published(modeladmin, request, queryset):
    for obj in queryset:
         obj.is_published = False
         obj.save()

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at', 'updated_at')
    list_filter = ('is_published', 'created_at', 'updated_at', 'category', 'sector')
    search_fields = ('title', 'description', 'content')
    readonly_fields = ('slug',)
    actions = [active_published, deactive_published]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:
            form.base_fields['author'].initial = request.user
        return form

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        if not obj.slug:
            obj.slug = slugify(obj.title)
        obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Sector, SectorAdmin)