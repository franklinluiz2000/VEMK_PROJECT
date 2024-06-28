from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from business.models import Profile
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from business.forms.userProfileForm import UserProfileForm, UserForm

def list_profile_view(request, id=None):
    profile = None
    if id is None and request.user:
        profile = Profile.objects.filter(user=request.user).first() 
        id = (profile.id) 
        print (id)      
    elif id is not None:
        profile = Profile.objects.filter(user__id=id).first()
    elif not request.user:
        return redirect(to='/')
    
    
    # print(request.user.is_autenticated)
    # print(profile.show_favorites())
    # favorites = profile.show_favorites()    
    # print(favorites)
    # if len(favorites) > 0:
    #     paginator = Paginator(favorites, 8)
    #     page = request.GET.get('page')
    #     favorites = paginator.get_page(page)
        
    context = {
        'profile': profile,
        # 'favorites': favorites
    }
    # return HttpResponse(id)
    return render(request, template_name='profile/profile2.html', context=context, status=200)

@login_required
def	edit_profile(request):
    profile	= get_object_or_404(Profile, user=request.user)
    emailUnused	=	True
    message = None
    if request.method == 'POST':
        profileForm = UserProfileForm(request.POST, request.FILES, instance=profile)
        userForm = UserForm(request.POST, instance=request.user)
        # Verifica se o	e-mail que o usuário está tentando utilizar	em	seu	perfil	já	existe	em	outro	perfil
        verifyEmail = Profile.objects.filter(user__email=request.POST['email']).exclude(user__id=request.user.id).first()
        emailUnused	= verifyEmail is None

    else:
        profileForm	= UserProfileForm(instance=profile)
        userForm = UserForm(instance=request.user)

    if profileForm.is_valid() and userForm.is_valid() and emailUnused:
        profileForm.save()
        userForm.save()

        message = { 'type': 'success', 'text': 'Dados atualizados com sucesso'}

    else:
        # Aqui verificamos se é do tipo post, para que na primeira vez que a página carregar a mensagem não apareça, já que	no primeiro	carregamento não enviamos um post, o form é dado como inválido e entra aqui.
        if request.method == 'POST':
            if emailUnused:
                # Se o email não está em uso e o usuário estiver algum dado inválido
                message = {'type': 'danger', 'text': 'dados inválidos'}
            else:
                # Se o emial que o usuário tentou cadastrar já está em uso com outr pessoa
                message = {'type':'warning', 'text': 'O email já usado por outro usuário'}
    
    context	= {
        'profileForm': profileForm,
        'userForm': userForm,
        'message': message,
    }
    return	render(request, template_name='user/profile.html', context=context, status=200)