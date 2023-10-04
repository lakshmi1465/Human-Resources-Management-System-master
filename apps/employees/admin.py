from django.contrib import admin

from .models import Employee


#admin.site = MyAdminSite(name='myadmin')
admin.site.register(Employee)

admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "HRMS_PORTAL"

