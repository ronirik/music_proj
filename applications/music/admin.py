from django.contrib import admin

from applications.music.models import Category

from applications.music.models import Music

admin.site.register(Category)
admin.site.register(Music)
