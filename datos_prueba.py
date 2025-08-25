from cliente_sac.models import Cliente

def crear_clientes_prueba():
    """Crear clientes de prueba para testing"""
    
    # Cliente 1
    Cliente.objects.create(
        tipo_documento='CC',
        numero_documento='12345678',
        nombre='Juan Carlos',
        apellido='Pérez González',
        correo='juan@test.com',
        telefono='3001234567'
    )
    
    # Cliente 2
    Cliente.objects.create(
        tipo_documento='CC',
        numero_documento='87654321',
        nombre='María Fernanda',
        apellido='López Rivera',
        correo='maria@test.com',
        telefono='3009876543'
    )
    
    # Cliente 3
    Cliente.objects.create(
        tipo_documento='NIT',
        numero_documento='900123456',
        nombre='Empresa ABC',
        apellido='S.A.S.',
        correo='contacto@empresa.com',
        telefono='3005551234'
    )
    
    print("Clientes de prueba creados exitosamente")

if __name__ == "__main__":
    import os
    import django
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tu_proyecto.settings')
    django.setup()
    
    crear_clientes_prueba()