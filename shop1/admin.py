from django.contrib import admin

# Register your models here.

from .models import slide, product, order


'''class orderAdmin(admin.ModelAdmin):
    readonly_fields = ('oid',)


admin.site.register(order, orderAdmin)
'''

admin.site.register(slide)



class productAdmin(admin.ModelAdmin):
    list_display = ('pname', 'chat', 'subchat',  'pid', 'price', 'dicount')
    list_editable = ('price', 'dicount',)


admin.site.register(product, productAdmin)


class orderAdmin(admin.ModelAdmin):
    list_display = ('fname', 'proid', 'oid', 'ostat', 'mobile_no')
    list_editable = ('ostat',)


admin.site.register(order, orderAdmin)
