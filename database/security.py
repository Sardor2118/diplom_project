import jwt
from datetime import datetime, timedelta

SECRET_KEY = '<Ksmqwjf@nxjfnlks412ndiljrqlk>'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 300

# наша JWT тут создает токен
def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({expire: expire.isoformat()})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


# проверка токена
def verify_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        return "Error"
