from django.contrib import admin
from .models import Instruction,Comment,Google_Add,Category
# Register your models here.

admin.site.register(Instruction)
admin.site.register(Comment)
admin.site.register(Google_Add)
admin.site.register(Category)