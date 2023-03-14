from django.contrib import admin
from home.models import Division
from home.models import Profit_center
from home.models import Organisation
from home.models import Range


# Register your models here.
admin.site.register(Division)
admin.site.register(Profit_center)
admin.site.register(Organisation)
admin.site.register(Range)
