from django.urls import path
from . import views

urlpatterns = [
    path('search', views.showProduct, name="search"),
    path('<product_title>/<search_item>', views.singlee_Product, name="singlee_Product"),
    path('compare/<id1>/<id2>', views.compare, name="compare_Product"),
    path('<id>', views.single_Product, name="single_Product"),
]
