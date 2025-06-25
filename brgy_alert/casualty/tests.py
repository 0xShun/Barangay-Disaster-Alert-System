from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CasualtyReport
from .forms import CasualtyReportForm

User = get_user_model()

class CasualtyModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.casualty_report = CasualtyReport.objects.create(
            reporter=self.user,
            victim_name='John Doe',
            contact_info='123-456-7890',
            condition='Minor injuries',
            location='123 Main St',
            status='pending'
        )

    def test_casualty_report_creation(self):
        self.assertEqual(self.casualty_report.victim_name, 'John Doe')
        self.assertEqual(self.casualty_report.contact_info, '123-456-7890')
        self.assertEqual(self.casualty_report.condition, 'Minor injuries')
        self.assertEqual(self.casualty_report.location, '123 Main St')
        self.assertEqual(self.casualty_report.status, 'pending')
        self.assertEqual(self.casualty_report.reporter, self.user)

    def test_casualty_report_str_representation(self):
        expected_str = f"John Doe (pending)"
        self.assertEqual(str(self.casualty_report), expected_str)

    def test_casualty_report_status_choices(self):
        self.assertIn(('pending', 'Pending'), CasualtyReport.STATUS_CHOICES)
        self.assertIn(('verified', 'Verified'), CasualtyReport.STATUS_CHOICES)
        self.assertIn(('resolved', 'Resolved'), CasualtyReport.STATUS_CHOICES)

class CasualtyFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_casualty_report_form_valid(self):
        form_data = {
            'victim_name': 'Jane Doe',
            'contact_info': '098-765-4321',
            'condition': 'Serious injuries',
            'location': '456 Oak Ave'
        }
        form = CasualtyReportForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_casualty_report_form_invalid(self):
        form_data = {
            'victim_name': '',  # Required field
            'contact_info': '098-765-4321',
            'condition': 'Serious injuries',
            'location': '456 Oak Ave'
        }
        form = CasualtyReportForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('victim_name', form.errors)

class CasualtyViewsTest(TestCase):
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
        self.casualty_report = CasualtyReport.objects.create(
            reporter=self.user,
            victim_name='John Doe',
            contact_info='123-456-7890',
            condition='Minor injuries',
            location='123 Main St',
            status='pending'
        )

    def test_casualty_report_create_view_get_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('casualty:report_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'casualty/report_form.html')

    def test_casualty_report_create_view_get_unauthenticated(self):
        response = self.client.get(reverse('casualty:report_form'))
        self.assertRedirects(response, f"{reverse('users:login')}?next={reverse('casualty:report_form')}")

    def test_casualty_report_create_view_post(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('casualty:report_form'), {
            'victim_name': 'Jane Doe',
            'contact_info': '098-765-4321',
            'condition': 'Serious injuries',
            'location': '456 Oak Ave'
        })
        self.assertRedirects(response, reverse('casualty:my_reports'))
        self.assertTrue(CasualtyReport.objects.filter(victim_name='Jane Doe').exists())

    def test_my_casualty_reports_view_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('casualty:my_reports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'casualty/my_reports.html')
        self.assertContains(response, 'John Doe')

    def test_my_casualty_reports_view_unauthenticated(self):
        response = self.client.get(reverse('casualty:my_reports'))
        self.assertRedirects(response, f"{reverse('users:login')}?next={reverse('casualty:my_reports')}")

    def test_all_casualty_reports_view_admin(self):
        self.client.login(username='adminuser', password='adminpass123')
        response = self.client.get(reverse('casualty:all_reports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'casualty/all_reports.html')
        self.assertContains(response, 'John Doe')

    def test_all_casualty_reports_view_non_admin(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('casualty:all_reports'))
        self.assertRedirects(response, reverse('home'))

    def test_update_casualty_report_view_admin(self):
        self.client.login(username='adminuser', password='adminpass123')
        response = self.client.get(reverse('casualty:update_report', kwargs={'pk': self.casualty_report.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'casualty/update_report.html')

    def test_update_casualty_report_view_post(self):
        self.client.login(username='adminuser', password='adminpass123')
        response = self.client.post(reverse('casualty:update_report', kwargs={'pk': self.casualty_report.pk}), {
            'status': 'verified'
        })
        self.assertRedirects(response, reverse('casualty:all_reports'))
        self.casualty_report.refresh_from_db()
        self.assertEqual(self.casualty_report.status, 'verified')
