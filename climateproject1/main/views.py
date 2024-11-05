from django.shortcuts import render, redirect, get_object_or_404
from .forms import climateform
from .models import climate, select_item
import logging
from django.urls import reverse

logger = logging.getLogger(__name__)

def index(request):
    climatedata = climate.objects.all()
    
    if request.method == 'POST':
        form = climateform(request.POST)
        if form.is_valid():
            climate_instance = form.save()
            logger.info("Data saved: %s", climate_instance)
            return redirect(reverse('climate_submit_with_id', args=[climate_instance.id]))
        else:
            logger.error("Form errors: %s", form.errors)
    else:
        form = climateform()
    
    context = {
        'climatedata': climatedata,
        'form': form,
    }
    return render(request, 'index.html', context)

def climate_submit(request, climate_id=None):
    submitted_data = None
    climatedata = climate.objects.all()

    if climate_id:
        climate_instance = get_object_or_404(climate, id=climate_id)
        submitted_data = climate_instance

    context = {
        'submitted_data': submitted_data,
        'climatedata': climatedata,
    }

    return render(request, 'climate_submit.html', context)




from django.shortcuts import render

def base_view(request):
    climatedata = climate.objects.all()  # Query to retrieve all Climate objects
    
    context = {
        'climatedata': climatedata  # Pass climate data to the template context
    }
    
    return render(request, 'base.html', context)

def select_view(request):
    item = select.objects.all()

    context = {
        "items":items
    }
    return render(request, 'select.html', context)
