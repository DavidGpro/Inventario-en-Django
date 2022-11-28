"""AIDTAKE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from APP.forms import LoginForm
from APP.views import CustomLoginView, base
from django.contrib.auth import views as auth_views

from APP import views

urlpatterns = [
    path('', base),
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='empresa/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('home/', views.Home.as_view(), name='home'),
    path('inventario/', views.ListCatgs.as_view(), name='inventario'),
    path('inventario/mostrar_articulo/<str:name>', views.ShowItem.as_view(), name='show_product'),
    path('inventario/editar_articulo/<str:name>', views.EditItem.as_view(), name='edit_product'),
    path('inventario/crear_articulo/', views.CreateItem.as_view(), name='create_product'),
    path('inventario/borrar_articulo/<str:name>', views.DeleteItem.as_view(), name='delete_product'),
    path('productos/', views.ViewProducts.as_view(), name='productos'),
    #path('inventario/mostrar_producto/<str:name>', views.ShowProduct.as_view(), name='show_product'),
    #path('inventario/editar_producto/<str:name>', views.EditProduct.as_view(), name='edit_product'),
    path('productos/crear_producto/', views.CreateProduct.as_view(), name='create_product'),
    path('empleados/', views.Members.as_view(), name='members'),
    path('empleados/crear_empleado/', views.CreateMember.as_view(), name='create_member'),
    path('empleados/mostrar_calendario/<str:name>', views.ShowItem.as_view(), name='show_member_calendar'),
    path('empleados/mostrar_ajustes/<str:name>', views.ShowItem.as_view(), name='show_member_settings'),
    path('empleados/mostrar_nominas/<str:name>', views.ShowItem.as_view(), name='show_member_money'),
    #path('inventario/borrar_producto/<str:name>', views.DeleteProduct.as_view(), name='delete_product'),
    path('logout/', auth_views.LogoutView.as_view(template_name='empresa/logout.html'), name='logout'),
]
