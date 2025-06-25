from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('<int:pk>/', views.service_detail, name='service_detail'),
    path('my-requests/', views.MyServiceRequestsListView.as_view(), name='my_requests'),
    path('hotlines/', views.emergency_hotlines, name='emergency_hotlines'),
    # Admin views
    path('admin/all-requests/', views.all_service_requests, name='all_requests'),
    path('admin/update-request/<int:pk>/', views.update_service_request, name='update_request'),
    path('admin/manage-services/', views.manage_services, name='manage_services'),
] 