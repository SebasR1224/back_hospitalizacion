from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.user import User
from authApp.serializers.medicalSerializer import MedicalSerializer
# from rest_framework_simplejwt.backends import TokenBackend
# from django.conf import settings

class MedicalDetailView(views.APIView):
    def get(self, request, *args, **kwargs):
        #login
        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False)
        pk = kwargs['pk']
        medical = User.objects.get(pk=pk)
        serializer = MedicalSerializer(medical)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        #login
        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False) 
        
        pk = kwargs['pk']
        medical = User.objects.get(pk=pk)
        medical.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        #login
        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False) 
        
        pk = kwargs['pk']
        medical = User.objects.get(pk=pk)
        serializer = MedicalSerializer(medical, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)