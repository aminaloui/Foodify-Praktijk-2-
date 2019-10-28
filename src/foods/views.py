from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Food


def detail_view(request, object_id):
    food = get_object_or_404(Food, id=object_id)
    template = "detail_view.html"
    context = {
             "food": food
          }
    return render(request, template, context)


#list view
def list_view(request):
    print request
    template = "list_view.html"
    allfoods = Food.objects.all()
    context = {
        "title": "Hello , List",
        "allfoods" : allfoods
    }
    return render(request, template, context)