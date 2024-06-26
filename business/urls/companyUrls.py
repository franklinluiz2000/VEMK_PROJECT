from django.urls import path
from business.views.companyView import list_company_view, company_view, add_favorite_view

urlpatterns = [
    path('', list_company_view, name='companys'),
    path('<int:id>', company_view, name='company'),
    path('favorite', add_favorite_view, name='company-favorite'),
]
