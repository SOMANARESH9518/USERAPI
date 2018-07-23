from .serializers import APIUserSerializer
from myapp.models import APIUser
from rest_framework import generics
from rest_framework import permissions
from django.http import JsonResponse


# from rest_framework import filters
# from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter


def index(request):
    api_user_list = list(APIUser.objects.values())
    return JsonResponse(api_user_list, safe=False)


'''
class APIUserFilter(filters.FilterSet):
    username = AllValuesFilter(
        name='username')
    email = AllValuesFilter(
        name='email')
    from_created_date = DateTimeFilter(
        name='created_date', lookup_expr='lte')
    to_created_date = DateTimeFilter(
        name='created_date', lookup_expr='gte')

    class Meta:
        model = APIUser
        fields = (
            'username',
            'email',
            'from_created_date',
            'to_created_date',
        )
'''


class CreateView(generics.ListCreateAPIView):
    queryset = APIUser.objects.all()
    serializer_class = APIUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()


'''    filter_fields = (
        'username',
        'email',
        'created_date'
    )
    search_fields = (
        '^username',
        'email',
        'created_date'
    )
    ordering_fields = (
        '^username',
        'email',
        'created_date'
    )
    filter_class = APIUserFilter
'''


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = APIUser.objects.all()
    serializer_class = APIUserSerializer
