from django.contrib import admin
from .models import Article
from django.contrib.auth.models import Permission
# Register your models here.

admin.site.register(Article)
admin.site.register(Permission)