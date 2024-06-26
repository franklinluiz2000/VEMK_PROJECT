from django.http import HttpResponse
from django.shortcuts import render, redirect
from business.models import Company, Profile
from django.db.models import Q
from django.core.paginator import Paginator

def list_company_view(request):    
    name = request.GET.get('name')    
    address = request.GET.get('address')
    city = request.GET.get('city')  
    category = request.GET.get('category')
    
    companys = Company.objects      
    if name is not None and name != '':
        companys = companys.filter(Q(name=name) | Q(name__contains=name))        
    if category is not None:
        companys = companys.filter(category__id=category)         
    if address is not None and address != '':
        companys = companys.filter(address=address)
    if city is not None and city != '':
        companys = companys.filter(city=city)
 
    # Paginação   
    if len(companys) > 0:
        paginator = Paginator(companys, 8)
        page = request.GET.get('page')
        companys = paginator.get_page(page)
        get_copy = request.GET.copy()
        parameters = get_copy.pop('page', True) and get_copy.urlencode()
    
    
    context = {
        'companys': companys,
        'parameters':parameters
    }
    
    return render(request, template_name='company/companys.html', context=context, status=200)

def company_view(request, id=None):
    if id is None and request.user.is_authenticated:
        id = request.user.id
        return 
    elif not request.user.is_authenticated:
        id = 0
        
    return HttpResponse("<h1>RESPOSTA PARA VER O PERFIL DA EMPRESA</>")

def add_favorite_view(request):
    page = request.POST.get("page")
    name = request.POST.get("name")
    category = request.POST.get("category")
    city = request.POST.get("city")
    state = request.POST.get("state")
    id = request.POST.get("id")
    # print("INICIO")
    # print(Company.objects.filter(id=id).first())
    # print("FIM")  
    
    try:
        profile = Profile.objects.filter(user=request.user).first()
        company = Company.objects.filter(id=id).first()
        profile.favorites.add(company)
        profile.save()
        msg = "Favovrito adicionado com sucesso"
        _type = "success"
    except Exception as e:
        print("Erro %s" % e)
        msg = "Um erro ocorreu ao salvar a empresa nos favoritos"
        _type = "danger"
                
    if page:
        arguments = "?page=%s" % (page)
    else:
        arguments = "?page=1"
        
    if name:
        arguments += "&name=%s" % name
    if category:
        arguments += "&specinality=%s" % category
    if city:
        arguments += "&city=%s" % city
    if state:
        arguments += "&state=%s" % state
        
        
    arguments += "&msg=%s&type=%s" % (msg, _type)
    
    return redirect(to='/company/%s' % arguments)
        
        
        
        