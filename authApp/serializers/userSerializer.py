from authApp.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        match user.role:
            case 1:
                role = "Medico"
            case 2:
                role = "Familiar"
            case 3:
                role = "Paciente"
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'name': user.name,
            'lastName': user.lastName,
            'phone': user.phone,
            'gender': user.gender,
            'role': role
        }