from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='rohit', password='1234rR@p')
        self.client.force_authenticate(user=self.user)

    def test_list_tasks(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, 200)

        # Add more test cases for other endpoints

    # Add more test methods for other endpoints and permissions
