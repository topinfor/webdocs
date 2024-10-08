from django.contrib import admin

from .models import Blog, Category, Sector


class CategoryAdmin(admin.ModelAdmin):
    ...

class SectorAdmin(admin.ModelAdmin):
    ...

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    ...
   
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sector, SectorAdmin)
