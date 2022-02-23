from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to render homepage """
    return render(request, "home/index.html")

def error500(request):
    """ A view to render 500 page """
    return render(request, "home/500.html")