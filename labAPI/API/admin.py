from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(movie)
admin.site.register(cast)
admin.site.register(category)
admin.site.register(series)