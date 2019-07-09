from django.shortcuts import render
from django.views.generic.list import ListView
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)

from .serializers import ContactRecordSerializer

from .models import ContactRecord

class EditContactRecordAPI(APIView):
    queryset = ContactRecord.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = ContactRecordSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                id = request.data['id']
                obj = ContactRecord.objects.get(pk=id)
                obj.firstname = serializer.validated_data['firstname']
                obj.lastname = serializer.validated_data['lastname']
                obj.email = serializer.validated_data['email']
                obj.phone_number = serializer.validated_data['phone_number']
                obj.dob = serializer.validated_data['dob']
                obj.save()
                return Response({'status': "updated"}, status=HTTP_200_OK)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'message':('Check parameters: {}').format(e)}, status=HTTP_400_BAD_REQUEST)

class AddContactRecordAPI(CreateAPIView):
    queryset = ContactRecord.objects.all()
    serializer_class = ContactRecordSerializer


class ContactRecordListView(ListView):
    model = ContactRecord