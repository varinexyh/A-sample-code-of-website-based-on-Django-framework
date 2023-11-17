from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import requests

def index(request):
    return render(request, 'chatapp/index.html')

def get_response(request):
    user_input = request.GET.get('user_input')
    gpt_response = f"这是对'{user_input}'的模拟回复。"
    return JsonResponse({'gpt_response': gpt_response})