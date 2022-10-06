from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.user import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.patientSerializer import PatientSerializer

# from rest_framework_simplejwt.backends import TokenBackend
# from django.conf import settings

class PatientView(views.APIView):
      def get(self, request, *args, **kwargs): 
         #login
         # token = request.META.get('HTTP_AUTHORIZATION')[7:]
         # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
         # valid_data = tokenBackend.decode(token,verify=False)
         patients = User.objects.filter(role=3)
         serializer = PatientSerializer(patients, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)

      def post(self, request, *args, **kwargs):
         #login
         # token = request.META.get('HTTP_AUTHORIZATION')[7:]
         # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
         # valid_data = tokenBackend.decode(token,verify=False)
         serializer = PatientSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         tokenData = {"username":request.data["username"], "password":request.data["password"]}

         tokenSerializer = TokenObtainPairSerializer(data=tokenData)
         tokenSerializer.is_valid(raise_exception=True)
         
         return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)