from django.contrib import admin
from .models import Score


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'score', 'start_date_time', 'end_date_time']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Score, ScoreAdmin)