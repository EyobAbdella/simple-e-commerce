from django.contrib import admin
from .models import Products, Order # Affiliate



# class AffiliateAdmin(admin.ModelAdmin):
#     def get_exclude(self, request, obj=None):
#         if request.method == 'POST':
#             return ("reward_amount",)
#         return None

# admin.site.register(Affiliate, AffiliateAdmin)
admin.site.register(Products)
admin.site.register(Order)
