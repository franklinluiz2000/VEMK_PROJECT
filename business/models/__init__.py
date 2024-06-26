from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Vendedor'),
    (3, 'Cliente'),
    (4, 'Entregador')
)

STATE_CHOICE = (
    (1, 'AC'), (2, 'AL'), (3, 'AP'), (4, 'AM'), (5, 'BA'), (6, 'CE'), (7, 'DF'), (8, 'ES'), (9, 'GO'),
    (10, 'MA'), (11, 'MS'), (12, 'MT'), (13, 'MG'), (14, 'PA'), (15, 'PB'), (16, 'PE'), (17, 'PI'), (18, 'PR'),
    (19, 'RJ'), (20, 'RN'), (21, 'RO'), (22, 'RR'), (23, 'RS'), (24, 'SC'), (25, 'SE'), (26, 'SP'), (27, 'TO') 
)

from .dayWeek import DayWeek
#from .state import State
from .category import Category
from .company import Company
from .product import Product
from .profile import Profile
