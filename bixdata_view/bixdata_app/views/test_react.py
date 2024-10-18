
from django.conf import settings
from django.http import JsonResponse, HttpResponse

import json
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout
from Crypto.Cipher import AES
import base64
from cryptography.fernet import Fernet
import logging
from Crypto.Util.Padding import unpad

from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

import jwt
from rest_framework_simplejwt.tokens import RefreshToken


logger = logging.getLogger(__name__)


@login_required
def test_react_request(request):
    if request.method == 'POST':
        # Carica i dati JSON dalla richiesta
        data = json.loads(request.body)
        number = data.get('numero')  # Ottieni il numero

        if number is not None:  # Verifica se il numero è presente
            number = int(number)
            number += 1
            return JsonResponse({'number': number})
        else:
            return JsonResponse({'error': 'Numero non fornito'}, status=400)
    return JsonResponse({'error': 'Metodo non supportato'}, status=405)


def check_authentication_react(request):
    jwt_token = request.headers.get('Authorization')
    if jwt_token is None:
        return JsonResponse({'error': 'Token mancante'}, status=401)
    
    try:
        # Il token dovrebbe essere nel formato "Bearer <token>"
        token = jwt_token.split()[1]
        # Verifica e decodifica il token    
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        # Qui puoi aggiungere ulteriori controlli sul payload se necessario
        # Ad esempio, verifica dell'expiration time, dell'issuer, ecc.
        
        return JsonResponse({'message': 'Token valido', 'user_id': payload.get('user_id')}, status=200)
    except jwt.ExpiredSignatureError:
        return JsonResponse({'error': 'Token scaduto'}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({'error': 'Token non valido'}, status=401)
    except IndexError:
        return JsonResponse({'error': 'Token malformato'}, status=401)





def csrf_token_view(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


def generate_jwt_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
}


def login_react(request):
    if request.method == 'POST': 
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')


        csrf_token = request.headers.get('X-CSRFToken')
        secret_key = csrf_token[:32].encode('utf-8')
        #print(secret_key)

        #print(username)
        #print(password)

    
        
        username = decrypt(username, secret_key)
        password = decrypt(password, secret_key)
        
        if username is None or password is None:
            return JsonResponse({'error': 'Decryption failed'}, status=400)

        #print(username)
        #print(password)

        user = authenticate(username=username, password=password)


        if user is not None:
            login(request, user)  # Effettua il login dell'utente
            #generate jwt token
            tokens = generate_jwt_token(user)
            #get the user id
            user_id = user.id
            return JsonResponse({'message': 'Login successful', 'tokens': tokens, 'userid': user_id}, status=200)        
        else:
            return JsonResponse({'error': 'Username o password errati'}, status=401)

    return JsonResponse({'error': 'Metodo non supportato'}, status=405)

    

def logout_react(request):
    logout(request)
    return HttpResponse('ok')




def decrypt(encrypted_data, key):
    try:
        # Decodifica base64 e separa IV e ciphertext
        encrypted = base64.b64decode(encrypted_data)
        iv = encrypted[:16]
        ciphertext = encrypted[16:]
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted.decode('utf-8')
    except Exception as e:
        logger.exception(f"Decryption error: {str(e)}")
        return None
    

@login_required(login_url='/login/')
def load_card_react(request):

    card_block = render_to_string('other/react_card.html')

    return JsonResponse({'card_block': card_block})   

