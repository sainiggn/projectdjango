from django.contrib import admin
from .models import Category, Item, VideoComment
from embed_video.admin import AdminVideoMixin

# Register your models here.

class MYModelAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass

admin.site.register(Item,MYModelAdmin)
admin.site.register(Category)
admin.site.register(VideoComment)
