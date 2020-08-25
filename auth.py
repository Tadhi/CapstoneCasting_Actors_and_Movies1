import json
from flask import request, _request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen
from config import auth0_config

#AUTH0_DOMAIN,ALGORITHMS,API_AUDIENCE#

AUTH0_DOMAIN = 'capstone-tota.au.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'http://localhost:5000'

#AuthError Exception#

class AuthError(Exception):
  def __init__(self, error, status_code):
    self.error = error
    self.status_code = status_code


#Auth Header#
def get_token_auth_header():
  
#Get the authorization header from the request#
  auth_header = request.headers.get('Authorization', None)

#Auth header is missing#
  if not auth_header:
    raise AuthError({
      'code': 'authorization_header_missing',
      'description': 'Authorization header is expected.'
    }, 401)

#Split Bearer and the token from the header#
  parts = auth_header.split()
  
#Auth header did not start with "Bearer"#
  if parts[0].lower() != 'bearer':
    raise AuthError({
      'code': 'invalid_header',
      'description': 'Authorization header must start with "Bearer".'
    }, 401)

#Token was not found inside the header#
  elif len(parts) == 1:
    raise AuthError({
      'code': 'invalid_header',
      'description': 'Token not found.'
    }, 401)

#Header was not a bearer token#
  elif len(parts) > 2:
    raise AuthError({
      'code': 'invalid_header',
      'description': 'Authorization header must be bearer token.'
    }, 401)

  token = parts[1]
  return token


def check_permissions(permission, payload):
#Permissions were not found in the token#
  if 'permissions' not in payload:
    raise AuthError({
      'code': 'invalid_claims',
      'description': 'Permissions were not included in the JWT.'
    }, 400)

#Token does not support the requested permission#
  if permission not in payload['permissions']:
    raise AuthError({
      'code': 'unauthorized',
      'description': 'Permission denied.'
    }, 403)
  return True


def verify_decode_jwt(token):
  jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
  jwks = json.loads(jsonurl.read())
  unverified_header = jwt.get_unverified_header(token)
  rsa_key = {}
  if 'kid' not in unverified_header:
    raise AuthError({
      'code': 'invalid_header',
      'description': 'Authorization malformed.'
    }, 401)

  for key in jwks['keys']:
    if key['kid'] == unverified_header['kid']:
      rsa_key = {
        'kty': key['kty'],
        'kid': key['kid'],
        'use': key['use'],
        'n': key['n'],
        'e': key['e']
      }
  if rsa_key:
    try:
      payload = jwt.decode(
        token,
        rsa_key,
        algorithms=ALGORITHMS,
        audience=API_AUDIENCE,
        issuer='https://' + AUTH0_DOMAIN + '/'
      )

      return payload

    except jwt.ExpiredSignatureError:
      raise AuthError({
        'code': 'token_expired',
        'description': 'Token expired.'
      }, 401)

    except jwt.JWTClaimsError:
      raise AuthError({
        'code': 'invalid_claims',
        'description': 'Incorrect claims. Please, check the audience and issuer.'
      }, 401)
    except Exception:
      raise AuthError({
        'code': 'invalid_header',
        'description': 'Unable to parse authentication token.'
      }, 400)
  raise AuthError({
    'code': 'invalid_header',
    'description': 'Unable to find the appropriate key.'
  }, 400)


def requires_auth(permission=''):
  def requires_auth_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
#Get the token from the auth header#
      token = get_token_auth_header()
#Decode the token#
      decoded_payload = verify_decode_jwt(token)

#Check if the token's permissions contain the requested permission#
      check_permissions(permission, decoded_payload)

      return f(decoded_payload, *args, **kwargs)

    return wrapper
  return requires_auth_decorator