# from django.contrib.auth import authenticate, login
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django_otp.views import LoginView,
#     OTPLoginView,
#     VerifyView,

# from django_otp.signals import user_authenticated
# from .forms import (
#     RequestTokenForm,
#     VerifyTokenForm,
#     SetNewPasswordForm,
# )


# class RequestTokenView(LoginView):
#     def form_valid(self, form):
#         user = form.get_user()
#         device = OTPDevice.objects.get_or_create(user=user)
#         token = generate_code()
#         method = self.request.POST.get('method')
#         if method == 'email':
#             send_email_token(user, token)
#         elif method == 'sms':
#             send_sms_token(user, token)
#         else:
#             raise ValueError('Invalid method')

#         messages.add_message(self.request, messages.INFO, 'Token de 6 dígitos enviado para o seu ' + method + '.')
#         return redirect('verify_token')


# class VerifyTokenView(OTPLoginView):
#     def get_form_class(self):
#         return VerifyTokenForm


# class SetNewPasswordView(VerifyView):
#     def form_valid(self, form):
#         form.save()
#         authenticated_user = authenticate(email=self.request.POST['email'], password=self.request.POST['new_password'])
#         login(self.request
