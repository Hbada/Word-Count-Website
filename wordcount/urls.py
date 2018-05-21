from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),

    path('nopage/', views.nopage), # create page at /nopage
    path('about/', views.about, name = 'about'), # create page at /about
    path('count/', views.count, name = 'count'), # create page at /count
    # name needs to match code in pages that use {% url 'name' %} to link to it
]
