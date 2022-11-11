from django.urls import path
from . import views


urlpatterns = [
    path('',views.index ,name='index'),
    path('<int:pk>',views.deleteItem,name='delete'),
    path('update/<int:pk>',views.updateItem,name='update'),
]