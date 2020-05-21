from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView
from companyapp.models import Company, Category


# Create your views here.

class MainView(TemplateView):
    template_name = 'main.html'


class AddCompanyView(CreateView):
    model = Company
    fields = '__all__'
    template_name = 'AddCompany.html'
    success_url = ('/companies_list')


class EditCompanyView(UpdateView):
    model = Company
    fields = '__all__'
    template_name = 'EditCompany.html'
    success_url = ('/add_company')

    def get_initial(self):
        initials = super(EditCompanyView, self).get_initial()
        initials['pk'] = self.kwargs['pk']
        return initials


class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'AddCategory.html'
    success_url = ('/add_company')


class EditCategoryView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'EditCategory.html'
    success_url = ('/add_company')

    def get_initial(self):
        initials = super(EditCategoryView, self).get_initial()
        initials['pk'] = self.kwargs['pk']
        return initials


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'CategoryList.html', {'categories': categories})


class CompanyView(View):
    def get(self, request, id):
        companies = Company.objects.filter(category__id=id)
        return render(request, 'Companies.html', {'companies': companies})


class CompanyDetailsView(View):
    def get(self, request, id):
        companies = Company.objects.filter(id=id)
        return render(request, 'CompaniesDetails.html', {'companies': companies})
