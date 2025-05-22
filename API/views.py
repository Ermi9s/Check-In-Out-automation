from django.http import JsonResponse
import subprocess

def checkin_view(request):
    try:
        subprocess.run(["python3", "checkin.py"], check=True)
        return JsonResponse({"status": "success", "message": "Check-in script executed"})
    except subprocess.CalledProcessError as e:
        return JsonResponse({"status": "error", "message": str(e)})

def checkout_view(request):
    try:
        subprocess.run(["python3", "checkout.py"], check=True)
        return JsonResponse({"status": "success", "message": "Checkout script executed"})
    except subprocess.CalledProcessError as e:
        return JsonResponse({"status": "error", "message": str(e)})
