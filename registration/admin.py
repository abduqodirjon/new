from django.contrib import admin
from .models import CustomUser
from .forms import CustomCreateUserForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    
    add_form = CustomCreateUserForm
    model = CustomUser
    list_display = ['username','u_fio', 'guruhi', 'm_fio',  'tel', 'manzil', 'image']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('u_fio',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('u_fio', 'guruhi', 'm_fio', 'username', 'tel', 'manzil', 'image')}),
    )



admin.site.register(CustomUser, CustomUserAdmin)

