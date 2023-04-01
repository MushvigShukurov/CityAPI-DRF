from rest_framework.views import APIView
from django.http import JsonResponse
from City.models import City
from City.api.serializers import CitySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from City.api.permissions import IsAuthOrReadOnly
# class CityListAPIView(APIView):
#     def get(self, request):
#         queryset = City.objects.all()
#         serializer = CitySerializer(queryset, many=True)
#         return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    
class CityListAPIView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthOrReadOnly]

class CityDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthOrReadOnly]
