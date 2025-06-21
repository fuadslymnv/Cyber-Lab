import jwt
import datetime

SECRET = "MySecretKey"
payload = {
    "user": "testDevice01",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
}

token = jwt.encode(payload, SECRET, algorithm="HS256")
print(f"Generated JWT: {token}")
