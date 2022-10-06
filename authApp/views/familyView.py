from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.user import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.familySerializer import FamilySerializer
# from rest_framework_simplejwt.backends import TokenBackend
# from django.conf import settings
class FamilyView(views.APIView):

      def get(self, request, *args, **kwargs): 

         #login
         # token = request.META.get('HTTP_AUTHORIZATION')[7:]
         # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
         # valid_data = tokenBackend.decode(token,verify=False)
         family = User.objects.filter(role=2)
         serializer = FamilySerializer(family, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)
    
      def post(self, request, *args, **kwargs):
         #login
         # token = request.META.get('HTTP_AUTHORIZATION')[7:]
         # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
         # valid_data = tokenBackend.decode(token,verify=False)
         serializer = FamilySerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         tokenData = {"username":request.data["username"], "password":request.data["password"]}

         tokenSerializer = TokenObtainPairSerializer(data=tokenData)
         tokenSerializer.is_valid(raise_exception=True)
         
         return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)