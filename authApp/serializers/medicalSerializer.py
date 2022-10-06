from authApp.models.user import User
from authApp.models.medical import Medical
from rest_framework import serializers

class MedicalSerializer(serializers.ModelSerializer):

    specialty = serializers.CharField(max_length=100)
    registration = serializers.CharField( max_length=255)
    role = serializers.IntegerField(default=1)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'name', 'lastName', 'phone', 'gender', 'role', 'specialty', 'registration']

    def create(self, validate_data):
        validate_data['role'] = 1
        specialtyData = validate_data.pop('specialty')
        registrationData = validate_data.pop('registration')

        userInstance = User.objects.create(**validate_data)
        Medical.objects.create(user=userInstance, specialty=specialtyData, registration=registrationData)
        
        return userInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        medical = Medical.objects.get(user= obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'name': user.name,
            'lastName': user.lastName,
            'phone': user.phone,
            'gender': user.gender,
            'role': user.role,
            'specialty': medical.specialty,
            'registration': medical.registration
        }