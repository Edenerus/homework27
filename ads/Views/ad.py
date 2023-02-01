import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads


@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):
    def get(self, request):
        ads = Ads.objects.all()
        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad. address,
                "is_published": ad.is_published,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)

        ads = Ads()
        ads.name = ads_data["name"]
        ads.author = ads_data["author"]
        ads.price = ads_data["price"]
        ads.description = ads_data["description"],
        ads.address = ads_data["address"]

        ads.save()

        return JsonResponse({
            "id": ads.id,
                "name": ads.name,
                "author": ads.author,
                "price": ads.price,
                "description": ads.description,
                "address": ads.address,
                "is_published": ads.is_published,
        })


class AdDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = self.get_object()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published,
        })
