from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Function to check if the user is an admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
 q