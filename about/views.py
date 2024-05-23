from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About

# Create your views here.
class AboutList(generic.ListView):
    about = About.objects.all().order_by('-updated_on').first()
    template_name = "about.html"

def about_starter(request):
    """
    Renders the About page
    """

    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )