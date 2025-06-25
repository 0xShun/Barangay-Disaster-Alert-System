from django.urls import path
from . import views

app_name = 'casualty'

urlpatterns = [
    path('report/', views.CasualtyReportCreateView.as_view(), name='report_form'),
    path('my-reports/', views.MyCasualtyReportsListView.as_view(), name='my_reports'),
    path('all-reports/', views.all_casualty_reports, name='all_reports'),
    path('update-report/<int:pk>/', views.update_casualty_report, name='update_report'),
] 