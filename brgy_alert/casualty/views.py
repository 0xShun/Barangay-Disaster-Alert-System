from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import CasualtyReport
from .forms import CasualtyReportForm

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
