from django.contrib import admin
from .models import ContactModule,CoursesModule,ScheduleModule,TeamDeatilsModule,TestimonialModule

class ContactDetails(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']

class CoursesDetails(admin.ModelAdmin):
    list_display = ['id','className', 'category', 'instructor']

class ScheduleDetails(admin.ModelAdmin):
    list_display = ['id', 'category', 'date', 'price', 'isdone']

class TeamDetails(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']

class TestimonialDetails(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'isvisible']

# Register your models here.
admin.site.register(ContactModule, ContactDetails)
admin.site.register(CoursesModule, CoursesDetails)
admin.site.register(ScheduleModule, ScheduleDetails)
admin.site.register(TeamDeatilsModule, TeamDetails)
admin.site.register(TestimonialModule, TestimonialDetails)