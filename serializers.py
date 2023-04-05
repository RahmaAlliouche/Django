from rest_framework.serializers import ModelSerializer
from .models import Medecine
from .models import Rapport
from .models import Patient
from rest_framework import serializers


class MedecineSerializers(serializers.ModelSerializer):
    class Meta:
        model= Medecine
        fields = ['email','password']


class PatientSerializers(ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'

class RapportSerializers(ModelSerializer):
    class Meta:
        model=Rapport
        fields='__all__'