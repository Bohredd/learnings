from django.urls import path
from processos.views import processos, criar_processo
app_name = 'processos'
urlpatterns = [
    path("", processos, name="processos"),
    path("api/criar_processo/", criar_processo.as_view(), name="criar_processo"),
]
