from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Equipos, Personas, Declaraciones
from contenido.models import Banner, Video, Hito, Actividade, Informativo, Img_Actividade, Indicadore
from noticias.models import Noticia
from proyectos.models import Proyecto, Img_Proyecto
from sustentabilidad.models import Practica, Img_Practica
from planificacion.models import Planificacione
from logistica.models import Reporte
from contenido.models import Comentario, Respuesta
from contenido.forms import ComentarioForm, RespuestaForm
from blogapp.forms import IdeaForm
# from django.views.decorators.csrf import csrf_protect


# Create your views here.


# Datos comunes utilizados en todas las vistas

def datos_comunes():
    practicas = Practica.objects.all()
    proyectos = Proyecto.objects.all().order_by("-id")
    equipos = Equipos.objects.all()
    actividades = Actividade.objects.all()
    kpis = Indicadore.objects.all()
    planificaciones_all = Planificacione.objects.all()
    reportes = Reporte.objects.all()
    hitos = Hito.objects.filter(categoria_hito='Actual')
    hitos_proximos = Hito.objects.filter(categoria_hito='Próximo')
    noticias = Noticia.objects.all().order_by("-id")

    return {'practicas': practicas,
            'proyectos': proyectos,
            'equipos': equipos,
            'actividades': actividades,
            'kpis': kpis,
            'planificaciones_all': planificaciones_all,
            'reportes': reportes,
            'hitos': hitos,
            'hitos_proximos': hitos_proximos,
            'noticias': noticias, }


# vistas de la sección : Nuestra
# @csrf_protect
def home(request):
    actividades_recent = Actividade.objects.filter(mostrar_inicio="Mostrar").order_by("-fecha_actividad")
    data_common = datos_comunes()  # Diccionario global
    datos = Banner.objects.all()
    informativos = Informativo.objects.all()
    personas = Personas.objects.all()
    videos = Video.objects.all()

    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            nueva_idea = form.save(commit=False)
            nueva_idea.save()
            form = IdeaForm()
            # Realiza cualquier redireccionamiento o respuesta necesaria
            return render(request, "pages/index.html", {'actividades_recent': actividades_recent,
                                                        'datos': datos, 'informativos': informativos,
                                                        'personas': personas,
                                                        'videos': videos,
                                                        'form': form,
                                                        **data_common})
    else:
        form = IdeaForm()

    return render(request, "pages/index.html", {'actividades_recent': actividades_recent,
                                                'datos': datos, 'informativos': informativos,
                                                'personas': personas,
                                                'videos': videos,
                                                'form': form,
                                                **data_common})


def quienes_somos(request):
    datos = Declaraciones.objects.all()
    data_common = datos_comunes()  # Diccionario global

    return render(request, "nosotros/nosotros.html", {'datos': datos,
                                                      **data_common})


def mision(request):
    datos = Declaraciones.objects.all()
    return render(request, "nosotros/mision.html", {'datos': datos})


def vision(request):
    datos = Declaraciones.objects.all()
    return render(request, "nosotros/vision.html", {'datos': datos})


def proposito(request):
    datos = Declaraciones.objects.all()
    return render(request, "nosotros/proposito.html", {'datos': datos})


# Vistas de la sección: Nuestra estratégia
def declaraciones(request):
    return render(request, "estrategia/declaraciones.html")


def plan_estrategico(request):
    data_common = datos_comunes()  # Diccionario global
    return render(request, "estrategia/plan_estrategico.html", {**data_common})


# Vistas de la sección: Indicadores
def kpi(request, kpi_id):
    kpis_selected = Indicadore.objects.filter(id=kpi_id)
    data_common = datos_comunes()  # Diccionario global

    return render(request, "indicadores/indicadores.html", {'kpis_selected': kpis_selected,
                                                            **data_common})


# Vistas de la sección: Sustentabilidad

def economia_circular(request, practica_id):
    detalle_practica = Practica.objects.filter(id=practica_id)
    imgs_practica = Img_Practica.objects.filter(practica=practica_id)
    data_common = datos_comunes()  # Diccionario global

    return render(request, "sustentabilidad/practica.html", {'detalle_practica': detalle_practica,
                                                             'imgs_practica': imgs_practica,
                                                             **data_common})


# Vistas de la sección: Empresas
## Vistas de la subsección Arquitectura de la sección: Empresas
##### Arquitectura
def team(request, equipo_id):
    equipo_selected = Equipos.objects.filter(id=equipo_id)
    data_common = datos_comunes()  # Diccionario global

    return render(request, "equipos/presentacion_comun.html", {'equipo_selected': equipo_selected,
                                                               **data_common})


