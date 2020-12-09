from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import json

@csrf_exempt
def obtener_qr(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            id_usuario = data['id_usuario']
            id_evento = data['id_evento']
        except:
            response = JsonResponse({'error': 'parametros incorrectos'})
            response.status_code = 500
            return response
        
        with open("recibos/qr/qr.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        with open('data/qrs.json') as qrs_file:
            qrs = json.load(qrs_file)
        
        for qr in qrs:
            if qr['id_usuario'] == id_usuario:
                if qr['id_evento'] == id_evento:
                    return HttpResponse(encoded_string)

        response = JsonResponse({'error': 'No se encontro usuario y/o evento'})
        response.status_code = 404
        return response        
    elif request.method == 'GET':
        with open('data/qrs.json') as qrs_file:
            qrs = json.load(qrs_file)
        
        return JsonResponse(qrs, safe=False)