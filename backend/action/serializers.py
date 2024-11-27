from rest_framework import serializers
from .models import Action

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['id', 'employee', 'measure', 'date_taken', 'points_awarded']