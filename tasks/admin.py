from django.db.models import Case, When, IntegerField
from django.contrib import admin
from .models import Task, Photo


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_at', 'priority', 'user', 'is_complete')
    list_filter = ('created_at', 'update_at', 'priority', 'is_complete')
    search_fields = ('title',)
    ordering = (Case(
        When(priority='High', then=1),
        When(priority='Medium', then=2),
        When(priority='Low', then=3),
        default=4,
        output_field=IntegerField(),
    ),)


admin.site.site_header = 'Task Manager Admin'
admin.site.site_title = 'Task Manager Admin'
admin.site.index_title = 'Task Manager Admin'

admin.site.register(Task, TaskAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('task', 'image')


admin.site.site_header = 'Task Manager Admin'
admin.site.site_title = 'Task Manager Admin'
admin.site.index_title = 'Task Manager Admin'

admin.site.register(Photo, PhotoAdmin)
# admin.site.register(Task, TaskAdmin)