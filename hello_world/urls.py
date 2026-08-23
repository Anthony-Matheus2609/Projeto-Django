from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hello_world.core import views as core_views
from meu_app import views

urlpatterns = [
    path("", core_views.index),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("dashboard/", views.painel_dashboard, name="dashboard"),
    path("equipamento/<int:id>/", views.detalhe_equipamento,name="detalhe_equipamento"),
    path("cadastrar/", views.cadastrar_equipamento, name="cadastrar_equipamento"),
    path("editar/<int:id>/", views.editar_equipamento, name="editar_equipamento"),
    path("deletar/<int:id>/", views.deletar_equipamento, name="deletar_equipamento"),
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)