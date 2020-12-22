from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import json

@csrf_exempt
def new_qr(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            id_cliente = data['id_cliente']
            id_evento = data['id_evento']
            id_transaccion = data['id_transaccion']
        except:
            response = JsonResponse({'error': 'Parametros incorrectos'})
            response.status_code = 500
            return response
        
        with open("recibos/qr/qr.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        return HttpResponse(encoded_string)