from django.contrib.auth import models as auth_models
from django.db import models
from django_otp.models import Device


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    # Campos do seu modelo de usuário

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class OTPDevice(Device):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    phone_number = models.CharField(max_length=16, verbose_name='Número de telefone', blank=True)

    class Meta:
        verbose_name = 'Dispositivo OTP'
        verbose_name_plural = 'Dispositivos OTP'

