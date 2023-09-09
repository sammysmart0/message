from django.urls import path
from . import views
# from .views  import Message

urlpatterns = [
    path('', views.index, name='home'),
    path('message/<str:pk>', views.detail, name='message-detail'),
    path('message-list/', views.list, name='message-list'),
    path('message-create', views.create, name='message-create'),
    path('message-update/<str:pk>', views.edit, name='message-update'),
    path('message-delete/<str:pk>', views.delete, name='message-delete')
]














