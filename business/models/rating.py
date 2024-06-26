from business.models import *

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='avaliou' ,on_delete=models.CASCADE)
    company_rated = models.ForeignKey(Company, related_name='avaliado', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    opinion =  models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at =models.DateField(auto_now=True)
    
    def __str__(self):
        return 'Avaliador: {} | Empresa: {}'.format(self.user, self.company_rated)