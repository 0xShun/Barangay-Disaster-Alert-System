from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from services.models import Service, EmergencyHotline
from blog.models import BlogPost
from django.utils import timezone

User = get_user_model()

class Command(BaseCommand):
    help = 'Load sample data for testing the Barangay Alert Hub'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')
        
        # Create sample services
        services_data = [
            {
                'name': 'Barangay Clearance',
                'description': 'Official clearance certificate required for various transactions.',
                'requirements': 'Valid ID, Proof of residency, Payment of fees',
                'availability_status': 'available'
            },
            {
                'name': 'Indigency Certificate',
                'description': 'Certificate for indigent residents to avail of government assistance.',
                'requirements': 'Valid ID, Proof of income, Proof of residency',
                'availability_status': 'available'
            },
            {
                'name': 'Business Permit',
                'description': 'Permit required for operating businesses within the barangay.',
                'requirements': 'Business registration, Location clearance, Payment of fees',
                'availability_status': 'available'
            },
            {
                'name': 'Community Service',
                'description': 'Volunteer opportunities for community development projects.',
                'requirements': 'Willingness to serve, Available time, Good health',
                'availability_status': 'available'
            }
        ]
        
        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                name=service_data['name'],
                defaults=service_data
            )
            if created:
                self.stdout.write(f'Created service: {service.name}')
        
        # Create sample emergency hotlines
        hotlines_data = [
            {
                'agency_name': 'Philippine National Police',
                'number': '911',
                'description': 'Emergency hotline for police assistance',
                'category': 'Police'
            },
            {
                'agency_name': 'Bureau of Fire Protection',
                'number': '160',
                'description': 'Fire emergency and rescue services',
                'category': 'Fire'
            },
            {
                'agency_name': 'Philippine Red Cross',
                'number': '143',
                'description': 'Emergency medical services and disaster response',
                'category': 'Medical'
            },
            {
                'agency_name': 'Department of Health',
                'number': '1555',
                'description': 'Health information and medical assistance',
                'category': 'Medical'
            },
            {
                'agency_name': 'Metro Manila Development Authority',
                'number': '136',
                'description': 'Traffic management and road assistance',
                'category': 'Traffic'
            },
            {
                'agency_name': 'National Emergency Hotline',
                'number': '911',
                'description': 'General emergency hotline',
                'category': 'General'
            }
        ]
        
        for hotline_data in hotlines_data:
            hotline, created = EmergencyHotline.objects.get_or_create(
                agency_name=hotline_data['agency_name'],
                number=hotline_data['number'],
                defaults=hotline_data
            )
            if created:
                self.stdout.write(f'Created hotline: {hotline.agency_name}')
        
        # Create sample blog posts if admin user exists
        try:
            admin_user = User.objects.get(username='admin')
            
            blog_posts_data = [
                {
                    'title': 'Welcome to Barangay Alert Hub',
                    'content': 'Welcome to our new online platform for disaster preparedness and emergency response. This system will help us serve you better during emergencies and provide easy access to barangay services.',
                    'author': admin_user,
                    'is_published': True
                },
                {
                    'title': 'Emergency Preparedness Tips',
                    'content': 'Always keep an emergency kit ready with essential items like water, food, first aid supplies, and important documents. Know your evacuation routes and emergency contact numbers.',
                    'author': admin_user,
                    'is_published': True
                },
                {
                    'title': 'New Barangay Services Available',
                    'content': 'We are pleased to announce new online services including barangay clearance applications, indigency certificates, and business permits. Visit our services section to learn more.',
                    'author': admin_user,
                    'is_published': True
                }
            ]
            
            for post_data in blog_posts_data:
                post, created = BlogPost.objects.get_or_create(
                    title=post_data['title'],
                    defaults=post_data
                )
                if created:
                    self.stdout.write(f'Created blog post: {post.title}')
                    
        except User.DoesNotExist:
            self.stdout.write('Admin user not found. Skipping blog posts creation.')
        
        self.stdout.write(self.style.SUCCESS('Sample data loaded successfully!')) 