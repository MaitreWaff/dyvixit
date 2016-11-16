from django.contrib import admin
from models import Consultant, Fournisseur, Client, CategoryProduit, CategoryService, Article, Info, Produit, Service, \
    Commande, Facture, Like, LikeArticle, LikeInfo, LikeProduit, LikeService

# Register your models here.

class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'phone', 'email')

class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('compagnie', 'phone', 'email', 'address')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('societe', 'phone', 'email', 'address')

class CategoryProduitAdmin(admin.ModelAdmin):
    list_display = ('photo', 'date', 'titre', 'desc')

class CategoryServiceAdmin(admin.ModelAdmin):
    list_display = ('photo', 'date', 'titre', 'desc')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('date', 'photo', 'titre', 'likes', 'link', 'desc')

class InfoAdmin(admin.ModelAdmin):
    list_display = ('date', 'photo', 'titre', 'likes', 'link', 'desc')

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('photo', 'date', 'libelle', 'prix_unitaire', 'quantite', 'fournisseur', 'desc')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('photo', 'date', 'nom', 'type', 'prix', 'desc')

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('client',)

class FactureAdmin(admin.ModelAdmin):
    list_display = ('commande',)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('liker',)


class LikeArticleAdmin(admin.ModelAdmin):
    list_display = ('liker',)


class LikeInfoAdmin(admin.ModelAdmin):
    list_display = ('liker',)


class LikeProduitAdmin(admin.ModelAdmin):
    list_display = ('liker',)


class LikeServiceAdmin(admin.ModelAdmin):
    list_display = ('liker',)

admin.site.register(Consultant, ConsultantAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(CategoryProduit, CategoryProduitAdmin)
admin.site.register(CategoryService, CategoryServiceAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(Facture, FactureAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(LikeArticle, LikeInfoAdmin)
admin.site.register(LikeInfo, LikeInfoAdmin)
admin.site.register(LikeProduit, LikeProduitAdmin)
admin.site.register(LikeService, LikeAdmin)
