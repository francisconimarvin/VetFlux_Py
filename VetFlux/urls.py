from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('/home', views.home, name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html', redirect_authenticated_user=True), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # pacientes
    path('paciente/', views.paciente, name='paciente'),
    path('paciente/lista/', views.paciente_lista, name='paciente_lista'),
    path('paciente/nuevo/', views.paciente_crear, name='paciente_crear'),
    path('paciente/<int:pk>/editar/', views.paciente_editar, name='paciente_editar'),
    path('paciente/<int:pk>/eliminar/', views.paciente_eliminar, name='paciente_eliminar'),

    # tutor
    path('tutor/', views.tutor, name='tutor'),
    path('tutor/lista/', views.tutor_lista, name='tutor_lista'),
    path('tutor/nuevo/', views.tutor_crear, name='tutor_crear'),
    path('tutor/<str:pk>/editar/', views.tutor_editar, name='tutor_editar'),
    path('tutor/<str:pk>/eliminar/', views.tutor_eliminar, name='tutor_eliminar'),

    # agenda
    path('agenda/', views.agenda, name='agenda'),
    path('agenda/lista/', views.agenda_lista, name='agenda_lista'),
    path('agenda/nueva/', views.agenda_crear, name='agenda_crear'),
    path('agenda/<int:pk>/editar/', views.agenda_editar, name='agenda_editar'),
    path('agenda/<int:pk>/eliminar/', views.agenda_eliminar, name='agenda_eliminar'),

    # inventario
    path('inventario/', views.inventario, name='inventario'),
    path('inventario/lista/', views.inventario_lista, name='inventario_lista'),
    path('inventario/<int:pk>/editar/', views.inventario_editar, name='inventario_editar'),

    # fichas
    path('fichas/', views.ficha, name='ficha'),
    path('fichas/lista/', views.ficha_lista, name='ficha_lista'),
    path('fichas/nueva/', views.ficha_crear, name='ficha_crear'),
    path('fichas/<int:pk>/editar/', views.ficha_editar, name='ficha_editar'),
    path('fichas/<int:pk>/eliminar/', views.ficha_eliminar, name='ficha_eliminar'),

    # receta
    path('recetas/', views.receta, name='receta'),
    path('recetas/lista/', views.receta_lista, name='receta_lista'),
    path('recetas/nueva/', views.receta_crear, name='receta_crear'),
    path('recetas/<int:pk>/editar/', views.receta_editar, name='receta_editar'),
    path('recetas/<int:pk>/eliminar/', views.receta_eliminar, name='receta_eliminar'),
]
