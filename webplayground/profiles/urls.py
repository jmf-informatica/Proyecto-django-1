from django.urls import path
from .views import ProfileList,ProfileDetail

urlpatterns = [
    path('', ProfileList.as_view(), name='profiles_list'),
    path('<username>/', ProfileDetail.as_view(), name='profiles_detail'),
]