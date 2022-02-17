from typing import Optional
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from . models import (Account, 
                    Student, 
                    Group, 
                    Professor,)

 
# Register your models here.
class AccountAdmin (admin.ModelAdmin):
    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:
        if obj:
            return self.readonly_fields + ('description',)
        return self.readonly_fields

admin.site.register(
    Account, AccountAdmin
)

class StudentAdmin(admin.ModelAdmin):
    
    list_filter = (
        'age',
        'GPA',
    )
    search_fields = (
        'account',
    )
    list_display = (
        'account',
        'age',
        'GPA',
    )

    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )

    MAX_AGE = 16
    def student_age_validation(
        self,
        obj: Student
    ) -> tuple:
        if obj and obj.age <= self.MAX_AGE:
            return self.readonly_fields + ('age',)
        return self.readonly_fields
        
    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Student] = None
    ) -> tuple:

        result: tuple = self.student_age_validation(obj)
        return result

        if obj and obj.age > self.MAX_AGE:
            return self.readonly_fields + ('age',)
        return self.readonly_fields

    
    
admin.site.register(
    Student, StudentAdmin
)


class GroupAdmin(admin.ModelAdmin):
    readonly_fields = (
    'datetime_created',
    'datetime_updated',
    'datetime_deleted',
    )

    group_name = 'group'

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:

        if obj and obj.name == 'group':
            return self.readonly_fields + ('name',)
        return self.readonly_fields

admin.site.register(
    Group, GroupAdmin
)


class ProfessorAdmin(admin.ModelAdmin):
    readonly_fields = (
    'datetime_created',
    'datetime_updated',
    'datetime_deleted',
    )
    pass
    

admin.site.register(
    Professor, ProfessorAdmin
)