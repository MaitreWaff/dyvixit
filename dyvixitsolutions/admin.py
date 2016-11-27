from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from models import Consultant, Fournisseur, Client, CategoryMateriel, CategoryService, Astuce, Info, Materiel, Service, \
    LigneCommandeMateriel, LigneCommandeService, Facture, LikeAstuce, LikeInfo, LikeMateriel, LikeService

# Register your models here.

class ConsultantAdmin(admin.ModelAdmin):
    list_display  = ('nom', 'prenom', 'phone', 'email')
    search_fields = ('nom', 'prenom')

class FournisseurAdmin(admin.ModelAdmin):
    list_display  = ('compagnie', 'phone', 'email', 'address')
    search_fields = ('compagnie', 'phone')

class ClientAdmin(admin.ModelAdmin):
    list_display  = ('societe', 'phone', 'email', 'address')
    search_fields = ('societe', 'phone')

class CategoryMaterielAdmin(admin.ModelAdmin):
    list_display        = ('titre', 'photo', 'date', 'desc')
    search_fields       = ('titre', 'date')
    prepopulated_fields = {'slug' : ('titre',)}

class CategoryServiceAdmin(admin.ModelAdmin):
    list_display        = ('titre', 'photo', 'date', 'desc')
    search_fields       = ('titre', 'date')
    prepopulated_fields = {'slug' : ('titre',)}

class AstuceAdmin(admin.ModelAdmin):
    list_display  = ('titre', 'likes', 'photo', 'desc', 'date', 'link')
    search_fields = ('titre', 'date','link')
    ordering      = ('-date',)

class InfoAdmin(admin.ModelAdmin):
    list_display  = ('titre', 'likes', 'photo', 'date', 'desc', 'link')
    search_fields = ('titre', 'date', 'link')
    ordering      = ('-date',)

class MaterielAdmin(admin.ModelAdmin):
    list_display        = ('libelle', 'photo', 'date', 'prix', 'category', 'quantite', 'fournisseur', 'desc')
    list_filter         = ('date', 'category', 'fournisseur')
    search_fields       = ('libelle', 'date', 'prix',)
    prepopulated_fields = {'slug' : ('libelle',)}

class ServiceAdmin(admin.ModelAdmin):
    list_display        = ('libelle', 'photo', 'date', 'prix','category', 'desc')
    list_filter         = ('date', 'category', 'consultant')
    search_fields       = ('libelle', 'date', 'prix',)
    prepopulated_fields = {'slug' : ('libelle',)}

class LigneCommandeMaterielAdmin(admin.ModelAdmin):
    list_display  = ('client', 'quantite', 'article') #, 'facture')
    search_fields = ('client', 'quantite', 'article')

class LigneCommandeServiceAdmin(admin.ModelAdmin):
    list_display  = ('client', 'quantite', 'article') #, 'facture')
    search_fields = ('client', 'quantite', 'article')

class FactureAdmin(admin.ModelAdmin):
    list_display  = ('numero_facture', 'montant', 'status','date')
    list_filter   = ('status', 'date')
    search_fields = ('numero_facture', 'status', 'date')
    ordering      = ('-date',)

class LikeAstuceAdmin(admin.ModelAdmin):
    list_display  = ('liker', 'ref_like')
    list_filter = ('ref_like',)
    search_fields = ('liker',)

class LikeInfoAdmin(admin.ModelAdmin):
    list_display  = ('liker', 'ref_like')
    list_filter = ('ref_like',)
    search_fields = ('liker',)

class LikeMaterielAdmin(admin.ModelAdmin):
    list_display  = ('liker', 'ref_like')
    list_filter = ('ref_like',)
    search_fields = ('liker',)

class LikeServiceAdmin(admin.ModelAdmin):
    list_display  = ('liker', 'ref_like')
    list_filter = ('ref_like',)
    search_fields = ('liker',)


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


# Site Customization
AdminSite.site_header = 'Luc Waffo'
