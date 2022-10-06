from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer
# from rest_framework_simplejwt.backends import TokenBackend
# from django.conf import settings

class UserListView(views.APIView):
    def get(self, request, *args, **kwargs):
        #login
        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)