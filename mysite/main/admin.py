from django.contrib import admin
from .models import (Project, Client, Employee, Position, Task, Bill)

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'in_charge', 'date_start', 'date_end')
    list_filter = ('in_charge__username', 'date_start', 'date_end')
    search_fields = ('name', 'in_charge__username', 'client__first_name',
    'client__last_name', 'client__company')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'email_field')
    list_filter = ('first_name', 'last_name', 'company', 'email_field')
    search_fields = ('first_name', 'last_name', 'company', 'email_field')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position')
    list_filter = ('first_name', 'last_name', 'position')
    search_fields = ('first_name', 'last_name', 'position')


class PositionAdmin(admin.ModelAdmin):
    list_display = ('position_name',)
    list_filter = ('position_name',)
    search_fields = ('position_name',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'status')
    list_filter = ('task_name', 'status')
    search_fields = ('first_name', 'last_name')


class BillAdmin(admin.ModelAdmin):
    list_display = ('bill_sum', 'issue_date', 'status')
    list_filter = ('bill_sum', 'issue_date', 'status')
    search_fields = ('bill_sum', 'issue_date', 'status')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Bill, BillAdmin)