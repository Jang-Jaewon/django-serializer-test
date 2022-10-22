from django.urls import path

from .views import json_example_view


urlpatterns = [
    path('json/example', json_example_view),
]
