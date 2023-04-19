from django import urls
from django.urls import path

from . import views
from .views import BooklistView, BookDetailView, BookCheckoutView, SearchResultsView, PaymentComplete, cart,add_to_cart, remove_from_cart
from django import urls
from .import views
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import BooklistView, BookDetailView, BookCheckoutView, PaymentComplete, \
    SearchResultsView
urlpatterns = [
    path('', views.home, name="home"),
    path('book_list',BooklistView.as_view(),name='list'),
    path('details/<int:pk>/',BookDetailView.as_view(),name = 'detail-view'),
    path('checkout/<int:pk>/',BookCheckoutView.as_view(),name = 'checkout'),
    path('complete', PaymentComplete, name='complete'),
    path('search', SearchResultsView.as_view(), name='search'),
    path('payment', views.payment, name='payment'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),



]