from rest_framework import serializers
from .models import Adviser
class AdviserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Adviser
        fields = '__all__'