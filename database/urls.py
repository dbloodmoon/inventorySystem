from django.urls import path, include
from rest_framework import routers
from database import views

router = routers.DefaultRouter()

router.register(r'departamento', views.DepartamentoViewSet)
router.register(r'empleado', views.EmpleadoViewSet)
router.register(r'equipo', views.EquipoViewSet)
router.register(r'telefono', views.TelefonoViewSet)
router.register(r'impresora', views.ImpresoraViewSet)
router.register(r'switch', views.SwitchViewSet)
router.register(r'router', views.RouterViewSet)
router.register(r'desincorporacion', views.DesincorporacionViewSet)

urlpatterns = [
    path('api/<str:name>/', views.DepartamentoViewSet.as_view({'get': 'list'})),
    path('api/<str:name>/', views.EmpleadoViewSet.as_view({'get': 'list'})),
    path('api/<str:name>/', views.EquipoViewSet.as_view({'get': 'list'})),
    path('api/<str:name>/', views.TelefonoViewSet.as_view({'get': 'list'})),
    path('api/<str:name>/', views.ImpresoraViewSet.as_view({'get': 'list'})),
    path('api/<str:name>/', views.SwitchViewSet.as_view({'get': 'list'})),
    path('api/<str:name>/', views.RouterViewSet.as_view({'get': 'list'})),
    path('api/<str:name>/', views.DesincorporacionViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
]