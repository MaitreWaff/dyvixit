from django.contrib import admin
from models import Consultant, Fournisseur, Client, CategoryMateriel, CategoryService, Astuce, Info, Materiel, Service, \
    LigneCommandeMateriel, LigneCommandeService, Facture, LikeAstuce, LikeInfo, LikeMateriel, LikeService

# Register your models here.

class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'phone', 'email')

class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('compagnie', 'phone', 'email', 'address')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('societe', 'phone', 'email', 'address')

class CategoryMaterielAdmin(admin.ModelAdmin):
    list_display = ('titre', 'photo', 'date', 'desc')

class CategoryServiceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'photo', 'date', 'desc')

class AstuceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'likes', 'photo', 'desc', 'date', 'link')

class InfoAdmin(admin.ModelAdmin):
    list_display = ('titre', 'likes', 'photo', 'date', 'desc', 'link')

class MaterielAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'photo', 'date', 'prix', 'category', 'quantite', 'fournisseur', 'desc')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'photo', 'date', 'prix','category', 'desc')

class LigneCommandeMaterielAdmin(admin.ModelAdmin):
    list_display = ('client', 'quantite', 'article') #, 'facture')

class LigneCommandeServiceAdmin(admin.ModelAdmin):
    list_display = ('client', 'quantite', 'article') #, 'facture')

class FactureAdmin(admin.ModelAdmin):
    list_display = ('numero_facture', 'cloturee', 'montant', 'ordonnee', 'date', 'livree', 'annulee')

class LikeAstuceAdmin(admin.ModelAdmin):
    list_display = ('liker', 'ref_like')

class LikeInfoAdmin(admin.ModelAdmin):
    list_display = ('liker', 'ref_like')

class LikeMaterielAdmin(admin.ModelAdmin):
    list_display = ('liker', 'ref_like')

class LikeServiceAdmin(admin.ModelAdmin):
    list_display = ('liker', 'ref_like')

admin.site.register(Consultant, ConsultantAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Client, ClientAdmin)

admin.site.register(Astuce, AstuceAdmin)
admin.site.register(Info, InfoAdmin)

admin.site.register(CategoryMateriel, CategoryMaterielAdmin)
admin.site.register(CategoryService, CategoryServiceAdmin)
admin.site.register(Materiel, MaterielAdmin)
admin.site.register(Service, ServiceAdmin)

admin.site.register(LigneCommandeMateriel, LigneCommandeMaterielAdmin)
admin.site.register(LigneCommandeService, LigneCommandeServiceAdmin)
admin.site.register(Facture, FactureAdmin)

admin.site.register(LikeAstuce, LikeAstuceAdmin)
admin.site.register(LikeInfo, LikeInfoAdmin)
admin.site.register(LikeMateriel, LikeMaterielAdmin)
admin.site.register(LikeService, LikeServiceAdmin)
