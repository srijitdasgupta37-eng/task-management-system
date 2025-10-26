from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User


# Create your views here.
@login_required
def dashboard(request):
    if request.user.role == 'Admin':
        return render(request, 'accounts/admin_dashboard.html')
    elif request.user.role == 'Teacher':
        return render(request, 'accounts/teacher_dashboard.html')
    elif request.user.role == 'Student':
        return render(request, 'accounts/student_dashboard.html')