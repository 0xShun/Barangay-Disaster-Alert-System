from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Service, ServiceRequest, EmergencyHotline, ServiceRequirement, ServiceRequestRequirementUpload
from .forms import ServiceRequestForm
from users.decorators import admin_required

def service_list(request):
    """Display all available services"""
    services = Service.objects.filter(availability_status='available')
    return render(request, 'services/service_list.html', {'services': services})

@login_required
def service_detail(request, pk):
    """Display service details and allow requesting"""
    service = get_object_or_404(Service, pk=pk)
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES, service=service)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.service = service
            service_request.save()
            # Save dynamic requirement uploads/values
            for req in service.service_requirements.all():
                field_name = f"requirement_{req.id}"
                if req.requirement_type in ['file', 'photo']:
                    file = form.cleaned_data.get(field_name)
                    if file:
                        ServiceRequestRequirementUpload.objects.create(
                            request=service_request,
                            requirement=req,
                            file=file
                        )
                elif req.requirement_type == 'text':
                    value = form.cleaned_data.get(field_name)
                    if value:
                        ServiceRequestRequirementUpload.objects.create(
                            request=service_request,
                            requirement=req,
                            value=value
                        )
            messages.success(request, f'Service request submitted successfully for {service.name}')
            return redirect('services:my_requests')
    else:
        form = ServiceRequestForm(service=service)
    
    return render(request, 'services/service_detail.html', {
        'service': service,
        'form': form
    })

@method_decorator(login_required, name='dispatch')
class MyServiceRequestsListView(ListView):
    """Display user's service requests"""
    model = ServiceRequest
    template_name = 'services/my_requests.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return ServiceRequest.objects.filter(user=self.request.user)

def emergency_hotlines(request):
    """Display emergency hotlines directory"""
    hotlines = EmergencyHotline.objects.filter(is_active=True)
    categories = {}
    
    for hotline in hotlines:
        if hotline.category not in categories:
            categories[hotline.category] = []
        categories[hotline.category].append(hotline)
    
    return render(request, 'services/emergency_hotlines.html', {
        'categories': categories
    })

@admin_required
def all_service_requests(request):
    """Admin view to see all service requests"""
    requests = ServiceRequest.objects.all().order_by('-timestamp')
    return render(request, 'services/all_requests.html', {'requests': requests})

@admin_required
def update_service_request(request, pk):
    """Admin view to update service request status"""
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    uploads = service_request.uploads.select_related('requirement').all()
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(ServiceRequest.STATUS_CHOICES):
            service_request.status = new_status
            service_request.save()
            messages.success(request, f'Service request status updated to {service_request.get_status_display()}')
            return redirect('services:all_requests')
    
    return render(request, 'services/update_request.html', {'service_request': service_request, 'uploads': uploads})

@admin_required
def manage_services(request):
    """Admin view to manage services"""
    services = Service.objects.all().order_by('-created_at')
    return render(request, 'services/manage_services.html', {'services': services})

@admin_required
def admin_dashboard(request):
    from users.models import CustomUser
    from blog.models import BlogPost, Comment
    from casualty.models import CasualtyReport
    from .models import Service, ServiceRequest, EmergencyHotline

    stats = {
        'total_users': CustomUser.objects.count(),
        'total_admins': CustomUser.objects.filter(role='admin').count(),
        'total_citizens': CustomUser.objects.filter(role='citizen').count(),
        'total_blog_posts': BlogPost.objects.count(),
        'total_comments': Comment.objects.count(),
        'total_casualty_reports': CasualtyReport.objects.count(),
        'pending_casualty_reports': CasualtyReport.objects.filter(status='pending').count(),
        'verified_casualty_reports': CasualtyReport.objects.filter(status='verified').count(),
        'resolved_casualty_reports': CasualtyReport.objects.filter(status='resolved').count(),
        'total_services': Service.objects.count(),
        'total_service_requests': ServiceRequest.objects.count(),
        'pending_service_requests': ServiceRequest.objects.filter(status='pending').count(),
        'approved_service_requests': ServiceRequest.objects.filter(status='approved').count(),
        'rejected_service_requests': ServiceRequest.objects.filter(status='rejected').count(),
        'completed_service_requests': ServiceRequest.objects.filter(status='completed').count(),
        'total_hotlines': EmergencyHotline.objects.count(),
        'active_hotlines': EmergencyHotline.objects.filter(is_active=True).count(),
    }
    return render(request, 'services/admin_dashboard.html', {'stats': stats})
