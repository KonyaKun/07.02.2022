from typing import Optional
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import admin
from . models import Account
from . models import Student
from . models import Group

 
# Register your models here.
class AccountAdmin (admin.ModelAdmin):
    readonly_fields = ()
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
    MAX_AGE = 16
    readonly_fields = ()
    def student_age_validation(
        self,
        obj: Optional[Student]
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


admin.site.register(
    Student, StudentAdmin
)

class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ()
    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:
        if obj:
            return self.readonly_fields + ('description',)
        return self.readonly_fields

admin.site.register(
    Group, GroupAdmin
)