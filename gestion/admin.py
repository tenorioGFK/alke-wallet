from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')

class CuentaAdmin(admin.ModelAdmin):
    list_display = ('numero_cuenta', 'cliente', 'tipo', 'saldo')
    search_fields = ('numero_cuenta',)

class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('cuenta', 'tipo', 'monto', 'fecha')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(Transaccion, TransaccionAdmin)