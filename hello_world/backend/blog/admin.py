from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.core import paginator
from django.utils.functional import cached_property
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

class BlogCustom4Admin(admin.ModelAdmin):
    list_display = ['title', 'create_at', 'author_full_name']

    def author_full_name(self, obj):
        return f'{obj.author.user.first_name} {obj.author.user.last_name}'

    def get_queryset(self, request):
        default_qs = super().get_queryset(request)
        improved_qs = default_qs.select_related('author', 'author__user')
        return improved_qs

# admin.site.register(Blog, BlogCustom4Admin)

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False

class CustomPaginator(paginator.Paginator):
    @cached_property
    def count(self):
        return 99999

class BlogCustom5Admin(admin.ModelAdmin):
    paginator = CustomPaginator

admin.site.register(Blog, BlogCustom5Admin)
