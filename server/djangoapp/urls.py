# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView
from .views import get_cars

app_name = 'djangoapp'
urlpatterns = [
    # API endpoint for login
    path('login-api/', views.login_user, name='login_api'),
    
    # Route to render the React app for login
    path('login/', TemplateView.as_view(template_name="index.html"), name='login_page'),

    # API endpoint for logout
    path('logout/', views.logout_request, name='logout_api'),

    # API endpoint for registration
    path('register/', views.registration, name='registration_api'),

    path(route='get_cars', view=views.get_cars, name ='getcars'),
    
    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

