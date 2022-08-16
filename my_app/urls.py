from django.urls import path

from .views import AppListCreateView, AppDetailView
urlpatterns = [
    path('', AppListCreateView.as_view(), name='country_list_create'),
    path('<int:pk>/', AppDetailView.as_view(), name='country_detail'),
]