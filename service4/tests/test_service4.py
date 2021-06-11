from flask_testing import TestCase
from flask import url_for
from service4.app import app, returnresult

class TestBase(TestCase):
    def create_app(self):
        return app

class TestQuery(TestBase):
    def test_service4(self):
        response = self.client.post(url_for('returnresult'), data='a pack of firebreathing lizards,on the outskirts of a city')
        self.assert200(response)
        expected = "This encounter has been censored because of excessive silliness"
        self.assertEqual(response.data.decode('utf-8'), expected)