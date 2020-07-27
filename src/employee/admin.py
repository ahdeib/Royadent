from django.contrib import admin

from .models import Department, Employee

class DepartmentAdmin(admin.ModelAdmin):

    list_display = ('name', 'created', 'modified')


class EmployeeAdmin(admin.ModelAdmin):

    # columns to be displayed on listing view
    list_display = ('name', 'email', 'department', 'created', 'modified')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)