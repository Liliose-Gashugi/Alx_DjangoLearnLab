"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import list_books
urlpatterns = [
    path('admin/', admin.site.urls),
]

from relationship_app.views import list_books, LibraryDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]






from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('register/', views.register, name='register'), ,
]


from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-only/', admin_view, name='admin_view'),
    path('librarian-only/', librarian_view, name='librarian_view'),
    path('member-only/', member_view, name='member_view'),
]




