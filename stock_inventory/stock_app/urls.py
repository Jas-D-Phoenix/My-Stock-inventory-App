from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register_page, name="register"),
    path('logout', views.logout_user, name="logout"),
    path('login', views.login_page, name="login"),
    path('stock_list', views.stock_list, name="stock_list"),
    path('add_stock', views.add_stock, name="add_stock"),
    path('update_stock/<str:pk>/', views.update_stock, name="update_stock"),
    path('delete_stock/<str:pk>/', views.delete_stock, name="delete_stock"),
    path('stock_info/<str:pk>/', views.stock_info, name="stock_info"),
    path('sale_stock/<str:pk>/', views.sale_stock, name="sale_stock"),
    path('purchase_stock/<str:pk>/', views.purchase_stock, name="purchase_stock"),
    path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),
    path('stock_details', views.stock_details, name="stock_details"),
]