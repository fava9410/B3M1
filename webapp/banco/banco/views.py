from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid
import json

@csrf_exempt
def debitar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            numero_tarjeta = data['numero_tarjeta']
            destino = data['destino']
            valor = data['valor']
        except:
            response = JsonResponse({'error': 'parametros incorrectos'})
            response.status_code = 500
            return response
        key = f'{numero_tarjeta}{destino}{valor}'
        return JsonResponse({'id_transaccion': uuid.uuid5(uuid.NAMESPACE_DNS, key)})

    
def cliente(request, id):    
    if request.method == 'GET':

        with open('data/clients.json', 'r') as f:
            clients = json.load(f)

        for client in clients:
            if client['id'] == id:
                return JsonResponse(client)
        
        response = JsonResponse({'error': 'No existe el usuario'})
        response.status_code = 404
        return response
