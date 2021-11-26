from django.contrib import admin

# Register your models here.
from d2e_share_splitter.sharecontributions.models import ContribLog
from d2e_share_splitter.sharecontributions.models import Contribution


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ["user", "slices", "date"]
    pass


@admin.register(ContribLog)
class ContribLogAdmin(admin.ModelAdmin):
    list_display = ["user", "date"]
    pass
