from authApp.models.user import User
from authApp.models.patient import Patient
from authApp.models.family import Family
from authApp.models.medical import Medical
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):

    direction = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=50)
    dateOfBirth = serializers.DateField()
    latitude = serializers.CharField(max_length=50,  allow_blank=True)
    length =  serializers.CharField(max_length=50,  allow_blank=True)
    family_id = serializers.IntegerField()
    medical_id = serializers.IntegerField()
    role = serializers.IntegerField(default=3)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'name', 'lastName', 'phone', 'gender', 'role', 'direction', 'city', 'dateOfBirth', 'latitude', 'length', 'family_id', 'medical_id']

    def create(self, validate_data):

        validate_data['role'] = 3
        directionData = validate_data.pop('direction')
        cityData = validate_data.pop('city')
        dateOfBirthData = validate_data.pop('dateOfBirth')
        latitudeData = validate_data.pop('latitude')
        lengthData = validate_data.pop('length')
        familyIdData = validate_data.pop('family_id')
        medicalIdData = validate_data.pop('medical_id')

        userInstance = User.objects.create(**validate_data)
        familyInstance = User.objects.get(id=familyIdData)
        medicalInstance = User.objects.get(id=medicalIdData)
        Patient.objects.create(user=userInstance, direction=directionData, city=cityData, dateOfBirth=dateOfBirthData, latitude=latitudeData, length=lengthData, family=familyInstance, medical=medicalInstance)
        
        return userInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        patient = Patient.objects.get(user= obj.id)

        family = User.objects.get(id=patient.family_id)
        familyDetail = Family.objects.get(user_id=patient.family_id)

        medical = User.objects.get(id=patient.medical_id)
        medicalDetail = Medical.objects.get(user_id=patient.medical_id)

        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'name': user.name,
            'lastName': user.lastName,
            'phone': user.phone,
            'gender': user.gender,
            'role': user.role,
            'direction': patient.direction,
            'city': patient.city,
            'dateOfBirth': patient.dateOfBirth,
            'latitude': patient.latitude,
            'length': patient.length,
            'family': {
                    'name': family.name,
                    'lastName': family.lastName,
                    'email': family.email,
                    'email': family.email,
                    'phone': family.phone,
                    'relationship': familyDetail.relationship
            },
            'medical': {
                'name': medical.name,
                'lastName': medical.lastName,
                'email': medical.email,
                'email': medical.email,
                'phone': medical.phone,
                'specialty': medicalDetail.specialty
            },
            'family_id': patient.family_id,
            'medical_id': patient.medical_id
        }