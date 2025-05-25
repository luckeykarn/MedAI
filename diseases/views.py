from django.shortcuts import render
from django.http import JsonResponse
from .models import Disease

# Create your views here.

def delete_diseases(request, diseases_id):
 
    return JsonResponse({"message": "deleted successfully"}, status=400)
 