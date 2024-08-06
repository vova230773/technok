from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from core import views
# from crm import core
# from carts.models import Cart
# from orders.models import Order, OrderItem
from core.models import Counterparts
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

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


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Ви увійшли в аккаунт")
                
                # if session_key:
                #     Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                    
                
            return HttpResponseRedirect(reverse('user:vidget'))
       

   
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизація',
        'form': form
    }
    return render(request, 'login.html', context)



def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                # Cart.objects.filter(session_key=session_key).update(user=user)
              messages.success(request, f"{user.username}, Ви успішно зареєструвались і увійшли в обліковий запис")
            return HttpResponseRedirect(reverse('core:main'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'registration.html', context)

def profile(request):
   if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Кабінет обновився")
            return HttpResponseRedirect(reverse('user:vidget'))
   else:
        form = ProfileForm(instance=request.user)

        # orders = Order.objects.filter(user=request.user).prefetch_related(
        #         Prefetch(
        #             "orderitem_set",
        #             queryset=OrderItem.objects.select_related("product"),
        #         )
        #     ).order_by("-id")
        

        context = {
        'title': 'Home - Кабінет',
        'form': form,
        # 'orders': orders,
    }
        return render(request, 'profile.html', context)

# class Main(CustomHtmxMixin, TemplateView):
#     template_name = "main2.html"

#     def get_context_data(self, **kwargs):
#         kwargs["title"] = "Контрагенти"
#         kwargs["fignua"] = Counterparts.objects.all

#         return super().get_context_data(**kwargs)
    
    

def logout(request):
    # messages.success(request, f"{request.user.username}, Ви вийшли з програми")
    auth.logout(request)
    context={  
        'title':'Ви вийшли з облікового запису !'}
    return render(request,'logout.html',context)