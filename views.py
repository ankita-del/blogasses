from django.shortcuts import render

from PIL import Image, ImageDraw, ImageFont
import os
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import User  # Assuming you have a User model

@require_http_methods(["GET"])
def search_users(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    location = request.GET.get('location')

    # Assuming you have fields 'name', 'email', and 'location' in your User model
    users = User.objects.filter(name__icontains=name, email__icontains=email, location__icontains=location)
    user_data = [{'name': user.name, 'email': user.email, 'location': user.location} for user in users]

    return JsonResponse({'users': user_data})


def generate_profile_image(username, gender):
    # Assuming you have a directory named 'profile_images' to save the images
    os.makedirs('profile_images', exist_ok=True)
    filename = f"profile_images/{username}.png"
    image = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Generate image based on gender
    if gender.lower() == 'male':
        color = 'blue'
    else:
        color = 'pink'
    draw.text((50, 50), username, fill=color, font=font)
    image.save(filename)
    return filename

