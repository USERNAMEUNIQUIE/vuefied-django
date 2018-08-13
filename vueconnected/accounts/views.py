from rest_framework.views import APIView
from rest_framework import  viewsets
from rest_framework.response import Response
from . import  serializers

from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
import json
from . import  permissions
from jwt.api_jwt import PyJWT


from . import  models




class Userprofileviewsset(viewsets.ModelViewSet):


    serializer_class = serializers.UserprofilesSearializers

    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes =  (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields= ('name','email',)


class Loginviewset(APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")

        email = request.data['email']
        password = request.data['password']
        print(email,password)

        user = models.UserProfile.objects.get(email=email)


        payload = {
                'email': user.email,
                'password': user.password
            }
        key = 'secretmustbecomplex'
        jwt_Obj = PyJWT()

        jwt_token = {'token': jwt_Obj.encode( payload=payload,key=key )}


        return Response(
            jwt_token

             )
