from django.shortcuts import render

# 1 item view
def detail_view(request):
    print request
    template = "detail_view.html"
    context = {}
    return render(request, template, context)
#list view
def list_view(request):
    print request
    template = "list_view.html"
    context = {}
    return render(request, template, context)