from django.contrib import admin
from django.contrib.admin import AdminSite
# from django.contrib.admin.sites import AdminSite
from models import Consultant, Fournisseur, Client, CategoryMateriel, CategoryService, Astuce, Info, Materiel, Service, \
    LigneCommandeMateriel, LigneCommandeService, Facture, LikeAstuce, LikeInfo, LikeMateriel, LikeService, \
    Contact, RealisationSimilaire, Reference

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    empty_value_display = '-Vide-'
    list_display = ('service', 'telephone', 'desc')

class RealisationSimilaireAdmin(admin.ModelAdmin):
    empty_value_display = '-Vide-'
    list_display = ('titre', 'client', 'description', 'photo', 'date')
    verbose_plural = ('Realisations Similaires',)

class ReferenceAdmin(admin.ModelAdmin):
    empty_value_display = '-Vide-'
    list_display = ('titre', 'client', 'description', 'photo', 'date')

class ConsultantAdmin(admin.ModelAdmin):
    empty_value_display = '-Vide-'
    list_display  = ('nom', 'prenom', 'phone', 'email')
    search_fields = ('nom', 'prenom')

class FournisseurAdmin(admin.ModelAdmin):
    empty_value_display = '-Vide-'
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

class LigneCommandeMaterielInline(admin.TabularInline): #StackedInline):TabularInline
    model = LigneCommandeMateriel

class LigneCommandeMaterielAdmin(admin.ModelAdmin):
    list_display  = ('article', 'quantite') #, 'facture')
    search_fields = ('article', 'quantite')
    # inlines = [
    #     LigneCommandeMaterielInline,
    # ]

class LigneCommandeServiceInline(admin.TabularInline): #StackedInline):
    model = LigneCommandeService

class LigneCommandeServiceAdmin(admin.ModelAdmin):
    list_display  = ('article', 'quantite') #, 'facture')
    search_fields = ('article', 'quantite')
    # inlines = [
    #     LigneCommandeServiceInline,
    # ]


EDITER, COMMANDER, VALIDER, ANNULER, LIVRER = 1, 2, 3, 4, 5

class FactureAdmin(admin.ModelAdmin):
    list_display  = ('numero_facture', 'client', 'montant', 'status','date')
    list_filter   = ('status', 'date')
    search_fields = ('numero_facture', 'status', 'date', 'client')
    save_on_top = True
    ordering      = ('-date','-numero_facture')
    actions = ['faireValider', 'faireAnnuler', 'faireLivrer',]
    inlines = [
        LigneCommandeMaterielInline, LigneCommandeServiceInline
    ]

    def faireCommander(self, request, queryset):
        rows_updated = queryset.update(status=COMMANDER)
        if rows_updated == 1:
            message_bit = "1 Facture a ete Commandee"
        else:
            message_bit = "%s Factures ont ete Commandees" % rows_updated
        self.message_user(request, "%s avec Succes." % message_bit)

    faireCommander.short_description = "Commander les Factures selectionne"


    def faireValider(self, request, queryset):
        rows_updated = queryset.update(status=VALIDER)
        if rows_updated == 1:
            message_bit = "1 Facture a ete Validee"
        else:
            message_bit = "%s Factures ont ete Validees" % rows_updated
        self.message_user(request, "%s avec Succes." % message_bit)


    faireValider.short_description = "Valider les Factures selectionne"


    def faireAnnuler(self, request, queryset):
        rows_updated = queryset.update(status=ANNULER)
        if rows_updated == 1:
            message_bit = "1 Facture a ete Annulee"
        else:
            message_bit = "%s Factures ont ete Annulees" % rows_updated
        self.message_user(request, "%s avec Succes." % message_bit)


    faireAnnuler.short_description = "Annuler les Factures selectionne"


    def faireLivrer(self, request, queryset):
        rows_updated = queryset.update(status=LIVRER)
        if rows_updated == 1:
            message_bit = "1 Facture a ete Livree"
        else:
            message_bit = "%s Factures ont ete Livrees" % rows_updated
        self.message_user(request, "%s avec Succes." % message_bit)


    faireLivrer.short_description = "Livrer les Factures selectionne"

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

#
# admin.site.register(LigneCommandeMateriel)
# admin.site.register(LigneCommandeService)
#



admin.site.register(Facture, FactureAdmin)

#
# admin.site.register(LikeAstuce, LikeAstuceAdmin)
# admin.site.register(LikeInfo, LikeInfoAdmin)
# admin.site.register(LikeMateriel, LikeMaterielAdmin)
# admin.site.register(LikeService, LikeServiceAdmin)
#

admin.site.register(Contact, ContactAdmin)
admin.site.register(RealisationSimilaire, RealisationSimilaireAdmin)
admin.site.register(Reference, ReferenceAdmin)


# Site Customization
# class MyAdminSite(AdminSite):
#     site_header = 'Luc Waffo'
#     empty_value_display = '-Vide-'
