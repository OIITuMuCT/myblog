from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Blog, BlogAdmin)

class BlogCustomAdmin(admin.ModelAdmin):
    search_fields = ['title']
    show_full_result_count = True
    list_filter = ['title']
    list_display = ['title', 'created_at']
    date_hierarchy = 'created_at'

# admin.site.register(Blog, BlogCustomAdmin)

class BlogCustom2Admin(admin.ModelAdmin):
    """Adding custom fields"""
    list_display = ['title', 'word_count', 'id']

    def word_count(self, obj):
        return obj.content.split()

# admin.site.register(Blog, BlogCustom2Admin)

class BlogCustom3Admin(admin.ModelAdmin):
    """Using filter_horizontal"""
    filter_horizontal = ['tags']

# admin.site.register(Blog, BlogCustom3Admin)
