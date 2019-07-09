from django.test import TestCase
from .models import ContactRecord
from django.urls import reverse_lazy
import re


class HomeTests(TestCase):
    def setUp(self):
        firstname = 'Ivan'
        lastname = 'Ivanov'
        email = 'example@admin.com'
        ContactRecord.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email
        )

    def test_list_view_content(self):
        firstname = 'Ivan'
        lastname = 'Ivanov'
        email = 'example@admin.com'
        url = reverse_lazy('list')
        response = self.client.get(url)
        decoded = response.content.decode("utf-8")
        result = [
            re.search(firstname, decoded),
            re.search(lastname, decoded),
            re.search(email, decoded),
            ]
        self.assertEquals(None in result, False)