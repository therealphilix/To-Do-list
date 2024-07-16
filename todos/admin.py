from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ToDoUser)
class ToDOUserAdmin(admin.ModelAdmin):
    pass
