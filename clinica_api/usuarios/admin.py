from django.contrib import admin
from .models import Animal, Tutor


admin.site.register([Animal, Tutor])
# admin.site.register(Animal)