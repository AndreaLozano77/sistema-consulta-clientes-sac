from django.db import models

class Cliente(models.Model):
    TIPOS_DOC = [
        ('CC', 'Cédula de Ciudadanía'),
        ('NIT', 'NIT'),
        ('PA', 'Pasaporte')
    ]
    
    tipo_documento = models.CharField(max_length=3, choices=TIPOS_DOC)
    numero_documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.numero_documento}"

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='compras')
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.cliente.nombre} - ${self.monto}"