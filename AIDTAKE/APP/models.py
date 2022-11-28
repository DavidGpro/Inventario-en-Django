from django.core.mail import send_mail
from django.db import models
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from multiselectfield import MultiSelectField


# Create your models here.


class Empresa(models.Model):
    NombreSociedad = models.CharField(max_length=255)
    Cif = models.CharField(max_length=255)
    Direccion = models.CharField(max_length=255)
    CuentaBancaria = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    NombreApellidos = models.CharField(max_length=255)
    Cargo = models.CharField(max_length=255)
    DNI = models.CharField(max_length=255)
    TelefonoContacto = models.CharField(max_length=255)
    EmailContacto = models.CharField(max_length=255)
    subdominio = models.CharField(max_length=255, null=True)


class Autonomo(models.Model):
    NombreApellidosResponsable = models.CharField(max_length=255)
    Cargo = models.CharField(max_length=255)
    DNI = models.CharField(max_length=255)
    CuentaBancaria = models.CharField(max_length=255)
    Direccion = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)


class OwnerEmpresa(models.Model):
    Nombre = models.CharField(max_length=255)
    Apellidos = models.CharField(max_length=255, null=True)
    DNI = models.CharField(max_length=255, null=True)
    Telf = models.CharField(max_length=255, null=True)
    Direccion = models.CharField(max_length=255, null=True)
    Negocio = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Email = models.CharField(max_length=255, null=True)
    PASS = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.Nombre + ' ' + self.Apellidos + ' | DNI:' + self.DNI

class Proveedor(models.Model):
    Nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre

class ItemsCategorias(models.Model):
    colores = [('1', 'Amarillo'), ('2', 'Naranja'), ('3', 'Rosa'), ('4', 'Rojo'), ('5', 'Morado'), ('6', 'Verde Agua'), ('7', 'Azul'), ('8', 'Azul Oscuro'), ('9', 'Verde'), ('10', 'Verde Oscuro'), ('11', 'Plateado'), ('12', 'Dorado')]
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Color = models.CharField(max_length=255, choices=colores)
    Icono = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.Nombre

class ProductosCategorias(models.Model):
    colores = [('1', 'Amarillo'), ('2', 'Naranja'), ('3', 'Rosa'), ('4', 'Rojo'), ('5', 'Morado'), ('6', 'Verde Agua'), ('7', 'Azul'), ('8', 'Azul Oscuro'), ('9', 'Verde'), ('10', 'Verde Oscuro'), ('11', 'Plateado'), ('12', 'Dorado')]
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Color = models.CharField(max_length=255, choices=colores)
    Icono = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.Nombre

class Items(models.Model):
    unidades =  [('1','Kilo'),('2','Gramos'),('3','Miligramos'),('4','Litro'),('5','Cl'),('6','Unidades')]
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Categoria = models.ForeignKey(ItemsCategorias, on_delete=models.CASCADE, null=True)
    UltimaCompra = models.DateField()
    CosteCompraSinIva = models.DecimalField(max_digits=9,decimal_places=2)
    CosteCompraConIva = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    Iva = models.DecimalField(max_digits=9,decimal_places=2)
    Unidad = models.CharField(max_length=20,choices=unidades)
    Stock = models.DecimalField(max_digits=9,decimal_places=2)
    Naranja = models.DecimalField(max_digits=9,decimal_places=0,null=True)
    Rojo = models.DecimalField(max_digits=9,decimal_places=0,null=True)
    # Imagen = models.ImageField(default='default.jpg')

    def __str__(self):
        return self.Nombre

    @staticmethod
    def get_all_items():
        return Items.objects.all()

    @staticmethod
    def get_items_by_category(category_id):
        if category_id:
            return Items.objects.filter(Categoria=category_id).order_by('Nombre')
        else:
            return Items.objects.order_by('Nombre')

    @staticmethod
    def get_items_by_stock(stock):
        if stock:
            if stock == 'green':
                return Items.objects.filter(Stock__gt=F('Naranja')).order_by('Nombre')
            elif stock == 'black':
                return Items.objects.filter(Stock=0).order_by('Nombre')
            elif stock == 'red':
                return Items.objects.filter(Stock__lte=F('Rojo')).order_by('Nombre')
            elif stock == 'orange':
                return Items.objects.filter(Stock__lte=F('Naranja')).exclude(Stock__lte=F('Rojo')).order_by('Nombre')
        else:
            return Items.objects.order_by('Nombre')

    @staticmethod
    def get_items_by_search(searched):
        if searched:
            return Items.objects.filter(Nombre__icontains=searched).order_by('Nombre')
        else:
            return Items.objects.order_by('Nombre')

    @staticmethod
    def get_item_by_id(id):
        return Items.objects.filter(id = id)

    @staticmethod
    def get_specific_item(item):
        if item:
            return Items.objects.filter(Nombre=item).order_by('Nombre')
        else:
            return Items.objects.order_by('Nombre')

    @staticmethod
    def delete_item(item):
        if item:
            return Items.objects.filter(Nombre=item).delete()
        else:
            return False

    @staticmethod
    def add_price_iva(name, price):
        return Items.objects.filter(Nombre=name).update(CosteCompraConIva=price)

