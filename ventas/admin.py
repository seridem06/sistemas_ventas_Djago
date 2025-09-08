from django.contrib import admin
from .models import *

class TelefonoClienteInline(admin.TabularInline):
    model = TelefonoCliente
    extra = 1

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'comuna', 'ciudad')
    search_fields = ('calle', 'comuna', 'ciudad')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'telefono', 'pagina_web')
    search_fields = ('codigo', 'nombre')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')
    inlines = [TelefonoClienteInline]

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio_actual', 'stock', 'proveedor', 'categoria')
    list_filter = ('categoria', 'proveedor')
    search_fields = ('nombre',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'fecha', 'cliente', 'descuento', 'monto_final')
    list_filter = ('fecha', 'cliente')
    inlines = [DetalleVentaInline]
    search_fields = ('numero_factura', 'cliente__nombre')

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'precio_venta', 'cantidad', 'monto_total')
    list_filter = ('venta', 'producto')

@admin.register(TelefonoCliente)
class TelefonoClienteAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'telefono')
    search_fields = ('cliente__nombre', 'telefono')