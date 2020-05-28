import geocoder
from companyapp.models import Company

companies = Company.objects.all()
for i in companies:
    loc = i.street + ", " + i.city
    g = geocoder.osm(loc)
    i.x = g.x
    i.y = g.y
    i.save()

