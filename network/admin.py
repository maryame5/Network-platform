from django.contrib import admin

# Register your models here.
from .models import *


class postAdmin(admin.ModelAdmin):
    list_display = ("user","content","like","timestamp")
  
    




admin.site.register(Post, postAdmin)

admin.site.register(User)
