from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def causes(request):
    return render(request, 'causes.html')
from django.shortcuts import render, redirect

def donate(request):
    if request.method == "POST":
        # 1. Django extracts the validated donor values from the form submission
        donor_name = request.POST.get('name')
        donor_email = request.POST.get('email')
        donor_address = request.POST.get('address')
        donation_amount = request.POST.get('amount')

        # 2. Add database save logic here if you want to store records later

        # 3. Securely redirect the browser straight to your thank_you page
        return redirect('donation_success')

    # Handles normal page visit (GET request)
    return render(request, 'donate.html')


# Changed function name from contact_view to contact
def contact(request):
    context = {
        'email': 'support@hopehands.org',
        'phone': '+91 98765 43210',
        'location': 'Chennai, India'
    }
    return render(request, 'contact.html', context)

def thank_you(request):
    return render(request, 'thank_you.html')



from django.shortcuts import render, redirect

def volunteer_view(request):
    if request.method == "POST":
        # Pulls data fields safely matching your new UI architecture layout
        volunteer_name = request.POST.get('name')
        volunteer_email = request.POST.get('email')
        volunteer_phone = request.POST.get('phone')
        interest_area = request.POST.get('interest_area')
        availability = request.POST.get('availability')

        # Run model creation logs or messaging processing blocks here if needed

        return redirect('home')

    return render(request, 'volunteer.html')

