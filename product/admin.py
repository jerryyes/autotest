from django.contrib import admin
from product.models import Product
from webtest.models import Webcasestep,Webcase


# Register your models here.
class WebcaseAdmin(admin.TabularInline):
    list_display = ['webcasename', 'webtestresult','create_time','id','product']
    model = Webcase
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']
    inlines = [WebcaseAdmin]


admin.site.register(Product)  # 把产品模块注册到 Django admin 后台并能显示
