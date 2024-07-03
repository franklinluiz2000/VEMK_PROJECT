from business.models import *
from django.db.models import Sum, Count


class Company(models.Model):
    name_company = models.OneToOneField(User, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    address = models.CharField(blank=True, max_length=100)
    cep = models.CharField(blank=True, max_length=8)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.IntegerField(choices=STATE_CHOICE, default=27)      
    phone = models.CharField(null=True, blank=True, max_length=50)    
    days_week = models.ManyToManyField(DayWeek, blank=True, related_name='days_week')
    category = models.ForeignKey(Category, null=True, blank=True, related_name='category', on_delete=models.SET_NULL)
    open_time = models.TimeField(blank=True)
    close_time = models.TimeField(blank=True)   
    image = models.ImageField(null=True, blank=True)
    latidude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True) 
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return '{} - {}'.format(self.name, self.cnpj)
    
    
    @receiver(post_save, sender=User)
    def create_user_company(sender, instance, created, **kwargs):
        try:
            if created:
                    Company.objects.create(user=instance)
        except:
            pass

    
    @receiver(post_save, sender=User)
    def save_user_company(sender, instance, **kwargs):
        try:
            instance.company.save()
        except:
            pass








    
    def show_scoring_average(self):
        from .rating import Rating
        try:
            ratings = Rating.objects.filter(company_rated=self.company).aaggregate(Sum('value'), Count('user'))
            if ratings['company__count'] > 0:
                scoring_average = ratings['value__sum'] / ratings['user__count']
                scoring_average = round(scoring_average, 2) # Arredondando o valor para duas casas decimais
                
                return scoring_average
            
            return "sem avaliações"                
                
        except:
            return "sem avaliações"   
        
    
  