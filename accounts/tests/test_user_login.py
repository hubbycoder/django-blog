from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views
from django.urls import reverse, resolve
from django.test import TestCase
    
class LoginTests(TestCase):
    def setUp(self):
        url = reverse('login')
        self.response = self.client.get(url)

    def test_login_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_register_url_resolves_login_view(self):
        view = resolve('/login/')
        self.assertEquals(view.func.view_class, auth_views.LoginView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, AuthenticationForm)

class SuccessfulLoginTests(TestCase):
    def setUp(self):
        url = reverse('login')
        self.credentials = {
            'username': 'john',
            'password': 'abcdef123456'}
        User.objects.create_user(**self.credentials)
        self.response = self.client.post(url, self.credentials, follow=True)
        self.home_url = reverse('blog-home')

    def test_redirection(self):
        '''
        A valid form submission should redirect the user to the home page
        '''
        self.assertRedirects(self.response, self.home_url)

    def test_user_authentication(self):
        '''
        Create a new request to an arbitrary page.
        The resulting response should now have a `user` to its context,
        after a successful sign up.
        '''
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)
