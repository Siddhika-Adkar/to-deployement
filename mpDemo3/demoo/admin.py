from django.contrib import admin
from demoo.models import Register
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id','rname','rmail','rpass','rrpass']

admin.site.register(Register,RegisterAdmin)