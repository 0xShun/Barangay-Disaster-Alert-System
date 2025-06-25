from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Service, ServiceRequest, EmergencyHotline
from .forms import ServiceRequestForm

User = get_user_model()

class ServiceModelTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            name='Test Service',
            description='This is a test service description.',
            requirements='Valid ID, Proof of residency',
            availability_status='available'
        )

    def test_service_creation(self):
        self.assertEqual(self.service.name, 'Test Service')
        self.assertEqual(self.service.description, 'This is a test service description.')
        self.assertEqual(self.service.requirements, 'Valid ID, Proof of residency')
        self.assertEqual(self.service.availability_status, 'available')

    def test_service_str_representation(self):
        self.assertEqual(str(self.service), 'Test Service')

    def test_service_availability_choices(self):
        self.assertIn(('available', 'Available'), Service.AVAILABILITY_CHOICES)
        self.assertIn(('unavailable', 'Unavailable'), Service.AVAILABILITY_CHOICES)

class ServiceRequestModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.service = Service.objects.create(
            name='Test Service',
            description='This is a test service description.',
            requirements='Valid ID, Proof of residency',
            availability_status='available'
        )
        self.service_request = ServiceRequest.objects.create(
            user=self.user,
            service=self.service,
            reason='I need this service for official purposes.',
            status='pending'
        )

    def test_service_request_creation(self):
        self.assertEqual(self.service_request.user, self.user)
        self.assertEqual(self.service_request.service, self.service)
        self.assertEqual(self.service_request.reason, 'I need this service for official purposes.')
        self.assertEqual(self.service_request.status, 'pending')

    def test_service_request_str_representation(self):
        expected_str = f"testuser - Test Service (pending)"
        self.assertEqual(str(self.service_request), expected_str)

    def test_service_request_status_choices(self):
        self.assertIn(('pending', 'Pending'), ServiceRequest.STATUS_CHOICES)
        self.assertIn(('approved', 'Approved'), ServiceRequest.STATUS_CHOICES)
        self.assertIn(('rejected', 'Rejected'), ServiceRequest.STATUS_CHOICES)
        self.assertIn(('completed', 'Completed'), ServiceRequest.STATUS_CHOICES)

class EmergencyHotlineModelTest(TestCase):
    def setUp(self):
        self.hotline = EmergencyHotline.objects.create(
            agency_name='Test Agency',
            number='123-456-7890',
            description='Test emergency hotline',
            category='General',
            is_active=True
        )

    def test_emergency_hotline_creation(self):
        self.assertEqual(self.hotline.agency_name, 'Test Agency')
        self.assertEqual(self.hotline.number, '123-456-7890')
        self.assertEqual(self.hotline.description, 'Test emergency hotline')
        self.assertEqual(self.hotline.category, 'General')
        self.assertTrue(self.hotline.is_active)

    def test_emergency_hotline_str_representation(self):
        expected_str = f"Test Agency - 123-456-7890"
        self.assertEqual(str(self.hotline), expected_str)

class ServiceFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_service_request_form_valid(self):
        form_data = {
            'reason': 'I need this service for official purposes.'
        }
        form = ServiceRequestForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_service_request_form_invalid(self):
        form_data = {
            'reason': ''  # Required field
        }
        form = ServiceRequestForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('reason', form.errors)

class ServiceViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.admin_user = User.objects.create_user(
            username='adminuser',
            email='admin@example.com',
            password='adminpass123',
            role='admin'
        )
        self.service = Service.objects.create(
            name='Test Service',
            description='This is a test service description.',
            requirements='Valid ID, Proof of residency',
            availability_status='available'
        )
        self.service_request = ServiceRequest.objects.create(
            user=self.user,
            service=self.service,
            reason='I need this service for official purposes.',
            status='pending'
        )

    def test_service_list_view(self):
        response = self.client.get(reverse('services:service_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/service_list.html')
        self.assertContains(response, 'Test Service')

    def test_service_detail_view_get(self):
        # Unauthenticated user should be redirected to login
        response = self.client.get(reverse('services:service_detail', kwargs={'pk': self.service.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('users:login'), response.url)

        # Authenticated user should get 200
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('services:service_detail', kwargs={'pk': self.service.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/service_detail.html')
        self.assertContains(response, 'Test Service')

    def test_service_detail_view_post_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('services:service_detail', kwargs={'pk': self.service.pk}), {
            'reason': 'I need this service for official purposes.'
        })
        self.assertRedirects(response, reverse('services:my_requests'))

    def test_service_detail_view_post_unauthenticated(self):
        response = self.client.post(reverse('services:service_detail', kwargs={'pk': self.service.pk}), {
            'reason': 'I need this service for official purposes.'
        })
        self.assertRedirects(response, f"{reverse('users:login')}?next={reverse('services:service_detail', kwargs={'pk': self.service.pk})}")

    def test_my_service_requests_view_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('services:my_requests'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/my_requests.html')

    def test_my_service_requests_view_unauthenticated(self):
        response = self.client.get(reverse('services:my_requests'))
        self.assertRedirects(response, f"{reverse('users:login')}?next={reverse('services:my_requests')}")

    def test_emergency_hotlines_view(self):
        response = self.client.get(reverse('services:emergency_hotlines'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/emergency_hotlines.html')

    def test_all_service_requests_view_admin(self):
        self.client.login(username='adminuser', password='adminpass123')
        response = self.client.get(reverse('services:all_requests'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/all_requests.html')

    def test_all_service_requests_view_non_admin(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('services:all_requests'))
        self.assertRedirects(response, reverse('home'))

    def test_update_service_request_view_admin(self):
        self.client.login(username='adminuser', password='adminpass123')
        response = self.client.get(reverse('services:update_request', kwargs={'pk': self.service_request.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/update_request.html')

    def test_update_service_request_view_post(self):
        self.client.login(username='adminuser', password='adminpass123')
        response = self.client.post(reverse('services:update_request', kwargs={'pk': self.service_request.pk}), {
            'status': 'approved'
        })
        self.assertRedirects(response, reverse('services:all_requests'))
        self.service_request.refresh_from_db()
        self.assertEqual(self.service_request.status, 'approved')

    def test_manage_services_view_admin(self):
        self.client.login(username='adminuser', password='adminpass123')
        response = self.client.get(reverse('services:manage_services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/manage_services.html')
        self.assertContains(response, 'Test Service')
