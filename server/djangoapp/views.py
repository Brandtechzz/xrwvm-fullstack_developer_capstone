# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate
from .models import CarMake, CarModel

# Get an instance of a logger
logger = logging.getLogger(__name__)


def get_cars(request):
    count = CarMake.objects.filter().count()
    print(count)
    if(count == 0):
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({"CarModel": car_model.name, "CarMake": car_model.car_make.name})
    return JsonResponse({"CarModels":cars})

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            # Load JSON data from the request body
            data = json.loads(request.body)
            username = data.get('userName')
            password = data.get('password')

            # Validate that both username and password are provided
            if not username or not password:
                return JsonResponse({"error": "Username and password are required."}, status=400)

            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                # Log in the user
                login(request, user)
                return JsonResponse({"userName": username, "status": "Authenticated"}, status=200)  # Successful login
            else:
                return JsonResponse({"error": "Invalid credentials."}, status=401)  # Failed login
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)  # Handle JSON parsing errors
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)  # General error handling

    return JsonResponse({"error": "Method Not Allowed"}, status=405)

@csrf_exempt  # This decorator allows the view to be accessed without CSRF validation
def logout_request(request):
    if request.method == 'POST':  # Ensure this view only handles POST requests
        logout(request)  # Logs out the user from the session
        data = {"userName": ""}  # Return an empty username in the response
        return JsonResponse(data)  # Return JSON response confirming logout
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# Registration view to handle sign-up requests
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('userName')
            password = data.get('password')
            first_name = data.get('firstName')
            last_name = data.get('lastName')
            email = data.get('email')

            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already registered"}, status=400)

            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email
            )
            login(request, user)  # Automatically log in the new user
            return JsonResponse({"userName": username, "status": "Authenticated"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)
        except Exception as e:
            logger.error("Error during registration: %s", str(e))
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Method not allowed. Please use a POST request for registration."}, status=405)

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...
