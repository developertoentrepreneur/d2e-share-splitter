from django.contrib import admin

# Register your models here.
from d2e_share_splitter.shareconf.models import ShareConfiguration


@admin.register(ShareConfiguration)
class ShareConfigurationAdmin(admin.ModelAdmin):
    list_display = ["nonCashMultiplier"]
    pass
