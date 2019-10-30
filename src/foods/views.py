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


class FoodCreateView(CreateView):
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


class FoodUpdateView(UpdateView):
    model = Food
    template_name = "form.html"
    form_class = FoodModelForm
    success_url = "/foods/"

    def get_context_data(self, *args, **kwargs):
        context = super(FoodUpdateView, self).get_context_data(*args, **kwargs)
        context["submit_btn"] = "Voeg product toe"
        return context

    def get_object(self, *args, **kwargs):
        user = self.request.user
        obj = super(FoodUpdateView, self).get_object(*args, **kwargs)
        if obj.user == user:
            return obj
        else:
            raise Http404


# Mixins

class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


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


#


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
