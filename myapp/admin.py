from django.contrib import admin
from .models import Adviser
# Register your models here.
@admin.register(Adviser)
class AdviserAdmin(admin.ModelAdmin):
    list_display = ['name','roll','city']