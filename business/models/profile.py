from business.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(null=True, blank=False, max_length=11)
    birthday = models.DateField(default=None, null=True, blank=True)
    address = models.CharField(blank=True, max_length=50)
    cep = models.CharField(blank=True, max_length=8)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.IntegerField(choices=STATE_CHOICE, default=27, null=True, blank=True) 
    role = models.IntegerField(choices=ROLE_CHOICE, default=4)    
    image = models.ImageField(null=True, blank=True)
    phone = models.CharField(blank=True, max_length=20)    
    token = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    favorites = models.ManyToManyField(Company, blank=True, related_name='favorites')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
          
    def __str__(self):
        return '{}'.format(self.user.username)
  
  
    '''create_user_profile: usaremos esse método para criar o perfil do usuário. Para que isso ocorra automaticamente,
    precisamos passar a notação @receiber(post_save, sender=User) , onde post_save informa que, em um
    determinado método post , create_user_profile deve ser acionado. Já sender=User informa qual classe Model
    está sendo chamada no post , sendo assim, quando houver um post na classe User , deverá ser chamado o
    método create_user_profile . Não podemos esquecer que requisições post são para criações, então um post
    na classe User aciona o método save dela. No resumo, toda vez que ocorrer a criação de um novo usuário, 
    um perfil será criado para ele'''
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass
        
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass
        
        
    def show_favorites(self):
        print("FRANKLIN")
        ids = [result.id for result in self.favorites.all()]
        print(ids)
        return Company.objects.filter(company__id__in=ids)