"""model serializer"""
from rest_framework import serializers
from testapi.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    """serializer for models"""

    class Meta:
        """meta class for model fields"""
        model = Contact
        fields = ('id', 'name', 'email', 'address')


