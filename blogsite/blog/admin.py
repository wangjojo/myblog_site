from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug','intro', 'home_display')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','published','pub_date','update_time')


admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)