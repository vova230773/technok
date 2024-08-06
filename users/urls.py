from django.urls import include, path, re_path

from core.views import Main, vidget
from users import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout



app_name = 'users'

urlpatterns = [
    path('', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('vidget/', vidget.as_view(), name='vidget'),
    path('core/', include('core.urls',namespace='core')),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
  
    
    
#    # restore password urls
    # path('password-reset/', include('django.contrib.auth.views.password_reset', name='password_reset')),
#  path('password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
#  path('password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
#  path('password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'), 
]

