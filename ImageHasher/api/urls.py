from django.urls import path
from .views import ImageRecordListCreate, ImageRecordRetrieveUpdateDestroy

urlpatterns = [
    path('images/', ImageRecordListCreate.as_view(), name='image-list-create'),
    path('images/<int:pk>/', ImageRecordRetrieveUpdateDestroy.as_view(), name='image-detail'),
]
