from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('toggle-favorite/<int:product_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorite-products/', views.favorite_products, name='favorite_products'),
    path('add/', views.add_product, name='add_product'),
]