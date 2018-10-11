from django.test import TestCase


class SystemTest(TestCase):

    def test_post(self):
        url = '/api/system/pdftoinvoice/'
        file1 = open("system/urls.py" , 'rb')
        file2 = open("system/views.py" , 'rb')
        response = self.client.post(url,{'files': [file1, file2]}, format='multipart')
        self.assertEqual(response.status_code, 200)
