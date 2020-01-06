from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Art

# Create your views here.
def art_list (request):
	arts = Art.objects.order_by('created_date')
	return render(request, 'rm/art_list.html', {'arts':arts})

def art_detail(request, pk):
    art = get_object_or_404(Art, pk=pk)
    return render(request, 'rm/art_detail.html', {'art': art})