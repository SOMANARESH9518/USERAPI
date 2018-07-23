from rest_framework import serializers
from myapp.models import APIUser
from django.contrib.auth.models import User


class APIUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIUser
        # fields = '__all__'
        exclude = ('created_date',)
        read_only_fields = ('created_date',)