class Productos(models.Model):
    tipos = [('pescado','Pescado'),('fsecos','Frutos Secos'),('lacteos','Lácteos'),('moluscos','Moluscos'),('cgluten','Cereales con Gluten'),('crustaceos','Crustáceos'),('huevos','Huevos'),('cacahuetes','Cacahuetes'),('soja','Soja'),('apio','Apio'),('mostaza','Mostaza'),('sesamo','Sésamo'),('altramuz','Altramuces'),('sulfito','Sulfitos')]
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255, unique=True)
    Categoria = models.ForeignKey(ProductosCategorias, on_delete=models.CASCADE, null=True)
    PrecioVentaSinIva = models.DecimalField(max_digits=9,decimal_places=2)
    PrecioVentaConIva = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    Iva = models.DecimalField(max_digits=9,decimal_places=2)
    Alergenos = MultiSelectField(choices=tipos)
    Componentes = models.ManyToManyField(
        Items,
        through='TamanosProductos'
    )

    def __str__(self):
        return self.Nombre
    #Tamaños = models.ManyToManyField(TamanosProductos)
    # Imagen = models.ImageField(default='default.jpg')

    @staticmethod
    def get_id_by_name(name):
        return Productos.objects.filter(Nombre=name)

class TamanosProductos(models.Model):
    tamanos = [('S', 'Pequeño'), ('M', 'Mediano'), ('L', 'Grande'), ('XL', 'Familiar'), ('XXL', 'Gigante'), ('MR', 'Media Ración'), ('RE', 'Ración Entera'), ('T', 'Tapa'), ('N', 'Normal'), ('MON', 'Montadito')]
    tipos = [('%', 'Porcentaje (%)'), ('Unid', 'Unidad')]
    Producto = models.ForeignKey(Productos, on_delete=models.PROTECT)
    Item = models.ForeignKey(Items, on_delete=models.PROTECT)
    Tamano = MultiSelectField(choices=tamanos)
    #Cantidad = models.DecimalField(max_digits=9,decimal_places=2, null=True)
    #Perdida = models.DecimalField(max_digits=9,decimal_places=2,null=True)
    #TotalPerdida = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    #Coste = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Cantidad_S = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    Cantidad_M = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    Cantidad_L = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    Cantidad_XL = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    Cantidad_XXL = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    Cantidad_MR = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    Cantidad_RE = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    Cantidad_T = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    Cantidad_N = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    Cantidad_MON = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    Perdida_S = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Perdida_M = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Perdida_L = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Perdida_XL = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Perdida_XXL = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Perdida_MR = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Perdida_RE = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Perdida_T = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Perdida_N = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Perdida_MON = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    TotalPerdida_S = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    TotalPerdida_M = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    TotalPerdida_L = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    TotalPerdida_XL = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    TotalPerdida_XXL = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    TotalPerdida_MR = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    TotalPerdida_ME = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    TotalPerdida_T = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    TotalPerdida_N = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    TotalPerdida_MON = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Coste_S = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Coste_M = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Coste_L = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Coste_XL = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Coste_XXL = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Coste_MR = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Coste_ME = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Coste_T = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Coste_N = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    Coste_MON = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    # Imagen = models.ImageField(default='default.jpg')

    @staticmethod
    def add_total_perdida(name, price):
        return TamanosProductos.objects.filter(Producto=name).update(TotalPerdida=price)

    @staticmethod
    def add_cost(name, price):
        return TamanosProductos.objects.filter(Producto=name).update(Coste=price)

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


@receiver(post_save, sender=OwnerEmpresa)
def send_email(sender, instance, **kwargs):
    username = instance.Nombre
    app = instance.Apellidos
    password = instance.PASS
    email_usr = instance.Email

    send_mail(
        'Bienvenido a Aidtake Business',
        'Bienvenido, ' + username + ' ' + app + '. \n Su usuario es ' + email_usr + '\n Su contraseña es ' + password + ', por seguridad la tendras que cambiar cuando inicies sesión \n Un saludo \n Eduardo Sainz, responsable de usuarios',
        settings.EMAIL_HOST_USER,
        [email_usr],
        fail_silently=False,
    )

@receiver(post_save, sender=Items)
def add_iva(sender, instance, **kwargs):
    name = instance.Nombre
    iva = instance.Iva
    precio = instance.CosteCompraSinIva

    total = precio + precio*(iva/100)
    return Items.add_price_iva(name, total)

#@receiver(post_save, sender=TamanosProductos)
def add_total_perdida(sender, instance, **kwargs):
    nombre = instance.Producto
    cantidad = instance.Cantidad
    perdida = instance.Perdida

    perdida_total = cantidad + perdida


    return TamanosProductos.add_total_perdida(nombre, perdida_total)


#@receiver(post_save, sender=TamanosProductos)
def add_cost(sender, instance, **kwargs):
    nombre = instance.Producto
    cantidad = instance.Cantidad
    perdida = instance.Perdida
    item = Items.get_item_by_id(nombre.id)
    precio = item[0].CosteCompraSinIva
    cantidad_prin = item[0].Stock
    perdida_total = cantidad + perdida
    cantidad_total = perdida_total + cantidad

    coste = (cantidad_total * precio) / cantidad_prin

    return TamanosProductos.add_cost(nombre, coste)


