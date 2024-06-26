from django.urls import path
from business.views.sellerView import list_seller_view

urlpatterns = [
    path('', list_seller_view, name='sellers')
]
