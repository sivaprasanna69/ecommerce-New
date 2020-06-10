from django.contrib import admin

# Register your models here.
from .models import product, productImage, Variation

class productAdmin(admin.ModelAdmin):
	date_hierarcy = 'timestamp'
	search_fields = ['title', 'description']
	list_display = ['title', 'price', 'active', 'updated']
	list_editable = ['price', 'active']
	list_filter = ['price', 'active']
	readonly_fields = ['updated', 'timestamp']
	prepopulated_fields = {"slug":("title",)}
	class Meta:
		model = product
			

admin.site.register(product, productAdmin)

admin.site.register(productImage)

admin.site.register(Variation)