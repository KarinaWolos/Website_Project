from faker import Faker
from companyapp.models import Company, Category

fake = Faker('pl_PL')
#
# for i in range(20):
#     Company.objects.create(name=fake.name(), rating=fake.random_int(min=0, max=5),
#                            street=fake.street_address(), city=fake.city(), website=fake.image_url(), phone=fake.phone_number())
#
#
#


companies = Company.objects.all()

for company in companies:
    category = Category.objects.get(pk=fake.random_int(min=1, max=5))
    company.category.add(category)

