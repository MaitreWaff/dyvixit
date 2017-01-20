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
        return "M./Mme. %s %s (%s): %d" % (self.prenom, self.nom, self.email, self.phone)

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
    address         = models.TextField(blank=True)

    class Meta:
        ordering    = ['nom']
	unique_together = ['societe', 'phone', 'address']

    def __unicode__(self):
        return "Client %s %s (%s a %s): %d" % (self.prenom, self.nom, self.fonction, self.societe, self.phone)

class RealisationAbstract(models.Model):
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
        return "%s" % self.titre

class Reference(RealisationAbstract):
    """
    References : References de l'entreprise.
    """
    pass

class RealisationSimilaire(RealisationAbstract):
    """
    RealisationSimilaire : Realisation Similaire par la Companie.
    """
    pass

    class Meta:
        verbose_name_plural = "Realisations Similaires"



class Contact(models.Model):
    """
    Contact: Differents Contacts de la Compagnie.
    """
    service   = models.CharField(max_length=CHARFIELD_LENGTH)
    telephone = models.IntegerField(max_length=KAMER_PHONE_CODE_MAX_LENGTH)
    desc      = models.CharField(max_length=CHARFIELD_LENGTH, blank=True)

    def __unicode__(self):
        return "%s" % self.service



class CategoryAbstract(models.Model):
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
        return "%s" % self.titre

class CategoryMateriel(CategoryAbstract):
    """
    CategoryMateriel : Categorie de Produit.
    """

    # @permalink
    # def get_absolute_url(self):
    #     return ('liste_materiel', (), {'slug': self.slug})

    @permalink
    def get_absolute_url(self):
        return reverse('get_materiel_in_cat', (), {'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super(CategoryMateriel, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories Materiel"



class CategoryService(CategoryAbstract):
    """
    CategoryService : Categorie de Service.
    """
    #
    # @permalink
    # def get_absolute_url(self):
    #     return ('liste_service', (), {'slug': self.slug})

    @permalink
    def get_absolute_url(self):
        return reverse('get_service_in_cat', (), {'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super(CategoryService, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories Service"



class ArticleAbstract(CategoryAbstract):
    """
    Article : Astuce ou Information a consulter sur le site. Classe Abstraite.
    """
    link  = models.URLField()
    likes = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "Article - %s ( %d Likes!)" % (self.titre, self.likes)



class Astuce(ArticleAbstract):
    """
    Astuce : Astuces a consulter sur le site
    """

    def __unicode__(self):
        return "Astuce - %s ( %d Likes!)" % (self.titre, self.likes)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super(Astuce, self).save(*args, **kwargs)


class Info(ArticleAbstract):
    """
    Info : Information a consulter sur le site.
    """

    def __unicode__(self):
        return "Information - %s ( %d Likes!)" % (self.titre, self.likes)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super(Info, self).save(*args, **kwargs)



class ProduitAbstract(models.Model):
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
        return "%s (%d)" % (self.libelle, self.prix)

    class Meta:
        abstract = True
        ordering    = ['libelle']
	unique_together = ['libelle', 'desc','prix']


class Materiel(ProduitAbstract):
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


class Service(ProduitAbstract):
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
        return "%s (%d)" % (self.numero_facture, self.montant)

    def update_montant_facture(self):
        lcm = LigneCommandeMateriel.objects.filter(facture=self.pk)
        montant_lcm = 0
        for cm in lcm:
            montant_lcm += cm.montant

        lcs = LigneCommandeService.objects.filter(facture=self.pk)
        montant_lcs = 0
        for cs in lcs:
            montant_lcs += cs.montant

        self.montant = montant_lcm + montant_lcs

    def save(self, *args, **kwargs):
        self.update_montant_facture()
        return super(Facture, self).save(*args, **kwargs)

class LigneCommandeAbstract(models.Model):
    """
    LigneCommande : Ligne de commande sur la Facture du client. Classe Abstraite.
    """
    # client           = models.ForeignKey(Client)
    quantite         = models.IntegerField(default=1)
    facture          = models.ForeignKey(Facture, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class LigneCommandeMateriel(LigneCommandeAbstract):
    """
    LigneCommandeMateriel : Ligne de commande en reference a un Materiel Informatique.
    """
    article = models.ForeignKey(Materiel)

    @property
    def montant(self):
        art = self.article #Materiel.objects.get(pk=self.article)
        mnt = art.prix * self.quantite
        return mnt

    def __unicode__(self):
        return "%s [ quantite : %d , Facture : %s ]" % (self.article, self.quantite, self.facture)
        # return "%s (%s)" % (self.article, self.montant())
    #     return "Commande: %s , Facture: %s" % (self.article, self.facture)

    def save(self, *args, **kwargs):
        super(LigneCommandeMateriel, self).save(*args, **kwargs)
        facture = Facture.objects.get(pk=self.facture.pk)
        facture.save()

    class Meta:
        verbose_name_plural = "Lignes Commande Materiel"



class LigneCommandeService(LigneCommandeAbstract):
    """
    LigneCommandeService : Ligne de commande en reference a un Service Informatique.
    """
    article = models.ForeignKey(Service)

    @property
    def montant(self):
        art = self.article
        mnt = art.prix * self.quantite
        return mnt

    def __unicode__(self):
        return "%s [ quantite : %d , Facture : %s ]" % (self.article, self.quantite, self.facture)
    #     return "Commande: %s , Facture: %s" % (self.article, self.facture)

    def save(self, *args, **kwargs):
        super(LigneCommandeService, self).save(*args, **kwargs)
        facture = Facture.objects.get(pk=self.facture.pk)
        facture.save()

    class Meta:
        verbose_name_plural = "Lignes Commande Service"


class LikeAbstract(models.Model):
    """
    Like : Mention Like sur un Article ou un Produit. Classe Abstraite.
    """
    liker        = models.URLField()
    date         = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-date']

class LikeAstuce(LikeAbstract):
    """
    LikeAstuce : Mention Like pour un Materiel Informatique.
    """
    ref_like = models.ForeignKey(Astuce) # Astuce du Like

    class Meta:
        unique_together = ['liker', 'ref_like']


class LikeInfo(LikeAbstract):
    """
    LikeInfo : Mention Like pour une Information.
    """
    ref_like = models.ForeignKey(Info) # Info du Like

    class Meta:
        unique_together = ['liker', 'ref_like']


class LikeMateriel(LikeAbstract):
    """
    LikeMateriel : Mention Like pour un Materiel Informatique.
    """
    ref_like = models.ForeignKey(Materiel) # Materiel du Like

    class Meta:
        unique_together = ['liker', 'ref_like']


class LikeService(LikeAbstract):
    """
    LikeService : Mention Like sur un Service Informatique.
    """
    ref_like = models.ForeignKey(Service) # Service du Like

    class Meta:
        unique_together = ['liker', 'ref_like']

