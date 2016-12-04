from django.db import models
from django.db.models import permalink
from time import time
from django.template.defaultfilters import slugify
#from django.utils import timezone

from django.core.urlresolvers import reverse

# Variables pour l'armonisation de la taille des champs.
CHARFIELD_LENGTH, TEXTFIELD_LENGTH = 256, 1024
KAMER_PHONE_CODE_MAX_LENGTH = 13



# Retourne le Nom De l'Image telechargee.
def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)

# Create your models here.
class Consultant(models.Model):
    """
    Consultant : Fournisseur de Services.
    """
    nom             = models.CharField(max_length=CHARFIELD_LENGTH)
    prenom          = models.CharField(max_length=CHARFIELD_LENGTH)
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
    compagnie       = models.CharField(max_length=CHARFIELD_LENGTH, unique=True)
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
    societe         = models.CharField(max_length=CHARFIELD_LENGTH, unique=True)
    prenom          = models.CharField(max_length=CHARFIELD_LENGTH, blank=True)
    nom             = models.CharField(max_length=CHARFIELD_LENGTH, blank=True)
    fonction        = models.CharField(max_length=CHARFIELD_LENGTH, blank=True)
    phone           = models.IntegerField(unique=True)
    email           = models.EmailField(unique=True)
    address         = models.TextField()

    class Meta:
        ordering    = ['nom']
	unique_together = ['societe', 'phone', 'address']

    def __unicode__(self):
        return "Client %s (%s): %d" % (self.societe, self.email, self.phone)

class Realisation(models.Model):
    """
    RealisationSimilaire : Descriptions des Realisations effectuees par la Comapanie.
    """
    titre        = models.CharField(max_length=CHARFIELD_LENGTH)
    description  = models.TextField(max_length=TEXTFIELD_LENGTH)
    client       = models.CharField(max_length=CHARFIELD_LENGTH)
    photo        = models.FileField(upload_to=get_upload_file_name, blank=True)
    date         = models.DateTimeField('Date Creation', auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-date']

    def __unicode__(self):
        return self.titre

class Reference(Realisation):
    """
    References : References de l'entreprise.
    """
    pass

class RealisationSimilaire(Realisation):
    """
    RealisationSimilaire : Realisation Similaire par la Companie.
    """
    pass


class Contact(models.Model):
    """
    Contact: Differents Contacts de la Compagnie.
    """
    service   = models.CharField(max_length=CHARFIELD_LENGTH)
    telephone = models.IntegerField(max_length=KAMER_PHONE_CODE_MAX_LENGTH)
    desc      = models.CharField(max_length=CHARFIELD_LENGTH, blank=True)

    def __unicode__(self):
        return self.service



class Category(models.Model):
    """
    Category : Caracteristiques de base de la Categorie. Classe Abstraite.
    """
    titre        = models.CharField(max_length=CHARFIELD_LENGTH, unique=True)
    desc         = models.TextField(max_length=TEXTFIELD_LENGTH)
    date         = models.DateTimeField('Date Creation', auto_now_add=True) #default=timezone.now)
    photo        = models.FileField(upload_to=get_upload_file_name, blank=True)

    slug         = models.SlugField(blank=True) #, prepopulate_from=('titre',)) default=slugify(titre),

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
    libelle         = models.CharField(max_length=CHARFIELD_LENGTH, unique=True)
    desc            = models.TextField(max_length=TEXTFIELD_LENGTH)
    prix            = models.IntegerField()
    photo           = models.FileField(upload_to=get_upload_file_name, blank=True)
    date            = models.DateTimeField('Date De Creation du Produit', auto_now_add=True)

    slug            = models.SlugField(blank=True) # , prepopulate_from=('titre',) default=slugify(libelle),

    def __unicode__(self):
        return self.libelle

    class Meta:
        abstract = True
        ordering    = ['libelle']
	unique_together = ['libelle', 'desc','prix']


class Materiel(Produit):
    """
    Materiel : Materiel Informatique a Vendre sur le site.
    """
    category = models.ForeignKey(CategoryMateriel)
    fournisseur = models.ForeignKey(Fournisseur)
    quantite = models.IntegerField(default=10)

    @permalink
    def get_absolute_url(self):
        return reverse('details_materiel', (), {'slug': self.slug}) # ('details_materiel', (), {'slug': self.slug})

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
        return reverse('details_service', (), {'slug': self.slug}) # ('details_service', (), {'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.libelle)
        super(Service, self).save(*args, **kwargs)


class Facture(models.Model):
    """
    Facture : Commande validee par un client.
    """

    # Differents Status dans lesquels peuvent etre une Facture...
    # En Edition, Commandee, Validee, Annulee, Livree.
    EDITER, COMMANDER, VALIDER, ANNULER, LIVRER = 1, 2, 3, 4, 5

    # Tuple de Choix pour les Factures.
    STATUS_FACTURE = (
        (EDITER, "Editer"),
        (COMMANDER, "Commander"),
        (VALIDER, "Valider"),
        (ANNULER, "Annuler"),
        (LIVRER, "Livrer"),
    )
    #
    # cloturee       = models.BooleanField(default=False)
    # ordonnee       = models.BooleanField(default=False)
    # livree         = models.BooleanField(default=False)
    # annulee        = models.BooleanField(default=False)
    #
    numero_facture = models.AutoField(primary_key=True)
    client         = models.ForeignKey(Client)

    status         = models.IntegerField(choices=STATUS_FACTURE, default=1)
    date           = models.DateTimeField('Date De Commande', auto_now_add=True) #default=timezone.now)
    montant        = models.IntegerField(default=0)

    # @property
    # def montant(self):
    #     result = self.lignecommandemateriel_set.aggregate(total=Sum(prix))
    #     return result['total']

    class Meta:
        ordering   = ['-date']

    def __unicode__(self):
        return self.numero_facture

class LigneCommande(models.Model):
    """
    LigneCommande : Ligne de commande sur la Facture du client. Classe Abstraite.
    """
    # client           = models.ForeignKey(Client)
    quantite         = models.IntegerField(default=1)
    facture          = models.ForeignKey(Facture)

    class Meta:
        abstract = True


class LigneCommandeMateriel(LigneCommande):
    """
    LigneCommandeMateriel : Ligne de commande en reference a un Materiel Informatique.
    """
    article = models.ForeignKey(Materiel)

    def __unicode__(self):
        return self.article
    #     return "Commande: %s , Facture: %s" % (self.article, self.facture)

class LigneCommandeService(LigneCommande):
    """
    LigneCommandeService : Ligne de commande en reference a un Service Informatique.
    """
    article = models.ForeignKey(Service)

    def __unicode__(self):
        return self.article
    #     return "Commande: %s , Facture: %s" % (self.article, self.facture)

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

    class Meta:
        unique_together = ['liker', 'ref_like']


class LikeInfo(Like):
    """
    LikeInfo : Mention Like pour une Information.
    """
    ref_like = models.ForeignKey(Info) # Info du Like

    class Meta:
        unique_together = ['liker', 'ref_like']


class LikeMateriel(Like):
    """
    LikeMateriel : Mention Like pour un Materiel Informatique.
    """
    ref_like = models.ForeignKey(Materiel) # Materiel du Like

    class Meta:
        unique_together = ['liker', 'ref_like']


class LikeService(Like):
    """
    LikeService : Mention Like sur un Service Informatique.
    """
    ref_like = models.ForeignKey(Service) # Service du Like

    class Meta:
        unique_together = ['liker', 'ref_like']

