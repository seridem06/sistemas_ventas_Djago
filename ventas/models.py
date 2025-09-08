from django.db import models

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    
    class Meta:
        unique_together = ('calle', 'numero', 'comuna', 'ciudad')
    
    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comuna}, {self.ciudad}"

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    codigo = models.CharField(max_length=20, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    pagina_web = models.URLField()
    
    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class Cliente(models.Model):
    codigo = models.CharField(max_length=20, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class TelefonoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='telefonos')
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.cliente.nombre}: {self.telefono}"

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio_actual}"

class Venta(models.Model):
    numero_factura = models.CharField(max_length=20, unique=True, primary_key=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    monto_final = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return f"Factura {self.numero_factura} - {self.cliente.nombre}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        unique_together = ('venta', 'producto')
    
    def __str__(self):
        return f"{self.venta.numero_factura} - {self.producto.nombre}"