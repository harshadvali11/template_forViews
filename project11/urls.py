"""project11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app import views
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv/',views.fbv,name='fbv'),
    path('cbv/',views.Cbv.as_view(),name='cbv'),
    path('fbvTemplate/',views.fbvTemplate,name='fbvTemplate'),
    path('CbvTemplate/',views.CbvTemplate.as_view(),name='CbvTemplate'),
    path('fbv_form/',views.fbv_form,name='fbv_form'),

    path('cbvform/',views.CbvForm.as_view(),name='cbvform'),
    path('C_Template/',views.C_Template.as_view(),name='C_Template'),
    #path('CBVTemp/',TemplateView.as_view(template_name='template1.html'),name='CBVTemp'),
    path('F_form/',views.F_form.as_view(),name='F_form'),
    path('Cbv_formview/',views.Cbv_formview.as_view(),name='Cbv_formview'),

]
