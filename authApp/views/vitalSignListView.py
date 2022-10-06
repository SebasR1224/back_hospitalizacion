from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.vitalSign import VitalSign
from authApp.serializers.vitalSignSerializer import VitalSignSerializer
# from rest_framework_simplejwt.backends import TokenBackend
# from django.conf import settings

class VitalSignListView(views.APIView):
    def get(self, request, *args, **kwargs):
        #login
        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False)
        vital = VitalSign.objects.all()
        serializer = VitalSignSerializer(vital, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        #login
        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False)
        serializer = VitalSignSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)