from django.contrib import admin
from .models import Jobs, Requirments, Responsibilites, Perks

# Register your models here.
class RequirmentsInline(admin.TabularInline):
	model = Requirments

class ResponsibilitesInline(admin.TabularInline):
	model = Responsibilites

class PerksInline(admin.TabularInline):
	model = Perks

class JobsAdmin(admin.ModelAdmin):
	inlines = [RequirmentsInline, ResponsibilitesInline, PerksInline]
admin.site.register(Requirments)
admin.site.register(Responsibilites)
admin.site.register(Perks)
admin.site.register(Jobs, JobsAdmin)