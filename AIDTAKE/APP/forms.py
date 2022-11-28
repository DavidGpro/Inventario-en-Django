from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField

from .models import OwnerEmpresa, Items, Productos, TamanosProductos


class OwnerEmpresaForm(forms.ModelForm):
    class Meta:
        model = OwnerEmpresa
        fields = ['Nombre', 'Apellidos', 'DNI', 'Telf', 'Direccion', 'Negocio', 'Email', 'PASS']
        widgets = {
            'PASS': forms.PasswordInput(),
            'Email': forms.EmailInput(),
        }


class ItemForm(forms.ModelForm):

    class Meta:
        model = Items

        fields = [
            'Nombre',
            'Proveedor',
            'Categoria',
            'UltimaCompra',
            'CosteCompraSinIva',
            'CosteCompraConIva',
            'Iva',
            'Unidad',
            'Stock',
            'Naranja',
            'Rojo',
        ]

        labels = {
            'Nombre': 'Nombre',
            'Proveedor':'Proveedor',
            'Categoria':'Categoria',
            'UltimaCompra':'Ultima Compra',
            'CosteCompraSinIva':'Sin IVA',
            'CosteCompraConIva':'Con IVA',
            'Iva':'% IVA',
            'Unidad':'Unidad',
            'Stock':'Stock',
            'Naranja':'Naranja',
            'Rojo':'Rojo',
        }

        widgets = {
            'Nombre': forms.TextInput(),
            'Proveedor': forms.Select(attrs={'class':'pop-up-form-data-fields-input'}),
            'Categoria': forms.Select(attrs={'class':'pop-up-form-data-fields-input'}),
            'UltimaCompra': forms.DateInput(format='%d/%m/%Y'),
            'CosteCompraSinIva': forms.NumberInput(attrs={'class':'S'}),
            'CosteCompraConIva': forms.NumberInput(attrs={'class':'S'}),
            'Iva': forms.NumberInput(attrs={'class':'S'}),
            'Unidad': forms.Select(attrs={'class':'pop-up-form-data-fields-input'}),
            'Stock': forms.NumberInput(),
            'Naranja': forms.NumberInput(attrs={'class':'S'}),
            'Rojo': forms.NumberInput(attrs={'class':'S'}),
        }

class ProductoForm(ModelForm):
    class Meta:
        model = Productos
        exclude = ()



class TProductoForm(ModelForm):
    class Meta:
        model = TamanosProductos
        exclude = ('TotalPerdida',)
        #fields = [
            #'Producto',
            #'Item',
            #'Tamano',
            #'Cantidad',
            #'Perdida',
            #'Coste',
        #]

        labels = {
            'Cantidad_S' : 'S',
            'Cantidad_M' : 'M',
            'Cantidad_L' : 'L',
            'Cantidad_XL' : 'XL',
            'Cantidad_XXL' : 'XXL',
            'Cantidad_MR' : 'MR',
            'Cantidad_RE' : 'RE',
            'Cantidad_T' : 'T',
            'Cantidad_N' : 'N',
            'Cantidad_MON' : 'MON',
            'Perdida_S' : '',
            'Perdida_M' : '',
            'Perdida_L' : '',
            'Perdida_XL' : '',
            'Perdida_XXL' : '',
            'Perdida_MR' : '',
            'Perdida_RE' : '',
            'Perdida_T' : '',
            'Perdida_N' : '',
            'Perdida_MON' : '',
            'TotalPerdida_S' : '',
            'TotalPerdida_M' : '',
            'TotalPerdida_L' : '',
            'TotalPerdida_XL' : '',
            'TotalPerdida_XXL' : '',
            'TotalPerdida_MR' : '',
            'TotalPerdida_ME' : '',
            'TotalPerdida_T' : '',
            'TotalPerdida_N' : '',
            'TotalPerdida_MON' : '',
            'Coste_S' : '',
            'Coste_M' : '',
            'Coste_L' : '',
            'Coste_XL' : '',
            'Coste_XXL' : '',
            'Coste_MR' : '',
            'Coste_ME' : '',
            'Coste_T' : '',
            'Coste_N' : '',
            'Coste_MON' : '',
        }

        widgets = {
            'Cantidad_S' : forms.NumberInput(attrs={'class':'S'}),
            'Cantidad_M' : forms.NumberInput(attrs={'class':'M'}),
            'Cantidad_L' : forms.NumberInput(attrs={'class':'L'}),
            'Cantidad_XL' : forms.NumberInput(attrs={'class':'XL'}),
            'Cantidad_XXL' : forms.NumberInput(attrs={'class':'XXL'}),
            'Cantidad_MR' : forms.NumberInput(attrs={'class':'MR'}),
            'Cantidad_RE' : forms.NumberInput(attrs={'class':'RE'}),
            'Cantidad_T' : forms.NumberInput(attrs={'class':'T'}),
            'Cantidad_N' : forms.NumberInput(attrs={'class':'N'}),
            'Cantidad_MON' : forms.NumberInput(attrs={'class':'MON'}),
            'Perdida_S' : forms.NumberInput(attrs={'class':'S'}),
            'Perdida_M' : forms.NumberInput(attrs={'class':'M'}),
            'Perdida_L' : forms.NumberInput(attrs={'class':'L'}),
            'Perdida_XL' : forms.NumberInput(attrs={'class':'XL'}),
            'Perdida_XXL' : forms.NumberInput(attrs={'class':'XXL'}),
            'Perdida_MR' : forms.NumberInput(attrs={'class':'MR'}),
            'Perdida_RE' : forms.NumberInput(attrs={'class':'RE'}),
            'Perdida_T' : forms.NumberInput(attrs={'class':'T'}),
            'Perdida_N' : forms.NumberInput(attrs={'class':'N'}),
            'Perdida_MON' : forms.NumberInput(attrs={'class':'MON'}),
            'TotalPerdida_S' : forms.NumberInput(attrs={'class':'S'}),
            'TotalPerdida_M' : forms.NumberInput(attrs={'class':'M'}),
            'TotalPerdida_L' : forms.NumberInput(attrs={'class':'L'}),
            'TotalPerdida_XL' : forms.NumberInput(attrs={'class':'XL'}),
            'TotalPerdida_XXL' : forms.NumberInput(attrs={'class':'XXL'}),
            'TotalPerdida_MR' : forms.NumberInput(attrs={'class':'MR'}),
            'TotalPerdida_ME' : forms.NumberInput(attrs={'class':'RE'}),
            'TotalPerdida_T' : forms.NumberInput(attrs={'class':'T'}),
            'TotalPerdida_N' : forms.NumberInput(attrs={'class':'N'}),
            'TotalPerdida_MON' : forms.NumberInput(attrs={'class':'MON'}),
            'Coste_S' : forms.NumberInput(attrs={'class':'S'}),
            'Coste_M' : forms.NumberInput(attrs={'class':'M'}),
            'Coste_L' : forms.NumberInput(attrs={'class':'L'}),
            'Coste_XL' : forms.NumberInput(attrs={'class':'XL'}),
            'Coste_XXL' : forms.NumberInput(attrs={'class':'XXL'}),
            'Coste_MR' : forms.NumberInput(attrs={'class':'MR'}),
            'Coste_ME' : forms.NumberInput(attrs={'class':'RE'}),
            'Coste_T' : forms.NumberInput(attrs={'class':'T'}),
            'Coste_N' : forms.NumberInput(attrs={'class':'N'}),
            'Coste_MON' : forms.NumberInput(attrs={'class':'MON'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
