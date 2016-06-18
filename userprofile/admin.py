from django.contrib import admin
from .models import UserProfile, University, Department, Semester, Group

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(University)
admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(Group)