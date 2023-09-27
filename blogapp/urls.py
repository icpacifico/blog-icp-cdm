from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Urls Base
    path('', views.home, name="Home"),
    # Urls de la sección: Somos
    path('somos', views.quienes_somos, name="somos"),
    path('mision', views.mision, name="Mision"),
    path('vision', views.vision, name="Vision"),
    path('proposito', views.proposito, name="Proposito"),
    # Urls de la sección: Estrategia
    path('dec_estr', views.declaraciones, name="Declaraciones"),
    path('plan_estrategico', views.plan_estrategico, name="mapa_estrategico"),
    # Urls de la sección: Indicadores
    path('kpis/<int:kpi_id>/', login_required(views.kpi), name="Kpi"),
    # Urls de la sección: Sustentabilidad
    path('prac_sust/<int:practica_id>/', views.economia_circular, name="Practica"),
    # Urls de la sección: Equipos
    path('team/<int:equipo_id>/', views.team, name="Team_Presentation"),
    path('integrantes_team/<int:equipo_id>/', views.integrantes_team, name="Integrantes"),
    # Urls de la sección: Nuestro Legago
    path('proyecto/<int:proyecto_id>/', views.proyectos, name="Proyecto"),
    # Urls de la sección: Actividades
    path('cumple', views.cumple, name="List_Cumples"),
    path('eventos', views.eventos, name="List_Eventos"),
    path('premiacion', views.premiacion, name="List_Premiaciones"),
    path('taller', views.taller, name="List_Talleres"),
    path('post_actividad/<int:act_post_id>/', views.post_actividad, name="Post_Act"),
    path('detalle_actividades/<int:actividad_id>/', views.detalle_actividades, name="Actividad"),
    # Urls de la sección: Planificación
    path('planificaciones/<int:plan_id>/', views.planificaciones, name="Planificacion"),
    # Urls de la sección: Logistica
    path('logistica/<int:reporte_id>/', views.reportes_logistica, name="Dashboard"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
