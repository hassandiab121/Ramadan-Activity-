from django.http import HttpResponse
from django.shortcuts import render as rendrer, redirect
from django.contrib import messages
from datetime import datetime, timedelta
from .forms import ActivityForm
from .models import Activity

# Create your views here.
def recieve_activities(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            day = int(form.cleaned_data['day'])
            
            # Calculate the date (assuming Ramadan 2026 starts on February 28)
            # Adjust the year and start date as needed
            ramadan_start = datetime(2026, 2, 18)  # Example: adjust to actual Ramadan date
            activity_date = ramadan_start + timedelta(days=day - 1)
            
            # Create and save the activity
            Activity.objects.create(
                name=name,
                description=description,
                location=location,
                date=activity_date,
                Ramdan_day=day
            )
            
            messages.success(request, 'تم إضافة النشاط بنجاح!')
            return redirect('show_activities')
    else:
        form = ActivityForm()
    
    return rendrer(request, 'recieve_activity.html', {'form': form})
