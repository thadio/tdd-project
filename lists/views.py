from django.http import HttpResponse


# Create your views here.
def home_page(request):
    html = "<html><head><title>To-Do lists</title></head><body></body></html>"
    return HttpResponse(html)