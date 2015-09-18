from django.contrib import admin
from models import Consultant, Fournisseur, Client, CategoryProduit, CategoryService, Produit, Service, Commande, Facture

# Register your models here.

class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'phone', 'email')

class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('compagnie', 'phone', 'email', 'address')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('societe', 'phone', 'email', 'address')

class CategoryProduitAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CategoryServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'prix_unitaire', 'quantite', 'fournisseur')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'prix')

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('client',)

class FactureAdmin(admin.ModelAdmin):
    list_display = ('commande', 'date_validation')

#class LigneProduitAdmin(admin.ModelAdmin):
#    list_display = ('quantite',)

#class LigneServiceAdmin(admin.ModelAdmin):
#    list_display = ('quantite',)

admin.site.register(Consultant, ConsultantAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(CategoryProduit, CategoryProduitAdmin)
admin.site.register(CategoryService, CategoryServiceAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(Facture, FactureAdmin)
#admin.site.register(LigneProduit, LigneProduitAdmin)
#admin.site.register(LigneService, LigneServiceAdmin)
