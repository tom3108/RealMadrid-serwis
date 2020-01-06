from django.shortcuts import render
from django.utils import timezone
from .models import Art

# Create your views here.
def art_list (request):
	arts = Art.objects.order_by('created_date')
	return render(request, 'rm/art_list.html', {'arts':arts})