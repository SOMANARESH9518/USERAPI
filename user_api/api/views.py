from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from myapp.models import APIUser


def index(request):
    api_user_list = list(APIUser.objects.values())
    return JsonResponse(api_user_list, safe=False)


class APIUserList(View):
    def get(self, request):
        api_user_list = list(APIUser.objects.values())
        return JsonResponse(api_user_list, safe=False)

        # To turn off CSRF validation (not recommended in production)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(APIUserList, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            new_api_user = APIUser(username=data["username"], state=data["state"], city_or_town=data['city_or_town'],
                                   email=data['email'], phone_number=data['phone_number'], gender=data['gender'])
            new_api_user.save()
            return JsonResponse({"created": data}, safe=False)
        except:
            return JsonResponse({"error": data}, safe=False)


class APIUserDetail(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(APIUserDetail, self).dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        api_user_list = {"api_user": list(APIUser.objects.filter(pk=pk).values())}
        return JsonResponse(api_user_list, safe=False)

    def put(self, request, pk):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            new_api_user = APIUser.objects.get(pk=pk)
            data_key = list(data.keys())
            for key in data_key:
                if key == "username":
                    new_api_user.username = data[key]
                if key == "state":
                    new_api_user.state = data[key]
                if key == "city_or_town":
                    new_api_user.city_or_town = data[key]
                if key == "email":
                    new_api_user.email = data[key]
                if key == "phone_number":
                    new_api_user.phone_number = data[key]
                if key == "gender":
                    new_api_user.gender = data[key]
            new_api_user.save()
            return JsonResponse({"updated": data}, safe=False)
        except APIUser.DoesNotExist:
            return JsonResponse({"error": "APIUser having provided primary key does not exist"}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)

    def delete(self, request, pk):
        try:
            new_api_user = APIUser.objects.get(pk=pk)
            new_api_user.delete()
            return JsonResponse({'deleted': True}, safe=False)
        except:
            return JsonResponse({'error': 'Not a Valid Primary Key'}, safe=False)
