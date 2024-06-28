from django.forms import ModelForm
from django	import forms
from business.models.profile import Profile
from django.contrib.auth.models import User

class UserProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.role != 1:
            del self.fields['role']

    class Meta:
        model = Profile
        fields = ['user', 'cpf',  'role', 'birthday', 'phone', 'address', 'cep', 'city', 'state', 'image']
        # Usamos '__all__' para	exibir todos os campos como itens do formulário
        # fields = '__all__'
        # Usamos uma lista para definir quando queremos	exibir campos específicos
        # fields = ['pub_date', 'headline', 'content', 'reporter'
        # Usamos exclude para excluir campos específicos do	siste
        # exclude = ['']

        widgets = {

            'user': forms.HiddenInput(),
            'cpf': forms.NumberInput({'class': "form-control"}),
            'role': forms.Select(attrs={'class': "form-control"}),
            'birthday': forms.DateInput(attrs={'class': "form-control", "type":"date"}),
            'phone': forms.NumberInput({'class': "form-control"}),
            'address': forms.TextInput(attrs={'class': "form-control"}),
            'cep': forms.NumberInput(attrs={'class': "form-control"}),
            'city': forms.TextInput(attrs={'class': "form-control"}),
            'state': forms.TextInput(attrs={'class': "form-control"}),
            'image': forms.FileInput(attrs={'class': "form-control"}),
            



        }
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.TextInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'class': "form-control"})
        }


