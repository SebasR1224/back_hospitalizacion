from authApp.models.vitalSign import VitalSign
from rest_framework import serializers

class VitalSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSign
        fields = '__all__'
    
    def to_representation(self, obj):
        vital = VitalSign.objects.get(id=obj.id)
        return {
            'id': vital.id,
            'name': vital.name,
        }