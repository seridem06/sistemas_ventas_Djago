from django.core.management.base import BaseCommand
from ventas.models import *
from django.utils import timezone
from decimal import Decimal

class Command(BaseCommand):
    help = 'Popula la base de datos con datos ficticios'

    def handle(self, *args, **kwargs):
        # Limpiar datos existentes
        Direccion.objects.all().delete()
        Categoria.objects.all().delete()
        Proveedor.objects.all().delete()
        Cliente.objects.all().delete()
        TelefonoCliente.objects.all().delete()
        Producto.objects.all().delete()
        Venta.objects.all().delete()
        DetalleVenta.objects.all().delete()

        # Crear direcciones
        dir1 = Direccion.objects.create(
            calle="Av. Principal",
            numero="123",
            comuna="Centro",
            ciudad="Santiago"
        )
        
        dir2 = Direccion.objects.create(
            calle="Calle Secundaria",
            numero="456",
            comuna="Providencia",
            ciudad="Santiago"
        )
        
        dir3 = Direccion.objects.create(
            calle="Av. Costanera",
            numero="789",
            comuna="Las Condes",
            ciudad="Santiago"
        )

        # Crear categorías
        cat_electronica = Categoria.objects.create(
            nombre="Electrónica",
            descripcion="Productos electrónicos y dispositivos"
        )
        
        cat_ropa = Categoria.objects.create(
            nombre="Ropa",
            descripcion="Prendas de vestir"
        )
        
        cat_hogar = Categoria.objects.create(
            nombre="Hogar",
            descripcion="Artículos para el hogar"
        )

        # Crear proveedores
        prov1 = Proveedor.objects.create(
            codigo="PROV001",
            nombre="TecnoImport",
            direccion=dir1,
            telefono="+56912345678",
            pagina_web="https://tecnoimport.cl"
        )
        
        prov2 = Proveedor.objects.create(
            codigo="PROV002",
            nombre="ModaStyle",
            direccion=dir2,
            telefono="+56987654321",
            pagina_web="https://modastyle.cl"
        )
        
        prov3 = Proveedor.objects.create(
            codigo="PROV003",
            nombre="HomeDecor",
            direccion=dir3,
            telefono="+56955555555",
            pagina_web="https://homedecor.cl"
        )

        # Crear clientes
        cliente1 = Cliente.objects.create(
            codigo="CLI001",
            nombre="Juan Pérez",
            direccion=dir1
        )
        
        cliente2 = Cliente.objects.create(
            codigo="CLI002",
            nombre="María González",
            direccion=dir2
        )
        
        cliente3 = Cliente.objects.create(
            codigo="CLI003",
            nombre="Carlos López",
            direccion=dir3
        )

        # Agregar teléfonos a clientes
        TelefonoCliente.objects.create(cliente=cliente1, telefono="+56911111111")
        TelefonoCliente.objects.create(cliente=cliente1, telefono="+56922222222")
        TelefonoCliente.objects.create(cliente=cliente2, telefono="+56933333333")
        TelefonoCliente.objects.create(cliente=cliente3, telefono="+56944444444")
        TelefonoCliente.objects.create(cliente=cliente3, telefono="+56955555555")

        # Crear productos
        prod1 = Producto.objects.create(
            nombre="Smartphone XYZ",
            precio_actual=299990,
            stock=50,
            proveedor=prov1,
            categoria=cat_electronica
        )
        
        prod2 = Producto.objects.create(
            nombre="Laptop ABC",
            precio_actual=599990,
            stock=25,
            proveedor=prov1,
            categoria=cat_electronica
        )
        
        prod3 = Producto.objects.create(
            nombre="Camiseta Casual",
            precio_actual=19990,
            stock=100,
            proveedor=prov2,
            categoria=cat_ropa
        )
        
        prod4 = Producto.objects.create(
            nombre="Jeans Clásicos",
            precio_actual=39990,
            stock=75,
            proveedor=prov2,
            categoria=cat_ropa
        )
        
        prod5 = Producto.objects.create(
            nombre="Juego de Sábanas",
            precio_actual=24990,
            stock=60,
            proveedor=prov3,
            categoria=cat_hogar
        )

        # Crear ventas
        venta1 = Venta.objects.create(
            numero_factura="F001-2024",
            fecha=timezone.now().date(),
            cliente=cliente1,
            descuento=10.0,
            monto_final=0  # Se calculará con los detalles
        )
        
        venta2 = Venta.objects.create(
            numero_factura="F002-2024",
            fecha=timezone.now().date(),
            cliente=cliente2,
            descuento=5.0,
            monto_final=0
        )
        
        venta3 = Venta.objects.create(
            numero_factura="F003-2024",
            fecha=timezone.now().date(),
            cliente=cliente3,
            descuento=0.0,
            monto_final=0
        )

        # Crear detalles de venta para venta1
        detalle1_1 = DetalleVenta.objects.create(
            venta=venta1,
            producto=prod1,
            precio_venta=299990,
            cantidad=1,
            monto_total=299990
        )
        
        detalle1_2 = DetalleVenta.objects.create(
            venta=venta1,
            producto=prod3,
            precio_venta=19990,
            cantidad=2,
            monto_total=39980
        )
        
        # Actualizar monto final de venta1
        total_venta1 = detalle1_1.monto_total + detalle1_2.monto_total
        venta1.monto_final = total_venta1 * (1 - Decimal(venta1.descuento/100))
        venta1.save()

        # Crear detalles de venta para venta2
        detalle2_1 = DetalleVenta.objects.create(
            venta=venta2,
            producto=prod2,
            precio_venta=599990,
            cantidad=1,
            monto_total=599990
        )
        
        detalle2_2 = DetalleVenta.objects.create(
            venta=venta2,
            producto=prod5,
            precio_venta=24990,
            cantidad=1,
            monto_total=24990
        )
        
        # Actualizar monto final de venta2
        total_venta2 = detalle2_1.monto_total + detalle2_2.monto_total
        venta2.monto_final = total_venta2 * (1 - Decimal(venta2.descuento/100))
        venta2.save()

        # Crear detalles de venta para venta3
        detalle3_1 = DetalleVenta.objects.create(
            venta=venta3,
            producto=prod4,
            precio_venta=39990,
            cantidad=3,
            monto_total=119970
        )
        
        # Actualizar monto final de venta3
        venta3.monto_final = detalle3_1.monto_total
        venta3.save()

        self.stdout.write(
            self.style.SUCCESS('Datos ficticios creados exitosamente!')
        )