from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import FoodAddForm, FoodModelForm
from .models import Food


class MultiSlugMixin(object):
    model = None

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        modelClass = self.model
        if slug is not None:
            try:
                obj = get_object_or_404(Food, slug=slug)
            except modelClass.MultipleObjectsReturned:
                obj = modelClass.objects.filter(slug=slug).order_by("-title").first()
        else:
            obj = super(MultiSlugMixin, *args, **kwargs)
        return obj


class FoodListView(ListView):
    model = Food

    def get_queryset(self, *args, **kwargs):
        queryset = super(FoodListView, self).get_queryset(**kwargs)
        # queryset = queryset.filter(title__icontains="Food")
        return queryset


class FoodDetailView(MultiSlugMixin,DetailView):
    model = Food

    # def get_object(self, *args, **kwargs):
    #     # print self.kwarg
    #     slug = self.kwargs.get("slug")
    #     modelClass = self.model
    #     if slug is not None:
    #         try:
    #             obj = get_object_or_404(Food, slug=slug)
    #         except modelClass.MultipleObjectsReturned:
    #             obj = modelClass.objects.filter(slug=slug).order_by("-title").first()
    #     else:
    #         obj = super(FoodDetailView, *args, **kwargs)
    #     return obj


def create_view(request):
    form = FoodModelForm(request.POST or None)
    if form.is_valid():
        print form.cleaned_data
        instance = form.save(commit=False)
        instance.save()

    template = "create_view.html"
    context = {
        "form": form
    }
    return render(request, template, context)


def detail_slug_view(request, slug=None):
    # print slug
    # food = 1
    try:
        food = get_object_or_404(Food, slug=slug)
    except Food.MultipleObjectsReturned:
        food = Food.objects.filter(slug=slug).order_by("-title").first()

    template = "detail_view.html"
    context = {
        "food": food
    }
    return render(request, template, context)


def detail_view(request, object_id):
    food = get_object_or_404(Food, id=object_id)
    template = "detail_view.html"
    context = {
        "food": food
    }
    return render(request, template, context)


def update_view(request, object_id):
    food = get_object_or_404(Food, id=object_id)
    form = FoodModelForm(request.POST or None, instance=food)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    template = "update_view.html"
    context = {
        "food": food,
        "form": form
    }
    return render(request, template, context)


# list view
def list_view(request):
    print request
    template = "list_view.html"
    allfoods = Food.objects.all()
    context = {
        "title": "Hello , List",
        "allfoods": allfoods
    }
    return render(request, template, context)
