from django.contrib import admin
# Register your models here.

from .models import Empresa,Items,Autonomo,Proveedor,ItemsCategorias,Productos,TamanosProductos,ProductosCategorias
from .forms import OwnerEmpresa
from .forms import OwnerEmpresaForm

admin.site.register(Empresa)
admin.site.register(Autonomo)
admin.site.register(Items)
admin.site.register(Proveedor)
admin.site.register(ItemsCategorias)
admin.site.register(ProductosCategorias)
admin.site.register(Productos)
admin.site.register(TamanosProductos)

@admin.register(OwnerEmpresa)
class FooAdmin(admin.ModelAdmin):
    form = OwnerEmpresaForm


