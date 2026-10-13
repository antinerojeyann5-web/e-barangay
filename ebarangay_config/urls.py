from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from residents import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),           # Welcome page is now the first page
    path('directory/', views.home, name='home'),       # Resident Directory moved here
    path('add/', views.add_resident, name='add_resident'),
    path('edit/<int:resident_id>/', views.edit_resident, name='edit_resident'),
    path('delete/<int:resident_id>/', views.delete_resident, name='delete_resident'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.resident_dashboard, name='resident_dashboard'),
    path('request/', views.request_document, name='request_document'),
    path('complaint/', views.submit_complaint, name='submit_complaint'),
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('guide/', views.guide_list, name='guide_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='welcome'), name='logout'),
]