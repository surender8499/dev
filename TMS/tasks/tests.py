from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task


class YourAppTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_login_view(self):
        response = self.client.get(reverse('my-login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my-login.html')

    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_create_task_view(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('create-task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/create-task.html')


    def test_view_task_view(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('view-tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/view-tasks.html')


    def test_update_task_view(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        task = Task.objects.create(user=user, description='Test Task')

        response = self.client.get(reverse('update-task', args=[task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/update-task.html')


    def test_delete_task_view(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        task = Task.objects.create(user=user, description='Test Task')

        response = self.client.get(reverse('delete-task', args=[task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/delete-task.html')


    def test_user_logout_view(self):
        response = self.client.get(reverse('user-logout'))
        self.assertEqual(response.status_code, 302)
