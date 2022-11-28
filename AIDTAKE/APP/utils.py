from .forms import ItemForm
from .models import Empresa, Items


def get_hostname(request):
    return request.get_host().split(':')[0].lower()

def get_empresa(request):
    hostname = get_hostname(request)
    subdomain = hostname.split('.')[0]
    return Empresa.objects.filter(subdominio=subdomain).first()

def complementarContexto(datos):

    contexto = {'usuario': datos.username, 'id_usuario': datos.id, 'nombre': datos.first_name, 'apellido': datos.last_name, 'correo': datos.email}

    return contexto

def GetProductForm(data2):
    data = Items.get_specific_item(data2)
    print(ItemForm())