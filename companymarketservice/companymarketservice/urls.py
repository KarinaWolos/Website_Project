"""companymarketservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from serviceapp.views import MainView, AddCompanyView, AddCategoryView
from serviceapp.views import EditCategoryView, EditCompanyView, CategoryView, CompanyView
from serviceapp.views import CompanyDetailsView
from serviceapp.views import LogView, SignUpView, LogOutView, ShowOnMapView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('add_company', AddCompanyView.as_view(), name='add-company'),
    path('add_category', AddCategoryView.as_view(), name='add-category'),
    path('edit_category/<int:pk>', EditCategoryView.as_view(), name='edit-category'),
    path('edit_company/<int:pk>', EditCompanyView.as_view(), name='edit-company'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('companies/<int:id>', CompanyView.as_view(), name='companies'),
    path('companydetails/<int:id>', CompanyDetailsView.as_view(), name='company-detail'),
    path('login', LogView.as_view(), name='login'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('logout', LogOutView.as_view(), name='logout'),
    path('show_on_map', ShowOnMapView.as_view(), name='show-on-map')

]
