from django.test import TestCase
import json
from rest_framework import status

class TestCalls(TestCase):

    def test_get_team_members(self):
        """
        This is to test get_field
        """
        response = self.client.get('/api/users/', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_team_members(self):
        """
        This is to test get_schedule
        :return:
        """
        input = {"id": 1, "first_name": "test1", "last_name": "last1", "email": "manjusha.y89@test.com", "is_superuser":True, "phone_number":"9022134211"}
        response = self.client.post('/api/users/', json.dumps(input), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['id'], input['id'])

