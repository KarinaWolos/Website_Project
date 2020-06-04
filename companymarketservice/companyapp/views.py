from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic.edit import FormView
from companyapp.models import Company, Category
from companyapp.forms import LogForm, SignUpForm, AddCompany, UpdateRating
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from statistics import mean
from django.views.generic import RedirectView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


# Create your views here.

class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        companies = Company.objects.all()
        ctx['companies'] = companies
        return ctx


class AddCompanyView(LoginRequiredMixin, CreateView):
    form_class = AddCompany
    template_name = 'AddCompany.html'
    success_url = ('/')


class EditCompanyView(PermissionRequiredMixin, UpdateView):
    permission_required = 'companyapp.change_company'
    permission_denied_message = 'Nie posiadasz wystarczających uprawnień!'
    model = Company
    fields = ('name', 'rating', 'street', 'city', 'website', 'phone', 'category')
    template_name = 'EditCompany.html'
    success_url = ('/add_company')

    def get_initial(self):
        initials = super(EditCompanyView, self).get_initial()
        initials['pk'] = self.kwargs['pk']
        return initials


class AddCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    fields = '__all__'
    template_name = 'AddCategory.html'
    success_url = ('/add_company')


class EditCategoryView(PermissionRequiredMixin, UpdateView):
    permission_required = 'companyapp.change_category'
    permission_denied_message = 'Nie posiadasz wystarczających uprawnień!'
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


class LogView(FormView):
    template_name = "log.html"
    form_class = LogForm

    def form_valid(self, form):
        username = form.cleaned_data['login']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print("Zautentykowano, logowanie", user)
            login(self.request, user)
            return HttpResponseRedirect('/')
        else:
            print("Nie udało sie zautentykować")
            return HttpResponseRedirect('/login?loginFaild=1')


class SignUpView(FormView):
    form_class = SignUpForm
    success_url = '/'
    template_name = 'Signup.html'

    def form_valid(self, form):
        new_user = form.instance
        password = form.cleaned_data["password1"]
        new_user.set_password(password)
        new_user.save()
        return super().form_valid(form)


class LogOutView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return '/'


class ShowOnMapView(View):
    def get(self, request, id):
        company = Company.objects.filter(id=id)
        ctx = {'company': company}
        return render(request, 'CompanyOnMap.html', ctx)


from decimal import Decimal


class UpdateRatingView(View):
    def get(self, request, id):
        form = UpdateRating()
        return render(request, 'UpdateRating.html', {'form': form})

    def post(self, request, id):
        form = UpdateRating(request.POST)
        company = Company.objects.get(id=id)
        if form.is_valid():
            new_rating = Decimal(form.cleaned_data['rating'])
            rating = Decimal(company.rating)
            total_rating = mean([new_rating, rating])
            company.rating = total_rating
            company.save()
            print(f'Wystawiono ocenę {new_rating}')
        return HttpResponseRedirect('/')
