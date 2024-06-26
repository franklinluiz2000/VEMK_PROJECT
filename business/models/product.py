from business.models import *

class Product(models.Model):
    company_name = models.ForeignKey(Company,null=False, related_name='company_name', on_delete=models.CASCADE)
    product_name = models.CharField(null=False, blank=False, max_length=50)
    preco = models.FloatField(max_length=10)    
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.product_name)