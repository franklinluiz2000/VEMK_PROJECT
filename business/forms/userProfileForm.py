from	django.forms	import	ModelForm
from	django	import	forms
from	business.models.profile import Profile

class UserProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.role != 1:
            del self.fields['role']

    class Meta:
        model = Profile
        fields = ['user', 'role', 'birthday', 'image']
        # Usamos '__all__' para	exibir todos os campos como itens do formulário
        # fields = '__all__'
        # Usamos uma lista para definir quando queremos	exibir campos específicos
        # fields = ['pub_date', 'headline', 'content', 'reporter'
        # Usamos exclude para excluir campos específicos do	siste
        # exclude = ['']

        widgets = {

            'user': forms.HiddenInput(),
            'role': forms.Select(attrs={'class': "form-control"}),
            'birthday': forms.DateInput(attrs={'class': "form-control", "type":"date"}),
            'image': forms.FileInput(attrs={'class': "form-control"})

        }
