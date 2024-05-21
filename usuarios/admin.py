from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('nome', 'email', 'password')}),
        ('Permissões', {'fields': ('is_active', 'is_staff')}),
        ('Datas importantes', {'fields': ('last_login',)}),
    )
    list_display = ('nome', 'email', 'is_active', 'is_staff')
    search_fields = ('nome', 'email')
    list_filter = ('is_active', 'is_staff')
    filter_horizontal = ()
    model = Usuario
    ordering = ()

admin.site.register(Usuario, UsuarioAdmin)
