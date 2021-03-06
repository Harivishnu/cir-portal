from django.contrib import admin
from registration.models import *
from registration.models import *

class UserAdmin(admin.ModelAdmin):
    pass
search_fields = ('first_name', 'last_name', 'email')
list_display = ('first_name', 'last_name', 'email')
admin.site.register(User, UserAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class TestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Test,TestAdmin)

class TechTestAdmin(admin.ModelAdmin):
    pass
admin.site.register(TechTest,TechTestAdmin)


class AptitudeTestAdmin(admin.ModelAdmin):
    pass
admin.site.register(AptitudeTest,AptitudeTestAdmin)

class EligibilityTestAdmin(admin.ModelAdmin):
    pass
admin.site.register(EligibilityTest,EligibilityTestAdmin)

class VerbalsTestAdmin(admin.ModelAdmin):
    pass
admin.site.register(VerbalsTest,VerbalsTestAdmin)


class QuantitaviveTestAdmin(admin.ModelAdmin):
    pass
admin.site.register(QuantitaviveTest,QuantitaviveTestAdmin)