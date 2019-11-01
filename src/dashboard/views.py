from django.shortcuts import render
from django.views.generic import View
from foods.models import Food


class DashboardView(View):
    def get(self, request, *args, **kwargs):
        tag_views = ""
        foods = ""
        top_tags = ""
        try:
            tag_views = request.user.tagview_set.all()[2]
        except:
            pass
        if tag_views:
            top_tags = [x.tag for x in tag_views]
            foods = Food.objects.filter(tag__in=top_tags).distinct()

        context = {
            "foods" : foods,
            "top_tags" : top_tags
        }
        return render(request, "dashboard/view.html", context,)
