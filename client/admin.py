from django.contrib import admin
from .models import Students, StudentsAdmin

admin.site.register(Students, StudentsAdmin)
