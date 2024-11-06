from django.contrib import admin

# Register your models here.
from .models import *


class postAdmin(admin.ModelAdmin):
    list_display = ("user","content","like","timestamp")
  
class likeAdmin(admin.ModelAdmin):
    list_display = ("user","post")
  
    




admin.site.register(Post, postAdmin)
admin.site.register(Like, likeAdmin) 

admin.site.register(User)
