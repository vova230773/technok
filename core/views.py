from decimal import Context
from typing import Self
from urllib import request
from django.contrib import auth
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import context
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, DetailView
from core.models import Counterparts,Priv
from operation.models import oper_mod
from product.models import product_mod
from technological_card.models import tk_mod
from core.forms import KontrForm, OPERForm, TMCForm, TkForm
from users.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView



# Create your views here.
import time

# class contr(request):
#   template_name = 'main.html'
#
#   context={'}
#   return render(request,template_name,context)


class CustomHtmxMixin:
    def dispatch(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        self.template_htmx = self.template_name
        if not self.request.META.get("HTTP_HX_REQUEST"):
            self.template_name = "components/include_block.html"
        else:
            time.sleep(1)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["template_htmx"] = self.template_htmx
        return super().get_context_data(**kwargs)


class Home(TemplateView):
    template_name = "home.html"


class Company(CustomHtmxMixin, TemplateView):
    template_name = "company.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = self.kwargs["company_slug"]
        # kwargs['hyu'] = Counterparts.objects.filter(slug=self.)
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["company_slug"]

        context["huy"] = Counterparts.objects.get(slug=slug)
        context["form"] = KontrForm()

        return context

    def post(self, request, *args, **kwargs):

        slug = self.kwargs["company_slug"]

        self.object = Counterparts.objects.get(slug=slug)
        return super().post(request, *args, **kwargs)


class CreateCompany(CustomHtmxMixin, TemplateView):
    template_name = "create_company.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Створити компанію"
        context = super().get_context_data(**kwargs)
        context["form"] = KontrForm()

        return context

    def post(self, request, *args, **kwargs):
        form = KontrForm(data=request.POST)
        # slug = self.kwargs["company_slug"]
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:main'))
        else:
            return HttpResponse(form.errors.values())
        # self.object = Counterparts.objects.get(slug=slug)
        # return super().post(request, *args, **kwargs)

    # if request.method == 'POST':
    #     form = KontrForm(data=request.POST)
    #     # form.slug=slugify(form['name'])
    #     if form.is_valid():
    #          post = form.save(commit=False)
    #         #  post.slug = slugify()
    #          post.save()
    #          context = {'form': KontrForm(),}

    #     else:
    #          return HttpResponse(form.errors.values())

    #  else:

    #      context = {'form': KontrForm(),}

    #  return render(request, "contr2.html", context)


class CreateUser(CustomHtmxMixin, TemplateView):
    template_name = "create_user.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Створити користувача"
        return super().get_context_data(**kwargs)


class Login(TemplateView):
    template_name = "login.html"

class vidget(CustomHtmxMixin, TemplateView  ):
    template_name = "vidget.html"
    def get_context_data(self, **kwargs):
        kwargs["title"] = ""
        return super().get_context_data(**kwargs)

class Main(CustomHtmxMixin, TemplateView  ):
    template_name = "main.html"

    def get_context_data(self,**kwargs):
        kwargs["title"] = "Контрагенти"
        # ddd=Priv.objects.filter(us=auth.user_logged_in)
        gr_us=list(Priv.objects.filter(us=self.request.user))
        ttt=[]
        for sss in gr_us:
            gr=sss.grup
            ttt.append(gr)
        
        kwargs["fignua"] =   Counterparts.objects.filter(group__in=ttt)
        
        return super().get_context_data(**kwargs)


class Users(CustomHtmxMixin, TemplateView):
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Всі користувачі"
        return super().get_context_data(**kwargs)
    
class vvid(CustomHtmxMixin, TemplateView):
    template_name = "vvodcoda.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Введіть код доступу"
        # kwargs["fignua"] = Counterparts.objects.all

        return super().get_context_data(**kwargs)
    
    def post(self, request, *args, **kwargs):
        # form = KontrForm(data=request.POST)
        
       
        s=str(request.POST['name1']) 
        contr=Counterparts.objects.get(okpo_cod=s)

        
        priv=Priv()
        priv.grup=contr.group
        priv.us=request.user
        priv.cod=s
        priv.save()
        
        # else:
        return HttpResponseRedirect(reverse('core:main'))

class TK(CustomHtmxMixin, TemplateView  ):

    template_name = "tk_list.html"

    def get_context_data(self,**kwargs):
        kwargs["title"] = "Тех.карти"
        kwargs["fignua"] =   tk_mod.objects.all()
        
        return super().get_context_data(**kwargs)  

class TK_e(CustomHtmxMixin, TemplateView):
    template_name = "tk_e.html"
    

    def get_context_data(self, **kwargs):
        kwargs["title"] = self.kwargs["tk_id"]
      
        context = super().get_context_data(**kwargs)
        tk_id = self.kwargs["tk_id"]

        context["tkk"] = oper_mod.objects.get(id=tk_id)
        context["form"] = TkForm()

        return context

    def post(self, request, *args, **kwargs):

        tk_id = self.kwargs["tk_id"]
        self.object = oper_mod.objects.get(id=tk_id)
        return super().post(request, *args, **kwargs)  

class CreateTK(CustomHtmxMixin, TemplateView):
    template_name = "create_company.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Створити технологічну карту"
        context = super().get_context_data(**kwargs)
        context["form"] = TkForm()

        return context 
     
    def post(self, request, *args, **kwargs):
        form = TkForm(data=request.POST)
        # slug = self.kwargs["company_slug"]
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:main'))
        else:
            return HttpResponse(form.errors.values())  
        
class TMC(CustomHtmxMixin, TemplateView  ):
    template_name = "tmc_list.html"

    def get_context_data(self,**kwargs):
        kwargs["title"] = "ТМЦ"
        kwargs["fignua"] =   product_mod.objects.all()
        

        return super().get_context_data(**kwargs)

    

class TMC_e(CustomHtmxMixin, TemplateView):
    template_name = "tmc_e.html"
    

    def get_context_data(self, **kwargs):
        kwargs["title"] = self.kwargs["tmc_id"]
      
        context = super().get_context_data(**kwargs)
        tmc_id = self.kwargs["tmc_id"]

        context["tmcc"] = product_mod.objects.get(id=tmc_id)
        context["form"] = TMCForm()

        return context

    def post(self, request, *args, **kwargs):

        tmc_id = self.kwargs["tmc_id"]
        

        self.object = product_mod.objects.get(id=tmc_id)
        return super().post(request, *args, **kwargs)  
    

class CreateTMC(CustomHtmxMixin, TemplateView):
    template_name = "create_company.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Створити ТМЦ"
        context = super().get_context_data(**kwargs)
        context["form"] = TMCForm()

        return context  
     
    def post(self, request, *args, **kwargs):
        form = TMCForm(data=request.POST)
        # slug = self.kwargs["company_slug"]
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:main'))
        else:
            return HttpResponse(form.errors.values())

class OPER(CustomHtmxMixin, TemplateView  ):
    template_name = "oper_list.html"

    def get_context_data(self,**kwargs):
        kwargs["title"] = "Операції"
        kwargs["fignua"] =   oper_mod.objects.all()
        
        return super().get_context_data(**kwargs)
    
 

class CreateOPER(CustomHtmxMixin, TemplateView):
    template_name = "create_company.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Створити Операцію"
        context = super().get_context_data(**kwargs)
        context["form"] = OPERForm()

        return context   
           
    def post(self, request, *args, **kwargs):
        form = OPERForm(data=request.POST)
        # slug = self.kwargs["company_slug"]
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:main'))
        else:
            return HttpResponse(form.errors.values())  
    
@api_view()
def hello_word_view(request: Request)->Response:
    return Response({"message":'huy'})




