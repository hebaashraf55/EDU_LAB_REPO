from django.contrib import admin
from .models import Meeting, Customer, Courses, Category
# Register your models here.
admin.site.register(Meeting)
admin.site.register(Customer)
admin.site.register(Courses)
admin.site.register(Category)