from django.http import Http404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import FoodAddForm, FoodModelForm
from .models import Food


from foodify.mixins import MultiSlugMixin, LoginRequiredMixin

from tags.models import Tag


class FoodCreateView(CreateView, MultiSlugMixin, LoginRequiredMixin):
    model = Food
    template_name = "form.html"
    form_class = FoodModelForm
    # success_url = "/foods/"

    def get_context_data(self, *args, **kwargs):
        context = super(FoodCreateView, self).get_context_data(*args, **kwargs)
        context["submit_btn"] = "Voeg product toe"
        return context

    def form_valid(self, form):
        user = self.request.user
        # Voegt product to aan current user
        form.instance.user = user
        valid_data = super(FoodCreateView, self).form_valid(form)
        return valid_data


class FoodUpdateView(UpdateView, MultiSlugMixin,):
    model = Food
    template_name = "form.html"
    form_class = FoodModelForm
    success_url = "/foods/"

    def get_initial(self):
        initial = super(FoodUpdateView, self).get_initial()
        initial["tags"] = ""
        return initial

    def form_valid(self, form):
        valid_data = super(FoodUpdateView, self).form_valid(form)
        tags = form.cleaned_data.get("tags")
        obj = self.get_object()
        obj.tag_set.clear()
        if tags:
            tags_list = tags.split(",")
            for tag in tags_list:
                new_tag = Tag.objects.get_or_create(title=str(tag).strip())[0]
                #voegt tag toe aan eten dat geupdate wordt
                new_tag.foods.add(self.get_object())
        return valid_data


class FoodDetailView(MultiSlugMixin, DetailView):
    model = Food


class FoodListView(ListView):
    model = Food

    def get_queryset(self, *args, **kwargs):
        qs = super(FoodListView, self).get_queryset(**kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(Q(title__icontains=query) | Q(description__icontains=query)).order_by("title")
        return qs


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
