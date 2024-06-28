from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuário: ", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    password = forms.CharField(label="Senha: ", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}), required=True)

class RegisterForm(forms.Form):
    username = forms.CharField(label="Usuário:", widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    email = forms.CharField(label="Email:", widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    password = forms.CharField(label="Senha:", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}), required=True)


class RecoveryForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}),required=True)