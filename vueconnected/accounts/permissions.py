from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication,  get_authorization_header
from rest_framework import status, exceptions
from jwt.api_jwt import PyJWT
from .models import UserProfile




class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id




class CustomizedAuthentication(TokenAuthentication):


    def authenticate(self, request):
        print('sadas')

        rawToken = get_authorization_header(request)
        print(request.data)
        print(rawToken)

        key = 'secretmustbecomplex'
        jwt_Obj = PyJWT()

        if not rawToken:
            return None
        payload=jwt_Obj.decode( rawToken,key=key )
        email=payload['email']
        password=payload['password']
        try:
            user = UserProfile.objects.get(email=email,password=password)
        except UserProfile.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)