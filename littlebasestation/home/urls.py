from .views import home_view
from .views import home_plain
from .views import home_periodic_ajax_view

from django.urls import path, re_path, include


urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),

    path('', home_view, name='home'),
    path('plain/', home_plain),
    path('periodic_ajax.json', home_periodic_ajax_view)
]