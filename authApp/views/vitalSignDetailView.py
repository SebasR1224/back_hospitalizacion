from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.vitalSign import VitalSign
from authApp.serializers.vitalSignSerializer import VitalSignSerializer
# from rest_framework_simplejwt.backends import TokenBackend
# from django.conf import settings

class VitalSignDetailView(views.APIView):
    def get(self, request, *args, **kwargs):
        #login
        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False)
        pk = kwargs['pk']
        vital = VitalSign.objects.get(pk=pk)
        serializer = VitalSignSerializer(vital)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        #login
        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False) 
        
        pk = kwargs['pk']
        vital = VitalSign.objects.get(pk=pk)
        vital.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        #login
        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False) 
        
        pk = kwargs['pk']
        vital = VitalSign.objects.get(pk=pk)
        serializer = VitalSignSerializer(vital, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)