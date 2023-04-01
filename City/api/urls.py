from django.urls import path 

from City.api.views import CityListAPIView, CityDetailAPIView

urlpatterns = [
    path('list/',CityListAPIView.as_view(), name="city-list"),
    path('detail/<int:pk>/',CityDetailAPIView.as_view(), name="city-detail"),
]