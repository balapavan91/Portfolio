from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def n(req):
    return render(req,"index.html")
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send an email
        send_mail(
            subject=f"New Contact Form Submission from {name}",
            message=f"Message: {message}\n\nFrom: {name} ({email})",
            from_email=email,
            recipient_list=['balapavan33@gmail.com'],  
        )
        
        return HttpResponse(f"Thank you, {name}. Your message has been sent.")
    return HttpResponse("Form not submitted correctly.")
