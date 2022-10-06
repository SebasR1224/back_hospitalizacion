from authApp.models.user import User
from authApp.models.family import Family
from rest_framework import serializers

class FamilySerializer(serializers.ModelSerializer):

    relationship = serializers.CharField(max_length=50)
    role = serializers.IntegerField(default=2)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'name', 'lastName', 'phone', 'gender', 'role', 'relationship']

    def create(self, validate_data):
        validate_data['role'] = 2
        relationshipData = validate_data.pop('relationship')

        userInstance = User.objects.create(**validate_data)
        Family.objects.create(user=userInstance, relationship=relationshipData)
        
        return userInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        family = Family.objects.get(user= obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'name': user.name,
            'lastName': user.lastName,
            'phone': user.phone,
            'gender': user.gender,
            'role': user.role,
            'relationship': family.relationship,
        }