from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import CasualtyReport
from .forms import CasualtyReportForm
from users.decorators import admin_required

# Create your views here.

@method_decorator(login_required, name='dispatch')
class CasualtyReportCreateView(CreateView):
    model = CasualtyReport
    form_class = CasualtyReportForm
    template_name = 'casualty/report_form.html'
    success_url = reverse_lazy('casualty:my_reports')

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class MyCasualtyReportsListView(ListView):
    model = CasualtyReport
    template_name = 'casualty/my_reports.html'
    context_object_name = 'reports'

    def get_queryset(self):
        return CasualtyReport.objects.filter(reporter=self.request.user)

@admin_required
def all_casualty_reports(request):
    """Admin view to see all casualty reports"""
    reports = CasualtyReport.objects.all().order_by('-timestamp')
    return render(request, 'casualty/all_reports.html', {'reports': reports})

@admin_required
def update_casualty_report(request, pk):
    """Admin view to update casualty report status"""
    report = get_object_or_404(CasualtyReport, pk=pk)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(CasualtyReport.STATUS_CHOICES):
            report.status = new_status
            report.save()
            messages.success(request, f'Report status updated to {report.get_status_display()}')
            return redirect('casualty:all_reports')
    
    return render(request, 'casualty/update_report.html', {'report': report})
