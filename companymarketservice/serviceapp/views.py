from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from companyapp.models import Company, Category


# Create your views here.

class MainView(TemplateView):
    template_name = 'base.html'


class AddCompanyView(CreateView):
    model = Company
    fields = '__all__'
    template_name = 'AddCompany.html'
    success_url = ('/companies_list')


class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'AddCategory.html'
    success_url = ('/add_company')
