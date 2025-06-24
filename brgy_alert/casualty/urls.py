from django.urls import path
from .views import CasualtyReportCreateView, MyCasualtyReportsListView

app_name = 'casualty'

urlpatterns = [
    path('report/', CasualtyReportCreateView.as_view(), name='report'),
    path('my-reports/', MyCasualtyReportsListView.as_view(), name='my_reports'),
] 