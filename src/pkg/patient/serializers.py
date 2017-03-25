from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.transaction import atomic

from rest_framework import serializers

from pkg.patient.models import Patient
from pkg.patient.services import PatientService
from pkg.diagnose.serializers import DiagnoseSerializer

User = get_user_model()


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'email')


class FullPatientSerializer(serializers.ModelSerializer):
    diagnoses = DiagnoseSerializer(many=True)

    class Meta:
        model = Patient
        fields = (
            'id', 'first_name', 'last_name', 'birthday', 'email',
            'blood_type', 'diagnoses',
        )


class PatientRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'password_confirm', 'first_name',
                  'last_name')

    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    default_error_messages = {
        'password_mismatch': 'The two password fields didn\'t match.',
        'user_exists': 'user with this E-mail already exists.'
    }

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')

        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError({
                'password': e
            })

        if password != password_confirm:
            raise serializers.ValidationError({
                'password_confirm': self.error_messages['password_mismatch']
            })

        return super().validate(attrs)

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise ValidationError(self.error_messages['user_exists'])
        return value.lower()

    @atomic()
    def create(self, validated_data):

        email = validated_data.get('email')
        password = validated_data.get('password')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        user = PatientService.register(email, password, first_name, last_name)
        return user
