from django.contrib import admin
from set.models import Set


# Register your models here.
class SetAdmin(admin.ModelAdmin):
    list_display = ['setname', 'setvalue', 'id']


admin.site.register(Set)  # 把系统设置模块注册到 Django admin 后台并显示
