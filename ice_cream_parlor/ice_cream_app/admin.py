from django.contrib import admin
from .models import *

admin.site.register(Flavor)
admin.site.register(Ingredient) 
admin.site.register(Suggestion)
admin.site.register(Allergen)
admin.site.register(UserAllergy)
admin.site.register(Cart)
admin.site.register(CustomUser)

# Register your models here.
