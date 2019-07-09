from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import ContactRecord


class ContactRecordSerializer(ModelSerializer):

    class Meta:
        model = ContactRecord
        # fields = '__all__'
        fields = ('firstname', 'lastname', 'phone_number', 'email', 'dob', 'pk')