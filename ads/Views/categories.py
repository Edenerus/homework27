import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Categories


def index(request):
    response = {"status": "ok"}
    return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        categories_data = json.loads(request.body)

        category = Categories()
        category.name = categories_data["name"]

        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


class CategoryDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })

