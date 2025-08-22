from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import csv
from .models import Cliente, Compra

def index(request):
    """Vista principal con el formulario"""
    return render(request, 'consultas/index.html')

@csrf_exempt
@require_http_methods(["POST"])
def buscar_cliente(request):
    """API para buscar cliente por número de documento"""
    try:
        data = json.loads(request.body)
        numero_doc = data.get('numero_documento')
        
        if not numero_doc:
            return JsonResponse({
                'success': False, 
                'error': 'Número de documento requerido'
            })
        
        cliente = Cliente.objects.get(numero_documento=numero_doc)
        
        # Obtener compras del cliente
        compras = cliente.compras.all()
        total_compras = sum(compra.monto for compra in compras)
        
        return JsonResponse({
            'success': True,
            'cliente': {
                'id': cliente.id,
                'tipo_documento': cliente.get_tipo_documento_display(),
                'numero_documento': cliente.numero_documento,
                'nombre': cliente.nombre,
                'apellido': cliente.apellido,
                'correo': cliente.correo,
                'telefono': cliente.telefono,
                'total_compras': str(total_compras),
                'cantidad_compras': compras.count()
            }
        })
        
    except Cliente.DoesNotExist:
        return JsonResponse({
            'success': False, 
            'error': 'Cliente no encontrado'
        })
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'error': f'Error interno: {str(e)}'
        })

def exportar_cliente_csv(request, cliente_id):
    """Exportar datos del cliente en CSV"""
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="cliente_{cliente.numero_documento}.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Tipo Documento', 'Número Documento', 'Nombre', 'Apellido', 'Correo', 'Teléfono'])
        writer.writerow([
            cliente.get_tipo_documento_display(),
            cliente.numero_documento,
            cliente.nombre,
            cliente.apellido,
            cliente.correo,
            cliente.telefono
        ])
        
        return response
        
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)