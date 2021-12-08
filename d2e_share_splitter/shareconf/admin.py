from django.contrib import admin

# Register your models here.
from d2e_share_splitter.shareconf.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name"]
    pass
