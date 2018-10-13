from django.test import TestCase
import json
from django.utils.encoding import smart_str

class SystemTest(TestCase):

    def test_post_1(self):
        url = '/api/system/pdftoinvoice/'
        file = open("system/test.zip", 'rb')
        response = self.client.post(url, {'file': file}, format='multipart')
        self.assertEqual(response.status_code, 200)

    def test_post_2(self):
        url = '/api/system/bi/'
        file = open("system/test.zip", 'rb')
        response = self.client.post(url, {'file': file}, format='multipart')
        self.assertEqual(response.status_code, 200)

    def test_post_3(self):
        url = '/api/system/frontend/'
        file = open("system/test.zip", 'rb')
        response = self.client.post(url, {'file': file}, format='multipart')
        self.assertEqual(response.status_code,  200)

    def test_post_4(self):
        url = '/api/system/management/'
        file = open("system/test.zip", 'rb')
        response = self.client.post(url, {'file': file}, format='multipart')
        self.assertEqual(response.status_code,  200)

    def test_version(self):
        url = '/api/system/management/'
        file = open("system/test.zip", 'rb')
        response = self.client.post(url, {'file': file}, format='multipart')
        self.assertEqual(json.loads(response.content)[1]['version'], 1)
        url = '/api/system/frontend/'
        file = open("system/test.zip", 'rb')
        response = self.client.post(url, {'file': file}, format='multipart')
        self.assertEqual(json.loads(response.content)[1]['version'], 2)

    def test_get_4(self):
        url = '/api/system/pdftoinvoice/'
        file = open("system/test.zip", 'rb')
        response = self.client.post(url, {'file': file}, format='multipart')
        url = '/api/system/bi/'
        file = open("system/test.zip",  'rb')
        response = self.client.post(url, {'file': file}, format='multipart')
        url = '/api/system/frontend/'
        file = open("system/test.zip", 'rb')
        response = self.client.post(url, {'file': file}, format='multipart')
        url = '/api/system/management/'
        file = open("system/test.zip", 'rb')
        response = self.client.post(url, {'file': file}, format='multipart')
        url = '/api/system/zip/'
        response = self.client.get(url)
        self.assertNotEquals(response.content, b'')
        url = '/api/system/version/'
        response = self.client.get(url)
        self.assertEquals(json.loads(response.content)['version'], 4)
