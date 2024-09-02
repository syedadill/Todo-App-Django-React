from django.urls import path
from .views import *

urlpatterns = [
    path('', list_todo),
    path('add', add_todo),
    path('<int:pk>/update', update_todo),
    path('<int:pk>/delete', delete_todo),
]