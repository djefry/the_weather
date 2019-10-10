from django.contrib import admin
from .models import Cities
# Register your models here.


class CityViews(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Cities, CityViews)
