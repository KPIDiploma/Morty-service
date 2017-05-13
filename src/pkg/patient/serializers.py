from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.transaction import atomic

from rest_framework import serializers

from src.pkg.patient.models import Patient, Doctor
from src.pkg.patient.services import PatientService
from src.pkg.diagnose.serializers import DiagnoseForPatientSerializer


User = get_user_model()

__all__ = [
    'PatientSerializer', 'FullPatientSerializer',
    'PatientCurrentUserSerializer',
    'PatientRegisterSerializer', 'PatientUpdatePasswordSerializer'
]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'fullname')


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'fullname')


class FullPatientSerializer(serializers.ModelSerializer):
    doctors = DoctorSerializer(many=True)
    diagnoses = DiagnoseForPatientSerializer(many=True)

    class Meta:
        model = Patient
        fields = (
            'id', 'email', 'fullname', 'birthday', 'address',
            'mobile', 'sex', 'blood_type', 'doctors', 'status',
            'diagnoses'
        )


class PatientCurrentUserSerializer(serializers.ModelSerializer):
    diagnoses = DiagnoseForPatientSerializer(many=True)

    class Meta:
        model = Patient
        fields = (
            'diagnoses',
        )


class PatientRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'fullname', 'birthday', 'address',
            'mobile', 'sex', 'blood_type'
        )

    default_error_messages = {
        'password_mismatch': 'The two password fields didn\'t match.',
        'user_exists': 'user with this E-mail already exists.'
    }

    def validate(self, attrs):
        birthday = attrs.get('birthday')

        try:
            if datetime.now().date() < birthday:
                raise ValidationError('Birthday is not correct')
        except ValidationError as e:
            raise serializers.ValidationError({
                'Field invalid': e
            })
        except Exception as e:
            raise serializers.ValidationError({
                'invalid': e
            })
        return super().validate(attrs)

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise ValidationError(self.error_messages['user_exists'])
        return value.lower()

    @atomic()
    def create(self, validated_data):

        email = validated_data.get('email')
        password = Patient.objects.make_random_password()
        fullname = validated_data.get('fullname')
        birthday = validated_data.get('birthday')

        user = PatientService.register(email, password, validated_data)
        return user


class PatientUpdatePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    new_password_confirm = serializers.CharField(write_only=True)
    email = serializers.EmailField()

    default_error_messages = {
        'wrong_password': 'Wrong old password.',
        'password_mismatch': 'The two password fields didn\'t match.'
    }

    def validate(self, attrs):
        user = authenticate(username=attrs.get('email'),
                            password=attrs.get('old_password'))
        if user is None:
            raise serializers.ValidationError({
                'old_password': self.error_messages['wrong_password']
            })

        new_password = attrs.get('new_password')
        try:
            validate_password(new_password)
        except ValidationError as e:
            raise serializers.ValidationError({
                'new_password': e
            })

        if new_password != attrs.get('new_password_confirm'):
            raise serializers.ValidationError({
                'new_password_confirm': self.error_messages[
                    'password_mismatch']
            })

        user.set_password(new_password)
        user.save()
        return attrs