def integrantes_team(request, equipo_id):
    personas = Personas.objects.filter(equipo=equipo_id)
    nombre_equipo = Equipos.objects.filter(id=equipo_id)
    data_common = datos_comunes()  # Diccionario global

    return render(request, "equipos/integrantes_comun.html", {'personas': personas,
                                                              'nombre_equipo': nombre_equipo,
                                                              **data_common})
    # return render(request,"equipos/equipos/arquitectura_team/integrantes.html")


# Vistas de la sección: Nuestro Legado
def proyectos(request, proyecto_id):
    detalle_proyecto = Proyecto.objects.filter(id=proyecto_id)
    imgs_proyecto = Img_Proyecto.objects.filter(proyecto=proyecto_id)
    data_common = datos_comunes()  # Diccionario global

    return render(request, "legado/proyecto.html", {'detalle_proyecto': detalle_proyecto,
                                                    'imgs_proyecto': imgs_proyecto,
                                                    **data_common})


# Vistas de la sección: Actividades
# Vistas para los Cumpleaños
# Vistas para los talleres
# Premiaciones
def cumple(request):
    datos = Actividade.objects.filter(categoria_actividad='Cumpleaños')
    data_common = datos_comunes()  # Diccionario global

    return render(request, "actividades/lista_actividades.html", {'datos': datos,
                                                                  **data_common})


# Vistas para los Eventos
def eventos(request):
    datos = Actividade.objects.filter(categoria_actividad='Evento')
    data_common = datos_comunes()  # Diccionario global

    return render(request, "actividades/lista_actividades.html", {'datos': datos,
                                                                  **data_common})


# Vistas para los Eventos
def taller(request):
    datos = Actividade.objects.filter(categoria_actividad='Taller')
    data_common = datos_comunes()  # Diccionario global

    return render(request, "actividades/lista_actividades.html", {'datos': datos,
                                                                  **data_common})


# Vistas para los Eventos
def premiacion(request):
    datos = Actividade.objects.filter(categoria_actividad='Premiación')
    data_common = datos_comunes()  # Diccionario global

    return render(request, "actividades/lista_actividades.html", {'datos': datos,
                                                                  **data_common})


def post_actividad(request, act_post_id):
    post = Actividade.objects.filter(id=act_post_id)
    imgs_post = Img_Actividade.objects.filter(actividad=act_post_id)
    comentarios = Comentario.objects.filter(post=act_post_id)
    respuestas = Respuesta.objects.all()
    data_common = datos_comunes()  # Diccionario global

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.post_id = act_post_id
            # nuevo_comentario.autor = request.user  # Asigna el autor (si tienes autenticación de usuarios)
            nuevo_comentario.save()
            form = ComentarioForm()
            # Realiza cualquier redireccionamiento o respuesta necesaria
            return render(request, "actividades/act_post.html", {'post': post,
                                                                 'imgs_post': imgs_post,
                                                                 'comentarios': comentarios,
                                                                 'respuestas': respuestas,
                                                                 'form': form,
                                                                 **data_common, })
    else:
        form = ComentarioForm()

    return render(request, "actividades/act_post.html", {'post': post,
                                                         'imgs_post': imgs_post,
                                                         'comentarios': comentarios,
                                                         'respuestas': respuestas,
                                                         'form': form,
                                                         **data_common, })


def detalle_actividades(request, actividad_id):
    fotos = Img_Actividade.objects.filter(actividad=actividad_id)
    data_common = datos_comunes()  # Diccionario global

    return render(request, "actividades/galeria_actividad.html", {'fotos': fotos,
                                                                  **data_common})


# Vistas de la Planificación:


def planificaciones(request, plan_id):
    planifi = Planificacione.objects.filter(id=plan_id)
    data_common = datos_comunes()  # Diccionario global

    return render(request, "planificacion/plan.html", {'planifi': planifi,
                                                       **data_common})


# Vistas de los reportes de Logistica:
def reportes_logistica(request, reporte_id):
    reportes = Reporte.objects.filter(id=reporte_id)
    data_common = datos_comunes()  # Diccionario global

    return render(request, "logistica/dashboard.html", {'reportes': reportes,
                                                        **data_common})


# En tu vista para agregar comentarios

def agregar_respuesta(request, comentario_id):
    # Obtén el comentario al que se responderá
    comentario = Comment.objects.get(pk=comentario_id)

    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            # Crea una nueva instancia de Reply pero no la guarda en la base de datos todavía
            nueva_respuesta = form.save(commit=False)
            nueva_respuesta.comment = comentario  # Asocia la respuesta con el comentario
            # nueva_respuesta.autor = request.user  # Asigna el autor (si tienes autenticación de usuarios)
            nueva_respuesta.save()  # Ahora, guarda la respuesta en la base de datos

            # Puedes redirigir a la página de detalles del comentario o a donde lo desees
            return redirect('detalle_comentario', comentario_id=comentario_id)
    else:
        form = RespuestaForm()

    return render(request, 'tu_template.html', {'form': form, 'comentario': comentario})


def agregar_idea(request):
    pass
