from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Producto, Prod_pop
from .forms import ProductoForm, Contacto, CustomUserCreation
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


@login_required
@permission_required('venta.view_producto')
def listar(request):
        productos = Producto.objects.all()
        
        data = {
               'productos': productos
        }
        
        return render(request, 'venta/listar.html', data) 
@login_required
@permission_required('venta.add_producto')
def agregar(request):
        formulario =   ProductoForm(request.POST or None, request.FILES or None)
        if formulario.is_valid():
                formulario.save()
                messages.success(request, "Producto Agregado Correctamente ")
                # return HttpResponseRedirect('/home/agregar')
        context = {
                "form": ProductoForm
                        }                                   
        return render(request, 'venta/addProductos.html', context)
@login_required
@permission_required('venta.change_producto')
def modificar(request, id):
        productos = Producto.objects.get(id_producto=id)
        context = {
                "form": ProductoForm(instance=productos)}  
        if request.method=='POST':
              formulario=ProductoForm(request.POST, files=request.FILES, instance=productos)  
              if formulario.is_valid:
                formulario.save()
                messages.success(request, "Producto Actualizado Correctamente ")
        return render(request, 'venta/editProductos.html',context)  
@login_required
@permission_required('venta.delete_producto')
def eliminar(request, id):
       productos = Producto.objects.get(id_producto=id)
       productos.delete()
       return redirect('/listar')

def home(request):
        prod_pops = Prod_pop.objects.all()
        return render(request, 'venta/index.html', {'prod_pops': prod_pops})

def nosotros(request):
        context={}
        return render(request, 'venta/nosotros.html',context)

def contacto(request):
        context={}
        return render(request, 'venta/contactanos.html',context)

def login(request):
        context={}
        return render(request, 'registration/login.html',context) 

def registro(request):
        context={
               'form': CustomUserCreation
        }
        if request.method == 'POST':
               formulario = CustomUserCreation(data=request.POST)
               if formulario.is_valid():
                      formulario.save()
                      user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
                      login(request, user)
                      messages.success(request, "te has registrado correctamente")
                      return redirect(to="login")
               
        return render(request, 'registration/registro.html',context) 



def post_list(request):
#    select * from Producto
     productos = Producto.objects.all()
     return render(request, 'venta/productos.html', {'productos': productos})



# def listar(request):
#         productos = Producto.objects.all()
#         page = request.GET.get('page', 1)
#         try:
#                 paginator = Paginator(productos, 5)
#                 productos = paginator.page(page)
#         except:
#                raise Http404
        
#         return render(request, 'venta/listar.html',{'productos': productos}) 




# def agregar(request):
#         data {
#                 'form'
#         }

# def agregar(request):
#        formulario =   ProductoForm(request.POST or None, request.FILES or None)
#        if formulario.is_valid():
#                formulario.save()
#                return redirect('Productos')
#        return render(request, 'venta/addProductos.html',{'formulario': formulario}) 

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'venta/index.html', {'posts': posts})

# def agregar(request):
#         context =  {
#                 'form': ProductoForm()
#         }
#         return render(request, 'venta/addProductos.html',context) 


# def agregar(request):
#        context={'form': ProductoForm()}
#        if request.method=='POST':
#               formulario=ProductoForm(request.POST, files=request.FILES)  
#               if formulario.is_valid:
#                 formulario.save()
#                 context={'mensaje':"Producto guardado"}    
#        return render(request, 'venta/addProductos.html',context)  