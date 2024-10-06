from django.shortcuts import render

# Create your views here.
def plantinfo(request):
  return render(request, "index.html")