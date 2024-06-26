from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from business.models import Profile
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from business.forms.userProfileForm import UserProfileForm

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


def	edit_profile(request):
    profile	=	get_object_or_404(Profile,	user=request.user)
    profileForm	=	UserProfileForm(instance=profile)

    context	= {
        'profileForm':	profileForm
    }
    return	render(request,	template_name='user/profile.html',	context=context,	status=200)