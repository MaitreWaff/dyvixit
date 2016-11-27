from django.db import models
from django.db.models import permalink
from time import time
from django.template.defaultfilters import slugify
#from django.utils import timezone



# Retourne le Nom De l'Image telechargee.
def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)

# Create your models here.
class Consultant(models.Model):
    """
    Consultant : Fournisseur de Services.
    """
    nom             = models.CharField(max_length=128)
    prenom          = models.CharField(max_length=128)
    phone           = models.IntegerField(unique=True)
    email           = models.EmailField(unique=True)

    class Meta:
        ordering    = ['nom']
	unique_together = ['nom', 'prenom']

    def __unicode__(self):
        return "M. %s %s (%s): %d" % (self.prenom, self.nom, self.email, self.phone)

class Fournisseur(models.Model):
    """
    Fournisseur : Fournisseur de Produits.
    """
    compagnie       = models.CharField(max_length=128, unique=True)
    phone           = models.IntegerField(unique=True)
    email           = models.EmailField(unique=True)
    address         = models.TextField()
    
    class Meta:
        ordering    = ['compagnie']
	unique_together = ['compagnie', 'phone', 'address']

    def __unicode__(self):
        return "Ste %s (%s): %d" % (self.compagnie, self.email, self.phone)

class Client(models.Model):
    """
    Client : Societe qui commande un Produit ou un Service.
    """
    societe         = models.CharField(max_length=128, unique=True)
    phone           = models.IntegerField(unique=True)
    email           = models.EmailField(unique=True)
    address         = models.TextField()

    class Meta:
        ordering    = ['societe']
	unique_together = ['societe', 'phone', 'address']

    def __unicode__(self):
        return "Client %s (%s): %d" % (self.societe, self.email, self.phone)

class Category(models.Model):
    """
    Category : Caracteristiques de base de la Categorie. Classe Abstraite.
    """
    titre        = models.CharField(max_length=48, unique=True)
    desc         = models.TextField()
    date         = models.DateTimeField('Date Creation', auto_now_add=True) #default=timezone.now)
    photo        = models.FileField(upload_to=get_upload_file_name, blank=True)

    slug         = models.SlugField(blank=True)

    class Meta:
        abstract = True
        ordering = ['titre']

    def __unicode__(self):
        return self.titre

class CategoryMateriel(Category):
    """
    CategoryMateriel : Categorie de Produit.
    """

    # @permalink
    # def get_absolute_url(self):
    #     return ('liste_materiel', (), {'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super(CategoryMateriel, self).save(*args, **kwargs)


class CategoryService(Category):
    """
    CategoryService : Categorie de Service.
    """
    #
    # @permalink
    # def get_absolute_url(self):
    #     return ('liste_service', (), {'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super(CategoryService, self).save(*args, **kwargs)


class Article(Category):
    """
    Article : Astuce ou Information a consulter sur le site. Classe Abstraite.
    """
    link  = models.URLField()
    likes = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "Article - %s ( %d Likes!)" % (self.titre, self.likes)



class Astuce(Article):
    """
    Astuce : Astuces a consulter sur le site
    """

    def __unicode__(self):
        return "Astuce - %s ( %d Likes!)" % (self.titre, self.likes)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super(Astuce, self).save(*args, **kwargs)


class Info(Article):
    """
    Info : Information a consulter sur le site.
    """

    def __unicode__(self):
        return "Information - %s ( %d Likes!)" % (self.titre, self.likes)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super(Info, self).save(*args, **kwargs)



class Produit(models.Model):
    """
    Produit : Materiel ou Service disponible sur le site.
    """
    libelle         = models.CharField(max_length=128, unique=True)
    desc            = models.TextField()
    prix            = models.IntegerField()
    photo           = models.FileField(upload_to=get_upload_file_name, blank=True)
    date            = models.DateTimeField('Date De Creation du Produit', auto_now_add=True)

    slug            = models.SlugField(blank=True)

    class Meta:
        abstract = True
        ordering    = ['libelle']
	unique_together = ['libelle', 'desc','prix']

    def __unicode__(self):
        return self.libelle



class Materiel(Produit):
    """
    Materiel : Materiel Informatique a Vendre sur le site.
    """
    category = models.ForeignKey(CategoryMateriel)
    fournisseur = models.ForeignKey(Fournisseur)
    quantite = models.IntegerField(default=100)

    @permalink
    def get_absolute_url(self):
        return ('details_materiel', (), {'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.libelle)
        super(Materiel, self).save(*args, **kwargs)


class Service(Produit):
    """
    Service : Services Informatiques disponible sur le site.
    """
    category            = models.ForeignKey(CategoryService)
    consultant      = models.ForeignKey(Consultant)

    @permalink
    def get_absolute_url(self):
        return ('details_service', (), {'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.libelle)
        super(Service, self).save(*args, **kwargs)


class Facture(models.Model):
    """
    Facture : Commande validee par un client.
    """
    EDITER, COMMANDER, VALIDER, ANNULER, LIVRER = 1, 2, 3, 4, 5

    STATUS_CHOICES = (
        (EDITER, "Editer"),
        (COMMANDER, "Commander"),
        (VALIDER, "Valider"),
        (ANNULER, "Annuler"),
        (LIVRER, "Livrer"),
    )

    numero_facture = models.AutoField(primary_key=True)
    client         = models.ForeignKey(Client)
    #
    cloturee       = models.BooleanField(default=False)
    ordonnee       = models.BooleanField(default=False)
    livree         = models.BooleanField(default=False)
    annulee        = models.BooleanField(default=False)
    #
    status         = models.IntegerField(choices=STATUS_CHOICES, default=1)
    date           = models.DateTimeField('Date De Validation De La Commande', auto_now_add=True) #default=timezone.now)
    montant        = models.IntegerField(default=0)

    class Meta:
        ordering   = ['-date']

    def __unicode__(self):
        return self.numero_facture

class LigneCommande(models.Model):
    """
    LigneCommande : Ligne de commande sur la Facture du client. Classe Abstraite.
    """
    client           = models.ForeignKey(Client)
    quantite         = models.IntegerField(default=1)
    facture          = models.ForeignKey(Facture)

    class Meta:
        abstract = True


class LigneCommandeMateriel(LigneCommande):
    """
    LigneCommandeMateriel : Ligne de commande en reference a un Materiel Informatique.
    """
    article = models.ForeignKey(Materiel)

class LigneCommandeService(LigneCommande):
    """
    LigneCommandeService : Ligne de commande en reference a un Service Informatique.
    """
    article = models.ForeignKey(Service)

class Like(models.Model):
    """
    Like : Mention Like sur un Article ou un Produit. Classe Abstraite.
    """
    liker        = models.URLField()
    date         = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-date']

class LikeAstuce(Like):
    """
    LikeAstuce : Mention Like pour un Materiel Informatique.
    """
    ref_like = models.ForeignKey(Astuce) # Astuce du Like


class LikeInfo(Like):
    """
    LikeInfo : Mention Like pour une Information.
    """
    ref_like = models.ForeignKey(Info) # Info du Like


class LikeMateriel(Like):
    """
    LikeMateriel : Mention Like pour un Materiel Informatique.
    """
    ref_like = models.ForeignKey(Materiel) # Materiel du Like


class LikeService(Like):
    """
    LikeService : Mention Like sur un Service Informatique.
    """
    ref_like = models.ForeignKey(Service) # Service du Like

