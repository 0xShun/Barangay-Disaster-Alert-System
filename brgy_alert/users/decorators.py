from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from functools import wraps

def admin_required(view_func):
    """
    Decorator to check if user is an admin.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in to access this page.')
            return redirect('users:login')
        
        if request.user.role != 'admin':
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('home')
        
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def citizen_required(view_func):
    """
    Decorator to check if user is a citizen.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in to access this page.')
            return redirect('users:login')
        
        if request.user.role != 'citizen':
            messages.error(request, 'This page is for citizens only.')
            return redirect('home')
        
        return view_func(request, *args, **kwargs)
    return _wrapped_view 