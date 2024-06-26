from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'birthday', 'image', )
    search_fields = ('user__username',)
    # list_display_links = ('user', 'role')
    # list_filter = ('user__is_active',)    
    # fields = ('user', ('role', ), 'image', 'birthday',)
    empty_value_display = 'Vazio'
    fieldsets = (
        ('Usuário', {
        'fields': ('user', 'cpf', 'birthday', 'phone', 'image', 'favorites')
        }),
        ('Função', {
        'fields': ('role',)
        }),
        ('Endereço', {
        'fields': ('address', 'cep', 'city', 'state')
        }),
       
    )

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Company)
admin.site.register(DayWeek)
admin.site.register(Product)
# admin.site.register(State)
admin.site.register(Category)
