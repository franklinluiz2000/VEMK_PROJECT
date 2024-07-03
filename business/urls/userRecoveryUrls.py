from django.urls import path
from business.views.userRecoveryView import RequestTokenView, VerifyTokenView, SetNewPasswordView

urlpatterns = [
    path('solicitar-token/', RequestTokenView.as_view(), name='request_token'),
    path('verificar-token/', VerifyTokenView.as_view(), name='verify_token'),
    path('definir-nova-senha/', SetNewPasswordView.as_view(), name='set_new_password'),
]
