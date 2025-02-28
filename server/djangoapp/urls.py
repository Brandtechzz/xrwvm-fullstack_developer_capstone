# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView

app_name = 'djangoapp'
urlpatterns = [
    # path for registration (if needed)

    # API endpoint for login
    path('login-api/', views.login_user, name='login_api'),
    
    # Route to render the React app for login
    path('login/', TemplateView.as_view(template_name="index.html"), name='login_page'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
