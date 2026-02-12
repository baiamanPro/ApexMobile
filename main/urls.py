from django.urls import path
from .views import home, catalog_view, product_detail
urlpatterns = [
    path("", home, name="home"),
    path("products/", catalog_view, name="products"),
    path("product/<int:pk>/", product_detail, name="product_detail"),
]
