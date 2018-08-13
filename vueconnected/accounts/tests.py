from jwt.api_jwt import PyJWT


payload = {
    'id': 5,
    'email': 'ASDASDA'
}

key = 'secret'

jwt_Obj=PyJWT()
jwt_token = jwt_Obj.encode( payload=payload,key= key )
decode_token=jwt_Obj.decode(jwt_token,key=key)

print (jwt_token)
print(decode_token)