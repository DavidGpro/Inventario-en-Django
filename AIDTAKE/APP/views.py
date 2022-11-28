from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.forms import modelform_factory, inlineformset_factory, modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views import View
from django.views.generic import CreateView

from .forms import LoginForm, ItemForm, TProductoForm
from .models import ItemsCategorias, Items, ProductosCategorias, Productos, TamanosProductos, User
from .utils import get_empresa, complementarContexto, GetProductForm

def base(request):
    return redirect('home')

def login(request):
    empresa = get_empresa(request)
    return render(request, 'empresa/login.html', {'empresa': empresa})

class Home(LoginRequiredMixin, View):
    login_url = '../login'
    redirect_field_name = None

    def get(self, request):
        data_user = complementarContexto(request.user)
        dic = {'data_user': data_user}
        return render(request, 'empresa/home.html', dic)

class Members(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        #data_user = complementarContexto(request.user)
        User = get_user_model()
        users = User.objects.all()
        dic = {'data': users}

        return render(request, 'miembros/memb.html', dic)

class CreateMember(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = ItemForm(request.POST)
        categorias = ItemsCategorias.objects.all()
        data_user = complementarContexto(request.user)
        items = Items.objects.order_by('Nombre')
        data = {'cat': categorias, 'data_user': data_user, 'form': form, 'item': items}
        return render(request, 'miembros/memb.html', data)

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados')

class ListCatgs(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        filter = request.GET
        items = Items.objects.order_by('Nombre')
        if filter:
            for i in filter:
                if i == 'category':
                    items = Items.get_items_by_category(filter['category'])
                elif i == 'stock':
                    items = Items.get_items_by_stock(filter['stock'])
                else:
                    items = Items.objects.order_by('Nombre')
        else:
            items = Items.objects.order_by('Nombre')

        categorias = ItemsCategorias.objects.all()
        data_user = complementarContexto(request.user)



        data = {'cat': categorias, 'data_user': data_user, 'item': items}

        return render(request, 'inventario/inv.html', data)

    def post(self, request):
        if request.POST['searched']:
            items = Items.get_items_by_search(request.POST['searched'])
        else:
            items = Items.objects.order_by('Nombre')

        print(items)

        categorias = ItemsCategorias.objects.all()
        data_user = complementarContexto(request.user)

        data = {'cat': categorias, 'data_user': data_user, 'item': items}
        return render(request, 'inventario/inv.html', data)

class CreateItem(LoginRequiredMixin, View):
    login_url = '../login'
    redirect_field_name = None

    def get(self, request):
        form = ItemForm(request.POST)
        categorias = ItemsCategorias.objects.all()
        data_user = complementarContexto(request.user)
        items = Items.objects.order_by('Nombre')
        data = {'cat': categorias, 'data_user': data_user, 'form': form, 'item': items}
        return render(request, 'inventario/inv.html', data)

    def post(self, request):

        form = ItemForm(request.POST)
        print(form)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('inventario')


class EditItem(LoginRequiredMixin, View):
    login_url = '../login'
    redirect_field_name = None

    def get(self, request, name):
        categorias = ItemsCategorias.objects.all()
        data_user = complementarContexto(request.user)
        items = Items.objects.order_by('Nombre')
        data_item = get_object_or_404(Items, Nombre=name)
        form = ItemForm(instance=data_item)
        data = {'cat': categorias, 'data_user': data_user, 'form': form, 'item': items}
        return render(request, 'inventario/inv.html', data)

    def post(self, request, name):
        data_item = get_object_or_404(Items, Nombre=name)
        form = ItemForm(request.POST, instance=data_item)
        if form.is_valid():
            form.save()
            return redirect('inventario')

class DeleteItem(LoginRequiredMixin, View):
    login_url = '../login'
    redirect_field_name = None

    def get(self, request, name):
        Items.delete_item(name)
        return redirect('inventario')



class ShowItem(LoginRequiredMixin, View):
    login_url = '../login'
    redirect_field_name = None

    def get(self, request,  name):
        categorias = ItemsCategorias.objects.all()
        data_user = complementarContexto(request.user)
        items = Items.objects.order_by('Nombre')
        data_item = get_object_or_404(Items, Nombre=name)
        form = ItemForm(instance=data_item)
        data = {'cat': categorias, 'data_user': data_user, 'form': form, 'item': items}
        return render(request, 'inventario/inv.html', data)

class ViewProducts(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        filter = request.GET
        items = Items.objects.order_by('Nombre')
        if filter:
            for i in filter:
                if i == 'category':
                    items = Items.get_items_by_category(filter['category'])
                elif i == 'stock':
                    items = Items.get_items_by_stock(filter['stock'])
                else:
                    items = Items.objects.order_by('Nombre')
        else:
            items = Items.objects.order_by('Nombre')

        categorias = ItemsCategorias.objects.all()
        data_user = complementarContexto(request.user)

        data = {'cat': categorias, 'data_user': data_user, 'item': items}

        return render(request, 'producto/prod.html', data)

    def post(self, request):
        if request.POST['searched']:
            items = Items.get_items_by_search(request.POST['searched'])
        else:
            items = Items.objects.order_by('Nombre')

        categorias = ItemsCategorias.objects.all()
        data_user = complementarContexto(request.user)

        data = {'cat': categorias, 'data_user': data_user, 'item': items}
        return render(request, 'inventario/inv.html', data)

ProductoForm = modelform_factory(Productos, exclude=['Componentes',])
#ProductoTForm = modelform_factory(TamanosProductos, exclude=['Producto',])

class CreateProduct(LoginRequiredMixin, CreateView):
    login_url = '../login'
    redirect_field_name = None

    def get(self, request):
        form = TProductoForm()
        formp = ProductoForm()
        categorias = ProductosCategorias.objects.all()
        data_user = complementarContexto(request.user)
        items = Productos.objects.order_by('Nombre')
        data = {'cat': categorias, 'data_user': data_user, 'formp': formp, 'form': form, 'item': items}
        return render(request, 'producto/prod.html', data)

    def post(self, request):
        data = TProductoForm(request.POST)
        prod = ProductoForm(request.POST)
        print(prod)
        if prod.is_valid():
            try:
                print('True')
                prod.save()
            except:
                print('False')

        print(request.POST)

        # if data.is_valid():
        #     instances = data.save(commit=False)
        #     for instance in instances:
        #         instance.Producto_id = Productos.get_id_by_name(request.POST['Nombre'])[0].id
        #         instance.save()

        return redirect('productos')



class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

