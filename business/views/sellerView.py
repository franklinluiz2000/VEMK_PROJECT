from django.shortcuts import render
from business.models.profile import Profile
from django.db.models import Q

def list_seller_view(request):
    name = request.GET.get('name')    
    address = request.GET.get('address')
    city = request.GET.get('city')  
    category = request.GET.get('category')
    sellers = Profile.objects     
    if name is not None and name != '':
        sellers = sellers.filter(Q(user__first_name__contains=name) | Q(user__username__contains=name))        
    if category is not None:
        sellers = sellers.filter(category__id=category)         
    if address is not None and address != '':
        sellers = sellers.filter(address=address)
    if city is not None and city != '':
        sellers = sellers.filter(city=city)
    # print(sellers)
    context = {
        'sellers': sellers
    }
        
    return render(request, template_name='seller/sellers.html', context=context, status=200)