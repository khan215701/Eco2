from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdminUser
from . import models
# Register your models here.

@admin.register(models.User)
class UserAdmin(BaseAdminUser):
    pass
