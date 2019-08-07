from django.contrib import admin
from apitest.models import Apistep,Apitest

# Register your models here.
class ApistepAdmin(admin.TabularInline):
    list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','apitest']
    model = Apistep
    extra=1

class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname', 'apitester','apitestresult','create_time','id']
    inlines = [ApistepAdmin]

admin.site.register(Apitest,ApitestAdmin)