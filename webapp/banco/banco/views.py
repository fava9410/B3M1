from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid
import json


def check_client(id_client, numero_tarjeta=None):
    with open('data/clients.json', 'r') as f:
        clients = json.load(f)
    print(id_client)
    for client in clients:
        if client['id'] == id_client and numero_tarjeta is None:
            return client
        elif client['id'] == id_client and client['numero_tarjeta'] == numero_tarjeta:
            return True
    
    return None


@csrf_exempt
def debitar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_cliente = data['id_cliente']
            numero_tarjeta = data['numero_tarjeta']
            id_evento = data['id_evento']
            valor = data['valor']
        except:
            response = JsonResponse({'error': 'Parametros incorrectos'})
            response.status_code = 500
            return response
        
        if check_client(id_cliente, numero_tarjeta):
            key = f'{id_cliente}{numero_tarjeta}{id_evento}{valor}'
            return JsonResponse({'id_transaccion': uuid.uuid5(uuid.NAMESPACE_DNS, key)})
        else:
            response = JsonResponse({'error': 'id_cliente y/o numero de tarjeta incorrectos'})
            response.status_code = 500
            return response


def cliente(request, id):    
    if request.method == 'GET':
        client = check_client(id)
        if client:
            return JsonResponse(client)
        
        response = JsonResponse({'error': 'No existe el usuario'})
        response.status_code = 404
        return response
