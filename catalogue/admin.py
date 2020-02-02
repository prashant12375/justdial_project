from django.contrib import admin
from .models import Datatable

# Register your models here.
#admin.site.register(Datatable)
@admin.register(Datatable)
class DatatableAdmin(admin.ModelAdmin):
    list_display=('product_name','brand_name','product_id','url','price','product_info')