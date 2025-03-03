# Uncomment the imports before you add the code
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path to register
    path('register/', TemplateView.as_view(template_name="index.html"), name='register_template'),
    
    # path for registration
    path('api/register/', views.registration, name='registration_api'),

    # path for login view
    path('login/', TemplateView.as_view(template_name="index.html")),

    # path for logout view
    path('logout/', TemplateView.as_view(template_name="index.html")),

    # Path for login user API
    path('api/login/', views.login_user, name='login_user'),  # API endpoint for login

    # path for get_cars
    path(route='get_cars', view=views.get_cars, name ='getcars'),

    # path to get dealerships
    path('get_dealers/', views.get_dealerships, name='get_dealers'),  # Route for all dealerships
    path('get_dealers/<str:state>/', views.get_dealerships, name='get_dealers_by_state'),  # Route for dealerships

    # path to get a specific dealer by id
    path('dealer/<int:dealer_id>/', views.get_dealer_by_id, name='get_dealer'),  # Route for a specific dealer by ID

    # path for dealer reviews view
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_details'),

    # path for add a review view
    path(route='add_review', view=views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
