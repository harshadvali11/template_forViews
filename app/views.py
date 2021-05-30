from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.views.generic import View,TemplateView,FormView
from app.forms import *
# responding a string by using FBV
def fbv(request):
    return HttpResponse('hai this is a Function based View')

# responding a string by using ClassBV
class Cbv(View):
    def get(self,request):
        return HttpResponse('hai tis is Class Based View')

# responding an Html page by using FBV

def fbvTemplate(request):
    return render(request,'fbvtemplate.html')

# responding an Html page by using CBV

class CbvTemplate(View):
    def get(self,request):
        return render(request,'cbvtemplate.html')


# validating Forms by using Function Based View

def fbv_form(request):
    form=NameForm()
    if request.method=='POST':
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'fbv_form.html',context={'form':form})


# validating of Form by using Class based View

class CbvForm(View):
    def get(self,request):
        form=NameForm()
        return render(request,'cbv_form.html',context={'form':form})
    
    def post(self,request):
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))


# rendering the Html file by using TempleView class

class C_Template(TemplateView):
    template_name='template1.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #context['name']='hai harshad'
        #context['age']=25
        context['form']=NameForm()
        return context
    
    def post(self,request):
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))


# validating the form by using FormView class

class F_form(FormView):
    template_name='formview.html'
    #form_class=DjangoForm class Address
    form_class=NameForm

    def form_valid(self,form):
        return HttpResponse(str(form.cleaned_data))



class Cbv_formview(FormView):
    template_name='CBV_FormView.html'
    form_class=StudentForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('data is inserted success fully')












