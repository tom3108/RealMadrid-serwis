from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Art
from .forms import ArtForm
from django.shortcuts import redirect

# Create your views here.
def art_list (request):
	arts = Art.objects.order_by('created_date')
	return render(request, 'rm/art_list.html', {'arts':arts})

def art_detail(request, pk):
    art = get_object_or_404(Art, pk=pk)
    return render(request, 'rm/art_detail.html', {'art': art})

def art_new(request):
    if request.method == "POST":
        form = ArtForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.author = request.user
            art.published_date = timezone.now()
            art.save()
            return redirect('art_detail', pk=art.pk)
    else:
        form = ArtForm()
    return render(request, 'rm/art_edit.html', {'form': form})