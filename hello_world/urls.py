from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from meu_app import views


urlpatterns = [
    
    path("", views.painel_dashboard, name="inicio"),
    path("admin/", admin.site.urls),
    path("dashboard/", views.painel_dashboard, name="dashboard"),
    path("cadastrar/",views.cadastrar_equipamento,name="cadastrar_equipamento"),
    path("equipamento/<int:id>/",views.detalhe_equipamento,name="detalhe_equipamento"),
    path("editar/<int:id>/",views.editar_equipamento,name="editar_equipamento"),
    path("deletar/<int:id>/",views.deletar_equipamento,name="deletar_equipamento"),
    path("__reload__/",include("django_browser_reload.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)