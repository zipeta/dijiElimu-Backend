from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Student


admin.site.register(Student)
admin.site.register(User)
admin.site.unregister(Group)
