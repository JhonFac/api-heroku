from django.urls import path
from .views import RequesForms

urlpatterns = [
    path('', RequesForms.hola),
    path('form_1/', RequesForms.as_view(), name='formulario 1'),
    # path('data/', GetData.as_view(), name='get data')
]
